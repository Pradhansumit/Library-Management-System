from django.contrib import admin
from . import models


@admin.register(models.Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_name',
                    'book_author', 'book_isbn', 'book_category']


class MemberAdmin(admin.ModelAdmin):
    list_display = ["id",  'username', 'first_name',
                    'last_name', 'email', 'password',]


admin.site.register(models.LMS_USERS, MemberAdmin)


@admin.register(models.Reading_list)
class ReadingListAdmin(admin.ModelAdmin):
    list_display = ['id', 'book_shelf']
