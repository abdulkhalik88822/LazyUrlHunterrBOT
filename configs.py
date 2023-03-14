# in & as LazyDeveloper
# Please Don't Remove Credit

import os


class Config(object):
    API_ID = int(os.environ.get("API_ID", "21872317'))
    API_HASH = os.environ.get("API_HASH', '1154f54e18b67c1239f9674c643b7bcb')
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6265513460:AAEVABfwA8nb-OamLRm_aTEzP9kUlsnvzos")
    BOT_SESSION_NAME = os.environ.get("BOT_SESSION_NAME", "MdiskSearchBot")
    USER_SESSION_STRING = os.environ.get("USER_SESSION_STRING", "1BVtsOJcBu3_a72xEoGQt8kT3LG9MFfTqsb8lH39QJzDyWv-feNShOGSOq6u3_UisU_70_F4LoOxDk6B7YnTCV3lcLMmGitajkf7vMvh5ri9-GB0or9jvKUVnC2fQx5ViXS3Yt38QgwrwUQbPT8jjpkj7yxarVjNDVSGP1jn2u6SIyRXmQ4id58S0HXkmjnBIaqYWvoENuLHfK6R0jb227t78NWrgxiaFkQ0UAL61_xUSFEXtzwn_YfnH6AZa87sANCjso3tj5CsafMv1q-f_fuPjsJs_mnl2hFa7q-NPCY_SrazNyKSCS7yMU08h_i3k5c4jqEhujQwR9n3qtpnswRByvqgn1IM=")
    CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001887632033")) 
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Auto_forword_dd_bot")
    BOT_OWNER = int(os.environ.get("BOT_OWNER", "6133440326"))
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://kailash:pass@cluster0.sqtztxm.mongodb.net/?retryWrites=true&w=majority")
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

