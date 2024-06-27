from django.urls import path

from contas import views

urlpatterns = [
    path(
        'contas/signup',
        views.AccountCreateView.as_view(),
        name="signup"
    ),
]