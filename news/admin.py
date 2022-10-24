from django.contrib import admin
from .models import News, Category, Marker
# Register your models here.



class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'created_at', 'updated_at', 'is_published', 'category')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'content')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


class MarkerAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_user', 'id_news', 'marker', 'date_marker', 'comment')
    list_display_links = ('id', 'id_user', 'id_news', 'marker', 'date_marker', 'comment')



admin.site.register(News, NewsAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Marker, MarkerAdmin)


