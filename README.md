Follow steps to create this project 

1. Install Django and Django REST Framework using following commands

pip install django djangorestframework 
pip install requests

2. Create Django Project and Appp

django-admin startproject joke_project
cd joke_project
python manage.py startapp jokes

3. Add recently created app in Installed Apps in joke_project/settings.py, so that django will came to know about new app created

INSTALLED_APPS = [
'rest_framework',
'jokes',
]

4. Create models.py for table schema or we can say structure
jokes/models.py


from django.db import models
class Joke(models.Model):
    CATEGORY_CHOICES = [
        ('Any', 'Any'),
        ('Programming', 'Programming'),
        ('Misc', 'Miscellaneous'),
        ('Dark', 'Dark'),
        ('Pun', 'Pun'),
        ('Spooky', 'Spooky'),
        ('Christmas', 'Christmas'),
    ]
    
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    type = models.CharField(max_length=10)
    joke = models.TextField(null=True, blank=True)
    setup = models.TextField(null=True, blank=True)
    delivery = models.TextField(null=True, blank=True)
    nsfw = models.BooleanField(default=False)
    political = models.BooleanField(default=False)
    sexist = models.BooleanField(default=False)
    safe = models.BooleanField(default=True)
    lang = models.CharField(max_length=10)

    def __str__(self):
        return self.category

5. Remember to hit 2 compulsory commands after creating models.py

python manage.py makemigrations
python manage.py migrate

6. Define serializers to convert incoming python data to complex data 

jokes/serializers.py

from rest_framework import serializers
from .models import Joke

class JokeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Joke
        fields = '__all__'

7. Create a Function to Fetch Jokes from JokeAPI

jokes/utils.py

import requests
from .models import Joke

def fetch_jokes_from_api(num_jokes=100):
    url = f"https://v2.jokeapi.dev/joke/Any?amount={num_jokes}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        jokes = []
        for joke_data in data.get("jokes", []):
            joke = {
                "category": joke_data["category"],
                "type": joke_data["type"],
                "joke": joke_data.get("joke"),
                "setup": joke_data.get("setup"),
                "delivery": joke_data.get("delivery"),
                "nsfw": joke_data["flags"]["nsfw"],
                "political": joke_data["flags"]["political"],
                "sexist": joke_data["flags"]["sexist"],
                "safe": joke_data["safe"],
                "lang": joke_data["lang"],
            }
            jokes.append(joke)
        return jokes
    return []

8. Define views.py....remember to exempt csrf token otherwise it will show error

from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Joke
from .serializers import JokeSerializer
from .utils import fetch_jokes_from_api

@csrf_exempt
@api_view(['POST'])
def fetch_and_store_jokes(request):
    jokes_data = fetch_jokes_from_api()
    jokes = []
    for joke_data in jokes_data:
        joke, created = Joke.objects.get_or_create(
            category=joke_data["category"],
            type=joke_data["type"],
            joke=joke_data.get("joke"),
            setup=joke_data.get("setup"),
            delivery=joke_data.get("delivery"),
            nsfw=joke_data["nsfw"],
            political=joke_data["political"],
            sexist=joke_data["sexist"],
            safe=joke_data["safe"],
            lang=joke_data["lang"],
        )
        jokes.append(joke)
    serializer = JokeSerializer(jokes, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

9. Setup Project Urls.py and redirect it to app urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
path('admin/', admin.site.urls),
path('api/', include('jokes.urls')),
]

10. setup app Urls.py

remember to route url properly

from django.urls import path
from .views import fetch_and_store_jokes

urlpatterns = [
    path('fetch_jokes/', fetch_and_store_jokes, name='fetch_jokes'),
]

11. setup admins.py so that your stored jokes can be seen in admin panel

from django.contrib import admin
from .models import Joke

@admin.register(Joke)
class JokeAdmin(admin.ModelAdmin):
    list_display = ('category', 'type', 'safe', 'lang')
    search_fields = ('category', 'type', 'lang')
    list_filter = ('category', 'safe', 'nsfw', 'political', 'sexist') 

12. create superuser

python manage.py createsuperuser

13. Run the Django Server

python manage.py runserver

14. To Fetch Jokes API Endpoint

http://127.0.0.1:8000/api/fetch_jokes/

 





        

        

        

        



