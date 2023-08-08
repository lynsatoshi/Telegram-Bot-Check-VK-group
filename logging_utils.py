import logging
from logging.handlers import TimedRotatingFileHandler
import os
from config import LOGS_DIR
from datetime import datetime

logs_files = LOGS_DIR

log_filename = f'app-{datetime.now().strftime("%Y-%m-%d")}.log'  # Формирование имени файла с логами на основе текущей даты

# Создание обработчика для ротации логов каждый день и удаления старых файлов через неделю
log_handler = TimedRotatingFileHandler(os.path.join(logs_files, log_filename),
                                       when='midnight',
                                       interval=1,  # Ротация каждый день
                                       backupCount=7)
log_handler.setLevel(logging.DEBUG)

# Установка форматирования сообщений логов
log_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
log_handler.setFormatter(log_formatter)

# Получение корневого логгера
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Добавление обработчика к корневому логгеру
logger.addHandler(log_handler)
