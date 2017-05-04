from django.shortcuts import render

from main.models import *


def index_view(request):
    context = {}
    template = 'main/index.html'

    return render(request, template, context)


def about_view(request):
    vacancy = Vacancy.objects.all()
    personal = Personal.objects.all()
    context = {"personal": personal, "vacancy": vacancy}
    template = 'about.html'

    return render(request, template, context)


def tours_view(request):
    tours = Tour.objects.all()
    context = {"tours": tours}
    template = 'tours.html'

    return render(request, template, context)


def todo_view(request):
    context = {}
    template = 'todolist.html'

    return render(request, template, context)


def review_view(request):
    context = {}
    template = 'review.html'

    return render(request, template, context)


def single_tour(request, id):
    item = Tour.objects.get(id=id)
    images = TourImage.objects.filter(tour=item)
    print item.winter
    print item.summer
    context = {"tour": item, "images": images}
    template = 'place.html'

    return render(request, template, context)
