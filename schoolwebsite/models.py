from django.db import models


class Category(models.Model):
    title=models.CharField(max_length=100, db_index=True)
    slug=models.SlugField(max_length=100)
    image = models.ImageField(upload_to='images/')
    def __str__(self):
        return self.title



    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категория'

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug=models.SlugField()
    description = models.TextField(max_length=100)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField()
  
    
   

    def __str__(self):
        return self.title

    class Meta:
        verbose_name ='Новости'
        verbose_name_plural ='Новости'

    


class Teacher(models.Model):

    full_name=models.CharField(max_length=100, db_index=True)
    description=models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.full_name



    class Meta:
        verbose_name='Педагоги'
        verbose_name_plural='Педагоги'



class Article(models.Model):

    title=models.CharField(max_length=100, db_index=True)
    description=models.TextField()
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title



    class Meta:
        verbose_name='Статья'
        verbose_name_plural='Статья'



class AboutSchool(models.Model):

    title=models.CharField(max_length=100, db_index=True)
    description=models.TextField()
    image = models.ImageField(upload_to='images/')


    def __str__(self):
        return self.title



    class Meta:
        verbose_name='О Школе'
        verbose_name_plural='О Школе'




    