from django.shortcuts import render

def bootstrap4a(request):
    return render(request, 'demos/bootstrap4a/index.html')

def bootstrap4b(request):
    return render(request, 'demos/bootstrap4b/index.html')

def bootstrap4c(request):
    return render(request, 'demos/bootstrap4c/index.html')

def bootstrap4d(request):
    return render(request, 'demos/bootstrap4d/index.html')

def bootstrap4dAbout(request):
    return render(request, 'demos/bootstrap4d/about.html')

def bootstrap4dBlog(request):
    return render(request, 'demos/bootstrap4d/blog.html')

def bootstrap4dContact(request):
    return render(request, 'demos/bootstrap4d/contact.html')

def bootstrap4dServices(request):
    return render(request, 'demos/bootstrap4d/services.html')

def jsjq1(request):
    return render(request, 'demos/jsjq1/index.html')
