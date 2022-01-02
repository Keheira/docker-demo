from django.http import HttpResponse

def index(request):
    return HttpResponse("Welcome to Bytes and Builds.")

def about(request):
    return HttpResponse("Welcome to the Bytes and Builds about page.")
