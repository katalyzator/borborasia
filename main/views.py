from django.shortcuts import render

from main.models import Personal


def index_view(request):
    context = {}
    template = 'main/index.html'

    return render(request, template, context)


def about_view(request):
    personal = Personal.objects.all()
    context = {"personal": personal}
    template = 'about.html'

    return render(request, template, context)


def tours_view(request):
    context = {}
    template = 'tours.html'

    return render(request, template, context)


def todo_view(request):
    context = {}
    template = 'todolist.html'

    return render(request, template, context)
