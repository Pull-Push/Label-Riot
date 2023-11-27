from django.shortcuts import render

# Create your views here.
def home(request):
    context = {'name':'Sokol'}
    return render(request, "labelriot/home.html", context)