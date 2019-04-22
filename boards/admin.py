from django.contrib import admin
from .models import Board, Topic, Post


admin.site.register(Board, list_display=('name','description'))
admin.site.register(Topic, list_display=('subject','board', 'starter', 'last_updated'))
admin.site.register(Post, list_display=('message', 'topic', 'created_at', 'updated_at', 'created_by', 'updated_by'))
