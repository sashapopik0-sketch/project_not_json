"""Модуль окна добавления новой заметки."""

import tkinter as tk
from state.json_state import JsonState
from core.note import Note
from tkinter import messagebox
from datetime import datetime


class AddNote(tk.Toplevel):
    """Окно для добавления новой заметки.

    Предоставляет пользовательский интерфейс для ввода названия и содержания
    новой заметки с последующим сохранением в JSON-файл через JsonState.

    Attributes:
        state: Экземпляр JsonState для работы с данными заметок.
        __title_label: Метка для поля названия заметки.
        __title_entry: Поле ввода для названия заметки.
        __text_label: Метка для поля содержания заметки.
        __text_input: Текстовое поле для содержания заметки.
        __save_button: Кнопка для сохранения заметки.
        __cancel_button: Кнопка для очистки полей ввода.
    """

    def __init__(self, parent: tk.Tk) -> None:
        """Инициализирует окно добавления заметки.

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

        self.__title_label: tk.Label
        self.__title_entry: tk.Entry

        self.__text_label: tk.Label
        self.__text_input: tk.Text

        self.__save_button: tk.Button
        self.__cancel_button: tk.Button

    def __configure_window(self) -> None:
        """Настраивает параметры окна добавления заметки.

        Устанавливает заголовок, размеры, возможность изменения размера
        и цвет фона окна.
        """
        self.title("Добавить заметку")
        self.geometry("600x500")
        self.resizable(True, True)
        self.configure(bg="#f8f9fa")

    def __configure_widgets(self) -> None:
        """Инициализирует и настраивает виджеты окна.

        Создает все необходимые элементы интерфейса: метки, поля ввода,
        текстовое поле и кнопки с соответствующими стилями и обработчиками.
        """
        self.__title_label = tk.Label(
            self, 
            text="Название:", 
            font=("Arial", 12, "bold"),
            bg="#f8f9fa",
            fg="#212529"
        )

        self.__title_entry = tk.Entry(
            self,
            font=("Arial", 11),
            relief=tk.FLAT,
            bg="white",
            highlightbackground="#ced4da",
            highlightcolor="#28a745",
            highlightthickness=1
        )

        self.__text_label = tk.Label(
            self,
            text="Содержание:",
            font=("Arial", 12, "bold"),
            bg="#f8f9fa",
            fg="#212529"
        )

        self.__text_input = tk.Text(
            self,
            font=("Arial", 11),
            relief=tk.FLAT,
            bg="white",
            highlightbackground="#ced4da",
            highlightcolor="#28a745",
            highlightthickness=1,
            height=12
        )

        self.__save_button = tk.Button(
            self,
            text="💾 Сохранить",
            command=self.__save_note,
            font=("Arial", 11, "bold"),
            bg="#28a745",
            fg="white",
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2"
        )

        self.__cancel_button = tk.Button(
            self,
            text="🗑️ Очистить",
            command=self.__cancel_note,
            font=("Arial", 11),
            bg="#6c757d",
            fg="white",
            relief=tk.FLAT,
            padx=20,
            pady=8,
            cursor="hand2"
        )

    def __pack_widgets(self) -> None:
        """Размещает виджеты в окне.

        Упаковывает все элементы интерфейса с заданными отступами и параметрами
        размещения для обеспечения корректного отображения.
        """
        padding = {'padx': 30, 'pady': (10, 5)}

        self.__title_label.pack(anchor="w", **padding)
        self.__title_entry.pack(fill=tk.X, **padding)

        self.__text_label.pack(anchor="w", **padding)
        self.__text_input.pack(fill=tk.BOTH, expand=True, **padding)

        self.__save_button.pack(pady=(20, 10))
        self.__cancel_button.pack(pady=(0, 20))

    def __add_icon(self) -> None:
        """Устанавливает иконку окна.

        Загружает иконку из файла 'static/icons/app.ico' и устанавливает
        ее для текущего окна.

        Raises:
            FileNotFoundError: Если файл иконки не найден.
            tk.TclError: Если формат иконки не поддерживается.
        """
        self.iconbitmap("static/icons/app.ico")

    def __save_note(self) -> None:
        """Сохраняет новую заметку.

        Получает данные из полей ввода, выполняет валидацию,
        создает новую заметку и сохраняет ее через JsonState.
        При успешном сохранении показывает информационное сообщение
        и закрывает окно.
        """
        title = self.__title_entry.get().strip()
        text = self.__text_input.get("1.0", tk.END).strip()

        if not title or not text:
            messagebox.showerror("Ошибка", "Заполните все поля!")
            return

        notes = self.state.load_notes()
        next_id = max([n.id for n in notes], default=0) + 1
        new_note = Note(next_id, title, text, date=datetime.now().strftime("%d.%m.%Y %H:%M"))
        notes.append(new_note)
        self.state.save_notes(notes)

        messagebox.showinfo("Успех", "Заметка успешно добавлена!")
        self.destroy()

    def __cancel_note(self) -> None:
        """Очищает поля ввода.

        Удаляет весь текст из поля названия и текстового поля содержания.
        """
        self.__title_entry.delete(0, tk.END)
        self.__text_input.delete('1.0', tk.END)
