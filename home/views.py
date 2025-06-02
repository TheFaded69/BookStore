from django.shortcuts import render

#todo to CBV
def home(request):
    return render(request, 'home/home.html')