from django.db import models


class Product(models.Model):
    title = models.CharField('Название', max_length=300)
    autor = models.CharField('ФИО', max_length=100)
    date = models.DateTimeField('Дата')
    price = models.PositiveIntegerField('Стоимость')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Lesson(models.Model):
    title = models.CharField('Название', max_length=200)
    video = models.FileField('Видео')
    products = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Group(models.Model):
    title = models.CharField('Название', max_length=200)
    products = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Student(models.Model):
    name = models.CharField('Имя', max_length=50)
    surname = models.CharField('Фамилия', max_length=50)
    patronymic = models.CharField('Отчество', max_length=50)
    email = models.EmailField()
    date = models.DateTimeField('Дата')
    groups = models.ForeignKey(Group,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'



