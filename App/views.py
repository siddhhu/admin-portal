from django.shortcuts import *
from .forms import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,Group
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from datetime import datetime
from tablib import Dataset
import random, string
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
@login_required(login_url='logins')
def home(r):
    data = {
        "user": User.objects.filter(username=r.user),
        "college": College.objects.filter(user_id=r.user)
    }
    return render(r,'home.html',data)

@login_required(login_url='logins')
def branch(r):
    college = College.objects.get(user_id=r.user)
    br = BranchForm(r.POST or None, r.FILES or None)
    if r.method == "POST":
        if br.is_valid():
            d = br.save(commit=False)
            d.college_id = College(college.college_id)
            d.save()
            messages.success(r, 'Branch add was successfully!')
            return redirect('branch')
    data = {
        "form": br,
        "branch": Branch.objects.filter(college_id=college.college_id).order_by('-branch_id')
    }
    return render(r,'branch.html',data)

@login_required(login_url='logins')
def subject(r):
    college = College.objects.get(user_id=r.user)
    sub = SubjectForm(r.POST or None, r.FILES or None)
    if r.method == "POST":
        if sub.is_valid():
            d = sub.save(commit=False)
            d.college_id = College(college.college_id)
            d.save()
            messages.success(r, 'Subject add was successfully!')
            return redirect('subject')
    data = {
        "form": sub,
        "subject": Subject.objects.filter(college_id=college.college_id).order_by('-subject_id')
    }
    return render(r,'subject.html',data)

@login_required(login_url='logins')
def semester(r):
    college = College.objects.get(user_id=r.user)
    sm = SemesterForm(r.POST or None, r.FILES or None)
    if r.method == "POST":
        if sm.is_valid():
            d = sm.save(commit=False)
            d.college_id = College(college.college_id)
            d.save()
            messages.success(r, 'Semester add was successfully!')
            return redirect('semester')
    data = {
        "form": sm,
        "semester": Semester.objects.filter(college_id=college.college_id).order_by('-semester_id')
    }
    return render(r,'semester.html',data)

@login_required(login_url='logins')
def exam(r):
    college = College.objects.get(user_id=r.user)
    ex = ExamForm(r.POST or None, r.FILES or None)
    if r.method == "POST":
        if ex.is_valid():
            ex.instance.college_id = College(college.college_id)
            ex.save()
            messages.success(r, 'Exam add was successfully!')
            return redirect('exam')
    data = {
        "form": ex,
        "exam": Exam.objects.filter(college_id=college.college_id).order_by('-exam_id')
    }
    return render(r,'exam.html',data)

@login_required(login_url='logins')
def proctor(r):
    college = College.objects.get(user_id=r.user)
    proctor = ProctorForm(r.POST or None, r.FILES or None)
    if r.method == "POST":
        if proctor.is_valid():
            d = proctor.save(commit=False)
            d.college_id = College(college.college_id)
            d.proctor_password = r.POST.get('proctor_phone')
            d.save()
            messages.success(r, 'Proctor add was successfully!')
            return redirect('proctor')
    data = {
        "form": proctor,
        "proctor": Proctor.objects.filter(college_id=college.college_id).order_by('-proctor_id')
    }
    return render(r,'proctor.html',data)

@login_required(login_url='logins')
def students(r):
    college = College.objects.get(user_id=r.user)
    data = {
        "students": Students.objects.filter(college_id=college.college_id).order_by('-student_id')
    }
    return render(r,'students.html',data)

@login_required(login_url='logins')
def questions(r):
    college = College.objects.get(user_id=r.user)
    data = {
        "questions": Questions.objects.filter(college_id=college.college_id).order_by('-question_id')
    }
    return render(r,'questions.html',data)

def logins(r):
    form = LoginForm(r.POST or None)
    if r.method == 'POST':
        if form.is_valid:
            email = r.POST['email']
            password = r.POST['password']
            try:
                username = User.objects.get(email=email.lower()).username
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(r, user)
                    return redirect('home')
                else:
                    messages.error(r,"Your password is incorrect!")
                    return redirect('logins')

            except User.DoesNotExist:
                messages.error(r,"The email address or password is incorrect. Please retry...")
                return redirect('logins')

    data = {"form": form}
    return render(r, 'signin.html', data)

def logouts(r):
    logout(r)
    return redirect('logins')

@login_required(login_url='logins')
def password_change(r):
    if r.method == 'POST':
        form = PasswordChangeForm(r.user, r.POST or None)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(r, user)  # Important!
            messages.success(r, 'Your password was successfully updated!')
            return redirect('password_change_renter')
        else:
            messages.error(r, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(r.user)
    data = {
        "form":form,
    }
    return render(r, 'password_change.html', data)

@login_required(login_url='logins')
def upload_data(r):
    password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    college = College.objects.get(user_id=r.user)
    if r.method == 'POST':
        dataset = Dataset()
        new_file = r.FILES['upload_file']
        imported_data = dataset.load(new_file.read(), format='xlsx')
        for data in imported_data:
            value = Students(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
            )
            value.student_password = password
            value.branch_id = Branch(r.POST.get('branch_id'))
            value.semester_id = Semester(r.POST.get('semester_id'))
            value.college_id = College(college.college_id)
            value.save()
            subject = "For student Exam Portal"
            message = f"Visit for ExamPortal: http://127.0.0.1:8000\nUsername: {data[2]}\n Password: {password}"
            sender = settings.EMAIL_HOST_USER
            send_mail(subject, message, sender, [data[2]])
        messages.success(r, 'Your Students File successfully upload!')
        return redirect('students')
    st = StudentForm(r.POST or None)
    ex = QuestionForm(r.POST or None)
    data = {
        "question": ex,
        "student": st,
        "branch": Branch.objects.filter(college_id=college.college_id)
    }
    return render(r, 'upload_data.html',data)

@login_required(login_url='logins')
def upload_questions(r):
    college = College.objects.get(user_id=r.user)
    if r.method == 'POST':
        dataset = Dataset()
        new_file = r.FILES['upload_questions']
        imported_data = dataset.load(new_file.read(), format='xlsx')
        for data in imported_data:
            value = Questions(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7]
            )
            value.college_id = College(college.college_id)
            value.branch_id = Branch(r.POST.get('branch_id'))
            value.subject_id = Subject(r.POST.get('subject_id'))
            value.exam_id = Exam(r.POST.get('exam_id'))
            value.section = r.POST.get('section')
            value.save()
        messages.success(r, 'Your Questions File successfully upload!')
        return redirect('questions')
    form = QuestionForm(r.POST or None)
    data = {
        "question":form,
    }
    return render(r, 'upload_data.html',data)

@login_required(login_url=logins)
def update_college(r,c_id):
    user = User.objects.get(username=r.user)
    college = College.objects.get(slug=c_id)
    clg_form = UpdateCollege(r.POST or None, instance=college)
    user_form = UpdateUser(r.POST or None, instance=user)
    if r.method == "POST":
        if user_form.is_valid() and clg_form.is_valid():
            user_form.save()
            clg_form.save()
            return redirect('home')
    else:
        user_form = UpdateUser(instance=user)
        clg_form = UpdateCollege(instance=college)
    data = {
        "college": clg_form,
        "user": user_form,
    }
    return render(r,'update_college.html',data)

@login_required(login_url='logins')
def student_view(r,st_id):
    student = Students.objects.get(slug=st_id)
    form = StudentUpdateForm(r.POST or None,instance=student)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../student_view/" + student.slug)
        else:
            form = StudentUpdateForm(instance=student)

    data = {
        "student": Students.objects.filter(slug=st_id),
        "form": form,
    }
    return render(r,'student_view.html',data)

@login_required(login_url='logins')
def proctor_view(r,pr_id):
    proctor = Proctor.objects.get(slug=pr_id)
    form = ProctorForm(r.POST or None,instance=proctor)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../proctor_view/" + proctor.slug)
        else:
            form = ProctorForm(instance=proctor)

    data = {
        "proctor": Proctor.objects.filter(slug=pr_id),
        "form": form,
    }
    return render(r, 'proctor_view.html', data)

@login_required(login_url='logins')
def exam_view(r,ex_id):
    exam = Exam.objects.get(slug=ex_id)
    form = ExamForm(r.POST or None,instance=exam)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../exam_view/" + exam.slug)
        else:
            form = ExamForm(instance=exam)

    data = {
        "exam": Exam.objects.filter(slug=ex_id),
        "questions": Questions.objects.filter(exam_id__slug=ex_id),
        "form": form,
    }
    return render(r, 'exam_view.html', data)

@login_required(login_url='logins')
def question_view(r,qs_id):
    question = Questions.objects.get(slug=qs_id)
    form = QuestionUpdateForm(r.POST or None,instance=question)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect("../question_view/" + question.slug)
        else:
            form = QuestionUpdateForm(instance=question)

    data = {
        "question": Questions.objects.filter(slug=qs_id),
        "form": form,
    }
    return render(r,'question_view.html',data)

@login_required(login_url='logins')
def branch_update(r,br_id):
    branch = Branch.objects.get(slug=br_id)
    form = BranchForm(r.POST or None,instance=branch)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('branch')
        else:
            form = BranchForm(instance=branch)

    data = {
        "form": form,
    }
    return render(r, 'branch_update.html', data)

@login_required(login_url='logins')
def subject_update(r,su_id):
    subject = Subject.objects.get(slug=su_id)
    form = SubjectForm(r.POST or None,instance=subject)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('subject')
        else:
            form = SubjectForm(instance=subject)

    data = {
        "form": form,
    }
    return render(r, 'branch_update.html', data)

@login_required(login_url='logins')
def semester_update(r,sem_id):
    semester = Semester.objects.get(slug=sem_id)
    form = SemesterForm(r.POST or None,instance=semester)
    if r.method == "POST":
        if form.is_valid():
            form.save()
            return redirect('semester')
        else:
            form = SemesterForm(instance=semester)

    data = {
        "form": form,
    }
    return render(r, 'branch_update.html', data)

@login_required(login_url=logins)
def subject_delete(r,dl_id):
    query = Subject.objects.get(slug=dl_id)
    query.delete()
    return redirect('subject')\

@login_required(login_url=logins)
def branch_delete(r,dl_id):
    query = Branch.objects.get(slug=dl_id)
    query.delete()
    return redirect('branch')

@login_required(login_url=logins)
def semester_delete(r,dl_id):
    query = Semester.objects.get(slug=dl_id)
    query.delete()
    return redirect('semester')

@login_required(login_url=logins)
def exam_delete(r,dl_id):
    query = Exam.objects.get(slug=dl_id)
    query.delete()
    return redirect('exam')

@login_required(login_url=logins)
def question_delete(r,dl_id):
    query = Questions.objects.get(slug=dl_id)
    query.delete()
    return redirect('questions')

@login_required(login_url=logins)
def student_delete(r,dl_id):
    query = Students.objects.get(slug=dl_id)
    query.delete()
    return redirect('students')

@login_required(login_url=logins)
def proctor_delete(r,dl_id):
    query = Proctor.objects.get(slug=dl_id)
    query.delete()
    return redirect('proctor')