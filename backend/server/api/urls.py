from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^login/', views.FBView.as_view()),
    url(r'^analyze/', views.AnalyzeView.as_view()),
]