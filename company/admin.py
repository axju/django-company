from django.contrib import admin

from company.models import Headline, Value, Feature, FeatureImage, Product, ProductImage, ProductDate, ProductOption, ProductValue, Request, RequestValue


class FeatureImageInline(admin.TabularInline):
    model = FeatureImage
    extra = 1

#class FeatureProductInline(admin.TabularInline):
#    model = Product.feature.through
#
#class FeatureAdmin(admin.ModelAdmin):
#    inlines = [FeatureImageInline, FeatureProductInline]
class FeatureAdmin(admin.ModelAdmin):
    inlines = [FeatureImageInline]
    list_display = ('title', 'count_products')
    filter_horizontal = ('products',)

    def count_products(self, obj):
        return obj.products.all().count()
    count_products.short_description = 'products'


class ProductValueInline(admin.TabularInline):
    model = ProductValue
    extra = 1
    ordering = ('-order',)

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

class ProductDateInline(admin.TabularInline):
    model = ProductDate
    extra = 1

class ProductOptionInline(admin.TabularInline):
    model = ProductOption
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, ProductDateInline, ProductOptionInline, ProductValueInline]
    filter_horizontal = ('feature',)


class RequestValueInline(admin.TabularInline):
    model = RequestValue
    extra = 0

class RequestAdmin(admin.ModelAdmin):
    inlines = [RequestValueInline]
    list_display = ('name', 'email', 'date', 'count_values')

    def count_values(self, obj):
        return obj.values.all().count()
    count_values.short_description = 'values'

admin.site.register(Headline)
admin.site.register(Value)
admin.site.register(Request, RequestAdmin)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(Product, ProductAdmin)
