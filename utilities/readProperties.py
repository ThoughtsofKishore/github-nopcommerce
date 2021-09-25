import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:

    @staticmethod
    def getURL():
        url = config.get("Common Info", "baseURL")
        return url

    @staticmethod
    def getUserName():
        username = config.get("Common Info", "username")
        return username

    @staticmethod
    def getPassword():
        password = config.get("Common Info", "password")
        return password

