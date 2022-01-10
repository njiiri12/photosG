from django.contrib import admin

from gram.views import make_a_post
from .models import *

# Register your models here.
admin.site.register(Picture)
