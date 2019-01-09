from django.shortcuts import render, get_object_or_404

from .models import Blog

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def blogDetail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog':blog
    }
    return render(request, 'blog/blog_detail.html', context)