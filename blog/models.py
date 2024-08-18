from django.db import models
from django.utils.text import slugify
# from taggit.managers import TaggableManager


class PublishManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class TotalPostManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().count()


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique_for_date='publish')
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    publish = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(to=Author, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)
    # tags = TaggableManager()

    # custom manger
    objects = models.Manager()  # default manager
    published = PublishManager()  # custom manager
    total_posts = TotalPostManager()  # custom manager

    def __str__(self):
        return self.title

    def get_post_title(self):
        return self.title

    def get_post_content(self):
        return self.content

    class Meta:
        ordering = ('-created',)

    def save(self, *args, **kwargs):
        slug = slugify(self.title)
        self.slug = slug
        super().save(*args, **kwargs)

    @classmethod
    def get_total_posts(cls):
        return cls.objects.count()

    @classmethod
    def get_latest_post(cls):
        return cls.objects.latest('-publish')


class Comment(models.Model):
    """

    """
    post = models.ForeignKey(to=Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.content

    class Meta:
        ordering = ('-created',)
        indexes = [
            models.Index(fields=['created', 'active']),
        ]
