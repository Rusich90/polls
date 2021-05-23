from rest_framework import serializers
from .models import Poll, Question, Choice, Answer


class PollSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance is not None:
            self.fields.get('start_date').read_only = True

    class Meta:
        fields = ('id', 'title', 'description', 'start_date', 'end_date')
        model = Poll


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('text',)
        model = Choice


class QuestionSerializer(serializers.ModelSerializer):


    class Meta:
        fields = ('id', 'poll', 'title', 'type', 'choice')
        model = Question


class AnswerSerializer(serializers.ModelSerializer):

    poll = serializers.ReadOnlyField(source='poll.title')
    question = serializers.ReadOnlyField(source='question.title')

    class Meta:
        fields = ('poll', 'question', 'user_id', 'answer')
        model = Answer


class UserAnswerSerializer(serializers.ModelSerializer):

    question = serializers.ReadOnlyField(source='question.title')

    class Meta:
        fields = ('question', 'answer')
        model = Answer
