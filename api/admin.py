from django.contrib import admin
from .models import User, Room


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "email", "first_name", "last_name")


class RoomAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "host", "guest_can_pause", "votes_to_skip", "created_at")


admin.site.register(User, UserAdmin)
admin.site.register(Room, RoomAdmin)