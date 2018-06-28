from django.contrib import admin

from company.models import Portfolio, Post, PostImage

class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 1

class PostAdmin(admin.ModelAdmin):
    inlines = [PostImageInline]
    list_display = ('title', 'category')

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'image')

admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(Post, PostAdmin)
