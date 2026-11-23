from django.contrib import admin
from .models import Category, Post
# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
	readonly_fields = ('created', 'updated')
	list_display = ('title','author', 'published', 'post_categories')
	ordering = ('author', 'published')
	search_fields = ('title', 'content', 'author__username', 'categories__title')
	date_hierarchy = 'published'
	list_filter = ('author__username', 'categories__title')

	def post_categories(self, obj):
		return ",".join([c.title for c in obj.categories.all().order_by("title")])
	post_categories.short_description = "Categorias"


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)	
