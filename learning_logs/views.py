from django.shortcuts import render
from .models import Topic

# Create your views here.

def index( request ):
    """ The home page for the Learning Log. """
    # The 2nd argument is the template to build the web page.
    return render( request, 'learning_logs/index.html' )


def topics( request ):
    """ Show all the defined topics. """
    topics = Topic.objects.order_by( 'date_added' )  # Query the database
    context = { 'topics': topics }                   # Setup the dictionary with the data
    return render( request, 'learning_logs/topics.html', context )


