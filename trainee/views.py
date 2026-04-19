from django.shortcuts import render
from django.shortcuts import redirect

from .models import Trainee


def trainee_list(request):
	return render(request, 'trainee/list.html')


def trainee_detail(request, id):
	return render(request, 'trainee/detail.html')


def trainee_update(request, id):
	return render(request, 'trainee/update.html')


def trainee_delete(request, id):
	return render(request, 'trainee/delete.html')


def trainee_add(request):
	if request.method == 'POST':
		name = request.POST.get('name', '').strip()
		if not name:
			return render(request, 'trainee/add.html', {'error': 'Name is required.'})

		Trainee.objects.create(name=name)
		return redirect('/trainee/')

	return render(request, 'trainee/add.html')
