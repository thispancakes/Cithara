from ....config import GENERATION_STRATEGY, SUNO_API_KEY
from ..strategies.mock import MockGeneratorStrategy
from ..strategies.suno_API import SunoAPIGeneratorStrategy
from threading import Timer
import requests


def get_generation_strategy():
    if GENERATION_STRATEGY == 'mock':
        return MockGeneratorStrategy()
    elif GENERATION_STRATEGY == 'suno':
        return SunoAPIGeneratorStrategy()
    else:
        raise ValueError('Non valid GENERATION_STRATEGY')

def generate_song_service(request, song):
    strategy = get_generation_strategy()

    strategy.generate_song(request, song)