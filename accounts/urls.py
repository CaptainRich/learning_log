""" Define the URL patterns for 'accounts'. """

from django.urls import path, include 

app_name = 'accounts'

urlpatterns = [
    # Include default auth urls.  This '' pattern matches the base URL,
    # which will be the default 'login' view.
    path( '', include( 'django.contrib.auth.urls' )),
]