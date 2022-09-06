from urllib.request import Request
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Student_list
from django.contrib import messages

# Create your views here.


def home(request):
    temp = 'home.html'
    return render(request , temp)
    
def forms(request , id=0):
    if request.method == 'POST':
        if id==0:
            f_name = request.POST.get('f_name')
            l_name = request.POST.get('l_name')
            email = request.POST.get('email')
            address = request.POST.get('address')
            content = Student_list(F_Name=f_name , L_Name = l_name , Email = email , Address = address)
            content.save()
            messages.success(request, "Student Detail Successfully Added")
            return redirect('/home')
        else:
            student = Student_list.objects.get(pk=id)
            student.F_Name = request.POST.get('f_name')
            student.L_Name = request.POST.get('l_name')
            student.Email = request.POST.get('email')
            student.Address = request.POST.get('address')
            # content = Student_list(F_Name=f_name , L_Name = l_name , Email = email , Address = address)
            # content.save()
            student.save()
            messages.success(request, "Student Detail Successfully Updated")
            return redirect('/student_list')
    else:
        if id==0:
            return render(request , 'form.html')
        else:
            student = Student_list.objects.get(pk=id)
            return render(request , 'form.html' , {'std':student})

def list(request):
    l = {
        'list' :  Student_list.objects.all()
    }
    return render(request , 'list.html' , l )

def Delete(request , id):
    student = Student_list.objects.get(pk=id)
    student.delete()
    return redirect('/student_list')