from django.shortcuts import render
from django.http import HttpResponse

from django import forms
from django.http import HttpResponse,HttpResponseRedirect

import cloudinary
import cloudinary.uploader
import cloudinary.api
from cloudinary.forms import cl_init_js_callbacks      
from .models import Item
from .forms import ItemForm, LogIn
# Create your views here.

def home(request):
	items = Item.objects.all()

	return render(request, 'home.html', {'items':items})

def item_detail(request, pk):
	item = Item.objects.get(pk=pk)
	request.session['post_log'] = '/delete'
	auth=False
	try:
		if request.session['auth'] != "Tru":
			return HttpResponseRedirect('/login')
		else:
			auth = True
	except:
		pass

	return render(request, 'item.html', {'item':item, 'auth':auth})

def delete(request, pk):
	try:
		if request.session['auth'] != "Tru":
			return HttpResponseRedirect('/login')
	except:
		return HttpResponseRedirect('/login')
	item = Item.objects.get(pk=pk)
	result = cloudinary.uploader.destroy(item.image.public_id)
	item.delete()
	return HttpResponseRedirect('/')


def upload(request):
	request.session['post_log'] = '/upload'
	try:
		if request.session['auth'] != "Tru":
			return HttpResponseRedirect('/login')
	except:
		return HttpResponseRedirect('/login')

	context = dict( backend_form = ItemForm())

	if request.method == 'POST':
		form = ItemForm(request.POST, request.FILES)
		context['posted'] = form.instance
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/success')

	return render(request, 'upload.html', context)

def auth(request):
	form = LogIn(request.POST or None)

	if form.is_valid():
		password = form.cleaned_data['password']
		request.session['auth'] = "Tru"
		try:
			return HttpResponseRedirect(request.session['post_log'])
		except:
			return HttpResponseRedirect('/')
	return render(request, 'login.html', {'form':form})

def success(request):
	return render(request, "success.html")