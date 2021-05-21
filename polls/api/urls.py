from django.urls import path, include
from .views import PollViewSet, QuestionViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('polls', PollViewSet)
router.register(r'polls/(?P<poll_id>\d+)/questions',
                QuestionViewSet,
                basename='questions')

urlpatterns = [
    path('', include(router.urls)),
]
