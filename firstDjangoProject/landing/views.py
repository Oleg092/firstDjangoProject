from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import *
from .models import Departament, People


def landing(request):

    departament = Departament.objects.all()
    people = People.objects.all()
    print(departament)
    form = PeopleForm(request.POST or None)
    form2 = DepartamentForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        new_form = form.save()

    if request.method == "POST" and form2.is_valid():
        new_form = form2.save()

    if request.method == "POST" and 'delete' in request.POST:
        if request.POST['delete'] == 'departament':
            id_dep = request.POST['id']
            b = Departament.objects.get(id=id_dep)
            b.delete()
        if request.POST['delete'] == 'people':
            id_people = request.POST['id']
            b = People.objects.get(id=id_people)
            b.delete()

    return render(request, 'landing/landing.html', locals())



