from django.contrib.auth.models import User
from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField()
    users = models.ManyToManyField(User, through='UserEvent')

    class Meta:
        verbose_name = 'Мероприятие'
        verbose_name_plural = 'Мероприятия'

    def __str__(self):
        return self.title


class UserEvent(models.Model):
    event = models.ForeignKey(Event, related_name='event_users', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_registrations',
                             on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('event', 'user')
        verbose_name = 'Регистрация на мероприятие'
        verbose_name_plural = 'Регистрации на мероприятие'

    def __str__(self):
        return f'Регистрации {self.user} на мероприятие "{self.event}"'