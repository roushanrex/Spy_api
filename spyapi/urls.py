from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Admin App
    path('admin/', admin.site.urls),
    path('list_user/', views.List_user.as_view()),
    path('create_user/', views.Create_user.as_view()),
    path('get_All_device/', views.Get_All_device.as_view()),

    # Victime App

    path('phonedata_created/', views.Phone_data_created.as_view()),
    path('phoneUpdate/<int:pk>/', views.Phone_data_Update.as_view()),

]