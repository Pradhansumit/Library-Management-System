from django.urls import path
from . import views

urlpatterns = [
    # home

    path('', views.index, name="home"),

    #     authentication part

    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),

    #     admin part

    path('fadmin', views.admin_dashboard, name="admin_dashboard"),
    path('admin-member-list', views.admin_member_list,
         name="admin_member_list"),
    path('admin-librarian-list', views.admin_librarian_list,
         name="admin_librarian_list"),
    path('admin-student-list', views.admin_student_list,
         name="admin_student_list"),
    path('member-add', views.admin_member_add,
         name="admin_member_add"),
    path('librarian-delete/<int:id>/', views.admin_member_delete,
         name="admin_member_delete"),
    path('<int:id>/', views.admin_member_update,
         name="admin_member_update"),

    # librarian part

    path('ldashboard', views.LibrarianView, name="librarian_dashboard"),
    path('librarian-book-list', views.librarian_book_list,
         name="librarian_book_list"),
    path('book-add', views.librarian_book_add,
         name="librarian_book_add"),
    path('book-delete/<int:id>/', views.librarian_book_delete,
         name="librarian_book_delete"),
    path('book/<int:id>/', views.librarian_book_update,
         name="librarian_book_update"),


    # student part
    path('sdashboard', views.StudentView, name="student_dashboard"),
    path('student-book-list', views.student_book_list,
         name="student_book_list"),
    path('reading-list/<int:id>/', views.add_to_reading_list,
         name="add_to_reading_list"),
    path("reading-book-list", views.reading_book_list, name="reading_book_list"),
    path('read-delete/<int:id>/', views.reading_list_book_delete,
         name="reading_list_book_delete"),


]
