from django.db import models
from django.urls import reverse

class Category(models.Model):
	category_name = models.CharField(max_length=50, unique=True)
	category_sex = models.CharField(max_length=10)
	slug = models.SlugField(max_length=100, unique=True)
	description = models.TextField(max_length=240, blank=True)
	cat_image = models.ImageField(upload_to='photos/categories', blank = True)
	price = models.DecimalField(max_digits=10, decimal_places=2)

	class Meta:
		verbose_name = 'category'
		verbose_name_plural = 'categories'

	def get_url(self): 
			return reverse('products_by_category', args=[self.slug])

	def __str__(self):
		return self.category_name