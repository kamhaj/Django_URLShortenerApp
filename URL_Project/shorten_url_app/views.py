from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from datetime import datetime
from .models import URL
from .URL_encoder import URL_encoder
from .forms import URLForm

URL_object = URL_encoder(id=len(URL.objects.all()), url_list=list(URL.objects.values('url_text'))  )     #id number based on current URL quantity in a database

# Get URLs and display them
def home_page(request):
    return render(request, 'shorten_url_app/home_page.html')


def show_form(request):
    form = URLForm()
    base_domain = request.META['HTTP_HOST']     #mydomain
    if request.method == "POST":                #populate url form with user data if POST request
        form = URLForm(request.POST)
        if form.is_valid():
            #add any form validation here
            user_url = form.cleaned_data['user_url']
            encoded_url = URL_object.encode_url(user_url=user_url, base_domain=str(base_domain))
            condition =  " {\'url_text\': \'" + str(user_url) + "\'}" not in URL_object.url_list
            if condition:                                                                           #avoid duplicates
                p = URL(url_text=user_url, short_url_text=encoded_url, pub_date=datetime.now())     #create model with gathered data
                p.save()

        context = {"form":form, "user_url":user_url, "encoded_url":encoded_url, "base_domain":base_domain}
        return render(request, 'shorten_url_app/form.html', context)

    else:                                   #GET method, empty form rendered
        return render(request, 'shorten_url_app/form.html', {"form": form})


# def index(request):
#     urls_list = URL.objects.order_by('-pub_date')
#     context = {'urls_list': urls_list}
#     return render(request, 'shorten_url_app/index.html', context)


