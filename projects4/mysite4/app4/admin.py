from django.contrib import admin
from . models import Student
from . models import *

# Register your models here.

admin.site.register(Student)
admin.site.register(Food)
admin.site.register(Restaurant)
admin.site.register(Food2)
admin.site.register(Pay)
