from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Poll(models.Model):
    title = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.TextField()