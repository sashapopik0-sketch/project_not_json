"""Модуль стратегии поиска заметки по ID."""

from strategies.base_strategy import BaseStrategy
from core.note import Note
from typing import List


class SearchByIDStrategy(BaseStrategy):
    """Стратегия поиска заметки по уникальному идентификатору.

    Реализует паттерн 'Стратегия' для поиска заметки по заданному ID.
    Наследуется от абстрактного базового класса BaseStrategy.

    Attributes:
        __data: Целочисленный идентификатор заметки для поиска.
    """

    def __init__(self, data: int) -> None:
        """Инициализирует стратегию поиска по ID.

        Args:
            data: Уникальный идентификатор заметки для поиска.
        """
        self.__data = data

    def execute(self, notes: List[Note]) -> str:
        """Выполняет поиск заметки по ID и форматирует результат.

        Производит поиск заметки с заданным ID в списке заметок.
        Возвращает отформатированную строку с найденной заметкой.

        Args:
            notes: Список объектов Note для обработки.

        Returns:
            Отформатированная строка с найденной заметкой или пустая
            строка, если заметка не найдена.
        """
        result = []
        for note in notes:
            if note.id == self.__data:
                result.append(f"ID: {note.id}")
                result.append(f"Название: {note.title}")
                result.append(f"Текст: \n{note.text}")
                result.append(f"Дата: {note.date}")
                result.append("=" * 40) 

        return "\n".join(result)