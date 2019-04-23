from django.urls import path, re_path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    re_path(r'^signup/$', views.signUp, name='signup'),
    re_path(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    re_path(r'^login/$',
            auth_views.LoginView.as_view(template_name='login.html'), name='login'),
]
