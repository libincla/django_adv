from django.contrib import admin
from books.models import Publisher, Author, Book, Person, Blog


class BookAdmin(admin.ModelAdmin):
    list_display = ('title','publisher', 'publication_date')
    list_filter = ('publication_date',)
    date_hierarchy = 'publication_date'
    ordering = ('-publication_date',)
    #fields = ('title', 'authors', 'publisher')
    filter_horizontal = ('authors',)
    raw_id_fields = ('publisher', )

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Blog)
admin.site.register(Person)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)

