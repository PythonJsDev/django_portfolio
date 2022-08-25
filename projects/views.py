from django.shortcuts import render, get_object_or_404

from projects.models import Project

WEB = ['javascript', 'python', 'django', 'drf', 'flask']
LANGUAGES = ['javascript', 'python']


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


def apps(request, category):
    if category == 'web':
        title = 'Applications Web'
        projects = filter_by_keyword('WEB_APP', WEB)
    else:
        title = 'Autres Applications'
        projects = filter_by_keyword('OTHERS', LANGUAGES)
    projects = {k: projects[k] for k in sorted(projects.keys())}
    return render(request, 'projects/apps.html', context={'projects': projects,
                                                          'category': category,
                                                          'title': title})


def projects_web(request, framework):
    projects = Project.objects.filter(keywords_list__icontains=framework).filter(category='W').order_by('name')
    title = framework.upper() if framework in LANGUAGES else 'Framework ' + framework.upper()
    return render(request, 'projects/projects.html', context={'projects': projects,
                                                              'title': title})


def others_projects(request, language):
    projects = Project.objects.filter(keywords_list__icontains=language).filter(category='O').order_by('name')
    title = language.upper()
    return render(request, 'projects/projects.html', context={'projects': projects,
                                                              'title': title})


def filter_by_keyword(category_app, keywords):
    if category_app == 'WEB_APP':
        projects = Project.objects.filter(category=Project.Categories.WEB_APP).order_by('name')
    else:
        projects = Project.objects.filter(category=Project.Categories.OTHERS).order_by('name')
    return {k: projects.filter(keywords_list__icontains=k) for k in keywords}
