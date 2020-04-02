"""events_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from registration.backends.simple.views import RegistrationView
from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from myevents import views

class ResetView(auth_views.LoginView):
    @property
    def success_url(self):
        return reverse('auth_login')

class ActivationCompleteView(auth_views.LoginView):
    @property
    def success_url(self):
        return reverse('auth_login')

urlpatterns = [ 
	path('', views.index, name='index'),
	path('myevents/', include('myevents.urls')),
    path('accounts/logout/<int:pk>/', RegistrationView.as_view(), name='registration_logout'),
    path('accounts/password/reset/complete/', ResetView.as_view(), name='reset_password'),
    path('accounts/activate/complete/', ActivationCompleteView.as_view(), name='activation_complete'),
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
    path('accounts/profile/', views.profile, name='profile'),
]
