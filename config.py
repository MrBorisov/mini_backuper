import configparser
import os


def create_config(path):
    """
    Create a config file
    """
    config = configparser.ConfigParser()
    config.add_section("Settings")
    config.set("Settings", "cur_dir", "None")
    config.set("Settings", "dst_dir", "None")
    config.set("Settings", "dir_info", "You are copying from %(cur_dir)s to %(dst_dir)s")

    config.add_section("mail")
    config.set("mail", "mail_to", "None")
    config.set("mail", "mail_smtp", "None")
    config.set("mail", "mail_pass", "None")
    config.set("mail", "mail_info", "You are send to %(mail_to)s from %(mail_smtp)s")
    with open(path, "w") as config_file:
        config.write(config_file)


def get_config(path):
    """
    Returns the config object
    """
    if not os.path.exists(path):
        create_config(path)

    config = configparser.ConfigParser()
    config.read(path)
    return config


def get_setting(path, section, setting):
    """
    Print out a setting
    """
    config = get_config(path)
    value = config.get(section, setting)
    msg = "{section} {setting} is {value}".format(
        section=section, setting=setting, value=value
    )

    print(msg)
    return value


def update_setting(path, section, setting, value):
    """
    Update a setting
    """
    config = get_config(path)
    config.set(section, setting, value)
    with open(path, "w") as config_file:
        config.write(config_file)


def delete_setting(path, section, setting):
    """
    Delete a setting
    """
    config = get_config(path)
    config.remove_option(section, setting)
    with open(path, "w") as config_file:
        config.write(config_file)


if __name__ == "__main__":
    path = "settings.ini"
    cur_dir = get_setting(path, 'Settings', 'cur_dir')
    dest_dir = get_setting(path, 'Settings', 'dst_dir')