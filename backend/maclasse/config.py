import json

with open("maclasse/config.json") as config_file:
    config = json.load(config_file)


class Config:
    SQLALCHEMY_DATABASE_URI = config.get("SQLALCHEMY_DATABASE_URI")
    SQLALCHEMY_TRACK_MODIFICATIONS = config.get("SQLALCHEMY_TRACK_MODIFICATIONS")
