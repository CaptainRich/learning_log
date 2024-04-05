from django.shortcuts import render

# Create your views here.

def index( request ):
    """ The home page for the Learning Log. """
    # The 2nd argument is the template to build the web page.
    return render( request, 'learning_logs/index.html' )

