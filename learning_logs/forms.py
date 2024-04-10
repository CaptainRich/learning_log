""" The webpage forms definitions. """

from django import forms
from .models import Topic

class TopicForm( forms.ModelForm ):  # TopicForm inherits from forms.ModelForm
    class Meta:
        model  = Topic               # The form is based on the Topic model
        fields = ['text']            # The form includes only the 'text' field
        labels = {'text': ''}        # '' indicates no label to be generated
        
