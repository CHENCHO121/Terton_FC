from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from .models import Contact, Student_Financial_Crisis, Gallery_Old_Age_Home, Gallery_Orphange, Gallery_player, \
    Old_Age_Home, Orphanage, Event, Course, Self_Training_Form, ScholarshipForm, Academy_Details


def index(request):
    event = Event.objects.all()
    gal = Gallery_player.objects.all()
    context = {'event': event, 'gal': gal}
    return render(request, 'index.html', context)


def academy(request):
    course = Course.objects.all()
    academy_detail=Academy_Details.objects.all()
    context = {"course": course,'academy':academy_detail}
    return render(request, 'academy.html', context)


def aboutUs(request):
    event = Event.objects.all()
    context = {'event': event}
    return render(request, 'about.html', context)


def contact(request):
    error = ""
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        try:
            Contact.objects.create(name=name, email=email, subject=subject, message=message)
            error = "no"
        except:
            error = "yes"

    context = {"error": error}
    return render(request, 'contact.html', context)


def charity(request):
    data = Old_Age_Home.objects.all()
    context = {'old': data}
    return render(request, 'old_age_home.html', context)


def orphange(request):
    data = Orphanage.objects.all()
    context = {'orphan': data}
    return render(request, 'orphange.html', context)


def financialcrisis(request):
    error = ""
    if request.method == 'POST':
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        email = request.POST['email']
        phone = request.POST['phone']
        age = request.POST['age']
        school_year = request.POST['education']
        address = request.POST['address']
        reason_for_applying = request.POST['reason']
        age_range = request.POST['age_range']
        school_type = request.POST['school_type']
        support_for = request.POST['support_for']
        try:
            Student_Financial_Crisis.objects.create(first_name=first_name, last_name=last_name, email=email,
                                                    phone=phone, age=age,
                                                    school_year=school_year,
                                                    address=address, reason_for_applying=reason_for_applying,
                                                    age_range=age_range,
                                                    school_type=school_type,
                                                    support_for=support_for)
            error = "no"
        except:
            error = "yes"

    context = {"error": error}
    return render(request, 'financial_crisis.html', context)


def galleryshow(request):
    pic = Gallery_Orphange.objects.all()
    pic1 = Gallery_Old_Age_Home.objects.all()
    pic3 = Gallery_player.objects.all()
    context = {
        "orphane": pic,
        'oldAge': pic1,
        'player': pic3
    }
    return render(request, 'gallery.html', context)


def admin_login(request):
    error = ""
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['password']
        user = authenticate(username=name, password=password)
        try:
            if user.is_staff:
                login(request, user)
                error = "no"
                return redirect('/admin_home')
            else:
                error = "yes"
        except:
            error = "yes"
    context = {"error": error}
    return render(request, 'admin_login.html', context)


def logout_admin(request):
    logout(request)
    return redirect('/admin_login')


def gallery(request):
    return render(request, 'upload_gallery.html')


def upload_gallery_orphane(request):
    error = ""
    if request.method == 'POST':
        image = request.FILES['image']
        try:
            Gallery_Orphange.objects.create(image=image)
            error = "no"
        except:
            error = "yes"

    context = {"error": error}
    return render(request, 'upload_gallery.html', context)


def upload_gallery_old_age(request):
    error = ""
    if request.method == 'POST':
        image = request.FILES['image']
        try:
            Gallery_Old_Age_Home.objects.create(image=image)
            error = "no"
        except:
            error = "yes"

    context = {"error": error}
    return render(request, 'upload_gallery.html', context)


def upload_gallery_football_player(request):
    error = ""
    if request.method == 'POST':
        image = request.FILES['image']
        try:
            Gallery_player.objects.create(image=image)
            error = "no"
        except:
            error = "yes"

    context = {"error": error}
    return render(request, 'upload_gallery.html', context)


def admin_dashboard(request):
    enquiry = Contact.objects.count()
    orphan = Orphanage.objects.count()
    course = Course.objects.count()
    event = Event.objects.count()
    scholarship = ScholarshipForm.objects.count()
    sfc = Student_Financial_Crisis.objects.count()
    oldAge = Old_Age_Home.objects.count()
    selfPaid = Self_Training_Form.objects.count()
    context = {'enq': enquiry, 'sfc': sfc, 'orphan': orphan, 'old': oldAge, 'event': event, 'scholarship': scholarship,
               'selfpaid': selfPaid, 'course': course}
    return render(request, 'admin_home.html', context)


def view_enquiry(request):
    data = Contact.objects.all()
    context = {'enq': data}
    return render(request, 'view_enquiry.html', context)


def delete_enquiry(request, pk):
    item = Contact.objects.get(pk=pk)
    item.delete()
    return redirect('/view_enquiry')


def view_financial_crisis(request):
    data = Student_Financial_Crisis.objects.all()
    context = {'sfc': data}
    return render(request, 'view_financial_crisis.html', context)


def delete_financial_crisis(request, pk):
    item = Student_Financial_Crisis.objects.get(pk=pk)
    item.delete()
    return redirect('/view_financial_crisis')


def add_Old_Age(request):
    error = ""
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']
        age = request.POST['age']
        info = request.POST['info']
        try:
            Old_Age_Home.objects.create(name=name, image=image, age=age, info=info)
            error = "no"
        except:
            error = "yes"

    context = {"error": error}
    return render(request, 'add_old_age.html', context)


def add_orphanage(request):
    error = ""
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']
        age = request.POST['age']
        info = request.POST['info']
        try:
            Orphanage.objects.create(name=name, image=image, age=age, info=info)
            error = "no"
        except:
            error = "yes"

    context = {"error": error}
    return render(request, 'add_orphanage.html', context)


def view_orphanage(request):
    data = Orphanage.objects.all()
    context = {'orphan': data}
    return render(request, 'view_orphanage.html', context)


def delete_orphanage(request, pk):
    item = Orphanage.objects.get(pk=pk)
    item.delete()
    return redirect('/view_orphanage')


def view_old_age(request):
    data = Old_Age_Home.objects.all()
    context = {'oldAge': data}
    return render(request, 'view_old_age.html', context)


def delete_old_age(request, pk):
    item = Old_Age_Home.objects.get(pk=pk)
    item.delete()
    return redirect('/view_old_age')


def edit_orphanage(request, pk):
    data = Orphanage.objects.get(pk=pk)
    error = ""
    try:
        if request.method == "POST":
            name = request.POST["name"]
            image = request.FILES["image"]
            age = request.POST["age"]
            info = request.POST["info"]

            data.name = name
            data.image = image
            data.age = age
            data.info = info

            data.save()
            error = "no"
            return redirect('/view_orphanage')
    except:
        error = "yes"

    context = {
        "data": data,
        "error": error
    }
    return render(request, 'update_orphanage.html', context)


def edit_old_age(request, pk):
    data = Old_Age_Home.objects.get(pk=pk)
    error = ""
    try:
        if request.method == "POST":
            name = request.POST["name"]
            image = request.FILES["image"]
            age = request.POST["age"]
            info = request.POST["info"]

            data.name = name
            data.image = image
            data.age = age
            data.info = info

            data.save()
            error = "no"
            return redirect('/view_old_age')
    except:
        error = "yes"

    context = {
        "data": data,
        "error": error
    }
    return render(request, 'update_old_age.html', context)


def add_event(request):
    error = ""
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']
        date = request.POST['date']
        description = request.POST['description']
        try:
            Event.objects.create(name=name, image=image, date=date, description=description)
            error = "no"
        except:
            error = "yes"

    context = {"error": error}
    return render(request, 'add_event.html', context)


def view_event(request):
    data = Event.objects.all()
    context = {'event': data}
    return render(request, 'view_event.html', context)


def delete_event(request, pk):
    item = Event.objects.get(pk=pk)
    item.delete()
    return redirect('/view_event')


def edit_event(request, pk):
    data = Event.objects.get(pk=pk)
    error = ""
    try:
        if request.method == "POST":
            name = request.POST["name"]
            image = request.FILES["image"]
            date = request.POST["date"]
            description = request.POST["description"]

            data.name = name
            data.image = image
            data.date = date
            data.description = description

            data.save()
            error = "no"
            return redirect('/view_event')
    except:
        error = "yes"

    context = {
        "data": data,
        "error": error
    }
    return render(request, 'update_event.html', context)


def add_course(request):
    error = ""
    if request.method == 'POST':
        name = request.POST['name']
        image = request.FILES['image']
        try:
            Course.objects.create(name=name, image=image)
            error = "no"
        except:
            error = "yes"

    context = {"error": error}
    return render(request, 'add_course.html', context)


def view_course(request):
    data = Course.objects.all()
    context = {'course': data}
    return render(request, 'view_course.html', context)


def delete_course(request, pk):
    item = Course.objects.get(pk=pk)
    item.delete()
    return redirect('/view_course')


def edit_course(request, pk):
    data = Course.objects.get(pk=pk)
    error = ""
    try:
        if request.method == "POST":
            name = request.POST["name"]
            image = request.FILES["image"]
            data.name = name
            data.image = image

            data.save()
            error = "no"
            return redirect('/view_course')
    except:
        error = "yes"

    context = {
        "data": data,
        "error": error
    }
    return render(request, 'update_course.html', context)


def view_gallery(request):
    data = Gallery_Old_Age_Home.objects.all()
    data1 = Gallery_Orphange.objects.all()
    data2 = Gallery_player.objects.all()
    context = {'old': data, 'orphan': data1, 'student': data2}
    return render(request, 'view_gallery.html', context)


def delete_gallery(request, pk):
    item = Gallery_Old_Age_Home.objects.get(pk=pk)
    item.delete()
    return redirect('/view_gallery')


def delete_gallery1(request, pk):
    item1 = Gallery_Orphange.objects.get(pk=pk)
    item1.delete()
    return redirect('/view_gallery')


def delete_gallery2(request, pk):
    item1 = Gallery_player.objects.get(pk=pk)
    item1.delete()
    return redirect('/view_gallery')


def scholarship(request):
    error = ""
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        father = request.POST['father']
        mother = request.POST['mother']
        age = request.POST['age']
        phone = request.POST['phone']
        email = request.POST['email']
        qualification = request.POST['qualification']
        address = request.POST['address']
        try:
            ScholarshipForm.objects.create(fname=fname, lname=lname, father=father, mother=mother, age=age, phone=phone,
                                           email=email, qualification=qualification, address=address)
            error = "no"
        except:
            error = "yes"

    context = {"error1": error}
    return render(request, 'academy.html', context)


def view_scholarship(request):
    data = ScholarshipForm.objects.all()
    context = {"scholarship": data}
    return render(request, 'view_scholarship.html', context)


def delete_scholarship(request, pk):
    item = ScholarshipForm.objects.get(pk=pk)
    item.delete()
    return redirect('/view_scholarship')


def view_SelfPaidTraining(request):
    data = Self_Training_Form.objects.all()
    context = {"selfPaid": data}
    return render(request, 'view_SelfPaid_Training.html', context)


def delete_SelfPaid(request, pk):
    item = Self_Training_Form.objects.get(pk=pk)
    item.delete()
    return redirect('/view_SelfPaidTraining')


def self_Training(request):
    error = ""
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        phone = request.POST['phone']
        email = request.POST['email']
        address = request.POST['address']
        try:
            Self_Training_Form.objects.create(fname=fname, lname=lname, phone=phone, email=email, address=address)
            error = "no"
        except:
            error = "yes"

    context = {"error2": error}
    return render(request, 'academy.html', context)


def add_academy_detail(request):
    error = ""
    if request.method == 'POST':
        full_scholarship = request.POST['full_scholarship']
        half_scholarship = request.POST['half_scholarship']
        self_paid = request.POST['self_paid']
        training = request.POST['training']
        football = request.POST['football']

        try:
            Academy_Details.objects.create(full_scholarship=full_scholarship, half_scholarship=half_scholarship,
                                           self_paid=self_paid, training=training, football=football)
            error = "no"
        except:
            error = "yes"

    context = {"error": error}
    return render(request,'add_academy_detail.html',context)

def view_academy_detail(request):
    data = Academy_Details.objects.all()
    context = {'academy': data}
    return render(request, 'view_academy.html', context)


def delete_academy_detail(request, pk):
    item = Academy_Details.objects.get(pk=pk)
    item.delete()
    return redirect('/view_academy_detail')


def edit_course(request, pk):
    data = Course.objects.get(pk=pk)
    error = ""
    try:
        if request.method == "POST":
            name = request.POST["name"]
            image = request.FILES["image"]
            data.name = name
            data.image = image

            data.save()
            error = "no"
            return redirect('/view_course')
    except:
        error = "yes"

    context = {
        "data": data,
        "error": error
    }
    return render(request, 'update_course.html', context)

