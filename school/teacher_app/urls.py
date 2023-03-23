from unicodedata import name
from django.urls import path
from teacher_app import views

app_name = "teacher_app"

urlpatterns = [
    
    path('', views.demo, name='demo'),
    path('teacher_home/', views.teacher_home, name='teacher_home'),

    path('teacher_signup/', views.teacher_signup, name='teacher_signup'),
    path('teacher_logout/', views.admin_logout, name='teacher_logout'),

    path('user_list/', views.UserList.as_view(), name="student_list"),
    path('user_list/<int:pk>', views.UserDetails.as_view(), name="student_details")

    


]