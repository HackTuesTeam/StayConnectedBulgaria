from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_of_action = models.DateTimeField(default=timezone.now)
    cities = [
    ('SOFIA', 'Sofia'),
    ]
    main_city = models.CharField(
        max_length=10,
        choices=cities,
        default='SOFIA',
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
