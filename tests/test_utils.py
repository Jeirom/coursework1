from unittest import Mock
from unittest.mock import mock_open

import pandas as pd
import unittest
from conftest import *
from src.utils import open_xlsx_file

data = [
    {
        "Дата операции": "06.10.2021 16:32:03",
        "Дата платежа": "06.10.2021",
        "Номер карты": "*7197",
        "Статус": "OK",
        "Сумма операции": -94.82,
        "Валюта операции": "RUB",
        "Сумма платежа": -94.82,
        "Валюта платежа": "RUB",
        "Кэшбэк": 'NaN',
        "Категория": "Супермаркеты",
        "MCC": 5411.0,
        "Описание": "Колхоз",
        "Бонусы (включая кэшбэк)": 1,
        "Округление на инвесткопилку": 0,
        "Сумма операции с округлением": 94.82
    }]


def test_open_xlsx_file(file):
    mock_data = Mock(return_value=data)
    pd.read_excel = mock_data
    assert open_xlsx_file() == data
    mock_data.assert_called_once_with()