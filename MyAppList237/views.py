from django.shortcuts import render, redirect, get_object_or_404
from .form import FormTask
from .models import Task

# Create your views here.


def index(request):
  form = FormTask(request.POST or None)
  if form.is_valid():
    form.save()
    form = FormTask()   #ici on cree une tache et on l'ajoute dans la base de données
  list = Task.objects.all()
  context = {
    'form': form,
    'taches': list,
  }
  return render(request, "index.html", context)

def update(request, my_id):
  obj = get_object_or_404(Task, id=my_id)
  form = FormTask(request.POST or None, instance=obj)  # !! ici on met à jour une tache dans la bd et on l'affiche
  context= {
    'form': form,
  }
  if form.is_valid():
    form.save()
    return redirect('index')
  return render(request, 'update.html', context)

def delete(request, my_id):
  obj = get_object_or_404(Task, id=my_id)
  obj.delete()
  return redirect('index')
