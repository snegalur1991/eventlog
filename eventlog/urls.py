"""eventlog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from eventlogapp import views
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

admin.site.site_header = "Sinch SDI DB Admin"
admin.site.site_title = "DB Admin"
admin.site.index_title = "Sinch"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('favicon-16x16.png', RedirectView.as_view(url=staticfiles_storage.url('/home/ubuntu/eventlogapp/eventlog/eventlogapp/static/img/favicon-16x16.png'))),
    path('', views.home, name="home"),
    path('add_event/', views.add_event, name="add_event"),
    path('list_event/', views.list_event, name='list_event'),
    path('add_server/', views.add_server, name='add_server'),
    path('list_server/', views.list_server, name='list_server'),
    path('add_site/', views.add_site, name='add_site'),
    path('list_site/', views.list_site, name='list_site'),
    path('accounts/', include("django.contrib.auth.urls")),
    path("password-reset", auth_views.PasswordResetView.as_view( template_name="registration/password_reset_form.html"), name="password_reset"),
    path("password-reset/done/", auth_views.PasswordResetDoneView.as_view( template_name="registration/password_reset_done.html"), name="password_reset_done"),
    path("password-reset-confirm/<uidb64>/<token>", auth_views.PasswordResetConfirmView.as_view( template_name="registration/password_reset_confirm.html"), name="password_reset_confirm"),
    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view( template_name="registration/password_reset_complete.html"), name="password_reset_complete"),
]