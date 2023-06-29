#
# Copyright (C) 2021-2022 by Alexa_Help@Github, < https://github.com/Jankarikiduniya >.
# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# All rights reserved. © Alisha © Alexa © Yukki


import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")

MONGO_DB_URI = getenv("MONGO_DB_URI", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "900"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", ""))

MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "乛𝘼𝙇𝙀𝙓𝘼🕊️⃝🦋⁪⁬𝙈𝙐𝙎𝙄𝘾")

OWNER_ID = list(map(int, getenv("OWNER_ID", "1748768168 1748768168").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

BOT_ID = getenv("BOT_ID")

HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/qwer2002hamd/i",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")

GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ah07v")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/ah07v")

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")

AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "11500"))

AUTO_SUGGESTION_TIME = int(getenv("AUTO_SUGGESTION_TIME", "5400"))

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", None)

AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", None)

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "3"))

TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "5"))

GITHUB_REPO = getenv("GITHUB_REPO", None)

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "3"))

SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "30"))

PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))

TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "randilogs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []

START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/a0b4ae6f5304825e45f8e.jpg"
)

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/4d4eca0ac2202c09cd2e8.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/a0b4ae6f5304825e45f8e.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/a0b4ae6f5304825e45f8e.jpg"

STATS_IMG_URL = "https://te.legra.ph/file/a0b4ae6f5304825e45f8e.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/a0b4ae6f5304825e45f8e.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/a0b4ae6f5304825e45f8e.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/a0b4ae6f5304825e45f8e.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/a0b4ae6f5304825e45f8e.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/a0b4ae6f5304825e45f8e.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/a0b4ae6f5304825e45f8e.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/a0b4ae6f5304825e45f8e.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/a0b4ae6f5304825e45f8e.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/4d4eca0ac2202c09cd2e8.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://telegra.ph/file/a0b4ae6f5304825e45f8e.jpg"
