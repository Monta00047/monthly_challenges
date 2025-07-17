from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
# Create your views here.

def monthly_challenge(request, month):
  challenge_text = None
  if month == 'january':
    challenge_text = 'Eat 500g proteins every day!'
  elif month == 'february':
    challenge_text = 'Learn how to fish!'
  elif month == 'march':
    challenge_text = 'Become a Django Developer!'
  else :
    return HttpResponseNotFound("This month is not supported")
  
  return HttpResponse(challenge_text)