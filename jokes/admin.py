from django.contrib import admin
from .models import Joke
# Register your models here.
@admin.register(Joke)
class JokeAdmin(admin.ModelAdmin):
    list_display = ('category', 'type', 'safe', 'lang')
    search_fields = ('category', 'type', 'lang')
    list_filter = ('category', 'safe', 'nsfw', 'political', 'sexist')
