from django.shortcuts import render


def home(request):
    return render(request,'home.html')
def bootcamp(request):
    return render(request,'bootcamp.html')
def courses(request):
    return render(request,'courses.html')