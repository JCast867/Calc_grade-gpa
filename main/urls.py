from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('', views.home, name='home'),
     path('add_class/', views.add_class, name='add_class'),
    path('gpa/', views.view_gpa, name='view_gpa'),
    path('grade_calculator/', views.grade_calculator, name='grade_calculator'),
    path('delete_class/<int:class_id>/', views.delete_class, name='delete_class'),
]
