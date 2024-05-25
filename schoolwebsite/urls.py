from django.urls import path
from .views import school_list,category_filter,teacher,aboutschool,article

urlpatterns = [
    path('', school_list, name='school_list'),
    path('category/', category_filter, name='category'),
    path('teacher/', teacher, name='teacher'),
    path('aboutschool/', aboutschool, name='aboutschool'),
     path('article/', article, name='article'),

]