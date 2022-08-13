from django.shortcuts import render, get_object_or_404

from projects.models import Project


def home(request):
    url_oc = "https://openclassrooms.com/fr/paths/518-developpeur-dapplication-python"
    title = 'Portfolio'
    return render(request, 'projects/home.html', context={'url_oc': url_oc,
                                                          'title': title})


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    title = project.name
    sub_title = "Projet d'étude Openclassrooms" if project.url_github_oc else ''
    return render(request, 'projects/detail.html',
                  context={'project': project,
                           'title': title,
                           'sub_title': sub_title})


def web(request):
    projects = Project.objects.filter(category=Project.Categories.WEB_APP)
    title = 'Applications Web'
    return render(request, 'projects/apps.html', context={'projects': projects,
                                                          'title': title})


def other(request):
    projects = Project.objects.filter(category=Project.Categories.OTHERS)
    title = 'Autres Applications'
    return render(request, 'projects/apps.html', context={'projects': projects,
                                                          'title': title})
