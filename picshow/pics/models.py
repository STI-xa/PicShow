from django.db import models

from users.models import User

COLORS = (
    ('red', 'Красный'),
    ('blue', 'Синий'),
    ('green', 'Зеленый'),
    ('yellow', 'Желтый'),
    ('orange', 'Оранжевый'),
    ('purple', 'Фиолетовый'),
    ('pink', 'Розовый'),
    ('brown', 'Коричневый'),
    ('gray', 'Серый'),
    ('black', 'Черный'),
    ('white', 'Белый'),
)

class Tag(models.Model):
    name = models.CharField(
        'Название тега',
        max_length=150
    )
    color = models.CharField(
        'Цвет',
        max_length=10,
        choices=COLORS,
        default='gray'
    )
    slug = models.SlugField(
        'Уникальный слаг',
        max_length=150
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(
        'Название категории',
        max_length=200,
    )
    slug = models.SlugField('URL address', unique=True)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return f'{self.name}'


class Photo(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='photos')
    description = models.TextField('Описание фото', blank=True, null=True)
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    image = models.ImageField(
        upload_to='photos/', blank=True, null=True)
    tag = models.ForeignKey(
        Tag, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='photos')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True,
        related_name='photos')
    comments = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = 'Фото'

    def __str__(self):
        return self.description
