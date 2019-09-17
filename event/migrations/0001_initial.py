# Generated by Django 2.2.5 on 2019-09-16 17:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('date', models.DateField()),
            ],
            options={
                'verbose_name': 'Мероприятие',
                'verbose_name_plural': 'Мероприятия',
            },
        ),
        migrations.CreateModel(
            name='UserEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_events', to='event.Event')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_events', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Регистрация на мероприятие',
                'verbose_name_plural': 'Регистрации на мероприятие',
                'unique_together': {('event', 'user')},
            },
        ),
    ]
