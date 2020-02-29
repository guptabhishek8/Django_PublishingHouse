from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.core.files.storage import FileSystemStorage
from .forms import BookForm
from .models import Book


def indexView(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def dashboardView(request):
    return render(request, 'dashboard.html')


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
def uploadView(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        context['url']= fs.url(name)
    return render(request, 'upload.html', context)


@login_required(login_url='login')
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {
        'books': books
    })


@login_required(login_url='login')
def upload_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'upload_book.html', {
        'form': form
    })
