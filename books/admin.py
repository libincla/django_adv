from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from books.models import Publisher, Author, Book, Person, Blog, Employee


class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    #fields = ('title', 'authors', 'publisher')
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher', )


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = False
    verbose_name_plural = 'employee'

class UserAdmin(UserAdmin):
    inlines = (EmployeeInline, )


# Register your models here.
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Publisher)
admin.site.register(Blog)
admin.site.register(Person)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
