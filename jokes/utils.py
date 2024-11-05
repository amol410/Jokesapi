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
