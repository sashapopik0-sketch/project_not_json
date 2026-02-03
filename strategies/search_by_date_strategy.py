"""Модуль стратегии поиска заметок по дате."""

from strategies.base_strategy import BaseStrategy
from core.note import Note
from typing import List


class SearchByDateStrategy(BaseStrategy):
    """Стратегия поиска заметок по дате создания.

    Реализует паттерн 'Стратегия' для фильтрации и форматирования
    заметок по заданной дате. Наследуется от абстрактного базового класса
    BaseStrategy.

    Attributes:
        __data: Строка с датой для поиска заметок.
    """

    def __init__(self, data: str) -> None:
        """Инициализирует стратегию поиска по дате.

        Args:
            data: Строка с датой в формате, соответствующем формату
                  хранения даты в объектах Note (например, "DD.MM.YYYY HH:MM").
        """
        self.__data = data

    def execute(self, notes: List[Note]) -> str:
        """Выполняет поиск заметок по дате и форматирует результат.

        Фильтрует список заметок, оставляя только те, у которых дата
        совпадает с заданной. Возвращает отформатированную строку с
        результатами поиска.

        Args:
            notes: Список объектов Note для обработки.

        Returns:
            Отформатированная строка с найденными заметками или пустая
            строка, если заметки не найдены.
        """
        notes = [note for note in notes if note.date == self.__data]
        results = []
        for note in notes:
            results.append(f"Название: {note.title}")
            results.append(f"Текст: \n{note.text}")
            results.append(f"Дата: {note.date}")
            results.append("-" * 40)

        return "\n".join(results)