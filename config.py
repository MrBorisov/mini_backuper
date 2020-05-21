import configparser
import os


def create_config(path='settings.ini'):
    """
    Create a config file
    Для отправки почты пропишите настройки почты в конфиге ручками.
    """
    config = configparser.ConfigParser()
    config.add_section('Settings')
    config.set('Settings', 'cur_dir', 'None')
    config.set('Settings', 'dst_dir', 'None')
    config.set('Settings', 'count', 'None')
    config.set('Settings', 'dir_info', 'You are copying from %(cur_dir)s to %(dst_dir)s')


    config.add_section('mail')
    config.set('mail', 'mail_from', 'None')
    config.set('mail', 'mail_subj', 'None')
    config.set('mail', 'mail_coding', 'windows-1251')
    config.set('mail', 'mysmtp', 'None')
    config.set('mail', 'smtp_port', 'None')
    config.set('mail', 'smtp_user', 'None')
    config.set('mail', 'smtp_pwd', 'None')
    config.set('mail', 'mail_to', 'None')
    config.set('mail', 'mail_info', 'You are send to %(mail_to)s from %(mail_smtp)s')
    with open(path, 'w') as config_file:
        config.write(config_file)


def get_config(path='settings.ini'):
    """
    Returns the config object
    """
    if not os.path.exists(path):
        create_config(path)
    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_setting(section, setting, path='settings.ini'):
    """
    Print out a setting
    """
    config = get_config(path)
    value = config.get(section, setting)
    return value


def update_setting(section, setting, value, path='settings.ini'):
    """
    Update a setting
    """
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, 'w') as config_file:
        config.write(config_file)


def delete_setting(section, setting, path='settings.ini'):
    """
    Delete a setting
    """
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, 'w') as config_file:
        config.write(config_file)


if __name__ == "__main__":
    path = 'settings.ini'
    cur_dir = get_setting(path, 'Settings', 'cur_dir')
    dest_dir = get_setting(path, 'Settings', 'dst_dir')
