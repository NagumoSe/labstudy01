from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("大富豪ページへようこそ.")

def index_template(request):
    return render(request, 'index.html')