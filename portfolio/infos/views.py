from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

name = "FirstName1 LastName1"

def general(request):
	return render(
		request=request,
		template_name="infos/general.html",
		context={"name": name, "title": "Homepage"}
	)

def me(request):
	return render(
		request=request,
		template_name="infos/me.html",
		context={"name": name, "title": "About me"}
	)

def contact(request):
	return render(
		request=request,
		template_name="infos/contact.html",
		context={"name": name, "title": "Contact"}
	)


