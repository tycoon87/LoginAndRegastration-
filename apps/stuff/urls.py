from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^$', views.index),
url(r'^index$', views.index),
url(r'^createUser$', views.createUser),
url(r'^Add$', views.Add),
url(r'^show/(?P<User_id>\d+)$' , views.show),
url(r'^edit/(?P<User_id>\d+)$' , views.edit),
url(r'^openEdit/(?P<User_id>\d+)$' , views.openEdit),
url(r'^delete/(?P<User_id>\d+)$' , views.delete),
url(r'^Login$' , views.Login),
url(r'^Logout$' , views.Logout),
]
