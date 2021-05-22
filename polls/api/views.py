from rest_framework import viewsets, pagination, status
from .serializers import PollSerializer, QuestionSerializer, ChoiceSerializer, AnswerSerializer
from .models import Poll, Question, Answer, Choice
from rest_framework.response import Response

class PollViewSet(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    pagination_class = pagination.PageNumberPagination


class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    pagination_class = pagination.PageNumberPagination

    def get_queryset(self):
        return Question.objects.filter(
            poll=self.kwargs['poll_id']
        )

    def perform_create(self, serializer):
        serializer.save(poll=Poll.objects.get(id=self.kwargs['poll_id']))


class ChoiceViewSet(viewsets.ModelViewSet):
    serializer_class = ChoiceSerializer
    pagination_class = pagination.PageNumberPagination

    def get_queryset(self):
        return Choice.objects.filter(
            question=self.kwargs['question_id']
        )

    def perform_create(self, serializer):
        serializer.save(question=Question.objects.get(id=self.kwargs['question_id']))


class AnswerViewSet(viewsets.ModelViewSet):
    serializer_class = AnswerSerializer
    pagination_class = pagination.PageNumberPagination

    def list(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def perform_create(self, serializer):
        serializer.save(question=Question.objects.get(id=self.kwargs['question_id']),
                        poll=Poll.objects.get(id=self.kwargs['poll_id']))


class UserAnswers():

