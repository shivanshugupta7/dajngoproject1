from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import CreateView
from .models import Employee
from .forms import EmployeeForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import EmployeeSerializer

def welcome(request):
    return render(request, "welcome.html")


def load_form(request):
    form = EmployeeForm
    return render(request, "index.html", {'form': form})

class EmployeeList(APIView):
    def get(self,request):
        employee1=Employee.objects.all()
        serializer=EmployeeSerializer(employee1, many=True)
        return Response(serializer.data)

    def post(selfself):
        pass


def add(request):
    form = EmployeeForm(request.POST or None, request.FILES or None)

    form.save()
    if request.method == 'POST':
        message = "Thanks for signing "+ "\n" + "your entered name is " + request.POST['ename'] + "\nyour entered id is "+ request.POST['eid']
        email = request.POST['eemail']
        print("email= "+email)
        print("message"+message)
        send_mail('Details',
                  message,
                  settings.EMAIL_HOST_USER,
                  [email],
                  fail_silently=False
                  )
    return redirect('/show')

def show(request):
    employee = Employee.objects.all
    return render(request, 'show.html',{'employee':employee})

def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request,'edit.html', {'employee':employee})

def update(request, id):
    employee = Employee.objects.get(id=id)
    # instance = get_object_or_404(Employee, id=id)
    # form = EmployeeForm(request.POST or None, request.FILES or None, instance=instance)
    file_data = request.FILES or None
    form = EmployeeForm(request.POST,file_data, instance=employee)

    form.save()
    return redirect('/show')

def delete(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('/show')

def search(request):
    given_name = request.POST['name']
    employee = Employee.objects.filter(ename__istartswith=given_name)
    return render(request,'show.html',{'employee':employee})


class EmployeeCreateView(CreateView):
    model = Employee
    fields = ('ID', 'NAME', 'EMAIL', 'CONTACT','profile_image')


