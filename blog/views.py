

# Create your views here.
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.views.generic import DetailView

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/sitemap_post_detail.html'  # Create this template
    context_object_name = 'post'