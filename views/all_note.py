"""Модуль окна просмотра всех заметок."""

import tkinter as tk
from strategies.view_all_strategy import ViewAllStrategy
from state.json_state import JsonState


class AllNote(tk.Toplevel):
    """Окно для просмотра всех сохраненных заметок.

    Предоставляет пользовательский интерфейс для отображения списка всех
    заметок с возможностью прокрутки длинного содержимого через Canvas
    и Scrollbar.

    Attributes:
        state: Экземпляр JsonState для загрузки данных заметок.
        __button: Кнопка для инициации загрузки и отображения заметок.
        __label_notes: Метка для отображения содержимого заметок.
        __label_error: Метка для отображения сообщений об ошибках.
        __canvas: Canvas для создания прокручиваемой области.
        __scrollbar: Вертикальный скроллбар для прокрутки содержимого.
        __scrollable_frame: Frame внутри Canvas для размещения метки с заметками.
    """

    def __init__(self, parent: tk.Tk) -> None:
        """Инициализирует окно просмотра всех заметок.

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

        self.__button: tk.Button
        self.__label_notes: tk.Label
        self.__label_error: tk.Label
        self.__canvas: tk.Canvas
        self.__scrollbar: tk.Scrollbar
        self.__scrollable_frame: tk.Frame

    def __configure_window(self) -> None:
        """Настраивает параметры окна просмотра заметок.

        Устанавливает заголовок, размеры и цвет фона окна.
        """
        self.title("Просмотр всех заметок")
        self.geometry("800x600")
        self.configure(bg="#f8f9fa")

    def __configure_widgets(self) -> None:
        """Инициализирует и настраивает виджеты окна.

        Создает кнопку просмотра, Canvas с Scrollbar для прокрутки,
        Frame для размещения метки и саму метку для отображения заметок.
        """
        self.__button = tk.Button(
            self, 
            text="🔍 Посмотреть все заметки", 
            command=self.__show_notes,
            font=("Arial", 12, "bold"),
            bg="#28a745",
            fg="white",
            relief=tk.FLAT,
            padx=25,
            pady=10,
            cursor="hand2"
        )

        self.__canvas = tk.Canvas(self, bg="#f8f9fa", highlightthickness=0)
        self.__scrollbar = tk.Scrollbar(self, orient="vertical", command=self.__canvas.yview)
        self.__canvas.configure(yscrollcommand=self.__scrollbar.set)

        self.__scrollable_frame = tk.Frame(self.__canvas, bg="#f8f9fa")
        self.__canvas.create_window((0, 0), window=self.__scrollable_frame, anchor="nw")

        self.__label_notes = tk.Label(
            self.__scrollable_frame,
            text="", 
            font=("Arial", 11),
            bg="#f8f9fa",
            fg="#212529",
            justify=tk.LEFT,
            wraplength=700
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

        Упаковывает кнопку, Canvas с Scrollbar и метки с заданными отступами
        и параметрами размещения для обеспечения корректного отображения
        и функциональности прокрутки.
        """
        self.__button.pack(pady=(40, 30))

        self.__canvas.pack(side="left", fill="both", expand=True, padx=30, pady=10)
        self.__scrollbar.pack(side="right", fill="y", pady=10)

        self.__label_notes.pack(anchor="w")
        self.__label_error.pack(pady=10)

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

    def __show_notes(self) -> None:
        """Отображает все сохраненные заметки.

        Очищает предыдущие результаты, загружает все заметки через JsonState,
        применяет стратегию ViewAllStrategy для форматирования и отображает
        результат в метке. Если заметок нет, показывает соответствующее сообщение.
        """
        self.__label_error["text"] = ""
        self.__label_notes["text"] = ""

        strategy = ViewAllStrategy()
        notes = self.state.load_notes()
        if strategy.execute(notes):
            self.__label_notes["text"] += strategy.execute(notes)
        else:
            self.__label_error["text"] = "Заметок нет"
