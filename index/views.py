from django.shortcuts import render

# Vista index

def index(request):
    return render(request, 'index.html')