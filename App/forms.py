from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import EmailValidator
from django import forms

class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['email','password',]

class ProctorForm(ModelForm):
    class Meta:
        model = Proctor
        widgets = {
            'proctor_email': forms.EmailInput(attrs={'class': 'form-control'}),
            'proctor_phone': forms.NumberInput(attrs={'class': 'form-control'})
        }
        exclude = ['college_id','doc','slug','proctor_password']

class BranchForm(ModelForm):
    class Meta:
        model = Branch
        exclude = ['college_id','doc','slug']

class SemesterForm(ModelForm):
    class Meta:
        model = Semester
        exclude = ['college_id','doc','slug']

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        widgets = {
            'total_marks': forms.NumberInput(attrs={'class': 'form-control'})
        }
        exclude = ['college_id','doc','slug']

class ExamForm(ModelForm):
    class Meta:
        model = Exam
        labels = {
            "duration": "Duration(in minutes)",
        }
        widgets = {
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'type':"date",'class': 'form-control'}),
            'starting_time': forms.TimeInput(attrs={'type':"time",'class': 'form-control'}),
            'ending_time': forms.TimeInput(attrs={'type':"time",'class': 'form-control'}),
        }
        exclude = ['college_id','doc','slug']

class QuestionForm(ModelForm):
    class Meta:
        model = Questions
        fields = ['branch_id','subject_id','exam_id','section']

class QuestionUpdateForm(ModelForm):
    class Meta:
        model = Questions
        exclude = ['college_id','doc','slug']

class StudentForm(ModelForm):
    class Meta:
        model = Students
        fields = ['branch_id','semester_id']

class StudentUpdateForm(ModelForm):
    class Meta:
        model = Students
        exclude = ['college_id','doc','slug','student_password']

class UpdateUser(forms.ModelForm):
    email = forms.EmailField(label="Email")
    class Meta:
        model = User
        fields = ['email',]

class UpdateCollege(forms.ModelForm):
    class Meta:
        model = College
        exclude = ['user_id','doc','slug']
