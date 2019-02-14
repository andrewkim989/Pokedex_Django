from django.shortcuts import render, redirect
import requests

def index(request):
    return render(request, "main.html")

def pokemon(request, num):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/" + num)
    pokemon = response.json()

    context = {
        "num": num,
        "name": pokemon["forms"][0]["name"].capitalize(),
        "types": pokemon["types"],
        "height": pokemon["height"],
        "weight": pokemon["weight"],
        "abilities": pokemon["abilities"],
        "appearances": pokemon["game_indices"],
        "experience": pokemon["base_experience"],
        "stats": pokemon["stats"],
        "moves": pokemon["moves"]
    }

    return render(request, "pokemon.html", context)