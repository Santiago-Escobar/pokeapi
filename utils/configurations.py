import configparser

def getConfig():
    config = configparser.ConfigParser()
    config.read('utils/properties.ini')
    return config
