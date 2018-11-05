from django.shortcuts import get_object_or_404, render
from .models import Post
from django.views.generic import ListView
from django.core.paginator import Paginator

class PostView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 3

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')

def projects(request):
    return render(request, 'blog/projects.html')

def post(request, post_id):
    post_obj = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post.html', {'post': post_obj})
