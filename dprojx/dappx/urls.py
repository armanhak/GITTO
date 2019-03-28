from django.conf.urls import url
from . import views
# SET THE NAMESPACE!
app_name = 'dappx'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^resercher_doctor/$',views.resercher_doctor,name='resercher_doctor'),
    url(r'^resercher_doctor/doctor/$',views.doctor,name='doctor'),
    url(r'^resercher_doctor/resercher/$',views.resercher,name='resercher'),
    url(r'resercher_doctor/doctor/addProfile/$', views.addprofile, name='addprofile'),
]