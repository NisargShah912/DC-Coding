from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('regan', views.qr_gen, name='qrgen'),
    path('login', views.login, name="login"),
    path('checklogin', views.checklogin, name="checklogin"),
    path('adduser', views.adduser, name="user"),
    path('signup', views.signup, name="signup"),
    path('contact', views.contact, name="contact"),
    path('graph', views.graph, name="graph"),
    # path('search', views.qrdis, name='qrdis'),
]