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

from vokabeltrainer.views.in_formal_views import InFormalListView, InFormalCreateView, InFormalUpdateView, \
    InFormalDeleteView
from vokabeltrainer.views.index import IndexView
from vokabeltrainer.views.lern_informals import LernInformalView, LernInformalErgebnisView
from vokabeltrainer.views.lernen import LernenView
from vokabeltrainer.views.lernen import LernenErgebnisView
from vokabeltrainer.views.lob_und_aufmunterung_views import (
    LobUndAufmunterungListView, LobUndAufmunterungCreateView,
    LobUndAufmunterungUpdateView, LobUndAufmunterungDeleteView)
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

    path('lernen', LernenView.as_view(), name='lernen'),
    path('lernen/<int:set_id>', LernenView.as_view(), name='lernen'),
    path('lernen_ergebnis', LernenErgebnisView.as_view(), name='lernen_ergebnis'),
    path('lernen_ergebnis/<int:set_id>', LernenErgebnisView.as_view(), name='lernen_ergebnis'),

    path('lern_informal', LernInformalView.as_view(), name='lern_informal'),
    path('lern_informal_ergebnis', LernInformalErgebnisView.as_view(), name='lern_informal_ergebnis'),
    path('lern_informal_ergebnis/<int:set_id>', LernInformalErgebnisView.as_view(), name='lern_informal_ergebnis'),


    path('vokabel/', VokabelListView.as_view(), name='list_vokabel'),
    path('vokabel/add/', VokabelCreateView.as_view(), name='new_vokabel'),
    path('vokabel/<int:pk>/', VokabelUpdateView.as_view(), name='update_vokabel'),
    path('vokabel/<int:pk>/delete/', VokabelDeleteView.as_view(), name='delete_vokabel'),

    path('vokabelset/', VokabelSetListView.as_view(), name='list_vokabel_set'),
    path('vokabelset/add/', VokabelSetCreateView.as_view(), name='new_vokabel_set'),
    path('vokabelset/<int:pk>/', VokabelSetUpdateView.as_view(), name='update_vokabel_set'),
    path('vokabelset/<int:pk>/delete/', VokabelSetDeleteView.as_view(), name='delete_vokabel_set'),

    path('lob/', LobUndAufmunterungListView.as_view(), name='list_lob'),
    path('lob/add/', LobUndAufmunterungCreateView.as_view(), name='new_lob'),
    path('lob/<int:pk>/', LobUndAufmunterungUpdateView.as_view(), name='update_lob'),
    path('lob/<int:pk>/delete/', LobUndAufmunterungDeleteView.as_view(), name='delete_lob'),

    path('in_formal/', InFormalListView.as_view(), name='list_in_formal'),
    path('in_formal/add/', InFormalCreateView.as_view(), name='new_in_formal'),
    path('in_formal/<int:pk>/', InFormalUpdateView.as_view(), name='update_in_formal'),
    path('in_formal/<int:pk>/delete/', InFormalDeleteView.as_view(), name='delete_in_formal'),

]
