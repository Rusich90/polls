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

    class Meta:
        ordering = ['end_date']


class Question(models.Model):
    TYPE_QUESTION = (
        ('text', 'ответ текстом'),
        ('single_choice', 'ответ с выбором одного варианта'),
        ('multiple_choice', 'ответ с выбором нескольких вариантов'),
    )
    poll = models.ForeignKey(
        Poll, on_delete=models.CASCADE, related_name='question')
    title = models.TextField()
    type = models.CharField(choices=TYPE_QUESTION, max_length=20)

    def __str__(self):
        return self.title


class Choice(models.Model):
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='choice')
    text = models.CharField(max_length=256)


class Answer(models.Model):
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    user_id = models.IntegerField()
    question = models.ForeignKey(
        Question, on_delete=models.CASCADE, related_name='user_answer')
    answer = models.CharField(max_length=256)
