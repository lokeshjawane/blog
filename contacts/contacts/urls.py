from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<contact_id>\d+)/$', views.detail, name='detail'),
    url(r'^new/$', views.new, name='new'),
    url(r'^addcon/$', views.addcon, name='addcon'),
    url(r'^(?P<cont_id>\d+)/edit/$', views.editcon, name='edit'),
    url(r'^updatecon/$', views.updatecon, name='updatecon'),
    url(r'^(?P<cont_id>\d+)/delete/$', views.deletecon, name='delete'),
    url(r'^(?P<cont_id>\d+)/comment/$', views.addcomm, name='addcomm'),
    url(r'^login/$', views.login_view, name='login_view'),
    url(r'^logout/$', views.logout_view, name='logout_view'),
	url(r'^register/$', views.register, name='register'),

]