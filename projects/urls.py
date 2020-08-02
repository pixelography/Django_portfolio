from django.urls import path
from . import views

urlpatterns = [
    path('', views.Projectindex, name='project_index'),
    path('<int:pk>/', views.Projectdetail, name='project_detail'),
]
