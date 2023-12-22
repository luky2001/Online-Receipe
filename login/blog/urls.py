from django.urls import path
from  blog import views


urlpatterns = [
    path("", views.home, name="home"),
    path("receipe/",views.receipe,name='receipe'),
    path("delete/<id>/", views.delete,name="delete"),
    path("update/<id>/",views.update , name="update"),
    path("login/",views.login_page,name="login"),
    path("register/",views.register,name="register"),
    path("logout/",views.logout_page,name="logout"),
    #path("index/",views.index,name="index"),
    
   
]