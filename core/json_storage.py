"""Модуль для работы с JSON-хранилищем заметок."""

import json
from core.note import Note
from pathlib import Path
from typing import List, Dict, Any


class JsonStorage:
    """Класс для чтения и записи заметок в JSON-файл.

    Обеспечивает сериализацию и десериализацию объектов Note в формат JSON
    и обратно. Работает с файловой системой через pathlib.Path.

    Attributes:
        filepath: Путь к JSON-файлу для хранения заметок.
    """

    def __init__(self, filepath: str = "data/notes.json") -> None:
        """Инициализирует JSON-хранилище.

        Args:
            filepath: Путь к JSON-файлу для хранения заметок.
                      По умолчанию "data/notes.json".
        """
        self.filepath: Path = Path(filepath)

    def read_data(self) -> List[Dict[str, Any]]:
        """Читает данные из JSON-файла.

        Загружает данные из указанного JSON-файла. В случае отсутствия файла
        или ошибки парсинга JSON возвращает пустой список.

        Returns:
            Список словарей с данными заметок или пустой список при ошибке.
        """
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def write_data(self, data: List[Dict[str, Any]]) -> None:
        """Записывает данные в JSON-файл.

        Сохраняет переданные данные в указанный JSON-файл с форматированием
        и поддержкой кириллицы.

        Args:
            data: Список словарей с данными заметок для сохранения.
        """
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

    @staticmethod
    def note_to_dict(note: Note) -> Dict[str, Any]:
        """Преобразует объект Note в словарь.

        Сериализует объект Note в формат словаря, подходящий для JSON.

        Args:
            note: Объект Note для преобразования.

        Returns:
            Словарь с полями id, title, text и date.
        """
        return {
            "id": note.id,
            "title": note.title,
            "text": note.text,
            "date": note.date
        }

    @staticmethod
    def dict_to_note(data: Dict[str, Any]) -> Note:
        """Преобразует словарь в объект Note.

        Десериализует словарь с данными заметки в объект Note.

        Args:
            data: Словарь с полями id, title, text и date.

        Returns:
            Объект Note, созданный из данных словаря.

        Raises:
            KeyError: Если в словаре отсутствуют необходимые ключи.
        """
        return Note(
            number=data["id"],
            title=data["title"],
            text=data["text"],
            date=data["date"]
        )