from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

import os
import tweepy


# Create your views here.
def index(request):
    return render(request, "index.html")

def project(request):
    bearer_token = os.environ.get('bearer_token_twitter_JOSEIZAM')
    client = tweepy.Client(bearer_token=bearer_token, return_type=dict)


    tweets = client.search_recent_tweets(query='IzkiaxBoricMV')

    context = {
       'data': tweets['data'],
       'hashtag': 'IzkiaxBoricMV'
    }

    return render(request, "proyecto.html", context=context)