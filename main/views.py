from django.shortcuts import render


def index_view(request):
    context = {}
    template = 'main/index.html'

    return render(request, template, context)


def about_view(request):
    context = {}
    template = 'about.html'

    return render(request, template, context)
