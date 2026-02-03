"""Модуль стратегии отображения списка названий заметок."""

from strategies.base_strategy import BaseStrategy
from core.note import Note
from typing import List


class SearchTitlesStrategy(BaseStrategy):
    """Стратегия отображения только названий всех заметок.

    Реализует паттерн 'Стратегия' для извлечения и форматирования
    списка названий заметок без дополнительной информации.
    Наследуется от абстрактного базового класса BaseStrategy.
    """

    def execute(self, notes: List[Note]) -> str:
        """Извлекает и возвращает список названий всех заметок.

        Преобразует список объектов Note в строку, содержащую только
        названия заметок, каждое с новой строки.

        Args:
            notes: Список объектов Note для обработки.

        Returns:
            Строка с названиями заметок, разделенными символом новой строки,
            или пустая строка, если список заметок пуст.
        """
        list_titles = []
        for note in notes:
            list_titles.append(note.title)
        return "\n".join(list_titles)