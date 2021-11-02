from django.shortcuts import render
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.urls import reverse

# todo list homepage
def todo(request):
    if request.method == 'GET':
        #tasks not completed
        tasks_pending = Todo.objects.filter(completed=False).order_by('-task_id')
        #tasks completed
        tasks_completed = Todo.objects.filter(completed=True).order_by('-task_id')
        form = TodoForm()
        return render(request=request,
                      template_name = 'list.html',
                      context = {'tasks_pending':tasks_pending,                              'tasks_completed':tasks_completed, 'form':form})
    
    # when user submits form
    if request.method == 'POST':
        form=TodoForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data['task']
            # add new Todo object to QuerySet
            Todo.objects.create(task=task)
        # "redirect" to the todo homepage   
        return HttpResponseRedirect(reverse('todo'))


def task(request, task_id):
    if request.method == 'GET':
        # looking up a specific Todo object 
        todo = Todo.objects.get(pk=task_id)
        # make a form, pre-populate char field with the name of the task
        form = TodoForm(initial = {'task':todo.task})
        return render(request = request,
                      template_name = 'detail.html',
                      context = {
                          'form':form,
                          'task_id': task_id
                      })
    
    if request.method == 'POST':
        if 'save' in request.POST:
            form = TodoForm(request.POST)
            if form.is_valid():
                task=form.cleaned_data['task']
                # update task attribute of the task of the correct task_id to match user input
                Todo.objects.filter(pk=task_id).update(task=task)
        elif 'delete' in request.POST:
            Todo.objects.filter(pk=task_id).delete()
        elif 'mark complete' in request.POST:
            Todo.objects.filter(pk=task_id).update(completed=True)

        return HttpResponseRedirect(reverse('todo'))


def notes(request):
    if request.method == 'GET':
        notes = Note.objects.all().order_by('note_id')
        form = NotesForm()
        return render(request=request,
                      template_name = 'notes.html', 
                      context = {'notes':notes, 'form':form})

    if request.method == 'POST':
        form = NotesForm(request.POST)
        if form.is_valid():
            note = form.cleaned_data['notes']
            Note.objects.create(note_text=note)

        return HttpResponseRedirect(reverse('notes'))
