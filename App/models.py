from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from datetime import datetime

# Create your models here.
class College(models.Model):
    college_id = models.AutoField(primary_key=True)
    college_name = models.CharField(max_length=200)
    college_code = models.CharField(max_length=200)
    college_university = models.CharField(max_length=200)
    college_address = models.CharField(max_length=200)
    college_contact = models.CharField(max_length=200)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    doc = models.DateTimeField(default=datetime.now(), blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.college_name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.college_name+'-'+str(self.doc))
        super(College, self).save(*args,**kwargs)

class Branch(models.Model):
    branch_id = models.AutoField(primary_key=True)
    branch_name = models.CharField(max_length=100)
    college_id = models.ForeignKey(College, on_delete=models.CASCADE)
    doc = models.DateTimeField(default=datetime.now(), blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.branch_name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.branch_name+'-'+str(self.doc))
        super(Branch, self).save(*args,**kwargs)

class Subject(models.Model):
    subject_id = models.AutoField(primary_key=True)
    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=100)
    total_marks = models.CharField(max_length=100)
    branch_id = models.ForeignKey(Branch,on_delete=models.SET_NULL,null=True)
    college_id = models.ForeignKey(College, on_delete=models.CASCADE)
    doc = models.DateTimeField(default=datetime.now(), blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.subject_name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.subject_name+'-'+str(self.doc))
        super(Subject, self).save(*args,**kwargs)

class Semester(models.Model):
    semester_id = models.AutoField(primary_key=True)
    semester_name = models.CharField(max_length=100)
    college_id = models.ForeignKey(College, on_delete=models.CASCADE)
    doc = models.DateTimeField(default=datetime.now(), blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.semester_name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.semester_name+'-'+str(self.doc))
        super(Semester, self).save(*args,**kwargs)

class Proctor(models.Model):
    proctor_id = models.AutoField(primary_key=True)
    proctor_name = models.CharField(max_length=100)
    proctor_email = models.CharField(max_length=100)
    proctor_phone = models.CharField(max_length=100)
    proctor_password = models.CharField(max_length=100)
    college_id = models.ForeignKey(College,on_delete=models.CASCADE)
    assign_section = models.CharField(max_length=100,blank=True,choices=(("A", "A"), ("B", "B"),("C","C"),("D","D")))
    doc = models.DateTimeField(default=datetime.now(), blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.proctor_name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.proctor_name+'-'+str(self.doc))
        super(Proctor, self).save(*args,**kwargs)

class Students(models.Model):
    student_id = models.AutoField(primary_key=True,blank=True)
    student_name = models.CharField(max_length=200)
    student_email = models.EmailField()
    student_phone = models.CharField(max_length=50)
    student_address = models.CharField(max_length=200)
    session = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    section = models.CharField(max_length=100,blank=True)
    student_password = models.CharField(max_length=100)
    college_id = models.ForeignKey(College, on_delete=models.CASCADE)
    branch_id = models.ForeignKey(Branch, on_delete=models.SET_NULL,null=True)
    semester_id = models.ForeignKey(Semester, on_delete=models.SET_NULL,null=True)
    doc = models.DateTimeField(default=datetime.now(), blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.student_name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.student_name+'-'+str(self.doc))
        super(Students, self).save(*args,**kwargs)

class Exam(models.Model):
    exam_id = models.AutoField(primary_key=True)
    exam_name = models.CharField(max_length=100)
    instructions = models.CharField(max_length=2000,blank=True)
    duration = models.CharField(max_length=100)
    date = models.DateField()
    starting_time = models.CharField(max_length=100)
    ending_time = models.CharField(max_length=100)
    semester_id = models.ForeignKey(Semester, on_delete=models.SET_NULL,null=True)
    subject_id = models.ForeignKey(Subject, on_delete=models.SET_NULL,null=True)
    branch_id = models.ForeignKey(Branch, on_delete=models.SET_NULL,null=True,blank=True)
    proctor_id = models.ManyToManyField(Proctor,blank=True)
    college_id = models.ForeignKey(College, on_delete=models.CASCADE)
    is_calc = models.CharField(max_length=200,default='true')
    doc = models.DateTimeField(default=datetime.now(), blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.exam_name

    def save(self,*args,**kwargs):
        self.slug = slugify(self.exam_name+'-'+str(self.doc))
        super(Exam, self).save(*args,**kwargs)


class Questions(models.Model):
    question_id = models.AutoField(primary_key=True)
    questions = models.TextField()
    option_a = models.CharField(max_length=200)
    option_b = models.CharField(max_length=200)
    option_c = models.CharField(max_length=200)
    option_d = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    marks = models.CharField(max_length=200)
    section = models.CharField(max_length=100,choices=(("ALL","ALL"),("A", "A"), ("B", "B"),("C","C"),("D","D"),("E","E"),("F","F"),("G","G")))
    subject_id = models.ForeignKey(Subject, on_delete=models.SET_NULL,null=True)
    branch_id = models.ForeignKey(Branch, on_delete=models.SET_NULL,null=True)
    college_id = models.ForeignKey(College, on_delete=models.CASCADE)
    exam_id = models.ForeignKey(Exam, on_delete=models.SET_NULL,null=True)
    doc = models.DateTimeField(default=datetime.now(), blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.questions

    def save(self,*args,**kwargs):
        self.slug = slugify(str(self.answer)+'-'+str(self.doc))
        super(Questions, self).save(*args,**kwargs)

class Answer(models.Model):
    answer_id = models.AutoField(primary_key=True)
    answer = models.CharField(max_length=200)
    exam_id = models.ForeignKey(Exam, on_delete=models.SET_NULL, null=True)
    question_id = models.ForeignKey(Questions,  on_delete=models.SET_NULL,null=True,blank=True,related_name='question')
    student_id = models.ForeignKey(Students,  on_delete=models.SET_NULL,null=True,blank=True)
    doc = models.DateTimeField(default=datetime.now(), blank=True)
    slug = models.SlugField()

    def __str__(self):
        return self.answer+"|"+str(self.student_id.student_name)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.answer+'-'+str(self.doc))
        super(Answer, self).save(*args,**kwargs)
