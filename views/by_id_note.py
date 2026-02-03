"""Модуль окна просмотра заметки по ID."""

import tkinter as tk
from strategies.view_by_id_strategy import SearchByIDStrategy
from state.json_state import JsonState


class ByIdNote(tk.Toplevel):
    """Окно для просмотра заметки по уникальному идентификатору.

    Предоставляет пользовательский интерфейс для ввода ID заметки
    и отображения найденной заметки с использованием стратегии поиска.

    Attributes:
        parent: Родительское окно Tkinter.
        state: Экземпляр JsonState для загрузки данных заметок.
        __label_id: Метка для поля ввода ID заметки.
        __entry_id: Поле ввода для ID заметки.
        __button_search: Кнопка для инициации поиска заметки.
        __label_note: Метка для отображения найденной заметки.
        __label_error: Метка для отображения сообщений об ошибках.
    """

    def __init__(self, parent: tk.Tk) -> None:
        """Инициализирует окно просмотра заметки по ID.

        Создает дочернее окно Toplevel, настраивает его параметры,
        инициализирует виджеты и устанавливает иконку приложения.

        Args:
            parent: Родительское окно Tkinter.
        """
        super().__init__(parent)
        self.parent = parent
        
        self.state = JsonState()
        
        self.__configure_window()
        self.__configure_widgets()
        self.__pack_widgets()
        self.__add_icon()
        
        self.__label_id: tk.Label
        self.__entry_id: tk.Entry
        self.__button_search: tk.Button
        
        self.__label_note: tk.Label
        self.__label_error: tk.Label

    def __configure_window(self) -> None:
        """Настраивает параметры окна просмотра заметки по ID.

        Устанавливает заголовок, размеры и цвет фона окна.
        """
        self.title("Просмотр заметки по номеру")
        self.geometry("700x500")
        self.configure(bg="#f8f9fa")
    
    def __configure_widgets(self) -> None:
        """Инициализирует и настраивает виджеты окна.

        Создает все необходимые элементы интерфейса: метки, поле ввода,
        кнопку поиска и метки для отображения результата и ошибок
        с соответствующими стилями и параметрами.
        """
        self.__label_id = tk.Label(
            self, 
            text="Введите номер заметки:", 
            font=("Arial", 12, "bold"),
            bg="#f8f9fa",
            fg="#212529"
        )

        self.__entry_id = tk.Entry(
            self,
            font=("Arial", 11),
            relief=tk.FLAT,
            bg="white",
            highlightbackground="#ced4da",
            highlightcolor="#28a745",
            highlightthickness=1,
            width=30
        )

        self.__button_search = tk.Button(
            self, 
            text="🔍 Найти заметку", 
            command=self.__show_note,
            font=("Arial", 12, "bold"),
            bg="#28a745",
            fg="white",
            relief=tk.FLAT,
            padx=25,
            pady=10,
            cursor="hand2"
        )

        self.__label_note = tk.Label(
            self, 
            text="", 
            font=("Arial", 11),
            bg="#f8f9fa",
            fg="#212529",
            justify=tk.LEFT,
            wraplength=600 
        )

        self.__label_error = tk.Label(
            self, 
            text="", 
            foreground="#dc3545",
            font=("Arial", 11, "bold"),
            bg="#f8f9fa"
        )
    
    def __pack_widgets(self) -> None:
        """Размещает виджеты в окне.

        Упаковывает все элементы интерфейса с заданными отступами и параметрами
        размещения для обеспечения корректного отображения и удобства
        использования.
        """
        self.__label_id.pack(anchor="w", padx=30, pady=(20, 5))
        self.__entry_id.pack(pady=(0, 20), padx=30)
        self.__button_search.pack(pady=20)
        self.__label_note.pack(padx=30, pady=10, anchor="w")
        self.__label_error.pack(pady=10)
    
    def __add_icon(self) -> None:
        """Устанавливает иконку окна.

        Загружает иконку из файла 'static/icons/app.ico' и устанавливает
        ее для текущего окна.

        Raises:
            FileNotFoundError: Если файл иконки не найден.
            tk.TclError: Если формат иконки не поддерживается.
        """
        self.iconbitmap("static/icons/app.ico")
    
    def __show_note(self) -> None:
        """Отображает заметку по введенному ID.

        Очищает предыдущие результаты, загружает все заметки через JsonState,
        применяет стратегию SearchByIDStrategy для поиска заметки по ID
        и отображает результат. Если заметка не найдена, показывает
        соответствующее сообщение об ошибке.
        """
        self.__label_note["text"] = ""
        self.__label_error["text"] = ""
        notes = self.state.load_notes()
        strategy = SearchByIDStrategy(int(self.__entry_id.get()))
        if strategy.execute(notes):
            self.__label_note["text"] += strategy.execute(notes)
        else:
            self.__label_error["text"] = "Заметки с таким номером не найдено"