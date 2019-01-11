from django.shortcuts import render, get_object_or_404

from .models import Work


def workIndex(request):
    work = Work.objects
    return render(request, 'work/work_index.html', {'work':work})

def workDetail(request, work_id):
    work = get_object_or_404(Work, pk=work_id)
    context = {
        'work':work
    }
    return render(request, 'work/work_detail.html', context)

