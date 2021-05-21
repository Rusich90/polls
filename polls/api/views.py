from rest_framework import viewsets, pagination
from .serializers import PollSerializer, QuestionSerializer
from .models import Poll, Question


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
