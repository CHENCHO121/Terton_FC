from django.db import models

class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    subject=models.CharField(max_length=50)
    message=models.TextField(max_length=500)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Contact'

class Gallery_Orphange(models.Model):
    image=models.ImageField(upload_to='media/upload')
    class Meta:
        verbose_name = 'Gallery Orphange'

class Gallery_Old_Age_Home(models.Model):
    image=models.ImageField(upload_to='media/upload')
    class Meta:
        verbose_name = 'Gallery Old Age Home'


class Gallery_player(models.Model):
    image=models.ImageField(upload_to='media/upload')
    class Meta:
        verbose_name = 'Gallery Player'

class Orphanage(models.Model):
    name=models.CharField(max_length=50)
    age = models.IntegerField()
    info=models.CharField(max_length=150)
    image = models.ImageField(upload_to='media/upload')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Orphanage'


class Student(models.Model):
    name=models.CharField(max_length=50)
    age = models.IntegerField()
    info=models.CharField(max_length=150)
    image = models.ImageField(upload_to='media/upload')
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Orphanage'
class Old_Age_Home(models.Model):
    name = models.CharField(max_length=50)
    age=models.IntegerField()
    info = models.CharField(max_length=150)
    image = models.ImageField(upload_to='media/upload')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Old Age Home'

class Student_Financial_Crisis(models.Model):
    first_name=models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    email=models.EmailField(max_length=60)
    phone=models.IntegerField()
    age=models.IntegerField()
    school_year=models.CharField(max_length=20)
    address=models.CharField(max_length=100)
    reason_for_applying=models.CharField(max_length=30)
    age_range=models.CharField(max_length=20)
    school_type=models.CharField(max_length=20)
    support_for=models.CharField(max_length=30)
    class Meta:
        verbose_name = 'Student Financial crisis Registration'
    def __str__(self):
        return self.first_name+" "+self.last_name


class Event(models.Model):
    name=models.CharField(max_length=50)
    date=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='media/upload')
    description=models.CharField(max_length=200)
    def __str__(self):
        return self.name


class Course(models.Model):
    name=models.CharField(max_length=30)
    image = models.ImageField(upload_to='media/upload')
    def __str__(self):
        return self.name

class ScholarshipForm(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    father=models.CharField(max_length=30,null=True)
    mother=models.CharField(max_length=30,null=True)
    age=models.IntegerField()
    phone=models.IntegerField()
    email=models.EmailField(max_length=100)
    qualification=models.CharField(max_length=40)
    address=models.TextField(max_length=250)


class Self_Training_Form(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    phone=models.IntegerField()
    email=models.EmailField(max_length=100)
    address=models.TextField(max_length=250)

class Academy_Details(models.Model):
    full_scholarship=models.TextField(max_length=500,null=True)
    half_scholarship = models.TextField(max_length=500, null=True)
    self_paid = models.TextField(max_length=500, null=True)
    training= models.TextField(max_length=500, null=True)
    football = models.TextField(max_length=500, null=True)



















