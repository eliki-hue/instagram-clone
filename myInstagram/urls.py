from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('first_page',views.first_page, name='login_page'),
    path('', views.home, name ='home'),
    path('my_profile', views.profile_display, name='profile_display')
    # path('accounts/register/', views.register, name='register'),
    

]
if settings.DEBUG:

    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)