from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView, CreateView
from .forms import *
from .models import People


def landing(request):
    people = People.objects.all()
    form = PeopleForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            flag = "на пидор, забирай свой флаг, и дальше написан какой то флаг"

    return render(request, 'landing/index.html', locals())
