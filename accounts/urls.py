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
    url(r'^pending/', views.book_pending, name="book_pending"),  # Admin View
    url(r'^approved/', views.book_approved, name="book_approved"),  # Admin View
    url(r'^disapproved/', views.book_disapproved, name="book_disapproved"),  # Admin View
    url(r'^deleted/', views.book_delete, name="book_delete_page"),  # Admin View render html page
    url(r'^approvedbook/', views.book_approved1, name="book_approved1"),  # ForHomePage
    path('deleting/<int:pk>/', views.permanently_delete_book, name="perm_delete_book"),  # for admin
    path('recover/<int:pk>/', views.recover_delete_book, name="recover_delete_book"),  # for admin to recover book
    path('delete/<int:pk>/', views.delete, name="delete_book"),  # for User
    path('approve/<int:pk>/', views.approve_book, name="approve_book"),  # AdminButton To approve
    path('disapprove/<int:pk>/', views.disapprove_book, name="disapprove_book"),  # AdminButton To disapprove

]
