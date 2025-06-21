from django.urls import path
from . import views 



urlpatterns = [
    path("", views.landing),
    path('login/', views.login_view, name='login'),
    path('register/', views.signup_view, name='register'),
    path("base/", views.base, name="base"),
    path("adminview/", views.adminview, name="adminview"),
    path("create_product/", views.create_product, name="create_product"),
    path("logout/", views.logout_view, name="logout"),
    path("user_data/", views.user_data, name="user_data"),
    path("create_event/", views.create_event, name="create_event"),
]
