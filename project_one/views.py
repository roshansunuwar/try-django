# To render the HTML webpages
import random
from django.http import HttpResponse
from django.template.loader import render_to_string
from app_one.models import Article

# html_string = """<h1>Hello World!</h1>"""
def home(request, *args, **kwargs):
    # return HttpResponse(html_string)
    random_id = random.randint(1, 5)

    #from Database
    article_obj = Article.objects.get(id = random_id)
    article_queryset = Article.objects.all()
    # my_list = article_list#[10, 20, 30, 40]
    
    context = {
        "object_list" : article_queryset,
        "id" : article_obj.id,
        "title" : article_obj.title,
        "content" : article_obj.content,
    }
    HTML_String = render_to_string("home.html", context = context)
    # HTML_String = """
    # <h1>{title} (id: {id})</h1>
    # <p>{content}!</p>
    # """.format(**context)
    return HttpResponse(HTML_String)
    

    # h1_string = f"""<h1>{article_obj.title} (id: {article_obj.id})</h1>"""
    # p_string = f"""<p>{article_obj.content}</p>"""
    # html_string = h1_string + p_string
    # return HttpResponse(html_string)
