from django.shortcuts import render,redirect
from .models import Data
from .forms import DataForm
from django.contrib import messages
from django.views.generic import ListView
from django.db.models import Q

def home(request):
	if request.method == "POST":
		form = DataForm(request.POST or None)
		if form.is_valid():
			form.save()
			messages.success(request,('Your form was successfully added'))
		else:
			messages.error(request, 'Error saving form')
		return redirect('firstapp:data')
	form = DataForm()
	return render(request,'firstapp/index.html',context={'form':form})

def data(request):
	datas = Data.objects.all()
	context ={
	'datas':datas
	}

	return render(request,'firstapp/data.html',context)

def search(request):
	return render(request,'firstapp/search.html')


class SearchResultsView(ListView):
	model= Data
	context_object_name = 'results'
	template_name='firstapp/searchresults.html'
	def get_queryset(self):
		query = self.request.GET.get('q')
		return Data.objects.filter(
			Q(name__icontains=query)| Q(email__icontains=query)
			)
	