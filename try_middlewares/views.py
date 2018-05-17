from django.http import HttpResponse


def index(request):
    output = "one"
    return HttpResponse(output)


def index2(request):
    output = "two"
    return HttpResponse(output)


def index3(request):
    output = "three"
    return HttpResponse(output)