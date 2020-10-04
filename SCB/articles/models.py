from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_of_action = models.DateTimeField(default=timezone.now)
    cities = [
    ('SOFIA', 'Sofia'),
    ('BURGAS', 'Burgas'),
    ('PLOVDIV', 'Plovdiv'),
    ('VARNA', 'Varna'),
    ('RUSE', 'Ruse'),
    ]
    city = models.CharField(
        max_length=10,
        choices=cities,
        default='SOFIA',
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('article-detail',kwargs={'pk':self.pk})
