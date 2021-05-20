from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Poll(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Question(models.Model):
    CHOICE = (
        ('text', 'text'),
        ('single_choice', 'single_choice'),
        ('miltiple_choice', 'miltiple_choice'),
    )
    poll = models.ForeignKey(
        Poll, on_delete=models.CASCADE, related_name='question')
    title = models.TextField()
    type = models.CharField(choices=CHOICE, max_length=20)

    def __str__(self):
        return self.title
