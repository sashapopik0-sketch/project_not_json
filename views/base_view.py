"""Модуль главного меню приложения менеджера заметок."""

import tkinter as tk
from views.add_note import AddNote
from views.all_note import AllNote
from views.by_id_note import ByIdNote
from views.title_note import TitleNote
from views.search_note import SearchNote


class BaseView(tk.Frame):
    """Главное меню приложения менеджера заметок.

    Предоставляет централизованное меню для навигации между различными
    функциональными окнами приложения: добавление, просмотр и поиск заметок.

    Attributes:
        children_windows: Список дочерних окон, открытых из главного меню.
        __title_label: Метка заголовка главного меню.
        __menu_label: Метка подзаголовка с инструкцией выбора действия.
        __button_add_note: Кнопка для открытия окна добавления заметки.
        __button_all_note: Кнопка для открытия окна просмотра всех заметок.
        __button_by_id_note: Кнопка для открытия окна просмотра заметки по ID.
        __button_title_notes: Кнопка для открытия окна просмотра названий заметок.
        __search_note: Кнопка для открытия окна поиска по заметкам.
    """

    def __init__(self, container: tk.Tk) -> None:
        """Инициализирует главное меню приложения.

        Создает фрейм главного меню с кнопками навигации и настраивает
        его визуальные параметры.

        Args:
            container: Родительское окно Tkinter, в котором размещается фрейм.
        """
        super().__init__(container, bg="#f8f9fa")
        
        self.children_windows: list = []
        
        self.__title_label: tk.Label
        self.__menu_label: tk.Label
        
        self.__button_add_note: tk.Button
        self.__button_all_note: tk.Button
        self.__button_by_id_note: tk.Button
        self.__button_title_notes: tk.Button
        self.__search_note: tk.Button
        
        self.__configure_widgets()
        self.__pack_widgets()

    def __configure_widgets(self) -> None:
        """Инициализирует и настраивает виджеты главного меню.

        Создает заголовок, подзаголовок и все кнопки навигации с единым
        стилем оформления и соответствующими обработчиками команд.
        """
        self.__title_label = tk.Label(
            self, 
            text="📝 Заметки", 
            font=("Arial", 32, "bold"),
            bg="#f8f9fa",
            fg="#212529"
        )

        self.__menu_label = tk.Label(
            self, 
            text="Выберите действие:", 
            font=("Arial", 16),
            bg="#f8f9fa",
            fg="#6c757d"
        )

        button_style = {
            "font": ("Arial", 12),
            "bg": "#28a745",
            "fg": "white",
            "relief": tk.FLAT,
            "padx": 25,
            "pady": 10,
            "cursor": "hand2",
            "width": 30
        }
        
        self.__button_add_note = tk.Button(
            self, 
            text="➕ Добавить заметку", 
            command=self.open_add_window,
            **button_style
        )
        
        self.__button_all_note = tk.Button(
            self, 
            text="📋 Просмотр всех заметок", 
            command=self.open_all_window,
            **button_style
        )
        
        self.__button_by_id_note = tk.Button(
            self, 
            text="🔍 Просмотр заметки по номеру", 
            command=self.open_by_id_window,
            **button_style
        )
        
        self.__button_title_notes = tk.Button(
            self, 
            text="🏷️ Просмотр названий заметок", 
            command=self.open_title_window,
            **button_style
        )
        
        self.__search_note = tk.Button(
            self, 
            text="🔎 Поиск по заметкам", 
            command=self.open_searech_note_window,
            **button_style
        )

    def __pack_widgets(self) -> None:
        """Размещает виджеты в фрейме главного меню.

        Упаковывает заголовок, подзаголовок и кнопки с заданными отступами
        и параметрами размещения для обеспечения центрированного и
        эстетически pleasing отображения.
        """
        self.__title_label.pack(pady=(40, 10))
        self.__menu_label.pack(pady=(0, 30))

        buttons = [
            self.__button_add_note,
            self.__button_all_note,
            self.__button_by_id_note,
            self.__button_title_notes,
            self.__search_note
        ]
        
        for btn in buttons:
            btn.pack(pady=8, padx=20)
    
    def open_add_window(self) -> None:
        """Открывает окно добавления новой заметки.

        Создает экземпляр AddNote и добавляет его в список дочерних окон.
        """
        window = AddNote(self.winfo_toplevel())
        self.children_windows.append(window)
    
    def open_all_window(self) -> None:
        """Открывает окно просмотра всех заметок.

        Создает экземпляр AllNote и добавляет его в список дочерних окон.
        """
        window = AllNote(self.winfo_toplevel())
        self.children_windows.append(window)
    
    def open_by_id_window(self) -> None:
        """Открывает окно просмотра заметки по ID.

        Создает экземпляр ByIdNote и добавляет его в список дочерних окон.
        """
        window = ByIdNote(self.winfo_toplevel())
        self.children_windows.append(window)
    
    def open_title_window(self) -> None:
        """Открывает окно просмотра названий заметок.

        Создает экземпляр TitleNote и добавляет его в список дочерних окон.
        """
        window = TitleNote(self.winfo_toplevel())
        self.children_windows.append(window)
    
    def open_searech_note_window(self) -> None:
        """Открывает окно поиска по заметкам.

        Создает экземпляр SearchNote и добавляет его в список дочерних окон.
        """
        window = SearchNote(self.winfo_toplevel())
        self.children_windows.append(window)
