from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Project
from .forms import ProjectForm
from django.contrib.auth.decorators import login_required

def index(request):
    projects = Project.objects.all()
    return render(request, 'index.html', {'projects': projects})

@login_required
def create_project(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        project = Project(title=title, description=description, user=request.user)
        project.save()
        return redirect('portfolio:index')  # Redirect to the project index page after saving the project

    return render(request, 'create_project.html')


@login_required
def edit_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    if request.user != project.user:
        return redirect('portfolio:index')  # Or an unauthorized page if needed

    if request.method == 'POST':
        form = ProjectForm(request.POST, instance=project)
        if form.is_valid():
            form.save()
            return redirect('portfolio:index')
    else:
        form = ProjectForm(instance=project)

    return render(request, 'edit_project.html', {'form': form, 'project': project})

@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)

    # Check if the user is the owner of the project
    if project.user != request.user:
        return redirect('portfolio:index')  # Or show an error message if needed

    # Delete the project
    if request.method == 'POST':
        project.delete()
        return redirect('portfolio:index')  # Redirect to the index page after deletion

    return render(request, 'delete_project.html', {'project': project})