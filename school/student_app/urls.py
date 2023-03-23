from django.urls import path
from student_app import views

app_name = "user_app"

urlpatterns = [
    
    path('', views.demo, name='demo'),
    path('student_home/', views.user_home, name='student_home'),
    
    path('login/', views.login_student, name='login_student'),
    path('logout/', views.logout_student, name='logout_student'),

    path('demo_submit/', views.images_submit, name='images_submit'),

    path('add_student/', views.add_student, name='add_student'),



]