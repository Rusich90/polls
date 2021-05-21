from rest_framework import serializers
from .models import Poll, Question, AnswerChoices


class PollSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'description', 'start_date', 'end_date')
        model = Poll


class AnswerChoicesSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'text')
        read_only_fields = ('id',)
        model = AnswerChoices


class QuestionSerializer(serializers.ModelSerializer):

    answer_choices = AnswerChoicesSerializer(many=True, required=False)

    class Meta:
        model = Question
        fields = ('id', 'poll', 'title', 'type', 'answer_choices')
        read_only_fields = ('id', )
        extra_kwargs = {
            'poll': {'write_only': True}
        }


    def create_answers(self, question, answer_choices):
        # AnswerChoices.objects.create(question=question, answer_choices=answer_choices)
        AnswerChoices.objects.bulk_create([
            AnswerChoices(question=question, **d) for d in answer_choices
        ])

    def create(self, validated_data):
        print(validated_data)
        answers = validated_data.pop('answer_choices', [])
        question = Question.objects.create(**validated_data)
        self.create_answers(question, answers)
        return question
