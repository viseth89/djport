from django.shortcuts import render, get_object_or_404

from .models import Blog


def blogIndex(request):
    blogs = Blog.objects.all().order_by('-pub_date')
    return render(request, 'blog/blog_index.html', {'blogs':blogs})

def blogDetail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    context = {
        'blog':blog
    }
    return render(request, 'blog/blog_detail.html', context)