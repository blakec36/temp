from django.shortcuts import render
from django.http.response import HttpResponse


def home(request):
    return render(request, 'dashboard/dashboard.html')
def about(request):
    return render(request, 'layout/about.html')
def kauai(request):
    return render(request, 'layout/kauai.html')
def catalina(request):
    return render(request, 'layout/catalina.html')
def mutau(request):
    return render(request, 'layout/mutau.html')
def canada(request):
    return render(request, 'layout/canada.html')
def ireland(request):
    return render(request, 'layout/ireland.html')
def poland(request):
    return render(request, 'layout/poland.html')
def golf(request):
    return render(request, 'layout/golf.html')
def upcoming(request):
    return render(request, 'layout/upcoming.html')