from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

name = "FirstName1 LastName1"

def general(request):
	c = {"name": name, "title": "Homepage"}
	return render(
		request=request,
		template_name="infos/general.html",
		context=c
	)

def me(request):
	c = {"name": name, "title": "About me"}
	return render(
		request=request,
		template_name="infos/me.html",
		context=c
	)

def contact(request):
	c = {"name": name, "title": "Contact"}
	return render(
		request=request,
		template_name="infos/contact.html",
		context=c
	)


