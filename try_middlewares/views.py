from django.http import HttpResponse


def index(request):
    output = {'val': "hi"}
    return HttpResponse(output)
