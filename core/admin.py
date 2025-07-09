from django.contrib import admin
from .models import Expense, Project, Task

admin.site.register(Expense)
admin.site.register(Project)
admin.site.register(Task)
