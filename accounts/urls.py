from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.indexView, name= "home"),
    url(r'^admin1/', views.adminView, name="admin"),
    url(r'^login/', views.loginView, name="login"),
    url(r'^dashboard/', views.dashboardView, name="dashboard"),
    url(r'^register/', views.registerView, name="register"),
    url(r'^logout/', views.logoutView, name= "logout"),
    url(r'^uploadbook/', views.upload_book, name="upload_book"),
    url(r'^books/', views.book_list, name="book_list"),
    url(r'^delete/<int:pk>/', views.delete_book, name="delete_book"),

]

