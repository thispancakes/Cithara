from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
from cithara.apps.user.models import User


# Validators
def limit_total_songs(value):
    if Song.objects.filter(owner=value).exclude(generation_status='FAI').count() >= 20:
        raise ValidationError('User already has maximum number of songs (20)')
    
def limit_generating_song(value):
    if Song.objects.filter(owner=value, generation_status='GEN').count() >= 3:
        raise ValidationError('User already has maximum number of generating songs (3)')

class Song(models.Model):
    GENERATING = "GEN"
    FINISHED = "FIN"
    FAILED = "FAI"
    GENERATION_STATUS_CHOICES = {
        GENERATING: "Generating",
        FINISHED: "Finished",
        FAILED: "Failed",
    }

    owner = models.ForeignKey(User, on_delete=models.CASCADE, validators=[limit_total_songs, limit_generating_song])

    generation_status = models.CharField(max_length=3, choices=GENERATION_STATUS_CHOICES, default=GENERATING)
    title = models.CharField(max_length=255)
    occasion = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    singer_voice_type = models.CharField(max_length=255)
    mood = models.CharField(max_length=255)

    track_length = models.PositiveIntegerField(default=0)
    share_link = models.CharField(max_length=255, default="", blank=True)