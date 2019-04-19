from django.contrib import admin
from .models import Board


admin.site.register(Board, list_display=('name','description'))
