import datetime
import logging
import shutil

import config
import mail_send


def copy_date(cur_dir, dst_dir, blok):
    """
    Функция копирования файлов из cur_dir в dst_dir, blok это блок из конфига
    cur_date: дата в виде строки добавляется к имени каталога назначения копирования
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
        mail_send.send_err(str(why))
    except IOError as why:
        logging.error(str(why))
        mail_send.send_err(str(why))
    logging.info(cur_date + " Finish copy" + blok)


cfg_file = config.get_config()
''' 
Читаем конфиг по секциям, пропускаем секцию mail и делаем копирование
'''
for el in cfg_file.sections():
    if el != 'mail' and el != 'area':
        cur_dir = config.get_setting(el, 'cur_dir')
        dst_dir = config.get_setting(el, 'dst_dir')
        copy_date(cur_dir, dst_dir, el)
