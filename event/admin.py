from django.contrib import admin

# Register your models here.
from event.models import Event, UserEvent


class UserEventInline(admin.TabularInline):
    model = UserEvent
    extra = 0


class EventAdmin(admin.ModelAdmin):
    inlines = (UserEventInline,)


admin.site.register(Event, EventAdmin)
admin.site.register(UserEvent)
