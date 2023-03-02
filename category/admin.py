from django.contrib import admin
from .models import Category

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('category_name',)}
	list_display = ('category_name', 'slug')
	##keywords = {'slug':('category_name')}
admin.site.register(Category, CategoryAdmin)
