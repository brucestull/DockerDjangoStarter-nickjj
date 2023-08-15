from django.urls import path

from accounts.views import CustomLoginView
from accounts.views import CustomUserDetailView
from accounts.views import CustomUserSignUpView
from accounts.views import CustomUserUpdateView
from accounts.views import ForbiddenView

urlpatterns = [
    # Try to override 'login' view.
    path(
        "login/",
        CustomLoginView.as_view(),
        name="login",
    ),
    path(
        "signup/",
        CustomUserSignUpView.as_view(),
        name="signup",
    ),
    path(
        "<int:pk>/edit/",
        CustomUserUpdateView.as_view(),
        name="edit",
    ),
    path(
        "<int:pk>/detail/",
        CustomUserDetailView.as_view(),
        name="detail",
    ),
    path(
        "403/",
        ForbiddenView.as_view(),
        name="forbidden",
    ),
]
