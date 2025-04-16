from django.contrib import admin
from .models import User, Team, Activity, Leaderboard, Workout

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name')

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name',)

# Additional admin configurations for Activity, Leaderboard, and Workout can be added similarly.
