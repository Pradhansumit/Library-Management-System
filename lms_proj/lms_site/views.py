from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import user_passes_test, login_required

# local files
from . import models, forms

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# is_user functions


def is_admin(user):
    if user.status == "admin":
        return True


def is_librarian(user):
    if user.status == "librarian":
        return True


def is_student(user):
    if user.status == "student":
        return True


# home page view


def index(request):
    return render(request, 'lms_site/index.html')

# ------------------
# authentication function views


def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            if user.is_superuser:
                return redirect('admin_dashboard')

            elif request.user.status == 'librarian':
                return redirect('librarian_dashboard')

            elif request.user.status == 'student':
                return redirect('student_dashboard')

            else:
                return redirect('home')

        else:
            raise ValueError("Put correct credentials")

    else:
        return render(request, 'lms_site/login.html')


def logout(request):
    auth_logout(request)
    return redirect('home')

# authentication function views
# ------------------

# ------------------
# admin function views


# @user_passes_test(is_admin)
def admin_dashboard(request):
    return render(request, 'lms_site/admin_dashboard.html',)


# View members

# all member list
def admin_member_list(request):
    user_list = models.LMS_USERS.objects.all()
    return render(request, 'lms_site/admin_member_list.html', {"user_list": user_list})


# all librarian list
def admin_librarian_list(request):
    user_list = models.LMS_USERS.objects.filter(status="librarian")
    return render(request, 'lms_site/admin_librarian_list.html', {"user_list": user_list})


# all Student list
def admin_student_list(request):
    user_list = models.LMS_USERS.objects.filter(status="student")
    return render(request, 'lms_site/admin_student_list.html', locals())

# Add members


@user_passes_test(is_admin)
def admin_member_add(request):
    if request.method == "POST":
        fm = forms.CustomUserCreationForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('admin_member_list')

        else:
            print(fm.errors)
            raise ValueError("Not correctly put.")

    else:
        fm = forms.CustomUserCreationForm()
        return render(request, 'lms_site/admin_member_add.html', {"fm": fm})


# All members delete

def admin_member_delete(request, id):
    if request.method == 'POST':
        user_list = models.LMS_USERS.objects.get(pk=id)
        user_list.delete()

        return redirect('admin_member_list')

# All members edit


def admin_member_update(request, id):
    if request.method == "POST":
        pi = models.LMS_USERS.objects.get(pk=id)
        fm = forms.CustomUserChangeForm(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
            return redirect('admin_member_list')
        else:
            print(fm.errors)
    else:
        pi = models.LMS_USERS.objects.get(pk=id)
        fm = forms.CustomUserChangeForm(instance=pi)
        return render(request, 'lms_site/admin_member_update.html', {'form': fm})

# +++++++++++++++++++++++++++++++++++++++++++++
# librarian functions


@login_required
@user_passes_test(is_librarian)
def LibrarianView(request):
    return render(request, 'lms_site/librarian_dashboard.html', )

# book list


def librarian_book_list(request):
    book_list = models.Books.objects.all()
    return render(request, 'lms_site/librarian_book_list.html', locals())

# Add books


def librarian_book_add(request):
    if request.method == "POST":
        fmbooks = forms.BooksForm(request.POST)
        if fmbooks.is_valid():
            fmbooks.save()
            return redirect('librarian_book_list')

        else:
            print(fmbooks.errors)
            raise ValueError("Not correctly put.")

    else:
        fmbooks = forms.BooksForm
        return render(request, 'lms_site/librarian_book_add.html', {"fmbooks": fmbooks})


# book delete


def librarian_book_delete(request, id):
    if request.method == 'POST':
        book_list = models.Books.objects.get(pk=id)
        book_list.delete()
        return redirect('librarian_book_list')

# book edit


def librarian_book_update(request, id):
    if request.method == "POST":
        pi = models.Books.objects.get(pk=id)
        fmbooks = forms.BooksForm(request.POST, instance=pi)
        if fmbooks.is_valid():
            fmbooks.save()
            return redirect('librarian_book_list')
    else:
        pi = models.Books.objects.get(pk=id)
        fmbooks = forms.BooksForm(instance=pi)
        return render(request, 'lms_site/librarian_book_update.html', {'fmbooks': fmbooks})
# +++++++++++++++++++++++++++++++++++++++++++++
# student functions


@login_required
@user_passes_test(is_student)
def StudentView(request):
    return render(request, 'lms_site/student_dashboard.html')


@login_required
@user_passes_test(is_student)
def student_book_list(request):
    book_list = models.Books.objects.all()
    return render(request, 'lms_site/student_book_list.html', locals())


@login_required
@user_passes_test(is_student)
def add_to_reading_list(request, id):
    user = request.user
    book = models.Books.objects.get(pk=id)
    models.Reading_list(user=user, book=book).save()
    return redirect('student_book_list')


@login_required
@user_passes_test(is_student)
def reading_book_list(request):
    user = request.user

    # get all the books added to reading list (for different users)
    reading_list_items = models.Reading_list.objects.filter(user=user)

    # get book details using sql traverse through relations made using foreign key
    book_list = [item.book for item in reading_list_items]

    return render(request, 'lms_site/student-reading-list.html', locals())


@login_required
@user_passes_test(is_student)
def reading_list_book_delete(request, id):
    if request.method == 'POST':
        book = models.Books.objects.get(pk=id)
        book.delete()
        return redirect('reading_book_list')
