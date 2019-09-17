# Create your views here.
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response

from event.models import Event, UserEvent
from event.serializers import EventSerializer, ListEventSerializer


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = ListEventSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ListEventSerializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'], name='Register user on event',
            permission_classes=[IsAuthenticated])
    def registration(self, request, pk=None):
        user = request.user
        event = self.get_object()
        UserEvent.objects.get_or_create(user=user, event=event)
        return Response({'status': 'user registration successful'})
