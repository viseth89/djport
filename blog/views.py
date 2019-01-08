from django.shortcuts import render

# Create your views here.
def allBlogs(request):
    return render(request, 'blog/all_blogs.html')

def blogDetail(request):
    return render(request, 'blog/blog_detail.html')