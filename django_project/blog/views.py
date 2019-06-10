from django.shortcuts import render
#from django.http import HttpResponse
# Create your views here.

posts = [
    {
        'author': 'Ashok',
        'title': 'Blog Post',
        'content': 'First post content',
        'date_posted': 'June 9, 20219'
    },
    {
        'author': 'Aditya',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'June 12, 20219'
    }

]


def home (request):
    context = {
        'posts': posts
    }
    return render (request, 'blog/home.html',context)

def about(request):
    return render (request, 'blog/about.html',{'title': '@About'})