"""Модуль стратегии поиска заметок по ключевому слову."""

from strategies.base_strategy import BaseStrategy
from core.note import Note
from typing import List


class SearchKeywordStrategy(BaseStrategy):
    """Стратегия поиска заметок по ключевому слову.

    Реализует паттерн 'Стратегия' для поиска заметок, содержащих
    заданное ключевое слово в тексте. Наследуется от абстрактного
    базового класса BaseStrategy.

    Attributes:
        __data: Ключевое слово для поиска в тексте заметок.
    """

    def __init__(self, data: str) -> None:
        """Инициализирует стратегию поиска по ключевому слову.

        Args:
            data: Ключевое слово для поиска в тексте заметок.
        """
        self.__data = data

    def execute(self, notes: List[Note]) -> str:
        """Выполняет поиск заметок по ключевому слову и форматирует результат.

        Производит поиск заданного ключевого слова в тексте каждой заметки
        (сравнение по словам, разделенным пробелами). Возвращает
        отформатированную строку со всеми найденными заметками.

        Args:
            notes: Список объектов Note для обработки.

        Returns:
            Отформатированная строка с найденными заметками или пустая
            строка, если заметки не найдены.
        """
        result = []
        for note in notes:
            for word in note.text.split():
                if word == self.__data:
                    result.append(f"ID: {note.id}")
                    result.append(f"Название: {note.title}")
                    result.append(f"Текст: \n{note.text}")
                    result.append(f"Дата: {note.date}")
                    result.append("=" * 40)
        return "\n".join(result)