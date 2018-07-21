#!/usr/bin/env python
# coding=utf-8


from django.urls import path
from app01 import views

app_name = "app01"
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:question_id>', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),

]
