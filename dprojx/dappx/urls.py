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
    url(r'^resercher_doctor/doctor/addProfile/$', views.addprofile, name='addprofile'),
    url(r'resercher_doctor/doctor/addProfile/add_to_db_Profile/', views.db_add_profile, name='db_add_profile'),

    url(r'resercher_doctor/doctor/addProfile/saved_ankets/$', views.saved_ankets, name='saved_ankets'),
    #Ccылка для удаления
    url(r'^resercher_doctor/doctor/addProfile/saved_ankets/delete$', views.deletes, name = 'del'),
    # (?# url(r'^resercher_doctor/doctor/addProfile/saved_ankets/exp$', views.exportFile, name = 'exp'),)
]