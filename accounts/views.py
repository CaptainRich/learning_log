from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# The view for the user registration page.

def register( request ):
    """ Register a new user. """
    if request.method != 'POST':
        # Display a blank registration form.
        form = UserCreationForm()

    else:
        # Process the (user's) completed form.
        form = UserCreationForm( data=request.POST )

        if form.is_valid():
            # Save user info to the database and return a 'user' object.
            new_user = form.save()  

            # Log the user in and then redirect to the home page.
            login( request, new_user )
            return redirect( 'learning_logs:index' )
        
    # Display a blank (or invalid) registration form.
    context = { 'form': form }
    return render( request, 'registration/register.html', context )

