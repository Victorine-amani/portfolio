from . import views
from django.urls import path, include

urlpatterns = [
   path('',views.home,name='home'),
   path('contact',views.contact,name='contact'),
   path('about',views.about,name='about'),
   path('projects', views.projects,name='projects'),
   path("<int:pk>", views.project_detail, name="project_detail")
   
]