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
from snippets import views as snippets_views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('auth/', include('registration.backends.simple.urls')),
    # path('', snippets_views.index, name="index"),
    # path('snippets/add/', snippets_views.add, name='add'),
    # path('snippets/<int:pk>/edit/', snippets_views.edit, name='edit'),
    # path('snippets/<int:pk>/delete/', snippets_views.delete, name='delete'),
    # path('snippets/<int:pk>/favorite/', snippets_views.favorite, name='favorite'),
    # path('category/<slug:slug>', snippets_views.category, name="category"),
]
