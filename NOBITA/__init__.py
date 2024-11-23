from NOBITA.core.bot import NOBITA
from NOBITA.core.dir import dirr
from NOBITA.core.git import git
from NOBITA.core.userbot import Userbot
from NOBITA.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = NOBITA()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

