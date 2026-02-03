"""Модуль состояния для работы с JSON-хранилищем заметок."""

from state.base_state import BaseState
from core.json_storage import JsonStorage
from core.note import Note
from typing import List


class JsonState(BaseState):
    """Состояние для управления заметками через JSON-хранилище.

    Реализует паттерн 'Состояние' и 'Singleton' для работы с заметками,
    хранящимися в JSON-файле. Обеспечивает загрузку и сохранение данных
    через JsonStorage.

    Attributes:
        __instance: Экземпляр класса для реализации паттерна Singleton.
        storage: Экземпляр JsonStorage для работы с файловой системой.
        _initialized: Флаг инициализации для предотвращения повторной инициализации.
    """

    __instance: 'JsonState' = None

    def __new__(cls) -> 'JsonState':
        """Создает или возвращает существующий экземпляр класса (Singleton).

        Реализует паттерн Singleton, обеспечивая существование только одного
        экземпляра класса JsonState.

        Returns:
            Единственный экземпляр класса JsonState.
        """
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, filepath: str = "data/notes.json") -> None:
        """Инициализирует состояние JSON-хранилища.

        Инициализирует JsonStorage с указанным путем к файлу. Благодаря флагу
        _initialized, инициализация происходит только при первом создании
        экземпляра (из-за паттерна Singleton).

        Args:
            filepath: Путь к JSON-файлу для хранения заметок.
                      По умолчанию "data/notes.json".
        """
        if getattr(self, '_initialized', False):
            return
        else:
            self._initialized = True

        self.storage = JsonStorage(filepath)

    def load_notes(self) -> List[Note]:
        """Загружает список заметок из JSON-файла.

        Читает данные из JSON-файла через JsonStorage и преобразует их
        в список объектов Note.

        Returns:
            Список объектов Note, загруженных из JSON-файла.
        """
        data = self.storage.read_data()
        return [self.storage.dict_to_note(item) for item in data]

    def save_notes(self, notes: List[Note]) -> None:
        """Сохраняет список заметок в JSON-файл.

        Преобразует список объектов Note в формат, подходящий для JSON,
        и записывает данные в файл через JsonStorage.

        Args:
            notes: Список объектов Note для сохранения.
        """
        data = [self.storage.note_to_dict(note) for note in notes]
        self.storage.write_data(data)