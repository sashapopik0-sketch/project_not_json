"""Модуль окна расширенного поиска по заметкам."""

import tkinter as tk
from strategies.search_by_date_strategy import SearchByDateStrategy
from strategies.search_by_title_strategy import SearchTitleStrategy
from strategies.search_by_keyword_strategy import SearchKeywordStrategy
from state.json_state import JsonState


class SearchNote(tk.Toplevel):
    """Окно для расширенного поиска по заметкам.

    Предоставляет пользовательский интерфейс для выполнения поиска
    по различным критериям: дата, название или ключевые слова,
    с возможностью прокрутки длинных результатов через Canvas и Scrollbar.

    Attributes:
        state: Экземпляр JsonState для загрузки данных заметок.
        __entry_word_search: Поле ввода для поискового запроса.
        __button_by_date: Кнопка для поиска по дате.
        __button_by_keyword: Кнопка для поиска по ключевым словам.
        __button_by_title: Кнопка для поиска по названию.
        __label_result: Метка для отображения результатов поиска.
        __label_error: Метка для отображения сообщений об ошибках.
        __canvas: Canvas для создания прокручиваемой области.
        __scrollbar: Вертикальный скроллбар для прокрутки содержимого.
        __scrollable_frame: Frame внутри Canvas для размещения меток.
    """

    def __init__(self, parent: tk.Tk) -> None:
        """Инициализирует окно расширенного поиска.

        Создает дочернее окно Toplevel, настраивает его параметры,
        инициализирует виджеты и устанавливает иконку приложения.

        Args:
            parent: Родительское окно Tkinter.
        """
        super().__init__(parent)
        
        self.state = JsonState()

        self.__configure_window()
        self.__configure_widgets()
        self.__pack_widgets()
        self.__add_icon()
        
        self.__entry_word_search: tk.Entry
        
        self.__button_by_date: tk.Button
        self.__button_by_keyword: tk.Button
        self.__button_by_title: tk.Button
        
        self.__label_result: tk.Label
        self.__label_error: tk.Label
        self.__canvas: tk.Canvas
        self.__scrollbar: tk.Scrollbar
        self.__scrollable_frame: tk.Frame

    def __configure_window(self) -> None:
        """Настраивает параметры окна расширенного поиска.

        Устанавливает заголовок, размеры и цвет фона окна.
        """
        self.title("Поиск по заметкам")
        self.geometry("700x600")
        self.configure(bg="#f8f9fa")
    
    def __configure_widgets(self) -> None:
        """Инициализирует и настраивает виджеты окна.

        Создает поле ввода поискового запроса, кнопки поиска по различным
        критериям, Canvas с Scrollbar для прокрутки и метки для отображения
        результатов и ошибок.
        """
        # Поле ввода поискового запроса
        self.__entry_word_search = tk.Entry(
            self,
            font=("Arial", 11),
            relief=tk.FLAT,
            bg="white",
            highlightbackground="#ced4da",
            highlightcolor="#28a745",
            highlightthickness=1,
            width=50
        )
        
        # Кнопки поиска с иконками и стилями
        button_style = {
            "font": ("Arial", 11, "bold"),
            "bg": "#28a745",
            "fg": "white",
            "relief": tk.FLAT,
            "padx": 20,
            "pady": 8,
            "cursor": "hand2"
        }
        
        self.__button_by_date = tk.Button(
            self, 
            text="📅 Поиск по дате", 
            command=self.__search_by_date,
            **button_style
        )
        self.__button_by_keyword = tk.Button(
            self, 
            text="🔑 Поиск по ключевому слову", 
            command=self.__search_by_keyword,
            **button_style
        )
        self.__button_by_title = tk.Button(
            self, 
            text="🔤 Поиск по названию", 
            command=self.__search_by_title,
            **button_style
        )
        
        # Создаём Canvas для прокрутки
        self.__canvas = tk.Canvas(self, bg="#f8f9fa", highlightthickness=0)
        self.__scrollbar = tk.Scrollbar(self, orient="vertical", command=self.__canvas.yview)
        self.__canvas.configure(yscrollcommand=self.__scrollbar.set)
        
        # Frame внутри Canvas для размещения метки
        self.__scrollable_frame = tk.Frame(self.__canvas, bg="#f8f9fa")
        self.__canvas.create_window((0, 0), window=self.__scrollable_frame, anchor="nw")
        
        # Метка результата теперь внутри scrollable_frame
        self.__label_result = tk.Label(
            self.__scrollable_frame,
            text="", 
            font=("Arial", 11),
            bg="#f8f9fa",
            fg="#212529",
            justify=tk.LEFT,
            wraplength=600
        )
        
        # Ошибки (остаются вне прокрутки)
        self.__label_error = tk.Label(
            self.__scrollable_frame, 
            text="", 
            foreground="#dc3545",
            font=("Arial", 11, "bold"),
            bg="#f8f9fa"
        )
    
    def __pack_widgets(self) -> None:
        """Размещает виджеты в окне.

        Упаковывает поле ввода, кнопки поиска, Canvas с Scrollbar и метки
        с заданными отступами и параметрами размещения для обеспечения
        корректного отображения и функциональности прокрутки.
        """
        # Отступы для лучшего восприятия
        self.__entry_word_search.pack(pady=(30, 20), padx=30)
        
        buttons_frame = tk.Frame(self, bg="#f8f9fa")
        buttons_frame.pack(pady=20)
        
        self.__button_by_date.pack(pady=5, padx=20, fill=tk.X)
        self.__button_by_keyword.pack(pady=5, padx=20, fill=tk.X)
        self.__button_by_title.pack(pady=5, padx=20, fill=tk.X)
        
        # Упаковываем canvas и scrollbar
        self.__canvas.pack(side="left", fill="both", expand=True, padx=30, pady=10)
        self.__scrollbar.pack(side="right", fill="y", pady=10)
        
        self.__label_result.pack(anchor="w")
        self.__label_error.pack(pady=10)
        
        # Обновляем прокрутку при изменении содержимого
        self.__scrollable_frame.bind(
            "<Configure>",
            lambda e: self.__canvas.configure(scrollregion=self.__canvas.bbox("all"))
        )
    
    def __add_icon(self) -> None:
        """Устанавливает иконку окна.

        Загружает иконку из файла 'static/icons/app.ico' и устанавливает
        ее для текущего окна.

        Raises:
            FileNotFoundError: Если файл иконки не найден.
            tk.TclError: Если формат иконки не поддерживается.
        """
        self.iconbitmap("static/icons/app.ico")
    
    def __search_by_date(self) -> None:
        """Выполняет поиск заметок по дате.

        Очищает предыдущие результаты, загружает все заметки через JsonState,
        применяет стратегию SearchByDateStrategy для поиска по дате
        и отображает результат. Если заметки не найдены, показывает
        соответствующее сообщение об ошибке.
        """
        self.__label_error["text"] = ""
        self.__label_result["text"] = ""
        notes = self.state.load_notes()
        
        strategy = SearchByDateStrategy(self.__entry_word_search.get())
        if strategy.execute(notes):
            self.__label_result["text"] += strategy.execute(notes)
        else:
            self.__label_error["text"] = "Заметок с такой датой не найдено"
    
    def __search_by_title(self) -> None:
        """Выполняет поиск заметок по названию.

        Очищает предыдущие результаты, загружает все заметки через JsonState,
        применяет стратегию SearchTitleStrategy для поиска по названию
        и отображает результат. Если заметки не найдены, показывает
        соответствующее сообщение об ошибке.
        """
        self.__label_error["text"] = ""
        self.__label_result["text"] = ""
        notes = self.state.load_notes()
        
        strategy = SearchTitleStrategy(self.__entry_word_search.get())
        if strategy.execute(notes):
            self.__label_result["text"] += strategy.execute(notes)
        else:
            self.__label_error["text"] = "Заметок с таким ключевым словом не найдено"
    
    def __search_by_keyword(self) -> None:
        """Выполняет поиск заметок по ключевым словам.

        Очищает предыдущие результаты, загружает все заметки через JsonState,
        применяет стратегию SearchKeywordStrategy для поиска по ключевым словам
        и отображает результат. Если заметки не найдены, показывает
        соответствующее сообщение об ошибке.
        """
        self.__label_error["text"] = ""
        self.__label_result["text"] = ""
        notes = self.state.load_notes()
        
        strategy = SearchKeywordStrategy(self.__entry_word_search.get())
        if strategy.execute(notes):
            self.__label_result["text"] += strategy.execute(notes)
        else:
            self.__label_error["text"] = "Заметок с таким заданным словом не найдено"