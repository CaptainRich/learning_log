""" The webpage forms definitions. """

from django import forms
from .models import Topic, Entry

class TopicForm( forms.ModelForm ):  # TopicForm inherits from forms.ModelForm
    class Meta:
        model  = Topic               # The form is based on the Topic model
        fields = ['text']            # The form includes only the 'text' field
        labels = {'text': ''}        # '' indicates no label to be generated
        

class EntryForm( forms.ModelForm ):  # EntryForm inherits from forms.ModelForm
    class Meta:
        model   = Entry              # The form is based on the Entry model
        fields  = ['text']           # The form includes on the 'text' field
        labels  = {'text': '' }      # '' indicates no label to be generated

        # Override Django's default 40 column text box.
        widgets = {'text': forms.Textarea( attrs={'cols':80})}

