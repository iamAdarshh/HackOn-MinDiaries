from django.urls import path
from django.urls.resolvers import URLPattern
from django.views.generic.base import View

from .views import blogGrid, home, detailBlog, test, testgrid, register, covidDashboard

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', view=home, name='home'),
    path('bloggrid/', view=blogGrid, name='bloggrid'),
    path('bloggrid/<blog_id>/', view=detailBlog, name='blog'),
    path('testgrid/', view=testgrid, name="testgrid"),
    path('test/', view=test, name='test'),
    path('register/', view = register, name = "register"),
    path('coviddashboard', view = covidDashboard, name='covidDashboard'),

    # Change Password
    path('change-password/', 
    auth_views.PasswordChangeView.as_view(template_name="registration\change-password.html", success_url="/change-password-done/"),
    name = "change_password"),
    path('change-password-done/',
    auth_views.PasswordChangeDoneView.as_view(template_name="registration\change-password-done.html"),
    name="change_password_done"),

    # Reset Password
    path('password-reset/',
    auth_views.PasswordResetView.as_view(template_name="registration\password-reset.html", subject_template_name="registration\email\password-reset-text.txt", email_template_name="registration\email\password-reset-email.html", success_url="/password-reset/done/"),
    name="reset_password"),
    path('password-reset/done/',
    auth_views.PasswordResetDoneView.as_view(template_name="registration\password-reset-sent.html"),
    name="password_reset_done"),
    path('password-reset-confirm/<uidb64>/<token>/',
    auth_views.PasswordResetConfirmView.as_view(template_name="registration\password-reset-confirm.html", success_url="/password-reset-complete/"),
    name="passwordresetconfirm"),
    path('password-reset-complete/',
    auth_views.PasswordResetDoneView.as_view(template_name="registration\password-reset-complete.html"),
    name="password_reset_complete"),
]