"""Главный модуль приложения менеджера заметок."""

import tkinter as tk
from views.base_view import BaseView
from PIL import Image, ImageTk


class Application(tk.Tk):
    """Главное приложение менеджера заметок.

    Отвечает за создание главного окна Tkinter, настройку базовых параметров
    и отображение главного меню через BaseView.

    Attributes:
        __user_widgets: Экземпляр главного меню приложения.
    """

    def __init__(self) -> None:
        """Инициализирует главное приложение.

        Создает главное окно Tkinter, настраивает его параметры,
        инициализирует главное меню и устанавливает иконку приложения.
        """
        super().__init__()

        self.__configure_windows()
        self.__configure_widgets()
        self.__user_widgets = BaseView(self)
        self.__pack_widgets()

        self._add_icon()

    def __configure_windows(self) -> None:
        """Настраивает параметры главного окна.

        Устанавливает заголовок окна и его геометрию (размеры).
        """
        self.title("Заметки")
        self.geometry("1000x500")

    def __configure_widgets(self) -> None:
        """Инициализирует виджеты главного окна.

        Создает экземпляр BaseView для отображения главного меню.
        """
        self.__user_widgets = BaseView(self)

    def __pack_widgets(self) -> None:
        """Размещает виджеты в главном окне.

        Упаковывает главное меню (BaseView) для отображения в окне приложения.
        """
        self.__user_widgets.pack()

    def _add_icon(self) -> None:
        """Устанавливает иконку приложения.

        Загружает изображение из файла 'static/imgs/app_2.png' и устанавливает
        его как иконку для главного окна приложения.

        Raises:
            FileNotFoundError: Если файл иконки не найден.
            PIL.UnidentifiedImageError: Если файл не является допустимым изображением.
        """
        img = Image.open("static/imgs/app_2.png")
        photo = ImageTk.PhotoImage(img)
        self.iconphoto(False, photo)

    def run(self) -> None:
        """Запускает основной цикл событий приложения.

        Вызывает метод mainloop() для запуска графического интерфейса
        и обработки пользовательских событий.
        """
        self.mainloop()


if __name__ == "__main__":
    app = Application()
    app.run()
