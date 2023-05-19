from django.contrib import admin
from .models import book , Author , Address , Country


# Register your models here.

class bookAdmin(admin.ModelAdmin):
    # readonly_fields = ("slug",)
    prepopulated_fields = {"slug" : ("title", )}
    list_filter = ("author" , "rating" ,)
    list_display = ("title" , "author")

admin.site.register(book,bookAdmin)
admin.site.register(Author)
admin.site.register(Address)
admin.site.register(Country)

