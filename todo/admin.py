from django.contrib import admin
from .models import TodoModel
#これは管理画面を操作するときに使います

admin.site.register(TodoModel)