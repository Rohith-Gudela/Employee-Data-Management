
from django.urls import path
from .import views

urlpatterns = [
    path('', views.home,name='home'),
    path('register',views.register,name='register'),
    path('registered',views.registered,name='registered'),
    path('details', views.details, name='details'),
    path('more_details/<int:id>', views.more_details, name='more_details'),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('updated/<int:id>', views.updated, name='updated'),
]
