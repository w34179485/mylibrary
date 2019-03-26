from django.db import models
from django.utils import timezone

class Library(models.Model):
    library_name = models.CharField('馆名',max_length=100)
    library_address = models.CharField('地址',max_length=300,default='')
    library_phone = models.CharField('电话',max_length=50,default='')

    def __str__(self):
        return self.library_name
    class Meta:
        verbose_name = '图书馆'
        verbose_name_plural = '图书馆'

class Author(models.Model):
    author_name = models.CharField('作者',max_length=100)
    
    def __str__(self):
        return self.author_name
    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'

class Book(models.Model):
    book_name = models.CharField('书名',max_length=200)
    book_price = models.FloatField('价格',default=0)
    book_code = models.CharField('条码',max_length=200)
    book_amount = models.IntegerField('数量',default=1)
    author = models.ForeignKey(Author,on_delete=models.CASCADE,default='')

    def __str__(self):
        return self.book_name
    class Meta:
        verbose_name = '书籍'
        verbose_name_plural = '书籍'

SEX_CHOICES = (('男','男'),('女','女'))

class Reader(models.Model):
    reader_name = models.CharField('读者',max_length=100)
    reader_sex = models.CharField('性别',max_length=1,choices=SEX_CHOICES)
    reader_phone = models.CharField('电话',max_length=100)
    reader_money = models.FloatField('压金',default=0)
    def __str__(self):
            return self.reader_name
    class Meta:
        verbose_name = '读者'
        verbose_name_plural = '读者'

class Record(models.Model):
    record_reader = models.ForeignKey(Reader,on_delete=models.CASCADE)
    record_book = models.ForeignKey(Book,on_delete=models.CASCADE)
    record_amount = models.IntegerField('数量',default=1)
    record_date = models.DateTimeField('借书日期')