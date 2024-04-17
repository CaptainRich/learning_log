""" Define the URL patterns for 'accounts'. """

from django.urls import path, include 
from . import views


app_name = 'accounts'

urlpatterns = [
    # Include default auth urls.  This '' pattern matches the base URL,
    # which will be the default 'login' view.
    path( '', include( 'django.contrib.auth.urls' )),

    # The path pattern for the user registration page.
    # http://localhost:8000/accounts/register/
    path( 'register/', views.register, name='register' ),

]