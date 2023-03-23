from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate, logout
# from django.contrib.auth.models import User

from .models import AuthUser

from .forms import DemoForm, UserloginForm


# Create your views here.

def demo(request):
    return redirect("student_app:login_student")

def user_home(request):
    return render(request, "student_home.html")

def login_student(request):

    if request.method == "POST":

        email = request.POST.get("email")
        password = request.POST.get("password")

        print("u>>>>", email)
        print("p>>>>", password)

        user = authenticate(email=email, password=password)

        print("user>>", user)

        if user is not None and user.is_admin:
            login(request, user)
            return redirect('teacher_app:teacher_home') #Go to admin home
        elif user is not None and user.is_user:
            login(request, user)
            return redirect('student_app:student_home') #Go to user home
        elif user and user.is_superuser:
            return render(request, 'superuser.html') # go to Superuser
            # login(request, user)
            # type_obj = AuthUser.objects.get(email=user)
            # if user.is_authenticated and type_obj.is_user:
            #     return redirect('user_app:user_home') #Go to user home
            # elif user.is_authenticated and type_obj.is_admin:
            #     return redirect('admin_app:admin_home') #Go to admin home
            # elif user.is_authenticated and type_obj.is_superuser:
            #     return render(request, 'superuser.html') # go to Superuser
                    
        #     login(request, user)
        #     return redirect("user_app:user_home")
        # else:
        #     # print("R>>>>>")
        #     return redirect("user_app:login_user")   
    else:   
        return render (request, "login.html")
      
        
        



def logout_student(request):
    logout(request)
    return redirect('student_app:login_student')
    # return render(request, "login_user.html")


def add_student(request):

    if request.method == "POST":
        form_v = UserloginForm(request.POST, request.FILES)
        if form_v.is_valid():
            asd = form_v.save()
            asd.is_user = True
            asd.set_password(asd.password)
            asd.save()
            return redirect("student_app:add_student")
        else:
            print(form_v.errors)

    else: 
        form_v = UserloginForm()
        
    return render (request, "add_student.html", {'form': form_v})

def images_submit(request):
    if request.method == "POST":
        print(request.FILES)
        form = DemoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        else:
            print(form.errors)
    else:
        form = DemoForm()
    return render(request, "demo_submit.html", {"form":form})