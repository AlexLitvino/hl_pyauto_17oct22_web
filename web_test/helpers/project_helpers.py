from configparser import ConfigParser


def get_config():
    config = ConfigParser()
    config.read('config.ini')
    return config


def get_base_url():
    return get_config().get('project', 'base_url')


def get_browser_name():
    return get_config().get('project', 'browser_name')
