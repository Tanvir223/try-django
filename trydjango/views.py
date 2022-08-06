"""
To render html web pages
"""
from django.http import HttpResponse
import random
from articles.models import Article
from django.template.loader import render_to_string

def home_view(request):
    """
    Take in a request (Django sends a request)
    Return HTML as a response (We pick to return the response)
    """

    random_id = random.randint(1, 4)
    #from database??
    article_obj = Article.objects.get(id=random_id)

    #static data
    name = "Tanvir"
    
    context = {
        "title" : article_obj.title,
        "id" : article_obj.id,
        "content" : article_obj.content
    }

    # html view for home page
    HTML_STRING = render_to_string('home-view.html', context = context)
    
    
    

    return HttpResponse(HTML_STRING)
