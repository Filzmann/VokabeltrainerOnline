"""VokabeltrainerOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path

from vokabeltrainer.views.index import IndexView
from vokabeltrainer.views.vokabel_set_views import (
    VokabelSetListView, VokabelSetCreateView,
    VokabelSetUpdateView, VokabelSetDeleteView
)
from vokabeltrainer.views.vokabel_views import (
    VokabelListView, VokabelCreateView,
    VokabelUpdateView, VokabelDeleteView
)

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('vokabel/', VokabelListView.as_view(), name='list_vokabel'),
    path('vokabel/add/', VokabelCreateView.as_view(), name='new_vokabel'),
    path('vokabel/<int:pk>/', VokabelUpdateView.as_view(), name='update_vokabel'),
    path('vokabel/<int:pk>/delete/', VokabelDeleteView.as_view(), name='delete_vokabel'),
    path('vokabelset/', VokabelSetListView.as_view(), name='list_vokabel_set'),
    path('vokabelset/add/', VokabelSetCreateView.as_view(), name='new_vokabel_set'),
    path('vokabelset/<int:pk>/', VokabelSetUpdateView.as_view(), name='update_vokabel_set'),
    path('vokabelset/<int:pk>/delete/', VokabelSetDeleteView.as_view(), name='delete_vokabel_set')

]
