from django.shortcuts import render
from .forms import*


def landing(request):
    form = PeopleForm(request.POST or None)
    form2 = DepartamentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_form = form.save()

    if request.method == "POST" and form2.is_valid():
        new_form = form2.save()

    return render(request, 'landing/landing.html', locals())
