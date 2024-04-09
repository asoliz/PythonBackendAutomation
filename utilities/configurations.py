import configparser


def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


def getPassword():
    return 'wibcoj-5kihxo-fefcUz'
