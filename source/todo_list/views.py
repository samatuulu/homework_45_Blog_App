from django.shortcuts import render, redirect, get_object_or_404

from todo_list.forms import JobForm
from todo_list.models import Things, STATUS_CHOICES


def home(request):
    jobs = Things.objects.all()
    return render(request, 'index.html', context={
        'jobs': jobs
    })


def detail_view(request, pk):
    job = get_object_or_404(Things, pk=pk)
    context = {'job': job}
    return render(request, 'detail_view.html', context)


def create(request, *args, **kwargs):
    if request.method == 'GET':
        form = JobForm()
        return render(request, 'create.html', context={'form': form})
    elif request.method == 'POST':
        form = JobForm(data=request.POST)
        if form.is_valid():
            Things.objects.create(
                description=form.cleaned_data['description'],
                status=form.cleaned_data['status'],
                date_of_completion=form.cleaned_data['date_of_completion'],
                description_more=form.cleaned_data['description_more']
            )
            response = redirect('home')
            return response
        else:
            return render(request, 'create.html', context={'form': form})


def job_update_view(request, pk):
    job = get_object_or_404(Things, pk=pk)
    if request.method == 'GET':
        form = JobForm(data={
            'status': job.status,
            'description': job.description,
            'description_more': job.description_more,
            'date_of_completion': job.date_of_completion
        })
        return render(request, 'update.html', context={'job': job, 'status': STATUS_CHOICES, 'form': form})
    elif request.method == 'POST':
        form = JobForm(data=request.POST)
        if form.is_valid():
            job.status = form.cleaned_data['status']
            job.description = form.cleaned_data['description']
            job.description_more = form.cleaned_data['description_more']
            job.date_of_completion = form.cleaned_data['date_of_completion']
            job.save()

        return redirect('detail', job.pk)


def delete_task(request, pk):
    job = get_object_or_404(Things, pk=pk)
    if request.method == 'GET':
        return render(request, 'delete.html', context={'job': job})
    elif request.method == 'POST':
        job.delete()
        return redirect('home')

#modified

