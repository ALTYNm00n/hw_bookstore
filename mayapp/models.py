from django.db import models
from django.contrib.auth.models import AbstractUser
class BookCategory(models.Model):
    name = models.CharField(max_length=120,verbose_name='категории')
    image = models.ImageField(upload_to='image/')
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name= 'Категория'
        verbose_name_plural = 'категории' 

class Author(AbstractUser):
    book_amount=models.PositiveBigIntegerField(default=0,null=True,verbose_name='количество книг')
    date_birthday =models.DateField(verbose_name='дата рождения')
    pseudonym = models.CharField(max_length=127,verbose_name='псевдоним')
    avatar = models.ImageField(upload_to='avatar/',null=True)
    book_category=models.ForeignKey(to=BookCategory,on_delete=models.CASCADE,related_name='authors',verbose_name='категория книг')
    def __str__(self) -> str:
        return self.username
    class Meta :
        verbose_name= 'автор'
        verbose_name_plural = verbose_name + 'ы'

class Book(models.Model):
    name=models.CharField(max_length=127,verbose_name='название')
    author=models.ForeignKey(to=Author,on_delete=models.CASCADE,related_name='books',verbose_name='автор')
    date_of_issue=models.DateField(verbose_name='дата выпуска')
    chapter_amount=models.PositiveBigIntegerField(default=0,null=True,verbose_name='количество глав')
    prewiew = models.CharField(max_length=127,verbose_name='оглавление')
    book_category=models.ForeignKey(to=BookCategory,on_delete=models.CASCADE,related_name='books',verbose_name='категория книг')
    price=models.PositiveBigIntegerField(default=0,null=True,verbose_name='цена')
    discount=models.PositiveBigIntegerField(default=0,null=True,verbose_name='скидка')
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name='книга'
        verbose_name_plural= 'книги'
    












