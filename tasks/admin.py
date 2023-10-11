from django.contrib import admin
from.models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display=('title','description','status')
    search_fields=('title',)


# Register your admin user here.
admin.site.register(Task,TaskAdmin)