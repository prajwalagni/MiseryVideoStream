from os import path, getenv
from dotenv import load_dotenv

if path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
BOT_TOKEN = getenv("BOT_TOKEN", "")
API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
SESSION_NAME = getenv("SESSION_NAME", "")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "50"))
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "MiseryVideoStreamer")
BOT_USERNAME = getenv("BOT_USERNAME", "MiseryStreamBot")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . ?").split())
