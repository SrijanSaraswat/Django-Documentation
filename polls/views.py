from django.http import HttpResponse


def index(request):
    # processing - database, cache, rendering HTML template
    return HttpResponse("Hello, world. You're at the polls index.")