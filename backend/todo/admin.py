from django.contrib import admin
from .models import Todo  # add this


class TodoAdmin(admin.ModelAdmin): 
    list_display = ('title', 'description', 'completed') 


admin.site.register(Todo, TodoAdmin)
