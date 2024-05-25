from django.contrib import admin
from .models import Category,Post,Teacher,AboutSchool,Article




@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=['id','title',]
    list_display_links=['id','title',]



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ['id','title','description','category','created','updated']
    list_display_links = ['id','title']
    list_filter = ['created','updated']
 


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    list_display=['id','full_name','description']
    list_display_links=['id','full_name']


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):

    list_display=['id','title','description']
    list_display_links=['id','title']
    

@admin.register(AboutSchool)
class AboutSchoolAdmin(admin.ModelAdmin):

    list_display=['id','title','description']
    list_display_links=['id','title']


