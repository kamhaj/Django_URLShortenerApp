from django.contrib import admin

# Register your models here.

#bring in models
from .models import URL

admin.site.site_header = "URL App Admin"
admin.site.site_title = "URL app Admin Area"
admin.site.index_title = "Welcome to the URL Shortener admin area"

admin.site.register(URL)

