"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
# from .views import profile
from snippets import views as snippets_views
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', snippets_views.home, name='home'),
    path('auth/', include('registration.backends.simple.urls')),
    path('profile/', snippets_views.profile, name='profile'),
    path('index', snippets_views.index, name="index"),
    path('snippets/add/', snippets_views.add, name='add'),
    path('snippet/<int:pk>/', snippets_views.detail, name='detail'),
    path('snippets/<int:pk>/edit/', snippets_views.edit, name='edit'),
    path('snippets/<int:pk>/delete/', snippets_views.delete, name='delete'),
    path('search', snippets_views.search, name='search'),
    # path('snippets/<int:pk>/favorite/', snippets_views.favorite, name='favorite'),
    path('category/<slug:slug>', snippets_views.category, name="category"),
    # path("snippets/<int:pk>/copy", snippets_views.copy_snippet, name="copy_snippet")
            ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

