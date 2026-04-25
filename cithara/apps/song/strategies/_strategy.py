from abc import ABC


class GeneratorStrategy(ABC):
    def generate_song(self, request, song):
        pass