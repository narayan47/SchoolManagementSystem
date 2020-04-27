from django.contrib import admin
from .models import*


admin.site.site_header = "Student Management System"



# Register your models here.
@admin.register(ClassSetup)
class ClassSetupAdmin(admin.ModelAdmin):
    list_display = ['class_name', 'section_name', 'subject_name', 'class_teacher',]


admin.site.register(Section)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Subject)
admin.site.register(Standard)
