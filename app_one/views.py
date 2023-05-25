from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from .forms import ArticleForm
from .models import Article
from django.db.models import Q



# Create your views here.
def article_search_view(request):
    query_dict = request.GET #This is a dictionary
    # query = query_dict.get("q") #<input type="text" name="q">
    try: 
        query = int(query_dict.get("q"))
    except:
        query = None
    article_obj = None
    if query is not None:
        article_obj = Article.objects.get(id = query)
    context = {
        "object" : article_obj
    }
    # print(request.GET)
    return render(request, 'articles/search.html', context = context)

# def article_create_view(request):
#     context = {}
#     if request.method == 'POST':    #if method is POST 
#         title = request.POST.get('title')   #takes entered title
#         content = request.POST.get('content')   #takes entered content
#         article_obj = Article.objects.create(title = title, content = content)    #creating new object with respective data
#         context['object'] = article_obj
#         context['created'] = True
#     return render(request, 'articles/create.html', context = context)


#! Cleaned_Data / Login required
# @login_required
# def article_create_view(request):
#     form = ArticleForm()
#     context = {
#         "form" : form
#     }
#     if request.method == 'POST':    #if method is POST 
#         form = ArticleForm(request.POST)
#         context['form'] = form
#         if form.is_valid():
#             title = form.cleaned_data.get('title')   #takes entered title
#             content = form.cleaned_data.get('content')   #takes entered content
#             article_obj = Article.objects.create(title = title, content = content)    #creating new object with respective data
#             context['object'] = article_obj
#             context['created'] = True
#     return render(request, 'articles/create.html', context = context)

# ! forms.From
# @login_required
# def article_create_view(request):
#     form = ArticleForm(request.POST or None)
#     context = {
#         "form" : form
#     }
#     if form.is_valid():
#         title = form.cleaned_data.get('title')   #takes entered title
#         content = form.cleaned_data.get('content')   #takes entered content
#         article_obj = Article.objects.create(title = title, content = content)    #creating new object with respective data
#         context['object'] = article_obj
#         context['created'] = True
#     return render(request, 'articles/create.html', context = context)


# ! forms.ModelForm
@login_required
def article_create_view(request):
    form = ArticleForm(request.POST or None)
    context = {
        "form" : form
    }

    if form.is_valid():
        article_obj = form.save()   #!replces the below three lines.
        context['form'] = ArticleForm() #!replaces the context lines
        # title = form.cleaned_data.get('title')   #takes entered title
        # content = form.cleaned_data.get('content')   #takes entered content
        # article_obj = Article.objects.create(title = title, content = content)    #creating new object with respective data
        # context['object'] = article_obj
        # context['created'] = True
    return render(request, 'articles/create.html', context = context)

def article_detail_view(request, id = None):
    # article_obj = None
    # if id is not None:
    # article_all = Article.objects.all()
    article_obj = Article.objects.get(id = id)
    # article_filter = Article.objects.filter(id = 2)
    # article_random = Article.objects.order_by('?')[:2]
    # article_conditions = Article.objects.filter(Q(content__icontains = 'Hello') & Q(title__icontains = 'title'))

    context = {
        # "article_all": article_all,
        "article_obj": article_obj,
        # "article_filter": article_filter,
        # "article_random": article_random,
        # "article_conditions": article_conditions,
    }
    return render(request, 'articles/detail.html', context = context)