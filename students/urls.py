from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('classe/<str:classe>/', views.students_by_class, name='students_by_class'),
    path('<int:id>/', views.student_detail, name='student_detail'),
]