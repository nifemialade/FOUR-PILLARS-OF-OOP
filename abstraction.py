from abc import ABC, abstractmethod


class Movie(ABC):
    @abstractmethod
    def show_details(self):
        pass


class ActionMovie(Movie):
    def __init__(self, title, year, genre):
        self.title = title
        self.year = year
        self.genre = genre

    def show_details(self):
        print(f"Title: {self.title}")
        print(f"Year: {self.year}")
        print(f"Genre: {self.genre}")


movie = ActionMovie("Black Panther", 2018, "Action")
movie.show_details()