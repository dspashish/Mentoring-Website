"""mentor_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mentor import views
from mentor.views import HomeWorkDetail
from django.conf.urls.static import static
from django.conf import settings
from users import views as user
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('registerStudent/', user.registerStudent, name="register"),
    path('registerTeacher/', user.registerTeacher),
    path('home/', views.main, name="main"),
    path("logout/", user.logout, name="logout"),
    path("login/", user.login, name="login"),
    path('profile/', user.profile, name='profile'),
    path('myhomework/', views.myHomeWork, name="myhomework"),
    path('myhomework/<int:pk>/', views.HomeWorkDetail, name="detail"),
    path('teachers/', views.teachers, name='teachers'),
    path('teachers/<int:pk>/', views.teachersDetail, name="td"),
    path('discuss/', views.discussion, name="discuss"),
    path('discussc/', views.create, name="create"),
    path("discuss/<int:pk>/", views.disDetail, name="dd"),
    path("discuss/edit/<int:pk>/", views.editDiscuss, name="ed"),
    path('discuss/<id>/delete/', views.delete_view ), 
    path('information/', views.informations, name="information"),
    path('information/<int:pk>/', views.informationDetail, name="information"),
    path("students/", views.students, name="students")



]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
