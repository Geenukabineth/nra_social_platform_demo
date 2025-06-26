from django.urls import path
from . import views 


urlpatterns = [
    path("", views.landing, name="landing"),
    path("login/", views.login_view, name="login"),
    path("register/", views.signup_view, name="register"),
    path("base/", views.dashboard_view, name="base"),
    path("adminview/", views.admin_panel_view, name="adminview"),
    path("create-product/", views.create_product, name="create_product"),
    path("logout/", views.logout_view, name="logout"),
    path("user_data/", views.user_data, name="user_data"),
    path("create_event/", views.create_event, name="create_event"),
]
