from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.indexView, name="home"),
    url(r'^login/', views.loginView, name="login"),
    url(r'^register/', views.registerView, name="register"),
    url(r'^logout/', views.logoutView, name="logout"),
    url(r'^uploadbook/', views.upload_book, name="upload_book"),
    url(r'^books/', views.book_list, name="book_list"),
    url(r'^admin1/', views.adminView, name="admin"),
    url(r'^pending/', views.book_pending, name="book_pending"),
    url(r'^approved/', views.book_approved, name="book_approved"),  # Admin View
    url(r'^approvedbook/', views.book_approved1, name="book_approved1"),  # ForHomePage
    path('delete/<int:pk>/', views.delete_book, name="delete_book"),
    path('approve/<int:pk>/', views.approve_book, name="approve_book"),  # AdminButton
    path('disapprove/<int:pk>/', views.disapprove_book, name="disapprove_book"),  # AdminButton

]
