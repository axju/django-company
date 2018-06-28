from django.db import models

PORTFOLIO_CATEGORY = (
    ('headline', 'Headline'),
    ('feature', 'Feature'),
)

POST_CATEGORY = (
    ('article', 'article'),
    ('news', 'news'),
)

class Post(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=POST_CATEGORY,default='article')
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-create_at']

    def __str__(self):
        return self.title

class PostImage(models.Model):
    info = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='post/')
    title = models.CharField(max_length=80, blank=True)
    description = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.title


class Portfolio(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=PORTFOLIO_CATEGORY)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/', default=None, null=True, blank=True)
    info = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='portfolios', null=True, blank=True)

    def __str__(self):
        return self.title
