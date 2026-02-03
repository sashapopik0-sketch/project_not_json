"""Модуль стратегии поиска заметок по названию."""

from strategies.base_strategy import BaseStrategy
from core.note import Note
from typing import List


class SearchTitleStrategy(BaseStrategy):
    """Стратегия поиска заметок по точному совпадению названия.

    Реализует паттерн 'Стратегия' для фильтрации заметок по заданному
    названию. Наследуется от абстрактного базового класса BaseStrategy.

    Attributes:
        __ Строка с названием для поиска заметок.
    """

    def __init__(self,  data: str) -> None:
        """Инициализирует стратегию поиска по названию.

        Args:
             Строка с названием заметки для поиска (точное совпадение).
        """
        self.__data = data

    def execute(self, notes: List[Note]) -> str:
        """Выполняет поиск заметок по названию и форматирует результат.

        Фильтрует список заметок, оставляя только те, у которых название
        точно совпадает с заданным. Возвращает отформатированную строку
        с результатами поиска.

        Args:
            notes: Список объектов Note для обработки.

        Returns:
            Отформатированная строка с найденными заметками или пустая
            строка, если заметки не найдены.
        """
        results = [note for note in notes if note.title == self.__data]

        output = []
        for note in results:
            output.append(f"Название: {note.title}")
            output.append(f"Текст: \n{note.text}")
            output.append(f"Дата: {note.date}")
            output.append("-" * 40)

        return "\n".join(output)