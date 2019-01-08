from django.shortcuts import render

# Create your views here.
def allWork(request):
    return render(request, 'all_work.html')

def workDetail(request):
    return render(request, 'work_detail.html')