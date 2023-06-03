import json
from django.http import JsonResponse
from django.shortcuts import render
from paraphrasing import parse_user_input

def home(request):
    return render(request, "home.html")

def result(request):
    user_input = request.GET.get('TEXT', '')
    
    paraphrased = parse_user_input(user_input)

    return render(request, "result.html", {"paraphrased": paraphrased, "user_input":user_input})

    # return JsonResponse(paraphrased, safe=False)