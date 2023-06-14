from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('save_resume', views.save_resume, name='save_resume'),
    path('resumes_pool', views.show_All_Resumes, name='resumes_pool'),
    path('<int:id>/', views.resume_layout, name='resume_layout'),
    path('<int:id>/edit/', views.resume_edit, name='resume_edit'),
    path('<int:id>/delete/', views.resume_delete, name='resume_delete'),
]
