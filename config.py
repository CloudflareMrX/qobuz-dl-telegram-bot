import logging, os, time
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    level=logging.INFO)
LOGGER = logging.getLogger(__name__)

class Config(object):
    APP_ID = 21712687
    API_HASH = "397ff79e47bafe94c6609f68c5a8e7f5"
    BOT_TOKEN = "6842307779:AAFZAclKkOA5aILTmvM1oVAMHO4PJtUNmOM
"
    BOT_USERNAME = "Nandumrxrips"
    OWNER_ID = 5960644989
    AUTH_IDS = []
    QOBUZ_MAIL = "paxetin714@ikuromi.com"
    HEROKU_APP_NAME = "xxxx" # dont touch
    HEROKU_API_KEY = "xxxx" # dont touch
    QOBUZ_PASS = "Forqobuz1213"
    QOBUZ_QUAL = 5
    UPDATE_ALL = True
    LOG_CHANNEL = []
    botStartTime = time.time() # dont touch
