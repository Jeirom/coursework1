import datetime
from typing import Optional
from dateutil.relativedelta import relativedelta

from src.utils import (date_now, date_three_months_ago, load_or_make,
                       open_xlsx_file, time_for_func)
import logging


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s: %(filename)s: %(levelname)s: %(message)s",
    filename="../logs/main.log",
    filemode="w",
    encoding="utf=8"
    )
main_logger = logging.getLogger("Universal logger")

@load_or_make(r"..\\data\\result.json")
def spending_by_category(file_path: str, word: str, date: Optional[str] = None):
    """Главная функция. Принимает на вход имя файла, слово для поиска, опционально - дату. Результат передает
    в декоратора, сохраняет файл в папке data"""

    main_logger.info(f'Start program; '
                     f'{file_path}, '
                     f'{word}, '
                     f'{date}')

    try:
        data_frame = open_xlsx_file(file_path)
        main_logger.info('ok')
    except Exception as error_file:
        main_logger.critical('File not open. Analysis is required')
    filtered_rows = []
    filtered_date = []

    try:
        for index, row in data_frame.iterrows():
            if word in str(row.values):
                 filtered_rows.append(dict(row))
        main_logger.info('ok')

    except Exception as e:
        main_logger.critical(f'Error {e}')
        return f'Error {e}.Call support, they won"t help you there'

    try:
        if not date:
            time_now = time_for_func()
            time_now2 = date_now()
            date_threshold = datetime.datetime.strptime(time_now, "%d.%m.%Y")
            time_start = datetime.datetime.strptime(time_now2, "%d.%m.%Y")
            for d in filtered_rows:
                if time_start >= datetime.datetime.strptime(d["Дата платежа"], "%d.%m.%Y") >= date_threshold:
                    filtered_date.append(dict(d))
        else:
            time_now = date_three_months_ago(date)
            date_threshold = datetime.datetime.strptime(time_now, "%d.%m.%Y")
            new_date = date_threshold + relativedelta(months=3)
            for d in filtered_rows:
                if new_date >= datetime.datetime.strptime(d["Дата платежа"], "%d.%m.%Y") >= date_threshold:
                    filtered_date.append(dict(d))
        main_logger.info('ok')
    except Exception as error:
        main_logger.warning(f'Error {error}. Check programs. Need debug')
        return f"Error {error}. If you haven't called support yet, don't call"
    return filtered_date


file = "../data/operations.xlsx"
catg = "Супермаркеты"
# time = '01.03.2021'
print(spending_by_category(file, catg))
