from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('student/', views.add_or_update_student, name='add_student'),
    path('delete/<int:id>/', views.delete_student, name='delete_student'),
    path('logout/', views.logout_view, name='logout'),
]
