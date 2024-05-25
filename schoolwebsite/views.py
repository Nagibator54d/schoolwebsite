from django.shortcuts import render,redirect
from .models import Category,Post,Teacher,AboutSchool,Article



# def home(request):
#     return render(request, 'home.html')

# def news(request):
#     posts = Post.objects.all().order_by('-published_date')
#     return render(request, 'news.html', {'posts': posts})


def school_list(request):
    schools=Post.objects.all()
    categories=Category.objects.all()
    context={
        'schools':schools,
        'categories':categories,
    }
    return render(request,'home.html',context)

def category_filter(request):
    schools=Post.objects.filter()
    categories=Category.objects.all()
    context={
        'schools':schools,
        'categories':categories,
    }
    
    return render(request,'category.html',context)





def teacher(request):
    teachers=Teacher.objects.all()
    context={
        'schools':schools,
       
    }
    return render(request,'teacher.html',context)

def aboutschool(request):
    aboutschools=AboutSchool.objects.all()
    context={
        'aboutschools':aboutschools,
       
    }
    return render(request,'aboutschool.html',context)



def article(request):
    articles= Article.objects.all()
    context={
        'articles':articles,
       
    }
    return render(request,'article.html',context)



