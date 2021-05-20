from rest_framework import serializers
from .models import Poll, Question


class PollSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'description', 'start_date', 'end_date')
        model = Poll


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'text', 'type')
        model = Question
