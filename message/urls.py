from . import views
from django.urls import path,include
urlpatterns = [
    path('',views.login_view,name='login'),
    path('user',views.all_user,name='all_user'),
    path('chat/<id>',views.chat,name='chat'),
    path('logout',views.logout_view,name='logout'),
    path('com',views.com,name='com'),
    path('receive_data',views.receive_data,name='receive_data'),
    path('register',views.register,name='register')
]
