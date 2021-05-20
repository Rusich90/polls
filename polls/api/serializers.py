from rest_framework import serializers
from .models import Poll


class PollSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'title', 'description', 'start_date', 'end_date')
        model = Poll
