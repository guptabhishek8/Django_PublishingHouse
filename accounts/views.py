from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .models import Book


def indexView(request):
    if not request.user.is_superuser:
        return render(request, 'home.html')
    else:
        return redirect('admin')


@login_required(login_url='login')
def dashboardView(request):
    if not request.user.is_superuser:
        return render(request, 'dashboard.html')
    else:
        return redirect('admin')


def registerView(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username Taken')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email Taken')
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name= first_name, last_name=last_name)
                user.save()
                print('user Created')
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('register')

    else:
        return render(request, 'register.html')


def loginView(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if request.user.is_superuser:
                return redirect("admin")
            else:
                return redirect("home")
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')

    else:
        return render(request, 'login.html')


def logoutView(request):
    auth.logout(request)
    return redirect('/')


@login_required(login_url='login')
def book_list(request):
    if not request.user.is_superuser:
        books = Book.objects.all()
        username = request.user.username
        return render(request, 'book_list.html', {
            'books': books, 'username': username,
        })
    else:
        return redirect('admin')


@login_required(login_url='login')
def upload_book(request):
    if not request.user.is_superuser:
        if request.method == 'POST':
            form = BookForm(request.POST, request.FILES)
            if form.is_valid():
                post = Book()
                post.title = request.POST.get('title')
                post.author = request.POST.get('author')
                post.username = request.user.username
                post.pdf = request.FILES.get('pdf')
                post.save()
                return redirect('book_list')
        else:
            form = BookForm()
        return render(request, 'upload_book.html', {
            'form': form
        })
    else:
        return redirect('admin')


def delete_book(request, pk):
    if not request.user.is_superuser:
        if request.method == "POST":
            book = Book.objects.get(pk=pk)
            book.delete()
        return redirect('book_list')
    else:
        return redirect('admin')


def adminView(request):
    if request.user.is_superuser:
        books = Book.objects.all()
        return render(request, 'admin.html', {
            'books': books,
        })
    else:
        messages.info(request, "You are not admin, Don't try to be one")
        return redirect('home')


def book_pending(request):
    if request.user.is_superuser:
        books = Book.objects.all()
        return render(request, 'admin_pending.html', {
            'books': books,
        })
    else:
        messages.info(request, "You are not admin, Don't try to be one")
        return redirect('home')


def book_approved(request):
    if request.user.is_superuser:
        books = Book.objects.all()
        return render(request, 'admin_approved.html', {
            'books': books,
        })
    else:
        messages.info(request, "You are not admin, Don't try to be one")
        return redirect('home')
