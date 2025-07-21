from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound,HttpResponseRedirect
from django.urls import reverse

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
  'october': 'Build and deploy a fullstack app!',
  'november': 'Practice meditation daily!',
  'december': None
}

def index(request):
  months = list(monthly_challenges.keys())

  return render (request, "challenges/index.html", {
    "months": months
  })

def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())
    if month > 12 or month < 1:
     return HttpResponseNotFound('<h1>Invalid Month!</h1>')
    redirect_month = months[month-1]
    redirect_path = reverse('month-challenge', args=[redirect_month])
    return HttpResponseRedirect(redirect_path)

def monthly_challenge(request, month):
  try:
    challenge_text = monthly_challenges[month]
    return render(request,"challenges/challenge.html",{
      "month": month,
      "text": challenge_text
    })
  except:
    return HttpResponseNotFound('<h1>This month is not supported!</h1>')
