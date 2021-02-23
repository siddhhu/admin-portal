from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *

@admin.register(Students)
class StudentAdmin(ImportExportModelAdmin):
    pass

@admin.register(Questions)
class QuestionAdmin(ImportExportModelAdmin):
    pass

admin.site.register(College)
admin.site.register(Branch)
admin.site.register(Subject)
admin.site.register(Answer)
admin.site.register(Exam)
admin.site.register(Proctor)
admin.site.register(Semester)