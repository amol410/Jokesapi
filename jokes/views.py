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
