from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
<<<<<<< HEAD
=======
from django.urls import reverse
>>>>>>> a77da727686d4a6b25a679b34e59940ff89634d0


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    date_of_action = models.DateTimeField(default=timezone.now)
    cities = [
    ('SOFIA', 'Sofia'),
<<<<<<< HEAD
    ]
    main_city = models.CharField(
=======
    ('BURGAS', 'Burgas'),
    ('PLOVDIV', 'Plovdiv'),
    ('VARNA', 'Varna'),
    ('RUSE', 'Ruse'),
    ]
    city = models.CharField(
>>>>>>> a77da727686d4a6b25a679b34e59940ff89634d0
        max_length=10,
        choices=cities,
        default='SOFIA',
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
<<<<<<< HEAD
=======

    def get_absolute_url(self):
        return reverse('article-detail',kwargs={'pk':self.pk})
>>>>>>> a77da727686d4a6b25a679b34e59940ff89634d0
