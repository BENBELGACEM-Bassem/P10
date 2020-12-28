#! usr/bin/env python3
# -*- Coding: UTF-8 -*-

"""Define urls wiring templates to users app views"""

from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

app_name = 'users'

urlpatterns = [

    path('login', views.ConnectView.as_view(), name='login'),

    path('logout', login_required(views.QuitView.as_view()), name='logout'),

    path('signup', views.SignUpView.as_view(), name='signup'),

    path('account', login_required(views.AccountView.as_view()), name='account'),

    path('password_reset', views.ResetView.as_view(), name='password_reset'),

    path('password_reset/done', views.ResetDoneView.as_view(), name='password_reset_done'),

    path('password_reset_confirm/<uidb64>/<token>/', views.ResetConfirmView.as_view(), name='password_reset_confirm'),

    path('password_reset_complete/', views.ResetCompleteView.as_view(), name='password_reset_complete'),

]
