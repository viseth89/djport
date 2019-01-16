from django.shortcuts import render

def bootstrap4a(request):
    return render(request, 'demos/bootstrap4a/index.html')

def bootstrap4b(request):
    return render(request, 'demos/bootstrap4b/index.html')
