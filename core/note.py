"""Модуль модели заметки."""

from datetime import datetime
from typing import Optional


class Note:
    """Модель данных для представления заметки.

    Хранит основную информацию о заметке: идентификатор, название,
    текстовое содержание и дату создания.

    Attributes:
        id: Уникальный числовой идентификатор заметки.
        title: Название (заголовок) заметки.
        text: Текстовое содержание заметки.
        date: Дата создания заметки в строковом формате.
    """

    def __init__(
        self, 
        number: int, 
        title: str, 
        text: str, 
        date: Optional[str] = None
    ) -> None:
        """Инициализирует объект заметки.

        Args:
            number: Уникальный числовой идентификатор заметки.
            title: Название (заголовок) заметки.
            text: Текстовое содержание заметки.
            date: Дата создания заметки в строковом формате.
                  Если не указана, будет использована текущая дата и время.
        """
        self.id: int = number
        self.title: str = title
        self.text: str = text
        self.date: str = date or datetime.now().strftime("%d.%m.%Y %H:%M")