from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('archive/category/<int:category_id>/', get_category_archive, name='category_archive'),
    path('news/<int:news_id>/', view_news, name='view_news'),
    path('news/<int:news_id>/btn_marker/', btn_marker, name='btn_marker'),
    path('archive/', archive, name='archive_list'),
    path('archive/news/<int:news_id>/', view_news_archive, name='view_news_archive'),
    path('big_boss_panel/', index, name='big_boss_panel'),
    path('news/add_news/', add_news, name='add_news'),
    path('big_boss_panel/updated_news/<int:pk>/', updated_news, name='updated_news'),
    path('big_boss_panel/delete_news/<int:pk>/', delete_news, name='delete_news'),

]
