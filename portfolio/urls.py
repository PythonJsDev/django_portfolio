
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from projects.views import home, project_detail, web, other


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('web', web, name='web'),
    path('other', other, name='other'),
    path('project/<str:slug>/', project_detail, name='project-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
