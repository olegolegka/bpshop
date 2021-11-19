from django.db import models
from django.urls import reverse
class Category(models.Model):
    on_delete = models.CASCADE,
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])
    def __str__(self):
        return self.name
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='Продукты',on_delete = models.CASCADE )   # категория
    name = models.CharField(max_length=200, db_index=True) # Имя
    slug = models.SlugField(max_length=200, db_index=True) # Абсолютная урла
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    hover_image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)# картинка
    description = models.TextField(blank=True) # Описание
    price = models.DecimalField(max_digits=10, decimal_places=2) # цена
    stock = models.PositiveIntegerField() # остатки
    available = models.BooleanField(default=True) # доступность
    created = models.DateTimeField(auto_now_add=True) # дата создания
    updated = models.DateTimeField(auto_now=True)# дата обновления

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        verbose_name_plural = 'Продукты'

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])
    def __str__(self):
        return self.name