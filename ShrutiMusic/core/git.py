import asyncio
import shlex
from typing import Tuple

from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError

import config

from ..logging import LOGGER


def install_req(cmd: str) -> Tuple[str, str, int, int]:
    async def install_requirements():
        args = shlex.split(cmd)
        process = await asyncio.create_subprocess_exec(
            *args,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await process.communicate()
        return (
            stdout.decode("utf-8", "replace").strip(),
            stderr.decode("utf-8", "replace").strip(),
            process.returncode,
            process.pid,
        )

    return asyncio.get_event_loop().run_until_complete(install_requirements())


def git():
    REPO_LINK = config.UPSTREAM_REPO
    if config.GIT_TOKEN:
        try:
            # Handle https://github.com/<username>/<repo>
            if REPO_LINK.startswith("http"):
                parts = REPO_LINK.rstrip("/").split("/")
                GIT_USERNAME = parts[-2]  # username
                TEMP_REPO = REPO_LINK.replace("https://", "")
                UPSTREAM_REPO = f"https://{GIT_USERNAME}:{config.GIT_TOKEN}@{TEMP_REPO}"
            # Handle SSH: git@github.com:<username>/<repo>.git
            elif REPO_LINK.startswith("git@"):
                TEMP_REPO = REPO_LINK.split("github.com:")[1]
                GIT_USERNAME = TEMP_REPO.split("/")[0]
                UPSTREAM_REPO = f"https://{GIT_USERNAME}:{config.GIT_TOKEN}@github.com/{TEMP_REPO}"
            else:
                raise ValueError("Invalid UPSTREAM_REPO format.")
        except (IndexError, ValueError) as e:
            LOGGER(__name__).error(f"Invalid UPSTREAM_REPO: {REPO_LINK} ({e})")
            return
    else:
        UPSTREAM_REPO = config.UPSTREAM_REPO

    try:
        repo = Repo()
        LOGGER(__name__).info("Git Client Found [VPS DEPLOYER]")
    except GitCommandError:
        LOGGER(__name__).info("Invalid Git Command")
        return
    except InvalidGitRepositoryError:
        repo = Repo.init()
        if "origin" not in repo.remotes:
            repo.create_remote("origin", UPSTREAM_REPO)
        origin = repo.remote("origin")
        origin.fetch()
        repo.create_head(
            config.UPSTREAM_BRANCH,
            origin.refs[config.UPSTREAM_BRANCH],
        )
        repo.heads[config.UPSTREAM_BRANCH].set_tracking_branch(
            origin.refs[config.UPSTREAM_BRANCH]
        )
        repo.heads[config.UPSTREAM_BRANCH].checkout(True)
        try:
            origin.pull(config.UPSTREAM_BRANCH)
        except GitCommandError:
            repo.git.reset("--hard", "FETCH_HEAD")
        install_req("pip3 install --no-cache-dir -r requirements.txt")
        LOGGER(__name__).info("Fetching updates from upstream repository...")