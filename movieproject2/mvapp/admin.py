from django.contrib import admin
from . models import Movie,Category
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'release_date', 'category')
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Movie, MovieAdmin)
