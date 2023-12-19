from django.urls import path
from ui import views

app_name = "ui"

urlpatterns = [
    path('', views.login, name= 'login'),
    path('log', views.log),
    path('home',views.home, name='home'),
    path('handle_login',views.handle_login),
    path('logout',views.logout),
    path('UserMannual', views.help),
    path('about',views.about),
    path('download-csv/', views.download_csv, name='download_csv'),
]