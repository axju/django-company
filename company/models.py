from django.db import models
from django.urls import reverse


class Headline(models.Model):
    image = models.ImageField(upload_to='headline/')
    title = models.CharField(max_length=100)
    description = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-order']


class BasicImage(models.Model):
    image = models.ImageField(upload_to='features/')
    title = models.CharField(max_length=80, blank=True)
    description = models.CharField(max_length=250, blank=True)
    main = models.BooleanField(default=False)
    jumbotron = models.BooleanField(default=False)
    gallery = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Feature(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    text = models.TextField()
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['-order']

    def __str__(self):
        return self.title

    def image(self):
        image = self.images.filter(main=True).first()
        if not image: image = self.images.first()
        if image:
            return image.image
        return None

    def get_detail_url(self):
       return reverse('company:feature-detail', args=(self.pk,))


class FeatureImage(BasicImage):
    feature = models.ForeignKey(Feature, on_delete=models.CASCADE, related_name='images')


class Value(models.Model):
    VALUE_KIND = (
        ('text', 'Text'),
        ('date', 'Datum'),
        ('choices', 'Choices'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    kind = models.CharField(max_length=8, choices=VALUE_KIND, default='text')

    def __str__(self):
        return self.title


class Product(models.Model):
    PRODUCT_KIND = (
        ('misc', 'Sonstiges'),
        ('seminar', 'Seminar'),
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    text = models.TextField()
    feature = models.ManyToManyField(Feature, related_name='products')
    price = models.FloatField(null=True, blank=True)

    kind = models.CharField(max_length=8, choices=PRODUCT_KIND, default='seminar')

    def __str__(self):
        return self.title

    def get_detail_url(self):
        return reverse('company:product-detail', args=(self.pk,))

    def image(self):
        image = self.images.filter(main=True).first()
        if not image: image = self.images.first()
        if image:
            return image.image
        return None

class ProductImage(BasicImage):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    

class ProductOption(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='options')
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)


class ProductDate(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='dates')
    date = models.DateField()
    description = models.TextField(null=True, blank=True)


class ProductValue(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='values')
    value = models.ForeignKey(Value, on_delete=models.CASCADE, related_name='+')
    order = models.IntegerField(default=0)
    required = models.BooleanField(default=True)

    class Meta:
        ordering = ['-order']


class Request(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='requests')
    create_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField(null=True, blank=True)


class RequestOption(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='options')
    option = models.ForeignKey(ProductOption, on_delete=models.CASCADE, related_name='+')


class RequestValue(models.Model):
    request = models.ForeignKey(Request, on_delete=models.CASCADE, related_name='values')
    source = models.ForeignKey(ProductValue, on_delete=models.CASCADE, related_name='+')
    value = models.CharField(max_length=100)
