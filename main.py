from abc import ABC, abstractmethod

ALLOWED_EXTENSION = ["html", "csv", "mp3", "mp4", "txt"]


class AbstractRender(ABC):
    @abstractmethod
    def render(self):
        pass


class HtmlRender(AbstractRender):
    def render(self):
        print("Render using HtmlRender")


class MP3Render(AbstractRender):
    def render(self):
        print("Render using MP3Render")


class MP4Render(AbstractRender):
    def render(self):
        print("Render using MP4Render")


class FileHandler:
    def __init__(self, file_name):
        self.file_name = file_name

    @classmethod
    def create(cls, filename):
        if filename.split(".")[-1] not in ALLOWED_EXTENSION:
            print("file extension not allowed")
        return cls(filename)

    @property
    def extension(self):
        return self.file_name.split(".")[-1]

    def render(self):
        handler_dict = {
            "html": HtmlRender,
            "mp3": MP3Render,
            "mp4": MP4Render
        }
        handler = handler_dict[self.extension]
        return handler().render()


if __name__ == "__main__":
    f1 = FileHandler.create("document.pdf")
    f2 = FileHandler.create("document.html")
    f3 = FileHandler.create("movie.mp3")
    f4 = FileHandler.create("movie.mp4")

    file_list = [f2, f3, f4]

    for filename in file_list:
        filename.render()
