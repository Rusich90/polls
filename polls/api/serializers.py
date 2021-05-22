from rest_framework import serializers
from .models import Poll, Question, Choice, Answer


class PollSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'description', 'start_date', 'end_date')
        model = Poll


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'text')
        model = Choice


class QuestionSerializer(serializers.ModelSerializer):

    choice = ChoiceSerializer(many=True, required=False)

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

    poll = serializers.ReadOnlyField(source='poll.title')
    question = serializers.ReadOnlyField(source='question.title')

    class Meta:
        fields = ('poll', 'question', 'answer')
        model = Answer
