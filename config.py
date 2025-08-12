#━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

import os
import re
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📲 Telegram & API Credentials
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

API_ID = int(os.getenv("22657083"))
API_HASH = os.getenv("d6186691704bd901bdab275ceaab88f3")
BOT_TOKEN = os.getenv("8477795771:AAHAL8ZauVa-qYlcRfxWTDGp6-76O9JAa98")
OWNER_ID = int(os.getenv("OWNER_ID", "8086485131"))
OWNER_USERNAME = os.getenv("OWNER_USERNAME", "IzCurse")
BOT_USERNAME = os.getenv("BOT_USERNAME", "AyakaXMusicBot")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🛠️ Database & Deployment Configs
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

MONGO_DB_URI = os.getenv("MONGO_DB_URI", "mongodb+srv://ahad0181888:ahad0181888@cluster0.f9casz0.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP_ID = int(os.getenv("LOG_GROUP_ID", "-1002791009509"))
HEROKU_APP_NAME = os.getenv("HEROKU_APP_NAME" "paapp")
HEROKU_API_KEY = os.getenv("HEROKU_API_KEY" "HRKU-AADP58F46wfUmelp4NVW5v2V7waz32SkCj4l3Ckw8p7Q_____wEg8asnTooh")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔄 Git & Update Settings
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

UPSTREAM_REPO = os.getenv("UPSTREAM_REPO", "https://github.com/Shadow737hub/Ayaka")
UPSTREAM_BRANCH = os.getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = os.getenv("GIT_TOKEN", "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")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔗 Support Links
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SUPPORT_CHANNEL = os.getenv("https://t.me/EX_BOT_UPDATES")
SUPPORT_GROUP = os.getenv("SUPPORT_GROUP", "https://t.me/+G42j7plUt91mYmQx")

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⏱️ Duration & Playlist Settings
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

DURATION_LIMIT_MIN = int(os.getenv("DURATION_LIMIT", 300))
PLAYLIST_FETCH_LIMIT = int(os.getenv("PLAYLIST_FETCH_LIMIT", 25))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 📦 File Size Limits (in bytes)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

TG_AUDIO_FILESIZE_LIMIT = int(os.getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(os.getenv("TG_VIDEO_FILESIZE_LIMIT", 2145386496))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🎧 Spotify Developer Credentials
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

SPOTIFY_CLIENT_ID = os.getenv("SPOTIFY_CLIENT_ID", "492a9216285f4466a115c6ee3964cae4")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIFY_CLIENT_SECRET", "444f4d6e6e66406a887f5d6703655c9e")
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🧵 Session Strings (Pyrogram V2)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

STRING1 = os.getenv("STRING_SESSION", "AQCOaU4AfezBEqvIgrIhRoznyu52Jwdnff_MGZP7TJ1m_8xrCtXUS9EzNg-dsqvqt0rGr1A8D0NXl9-TqUDTQJpGxdWkWVzw2Daooaq4Q36E77FAUT2wmQiP7hDhigtYlsp41ykkUiuDwfW-dADhXYPbZ_jMgZ_FBrdcami_lhktfbR8-0pcwYicGUikpwFUrgwyhOdI8wDkrAnvXI5E6iRgqGSU296shpseXukxT-HvwNOFw3LTofLscVfnRWW4Ab6nbkzNc-dAUq4UHrU8sJrfuWfsW-o4u36xj33-43ozzColiejdOkZDxYdAGO27tQyOLdXp6B6r4UhFDf_VbJJX5MzlzQAAAAG-FGdAAA")
STRING2 = os.getenv("STRING_SESSION2", None)
STRING3 = os.getenv("STRING_SESSION3", None)
STRING4 = os.getenv("STRING_SESSION4", None)
STRING5 = os.getenv("STRING_SESSION5", None)

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⚙️ Runtime Configurations
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AUTO_LEAVING_ASSISTANT = bool(os.getenv("AUTO_LEAVING_ASSISTANT", False))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🖼️ Image URLs (Can be customized)
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

START_IMG_URL = os.getenv("START_IMG_URL", "https://files.catbox.moe/408ozy.jpg")
PING_IMG_URL = os.getenv("PING_IMG_URL", "https://files.catbox.moe/2kxtxa.jpg")
PLAYLIST_IMG_URL = "https://files.catbox.moe/ghaqbv.jpg"
STATS_IMG_URL = "https://files.catbox.moe/wk8hlz.jpg"
TELEGRAM_AUDIO_URL = "https://files.catbox.moe/ghaqbv.jpg"
TELEGRAM_VIDEO_URL = "https://files.catbox.moe/ghaqbv.jpg"
STREAM_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SOUNCLOUD_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
YOUTUBE_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://files.catbox.moe/eehxb4.jpg"

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# 🔐 User & Bot State Stores
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}

TEMP_DB_FOLDER = "tempdb"
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ⏳ Time Conversion Utility
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))

DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
# ❌ Validate Support Links
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

if SUPPORT_CHANNEL:
    if not re.match(r"(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - SUPPORT_CHANNEL URL is invalid. It must start with https://"
        )

if SUPPORT_GROUP:
    if not re.match(r"(?:http|https)://", SUPPORT_GROUP):
        raise SystemExit(
            "[ERROR] - SUPPORT_GROUP URL is invalid. It must start with https://"
        )

# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
#     ✅ CONFIG LOADED SUCCESSFULLY
# ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━


# ===========================================

