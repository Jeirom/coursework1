import datetime
import json
from typing import Any

import pandas as pd
from dateutil.relativedelta import relativedelta


def open_xlsx_file(path_file: str) -> pd.DataFrame:
    """Минималистичная функция для открытия файла. Используется в головной функции"""
    result = pd.read_excel(path_file)
    return result


def time_for_func() -> str:
    """Функция решает когда будет три месяца назад от нынешнего момента"""
    return date_three_months_ago(date_now())


def date_three_months_ago(date: Any) -> str:
    """Функция подбивает трехмесячный отрезок. Используется в головной функции"""
    date_format = "%d.%m.%Y"
    date = datetime.datetime.strptime(date, date_format)
    new_date = date - relativedelta(months=3)
    return new_date.strftime(date_format)


def date_now() -> str:
    """Функция дает дату в формате ниже на данный момент времени"""
    now = datetime.datetime.now()
    formatted_date = now.strftime("%d.%m.2021")
    return formatted_date


def load_or_make(file_name: str):
    """Декоратор принимающий путь до файла, записывает туда результат из функции main."""

    def decorator(func: Any):
        def wrapped(*args: Any):

            data = func(*args)
            with open(file_name, "w", encoding="utf=8") as out:
                json.dump(data, out, ensure_ascii=False, indent=4)

        return wrapped

    return decorator


def load_not_filename():
    """Результат соития ctrl+c+load_or_make, не принимает путь до файла."""

    def decorator(func):
        def wrapped(*args):

            data = func(*args)
            with open(r"..\data\load_result.json", "w", encoding="utf=8") as out:
                json.dump(data, out, ensure_ascii=False, indent=4)

        return wrapped

    return decorator
