from django.http import HttpResponse

def dashboard(request):
    return HttpResponse("Welcome to Alltoys!")

