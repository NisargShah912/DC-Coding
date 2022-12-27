from django.contrib import admin
from django.urls import path, include,re_path
from django.conf import settings
from django.conf.urls.static import static
from dcan import views

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('regan', views.qr_gen, name='qrgen'),
    path('login', views.login, name="login"),
    path('checklogin', views.checklogin, name="checklogin"),
    path('adduser', views.adduser, name="user"),
    path('signup', views.signup, name="signup"),
    path('contact', views.contact, name="contact"),
    path('graph', views.graph, name="graph"),
    
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)