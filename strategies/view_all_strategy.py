"""Модуль стратегии отображения всех заметок."""

from strategies.base_strategy import BaseStrategy
from core.note import Note
from typing import List


class ViewAllStrategy(BaseStrategy):
    """Стратегия отображения всех заметок в форматированном виде.

    Реализует паттерн 'Стратегия' для форматирования и вывода полного
    списка всех заметок. Наследуется от абстрактного базового класса
    BaseStrategy.
    """

    def execute(self, notes: List[Note]) -> str:
        """Форматирует и возвращает строковое представление всех заметок.

        Преобразует список объектов Note в отформатированную строку,
        где каждая заметка отображается с ID, названием, текстом и датой,
        разделенных декоративной линией.

        Args:
            notes: Список объектов Note для форматирования.

        Returns:
            Отформатированная строка со всеми заметками или пустая
            строка, если список заметок пуст.
        """
        result = []
        for note in notes:
            result.append(f"ID: {note.id}")
            result.append(f"Название: {note.title}")
            result.append(f"Текст: \n{note.text}")
            result.append(f"Дата: {note.date}")
            result.append("=" * 40) 

        return "\n".join(result)