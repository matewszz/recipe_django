from . import views
from django.urls import path

app_name = 'authors'

urlpatterns = [

    path('register/', views.register_view, name="register"),
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('dashboard/recipe/<int:id>/edit', views.dashboard_recipe_edit, 
         name="dashboard_recipe_edit"),
    path('dashboard/recipe/<int:id>/delete', views.dashboard_recipe_delete, 
         name="dashboard_recipe_delete"),
]
