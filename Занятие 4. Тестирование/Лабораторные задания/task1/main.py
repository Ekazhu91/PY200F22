class Newspaper:
    """ Базовый класс, который описывает журнал. """

    def __init__(self, pages: int, name: str):
        """
        Определяем журнал
        :param pages: Количество страниц в журнале
        :param name: Название
        """
        if not isinstance(pages, int):
            raise TypeError("Количество страниц должно быть типа int")
        if pages < 0:
            raise ValueError("Количество страниц должно быть больше 0")
        # Атрибутам присваиваются значения аргументов конструктора объекта
        self._pages = pages
        self.name = name

    # @staticmethod
    # def is_newspaper_equal(book1: PaperNewspaper, book2: ENewspaper):
    #     """ Метод, который определяет похожи ли книги
    #     :param book1: Название книги печатного журнала
    #     :param book2: Название электронного журнала
    #     """
    #     return book1.name == book2.name

    @property
    def pages(self) -> int:
        """Возвращает количестко страниц в журнале"""
        return self._pages

    @pages.setter
    def pages(self, new_pages: int) -> None:
        """Устанавливает количестко страниц в журнале"""
        self._pages = new_pages


class PaperNewspaper(Newspaper):
    """ Дочерний класс, который описывает бумажный журнал. """
    def __init__(self, cover: str, pages: int, name: str):
        """
        Определяем журнал
        :param pages: Количество страниц в журнале
        :param name: Название
        :param cover: Переплет журнала
        """
        super().__init__(pages, name)
        self.cover = cover


class ENewspaper(Newspaper):
    """ Дочерний класс, который описывает электронный журнал. """
    def __init__(self, format: str, pages: int, name: str):
        """
        Определяем журнал
        :param pages: Количество страниц в журнале
        :param name: Название
        :param format: Формат электронного журнала
        """
        super().__init__(pages, name)
        self.format = format


if __name__ == "__main__":
    # Write your solution here
    pass
