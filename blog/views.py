from django.shortcuts import render, get_object_or_404
from django.http import Http404

# from .mocks import Post
from .models import Post

# Create your views here.
def index(request):
    # posts = []
    # posts = Post.all()
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts': posts})

def show(request, id):
    # post = Post.find(id)
    post = get_object_or_404(Post, pk=id)
    # try:
    #     post = Post.objects.get(pk=id)
    # except Post.DoesNotExist:
    #     # return {'id': 0, 'title': 'Sorry no post', 'body': ''}
    #     raise Http404('Sorry') # fonctionne avec raise :-)

    return render(request, 'blog/show.html', {'post' : post})