from django.shortcuts import render
from work.models import Work

# Create your views here.
def index(request):
    work = Work.objects.all()[:4]
    return render(request, 'pages/index.html', {'work':work})

def about(request):
    return render(request, 'pages/about.html')