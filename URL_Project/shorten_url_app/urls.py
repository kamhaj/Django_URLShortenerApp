from django.urls import path

from . import views

app_name = 'shorten_url_app'
urlpatterns = [
    path('show_form/', views.show_form, name='show_form'),
    path('aaa/', views.home_page, name='home_page')

]