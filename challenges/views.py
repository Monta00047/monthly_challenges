from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect

monthly_challenges = {
  'january': 'Eat 500g proteins every day!',
  'february': 'Learn how to fish!',
  'march': 'Become a Django Developer!',
  'april': 'Wake up at dawn every day!',
  'may': 'Read one book per week!',
  'june': 'Run 100 kilometers in total!',
  'july': 'Launch a personal blog!',
  'august': 'No sugar for 30 days!',
  'september': 'Master the basics of Spanish!',
  'october': 'Build and deploy a mobile app!',
  'november': 'Practice meditation daily!',
  'december': 'Reflect and write your yearly review!'
}

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > 12 or month < 1:
     return HttpResponseNotFound('Invalid Month!')
    redirect_month = months[month-1]
    return HttpResponseRedirect('/challenges/' + redirect_month)

def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
  except:
    return HttpResponseNotFound('This month is not supported!')
  return HttpResponse(challenge_text)