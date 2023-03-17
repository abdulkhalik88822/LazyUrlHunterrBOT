# in & as LazyDeveloper
# Please Don't Remove Credit

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "24431302"))
    API_HASH = os.environ.get("API_HASH", "63df50d25da8390785aa654173652790")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6265513460:AAEVABfwA8nb-OamLRm_aTEzP9kUlsnvzos")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "1BVtsOH0BuzXq9XdMPGD44MOtSRxsRlyzSHtSBeUi3tT554ad-aF7q0DbFzi8ApAnH_u1aAEDhJb7eYKWGjPUNpAZ2WDVM5JQdZMc4l9XWgtEplXfR6FStIpZiOtW43nbtMLpMTkppR-Qt_JIJd9QwXYKkkJ4VxBAC0cDa07oNBwHhGfRN1zU8baTch7WOgZT1J2tEIzTUf7rOP4jHsNJj-tbh8f1Vg7MNpPgnwCt16UfBerYX0r1Z6AX7v3-lZGOos5TFpWuWj13-cJqkqpEqqYRBnANvmf-830WXHwzOpVhy1Nh4gxFyszmfrvkumoS_YXv4c9MvL4ghBj8HLZDzkVNmAFKQ0g=")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001887632033")) 
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Auto_forword_dd_bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "6133440326"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://Abdul12:Abdul12@cluster0.o6jx2be.mongodb.net/?retryWrites=true&w=majority")
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)
    ABOUT_BOT_TEXT = """<b> <a href='https://t.me/LazyUrlHunterrBOT'>Lazy Url Hunterr</a> is an open source project.

    Devs: 
        <a href='https://t.me/mRiderDM'>❤️ LazyDeveloper ❤️</a>
    
    
🤖 My Name: <a href='https://t.me/Official_Movies_Group'>Mdisk Search Robot</a>

📝 Language: <a href='https://www.python.org'>Python V3</a>

📚 Library: <a href='https://docs.pyrogram.org'>Pyrogram</a>

📡 Server: <a href='https://heroku.com'>Heroku</a>

📡 Server 2: <a href='https://heroku.com'>koyeb</a> <i>comming soon</i>

👨‍💻 Developer Channel: <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a></b>
"""

    ABOUT_HELP_TEXT = """<b>💋 Developer : <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a>

If You Want Your Own Bot Like This Then You Can Contact Our Developer.</b>
"""

    HOME_TEXT = """
<b>Hello Baby ! {}😅,

I'm the one and only fastest URL finder BOT. Add me to any Group and Give me Hunting rights !!

I will be only yours if you will restrict adding me to other groups.
Go to @BotFather to change settings.

Don't be sad ! Your all urls are in safe Hand.

»»» <b>Happy Hunting</b> «««

🔺Thank You <a href='https://t.me/LazyDeveloper'>LazyDeveloper</a>🔺 </b>
"""


    START_MSG = """
<b>Hello Baby ! {}😅,

I'm the one and only fastest URL & post finder BOT. Add me to any Group and Give me Hunting rights !!

Don't be sad ! Your all urls are in safe Hand.</b>

   »»»» <b>Happy Hunting</b> ««««

💸<b>Donate us to Keep service Alive.💸</b>
»» A small amount of ₹5 - ₹20 - ₹50 - ₹100 will be great help !
🔺 Thank You 🔺 
"""

