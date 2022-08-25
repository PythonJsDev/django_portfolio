
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from projects.views import home, project_detail, apps, projects_web, others_projects


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('apps/<str:category>/', apps, name='apps'),
    path('projects/<str:framework>', projects_web, name='projects'),
    path('<str:language>', others_projects, name='others-projects'),
    path('project/<str:slug>/', project_detail, name='project-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
