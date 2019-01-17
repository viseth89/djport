from django.shortcuts import render

def bootstrap4a(request):
    return render(request, 'demos/bootstrap4a/index.html')

def bootstrap4b(request):
    return render(request, 'demos/bootstrap4b/index.html')

def bootstrap4c(request):
    return render(request, 'demos/bootstrap4c/index.html')

def jsjq1(request):
    return render(request, 'demos/jsjq1/index.html')