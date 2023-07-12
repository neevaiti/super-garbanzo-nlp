from django.contrib import admin
from django.urls import path
from emotion import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path("new-text/", views.new_text, name="new_text"),
    path('patient/<int:id>/', views.text_by_id, name='text_by_id'),
    # path("research/", views.research, name="research"),
    path('login-user/', views.login_user, name='login'),
    path('logout-user/', views.logout_user, name='logout'),
    path('register-user/', views.register_user, name='register')
]