import datetime
import logging
import shutil

import config


def copy_date(cur_dir, dst_dir, blok):
    """
    Функция копирования файлов из cur_dir в dst_dir, blok это блок из конфига
    """
    dt = datetime.datetime.now()
    cur_date = dt.strftime('%Y_%m_%d-%H%M')
    logging.basicConfig(filename="log.log", level=logging.INFO)
    dst_dir = dst_dir + '/' + cur_date
    try:
        shutil.copytree(cur_dir, dst_dir)
        logging.info(cur_date + " Start copy" + blok)
    except OSError as why:
        logging.error(cur_date + ' ' + str(why))
    except IOError as why:
        logging.error(str(why))
    logging.info(cur_date + " Finish copy" + blok)


path = "settings.ini"
cfg_file = config.get_config(path)
for el in cfg_file.sections():
    if el != 'mail':
        cur_dir = config.get_setting(path, el, 'cur_dir')
        dst_dir = config.get_setting(path, el, 'dst_dir')
        copy_date(cur_dir, dst_dir, el)
