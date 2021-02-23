from django.contrib import admin
from django.urls import path,include
from App import views
from django.conf.urls.static import static
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home,name='home'),
    path('logins/',views.logins,name="logins"),
    path('logouts/',views.logouts,name="logouts"),
    path('password_change/',views.password_change,name="password_change"),
    path('upload_data/',views.upload_data,name="upload_data"),
    path('upload_questions/',views.upload_questions,name="upload_questions"),
    path('branch/',views.branch,name="branch"),
    path('branch_update/<slug:br_id>',views.branch_update,name="branch_update"),
    path('semester/',views.semester,name="semester"),
    path('semester_update/<slug:sem_id>',views.semester_update,name="semester_update"),
    path('subject/',views.subject,name="subject"),
    path('subject_update/<slug:su_id>',views.subject_update,name="subject_update"),
    path('proctor/',views.proctor,name="proctor"),
    path('proctor_view/<slug:pr_id>',views.proctor_view,name="proctor_view"),
    path('exam/',views.exam,name="exam"),
    path('exam_view/<slug:ex_id>',views.exam_view,name="exam_view"),
    path('students/',views.students,name="students"),
    path('student_view/<slug:st_id>',views.student_view,name="student_view"),
    path('questions/',views.questions,name="questions"),
    path('question_view/<slug:qs_id>',views.question_view,name="question_view"),
    path('update_college/<slug:c_id>',views.update_college,name="update_college"),
    path('subject_delete/<slug:dl_id>',views.subject_delete,name="subject_delete"),
    path('semester_delete/<slug:dl_id>',views.semester_delete,name="semester_delete"),
    path('branch_delete/<slug:dl_id>',views.branch_delete,name="branch_delete"),
    path('student_delete/<slug:dl_id>',views.student_delete,name="student_delete"),
    path('question_delete/<slug:dl_id>',views.question_delete,name="question_delete"),
    path('exam_delete/<slug:dl_id>',views.exam_delete,name="exam_delete"),
    path('proctor_delete/<slug:dl_id>',views.proctor_delete,name="proctor_delete"),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':  settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
