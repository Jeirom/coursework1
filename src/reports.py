from src.main import spending_by_category
from typing import Optional

def start_programs(file_path: str, word: str, date: Optional[str] = None):
    spending_by_category(file_path,word,date)


file = r'..\data\operations.xlsx'
word = 'Супермаркеты'
print(start_programs(file,word))