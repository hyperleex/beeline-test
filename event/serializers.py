from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from rest_framework.relations import PrimaryKeyRelatedField

from event.models import Event


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class EventSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'users']
        depth = 1


class ListEventSerializer(serializers.ModelSerializer):
    has_registration = serializers.SerializerMethodField('check_registration')

    class Meta:
        model = Event
        fields = ['id', 'title', 'description', 'date', 'has_registration']

    def check_registration(self, obj):
        return obj.users.exists()
