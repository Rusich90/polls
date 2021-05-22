from django.urls import path, include
from .views import PollViewSet, QuestionViewSet, ChoiceViewSet, AnswerViewSet, UserAnswersListView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('polls', PollViewSet)
router.register(r'polls/(?P<poll_id>\d+)/questions',
                QuestionViewSet,
                basename='questions'),
router.register(r'polls/(?P<poll_id>\d+)/questions/(?P<question_id>\d+)/choices',
                ChoiceViewSet,
                basename='choices')
router.register(r'polls/(?P<poll_id>\d+)/questions/(?P<question_id>\d+)/answers',
                AnswerViewSet,
                basename='answers')

urlpatterns = [
    path('', include(router.urls)),
    path('user-answers/<int:user_id>/', UserAnswersListView.as_view()),
]
