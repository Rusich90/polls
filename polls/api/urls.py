from django.urls import path, include
from .views import (PollViewSet, QuestionViewSet, ChoiceViewSet,
                    AnswerViewSet, UserAnswersListView, UserPollsListView)
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.schemas import get_schema_view
from django.views.generic import TemplateView

router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')
router.register(r'polls/(?P<poll_id>\d+)/questions',
                QuestionViewSet,
                basename='questions'),
router.register(
    r'polls/(?P<poll_id>\d+)/questions/(?P<question_id>\d+)/choices',
    ChoiceViewSet,
    basename='choices'
)
router.register(
    r'polls/(?P<poll_id>\d+)/questions/(?P<question_id>\d+)/answers',
    AnswerViewSet,
    basename='answers'
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(router.urls)),
    path('user-answers/<int:user_id>/', UserPollsListView.as_view()),
    path('user-answers/<int:user_id>/<int:poll_id>/',
         UserAnswersListView.as_view()),
    path('schema', get_schema_view(
        title="PollsAPI",
        description="API for polls",
        version="1.0.0"
    ), name='openapi-schema'),
    path('redoc/', TemplateView.as_view(template_name='redoc.html'),
         name='redoc'),
]
