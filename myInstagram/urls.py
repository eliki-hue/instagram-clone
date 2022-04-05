from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    path('first_page',views.first_page, name='login_page'),
    path('', views.home, name ='home'),
    path('my_profile', views.profile_display, name='profile_display'),
    path('update_profile', views.profile_update, name='profile_update'),
    path('my_post', views.add_post, name='my_post'),
    path('add_comment', views.add_comment, name='add_comment'),
    
    # path('accounts/register/', views.register, name='register'),
    

]
if settings.DEBUG:

    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)