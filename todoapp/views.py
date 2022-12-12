from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TodoForm
from .models import Todo


@login_required
def index(request):
    user = request.user
    todos = Todo.objects.filter(author=user).order_by('-updated_at')
    q = request.GET.get('q')
    if q:
        todos = todos.filter(status__exact=int(q))
    ctx = {
        'todos': todos
    }
    return render(request, 'index.html', ctx)


@login_required
def single(request, pk):
    todo = Todo.objects.get(id=pk)
    form = TodoForm(request.POST or None, instance=todo)

    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = request.user
        obj.save()
        messages.success(request, 'successfully updated')
        return redirect('/')
    ctx = {
        'form': form
    }
    return render(request, 'single.html', ctx)


@login_required
def delete(request, pk):
    obj = get_object_or_404(Todo, id=pk)
    if request.method == 'POST':
        obj.delete()
        messages.error(request, 'successfully deleted')
        return redirect('/')
    return render(request, 'delete.html', {'obj': obj})


@login_required
def create(request):
    user = request.user
    form = TodoForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.author = user
        obj.save()
        messages.success(request, 'successfully created')
        return redirect('/')
    return render(request, 'single.html', {'form': form})
