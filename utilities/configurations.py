import configparser

import pandas


def getConfig():
    config = configparser.ConfigParser()
    config.read('utilities/properties.ini')
    return config


def getPassword():
    return 'wibcoj-5kihxo-fefcUz'


def getCsv(filename):
    csv = pandas.read_csv(filename)
    return csv


# generate a dictionary using values from properties.ini
# connect_config = {
#     'user': getConfig()['SQL']['user'],
#     'password': getConfig()['SQL']['password'],
#     'host': getConfig()['SQL']['host'],
#     'database': getConfig()['SQL']['password']
# }
