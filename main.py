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
    def __init__(self, filename):
        self.filename = filename

    @classmethod
    def create(cls, filename):
        if filename.split(".") not in ALLOWED_EXTENSION:
            print("file extension not allowed")
        return filename
