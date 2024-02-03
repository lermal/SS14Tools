from django.shortcuts import render

# Create your views here.
def base(request):
    return render("<h1>Hellp world</h1>")