from django.db import models
from django.contrib.auth.models import User, AbstractUser


class LMS_USERS(AbstractUser):
    USER_STATUS = [
        ('admin', 'Admin'),
        ('librarian', 'Librarian'),
        ('student', 'Student'),
    ]
    status = models.CharField(
        max_length=20, choices=USER_STATUS, default='student')


class Books(models.Model):
    BOOK_CATEGORIES = [
        ("education", "Education"),
        ("history", "History"),
        ("fiction", "Fiction"),
        ("non-fiction", "Non-Fiction"),
        ("romance", "Romance"),
        ("suspense", "Suspense"),
        ("self-help", "Self-Help"),
    ]
    book_name = models.CharField(max_length=255)
    book_author = models.CharField(max_length=255)
    book_isbn = models.IntegerField()
    book_category = models.CharField(
        max_length=20, default=None, choices=BOOK_CATEGORIES)


class Reading_list(models.Model):
    BOOK_READ_STATUS = [
        ("read", "Read"),
        ("want_to_read", "Want_To_Read"),
        ("currently_reading", "Currently_Reading"),
    ]
    user = models.ForeignKey(LMS_USERS, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.PROTECT)
    book_shelf = models.CharField(
        max_length=20, choices=BOOK_READ_STATUS, default="want_to_read")
