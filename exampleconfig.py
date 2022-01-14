import os


class Development(Config):
  # get this values from my.telegram.org. 
  # 6 is just a placeholder. Fill your own api id & hash.
  APP_ID = 6
  API_HASH = "eb06d4abfb49dc3eeb1aeb98ae0f581e"

  # the name to display in your alive message.
  # If not filled anything then default value is LEGEND User.
  ALIVE_NAME = "Pro Boy"

  # create any PostgreSQL database.
  # I recommend to use elephantsql and paste that link here
  DB_URI = "Your value"

  # After cloning the repo and installing requirements...
  # String session will be saved in your saved message of telegram.
  # Put that string here.
  PRO_STRING = "Your value"

  # Create a bot in @botfather and fill the following values with bot token and username.
  BOT_TOKEN = "Your value" #token
  BOT_USERNAME = "Your value" #username

  # Create a private group and add rose bot to it.
  # and type /id and paste that id here.
  # replace that -100 with that group id.
  LOGGER_ID = -100

  # Custom Command Handler. 
  HANDLER = os.environ.get("HANDLER", r"\.")
  #User Command Handler
  HANDLER = os.environ.get("HANDLER", r"\.")
  # enter the userid of sudo users.
  # you can add multiple ids by separating them by space.
  # fill values in [] only.
  SUDO_USERS = []

  # command hanler for sudo users.
  SUDO_HANDLER = os.environ.get("SUDO_HANDLER", r"\,")
