from django.shortcuts import render
from django.http import HttpResponse
from .models import Department,medical,Doctor
from .forms import BookingForm



def index(request):

    return render(request,"index.html")

def about(request):

    return render(request,"about.html")

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirm.html')
        
    form = BookingForm()
    dict_form={
        'xyz' : form
    }

    return render(request, "booking.html",dict_form)

def contact(request):
    return render(request,"contact.html")

def department(request):
    x={
        'dept': Department.objects.all()
    }
    return render(request,"department.html",x)

def doctors(request):
    z={
        'doc': Doctor.objects.all()
    }
    return render(request,"doctors.html",z)

def medicals(request):
    y={
        'med': medical.objects.all()
    }
    return render(request,"medical.html",y)