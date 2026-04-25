from ._strategy import GeneratorStrategy


class MockGeneratorStrategy(GeneratorStrategy):
    def generate_song(self, request, song):
        song.audio_url = "https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3"
        song.track_length = 229
        song.generation_status = "FIN"
        song.save()