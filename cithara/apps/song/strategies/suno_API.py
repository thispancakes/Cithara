from ._strategy import GeneratorStrategy
from ....config import SUNO_API_KEY
import requests
from threading import Thread
from time import sleep


class SunoAPIGeneratorStrategy(GeneratorStrategy):

    def generate_song(self, request, song):
        url = "https://api.sunoapi.org/api/v1/generate"
        headers = {
            "Authorization": f"Bearer {SUNO_API_KEY}",
            "Content-Type": "application/json"
        }

        data = request
        title = data.get('title')
        occasion = data.get('occasion')
        genre = data.get('genre')
        singer_voice_type = data.get('singer_voice_type')
        mood = data.get('mood')

        payload = {
            "prompt": f"Genre: {genre}, Mood: {mood}, Occasion: {occasion}, Singer voice: {singer_voice_type}",
            "title": f"{title}",
            "customMode": False,
            "instrumental": False,
            "model": "V4_5ALL",
            "callBackUrl": "https://your-server.com/callback"
        }

        response = requests.post(url, json=payload, headers=headers)
        result = response.json()

        task_id = result['data']['taskId']
        print(f"Task ID: {result['data']['taskId']}")

        thread = Thread(target=self.poll_status, args=(task_id, song), daemon=True)
        thread.start()

    def poll_status(self, task_id, song):
        time = 0
        while time < 600:
            status = self.check_task_status(task_id, song)
            if status == 'SUCCESS':
                break
            sleep(30)
            time += 30
        song.generation_status = 'FAI'

    def check_task_status(self, task_id, song):
        url = f"https://api.sunoapi.org/api/v1/generate/record-info?taskId={task_id}"
        headers = {"Authorization": f"Bearer {SUNO_API_KEY}"}
        
        response = requests.get(url, headers=headers)
        result = response.json()
        print(result)
        
        status = result['data']['status']
        
        if status == 'SUCCESS':
            print("Generation complete!")
            audio_data = result['data']['response']['sunoData']
            for i, audio in enumerate(audio_data):
                print(f"Track {i+1}: {audio['streamAudioUrl']}")
                song.audio_url = audio['streamAudioUrl']
                song.track_length = int(audio['duration'])
                song.generation_status = 'FIN'
                song.save()
            return status
        elif status == 'GENERATING':
            print("Still generating...")
            return status
        else:
            print(f"Generation failed: {status}")
            return status