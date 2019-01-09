from django.shortcuts import render, get_object_or_404

from .models import Job 


def jobIndex(request):
    job = Job.objects

    return render(request, 'jobs/job_index.html', {'job':job})

def jobDetail(request, job_id):
    job = get_object_or_404(Job, pk=job_id)
    context = {
        'job':job
    }
    return render(request, 'jobs/job_detail.html', context)

