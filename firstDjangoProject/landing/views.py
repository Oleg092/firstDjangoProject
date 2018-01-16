from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView, DetailView, ListView
from .forms import *
from .models import Departament, People


# class HomeView(TemplateView):
#    template_name = "landing/home.html"


class PeopleListView(ListView):
    model = People
    template_name = "landing/home.html"


def landing(request):
    departament = Departament.objects.all()
    people = People.objects.all()
    print(departament)
    form = PeopleForm(request.POST or None)
    form2 = DepartamentForm(request.POST or None)

    if request.method == "POST" and 'add' in request.POST:  # Добавление нового департамента
        if request.POST['add'] == 'departament' and form2.is_valid():
            new_form = form2.save()
        if request.POST['add'] == 'people' and form.is_valid():
            new_form = form.save()

    if request.method == "POST" and 'delete' in request.POST:  # блок кода для удаления департаментов и сотрудникков
        if request.POST['delete'] == 'departament':
            id_dep = request.POST['id']
            b = Departament.objects.get(id=id_dep)
            b.delete()
        if request.POST['delete'] == 'people':
            id_people = request.POST['id']
            b = People.objects.get(id=id_people)
            b.delete()
    if request.method == "POST" and 'update' in request.POST:   #Обновление данных в таблице департамент
        if request.POST['update'] == 'departament' and form2.is_valid():
            id_dep = request.POST['id']
            b = Departament.objects.get(id=id_dep)
            b.name = request.POST['name']
            b.address = request.POST['address']
            b.website = request.POST['website']
            b.save()
        if request.POST['update'] == 'people' and form.is_valid():
            id_people = request.POST['id']
            b = People.objects.get(id=id_people)
            b.name = request.POST['name']
            b.surName = request.POST['surName']
            b.lastName = request.POST['lastName']
            b.birdDate = request.POST['birdDate']
            b.email = request.POST['email']
            b.photo = request.POST['photo']
            add = Departament.objects.get(id=request.POST['departament'])
            b.departament = add
            b.save()

    return render(request, 'landing/landing.html', locals())
