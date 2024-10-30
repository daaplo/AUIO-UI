import logging
import os
import time
from config.conf import base_dir
import colorlog

log_colors_config = {
    'DEBUG': 'white',
    'INFO': 'green',
    'WARNING': 'yellow',
    'ERROR': 'red',
    'CRITICAL': 'bold_red',
}
log = logging.getLogger('log_name')
# 输出控制台
console_handler = logging.StreamHandler()
daytime = time.strftime('%Y-%m-%d', time.localtime(time.time()))
path = base_dir + '/log/'
if not os.path.exists(path):
    os.makedirs(path)
file_name = path + f'/run_log_{daytime}.log'
# 输出文件
file_handler = logging.FileHandler(filename=file_name, encoding='utf-8', mode='a')

log.setLevel(logging.DEBUG)
console_handler.setLevel(logging.DEBUG)
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter(
    fmt='[%(levelname)s] [%(asctime)s: %(msecs)03d]: %(message)s %(filename)s -> %(funcName)s line:%(lineno)d',
    datefmt='%Y-%m-%d %H:%M:%S'
)
console_formatter = colorlog.ColoredFormatter(
    fmt='[%(levelname)s] %(log_color)s[%(asctime)s: %(msecs)03d]: %(message)s %(filename)s ->%(funcName)s  line:%(lineno)d',
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors=log_colors_config
)
console_handler.setFormatter(console_formatter)
file_handler.setFormatter(file_formatter)

if not log.handlers:
    log.addHandler(console_handler)
    log.addHandler(file_handler)
console_handler.close()
file_handler.close()

if __name__ == '__main__':
    log.debug('debug')
    log.info('info')
    log.warning('warning')
    log.error('error')
    log.critical('critical')