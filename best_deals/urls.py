from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.index,name='Index'),
    url(r'^create/profile$',views.create_profile, name='create-profile'),
    url(r'^my-profile/(\d+)',views.my_profile, name='my-profile'),
    url(r'^businesses',views.businesses, name='businesses'),
    url(r'^new/business$',views.new_business, name='new-business'),
    url(r'^update/profile$',views.update_profile, name='update-profile'),
   
   
    

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)