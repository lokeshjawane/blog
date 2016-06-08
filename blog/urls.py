from django.conf.urls import url
from . import views

urlpatterns = (
    url(r'^$', views.newblog, name='blog'),
    url(r'^saveblog/$', views.saveblog, name='saveblog'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^lo/$', views.logout, name='logout'),
    url(r'^user/(?P<use_id>\d+)/edit$', views.user_edit, name='user_edit'),
    # url(r'^list/$', views.show, name='list'),
)
