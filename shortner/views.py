from django.http.response import HttpResponse
from django.shortcuts import render
import requests


# Create your views here.
def index(request):
    if request.method == "POST":
        link = request.POST["link"]
        url = "https://url-shortener-service.p.rapidapi.com/shorten"

        payload = f"url={ link }"
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'x-rapidapi-host': "url-shortener-service.p.rapidapi.com",
            'x-rapidapi-key': "your api key here"
        }

        response = requests.request("POST", url, data=payload, headers=headers)
        if  not response:
            return HttpResponse("Error")
        else:
            final_url = response.json()['result_url']
            return render(request,"shortner/index.html",{
                "message":final_url
            })
    return render(request, "shortner/index.html")
