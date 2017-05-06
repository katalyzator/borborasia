from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from cart.cart import Cart
from main.models import *


# def add_to_cart(request, id):
#     tour = Tour.objects.get(id=id)
#     cart = Cart(request)
#     cart.add(tour, 10, 1)
#
#     return HttpResponseRedirect('/tours')
#
#
# def get_cart(request):
#     return render_to_response('cart.html', dict(cart=Cart(request)))


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
    tours_list = Tour.objects.all()
    paginator = Paginator(tours_list, 1)

    page = request.GET.get('page')

    try:
        tours = paginator.page(page)

    except PageNotAnInteger:
        tours = paginator.page(1)

    except EmptyPage:

        tours = paginator.page(paginator.num_pages)

    context = {"tours": tours}
    template = 'tours.html'

    return render_to_response(template, context)


def todo_view(request):
    context = {}
    template = 'todolist.html'

    return render(request, template, context)


def review_view(request):
    feedback = Feedback.objects.all()
    context = {"feedback": feedback}
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


def region_view(request):
    context = {}
    template = 'region.html'

    return render(request, template, context)
