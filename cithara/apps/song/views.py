from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.core.exceptions import ValidationError

from .models import Song, User


# Create your views here.
MODEL = Song

class IndexView(generic.ListView):
    model = MODEL
    template_name = "song_index.html"
    context_object_name = "songs"

class CreateView(generic.CreateView):
    model = MODEL
    template_name = "song_create.html"
    fields = [f.name for f in MODEL._meta.get_fields()]

class UpdateView(generic.UpdateView):
    model = MODEL
    template_name = "song_update.html"
    fields = [f.name for f in MODEL._meta.get_fields()]

def create_song(request):
    if request.method == 'POST':
        data = request.POST

        ownerid = data.get('owner')
        owner = get_object_or_404(User, id=ownerid)

        title = data.get('title')
        occasion = data.get('occasion')
        genre = data.get('genre')
        singer_voice_type = data.get('singer_voice_type')
        mood = data.get('mood')

        MODEL.objects.create(
            owner = owner,
            title = title,
            occasion = occasion,
            genre = genre,
            singer_voice_type = singer_voice_type,
            mood = mood,
        )
        return redirect('/songs/')
    return render(request, "song_create.html")

def update_song(request, id):
    song = get_object_or_404(MODEL, id=id)

    if request.method == 'POST':
        data = request.POST

        ownerid = data.get('owner')
        owner = get_object_or_404(User, id=ownerid)

        generation_status = data.get('generation_status')
        if not generation_status in ['GEN', 'FIN' ,'FAI']:
            raise ValidationError('Generation status invalid')
        title = data.get('title')
        occasion = data.get('occasion')
        genre = data.get('genre')
        singer_voice_type = data.get('singer_voice_type')
        mood = data.get('mood')
        track_length = data.get('track_length')
        share_link = data.get('share_link')

        song.owner = owner
        song.generation_status = generation_status
        song.title = title
        song.occasion = occasion
        song.genre = genre
        song.singer_voice_type = singer_voice_type
        song.mood = mood 
        song.track_length = track_length
        song.share_link = share_link
        song.save()
        return redirect('/songs/')
    return render(request, 'song_update.html', {'song': song})

def delete(request, id):
    song = get_object_or_404(MODEL, id=id)
    song.delete()
    return redirect('/songs/')