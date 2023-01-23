from django.shortcuts import render,redirect
from .models import Employee
from .forms import employee_create
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'home.html')

def register(request):   
    return render(request,'register.html')

def registered(request):
    name=request.POST['name']
    identity_number=request.POST['identity_number']
    department=request.POST['department']
    phone_number=request.POST['phone_number']
    address=request.POST['address']
    registered=Employee()
    if registered.identity_number !=identity_number:
        registered.name= name
        registered.identity_number= identity_number
        registered.department= department
        registered.phone_number= phone_number
        registered.address= address
        registered.save()
    else:
        messages.info(request, "This student id already exists")
        return redirect('register')


    return render(request,'registered.html')


def details(request):
    employees=Employee.objects.all().values().order_by('identity_number')
    return render(request, 'details.html',{'employee':employees})

def more_details(request,id):
    employees=Employee.objects.get(id=id)
    return render(request,'more_details.html',{'employee':employees})

def delete(request,id):
    delete_employee=Employee.objects.get(id=id)
    delete_employee.delete()
    return render(request,'delete.html')

def update(request,id):
    update=Employee.objects.get(id=id)   
    return render(request,'update.html',{ 'update':update})

def updated(request,id):
    name=request.POST['name']
    identity_number=request.POST['identity_number']
    department=request.POST['department']
    phone_number=request.POST['phone_number']
    address=request.POST['address']
    update_details=Employee.objects.get(id=id)
    update_details.name= name
    update_details.identity_number= identity_number
    update_details.department= department
    update_details.phone_number= phone_number
    update_details.address= address
    update_details.save()
    return render(request,'updated.html')


