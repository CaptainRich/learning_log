""" Define the URL patterns for learning_logs. """

from django.urls import path
from .import views              # Import 'views.py' from the same directory as this file.

app_name = 'learning_logs'

urlpatterns = [
    # The home page. A list of pages that can be requested from this app.  The '' empty
    # string matches the base URL.  The 2nd argument defines which function to call in
    # views.py.  The 3rd argument defines a name for this pattern for later reference. 
    path( '', views.index, name='index' ),

    # The URL pattern for the 'Topics' page.
    path( 'topics', views.topics, name='topics' ),

    # The detail page (URL) for a single topic.
    path( 'topics/<int:topic_id>/', views.topic, name='topic' ),

    # The page to allow users to create a new topic.
    path( 'new_topic/', views.new_topic, name='new_topic' ),

    # The page for adding a new entry to a topic. topic_id matches the Topic ID.
    path( 'new_entry/<int:topic_id>/', views.new_entry, name='new_entry' ),

    # The page to allow user editing of an entry to a topic. entry_id matches the entry to edit
    path( 'edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry' ),

]