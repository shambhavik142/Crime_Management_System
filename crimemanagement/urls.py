

from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^$',views.homepage,name='homepage'),
    url(r'^police/$',views.police,name='police'),
    url(r'^user/$',views.user,name='user'),
    url(r'^complaint1/$',views.complaint1,name='complaint1'),
    url(r'^complaint_info/$',views.complaint_info,name='complaint_info'),
    url(r'^complaint_status/$',views.complaint_status,name='complaint_status'),
    url(r'^view_status/$',views.view_status,name='view_status'),
    url(r'^helplines/$',views.helplines, name='helplines'),
    url(r'^contacts/$',views.contacts,name='contacts'),
    url(r'^enter/$',views.enter,name='enter'),
    url(r'^entry_details/$',views.entry_details, name='entry_details'),
    url(r'^view_details/$',views.view_details, name='view_details'),
    url(r'^records/$',views.records,name='records'),
    url(r'^update/$',views.update,name='update'),
    url(r'^update_status/$', views.update_status, name='update_status'),
    url(r'^view/$',views.view,name='view'),
       
]
