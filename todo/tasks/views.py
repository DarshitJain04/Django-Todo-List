from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.views.decorators.http import require_POST

def index(request):
	tasks=Task.objects.all()
	form=TaskForm() 
	context={'tasks':tasks , 'form':form}	
	return render(request, 'tasks/homepage.html',context)


@require_POST
def addtask(request):
	form = TaskForm(request.POST)
	print(request.POST['title'])
	if form.is_valid():
		new_task = Task(title=request.POST['title'])
		new_task.save()
	return redirect('tasks')

def updateTask(request,pk):
	task = Task.objects.get(id=pk)

	form = TaskForm(instance=task)

	if request.method == 'POST':
		form = TaskForm(request.POST ,instance=task)
		if form.is_valid():
			form.save()
		return redirect('/') 

	context = {'form':form}


	return render(request, 'tasks/update_task.html',context)

def deleteTask(request,pk):
	item = Task.objects.get(id=pk)

	if request.method == 'POST':
		item.delete()
		return redirect('/') 

	context = {'item':item}

	return render(request,'tasks/delete.html',context)
