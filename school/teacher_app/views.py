from pyexpat import model
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout

from student_app.forms import UserloginForm
from django.views.generic import ListView, DetailView
from student_app.models import AuthUser
# from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin

# Create your views here.


def demo(request):
    return redirect('teacher_app:teacher_signup')

def teacher_home(request):
    return render(request, "teacher_home.html")

class UserList(ListView):
    model = AuthUser
    template_name = "teacher_app/student_list.html"
    context_object_name = "student_list"    

class UserDetails(DetailView):
    model = AuthUser
    template_name = "teacher_app/student_details.html"
    context_object_name = "user"


# def details(request,id):
#     user = AuthUser.objects.get(id=id)
#     return render(request,'show.html', {'user':user})


def teacher_signup(request):
    if request.method == "POST":
        form_v = UserloginForm(request.POST)
        if form_v.is_valid():
            asd = form_v.save()
            asd.is_admin = True
            asd.set_password(asd.password)
            asd.save()
            return redirect("teacher_app:teacher_signup")
        else:
            print(form_v.errors)
    else: 
        form_v = UserloginForm()
    return render (request, "teacher_signup.html", {'form_v': form_v})


def admin_logout(request):
    logout(request)
    return redirect('student_app:login_student')
