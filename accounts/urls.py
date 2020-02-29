from django.urls import path

from . import views
# '' empty leads to /listings(render file in def index() in views)
urlpatterns = [
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('logout', views.logout, name="logout"),
    path('dashboard', views.dashboard, name="dashboard")
]
