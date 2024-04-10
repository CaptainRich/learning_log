from django.shortcuts import render, redirect
from .models import Topic
from .forms import TopicForm

# Create your views here.

def index( request ):
    """ The home page for the Learning Log. """
    # The 2nd argument is the template to build the web page.
    return render( request, 'learning_logs/index.html' )


def topics( request ):
    """ Show all the defined topics. """
    topics  = Topic.objects.order_by( 'date_added' )  # Query the database
    context = { 'topics': topics }                    # Setup the dictionary with the data
    return render( request, 'learning_logs/topics.html', context )


def topic( request, topic_id ):
    """ Show a single topic and all its entries. """
    topic   = Topic.objects.get( id=topic_id )
    entries = topic.entry_set.order_by( '-date_added' )    #  Sort by 'reverse' date
    context = {'topic': topic, 'entries': entries }
    return render( request, 'learning_logs/topic.html', context )


def new_topic( request ):
    """ Allow a user to add a new topic. """
    if request.method != 'POST':       # Request must be 'GET"
        # No data submitted; create a blank form.
        form = TopicForm()

    else:
        # The user posted data, process it.
        form = TopicForm( data=request.POST )
        if form.is_valid():
            form.save()
            return redirect( 'learning_logs:topics' )
        
    # Display a blank or invalid form, via the 'context' dictionary.
    context = { 'form': form }
    return render( request, 'learning_logs/new_topic.html', context )










      


