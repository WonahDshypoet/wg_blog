from django.shortcuts import render
from .database import Database
from .post import Post

# Create your views here.


def blog(request):

    template_name = 'blog.html'

    if request.method == GET:

        posts = Post.from_blog('123')

        for post in posts:
            print(post)

        context = {
            'post': post,
        }
        return render(request, template_name, context)