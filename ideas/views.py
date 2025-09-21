from django.shortcuts import render
from .models import Idea

def idea_list(request):
    # 1. Get all Idea objects from the database
    ideas = Idea.objects.all().order_by('-created_at') # Show newest first

    # 2. Define the context dictionary to pass data to the template
    context = {
        'ideas': ideas
    }

    # 3. Render the HTML template with the context data
    return render(request, 'ideas/idea_list.html', context)