from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cities = [
    ('SOFIA', 'Sofia'),
    ('BURGAS', 'Burgas'),
    ('PLOVDIV', 'Plovdiv'),
    ('VARNA', 'Varna'),
    ('RUSE', 'Ruse'),
    ]
    content = models.TextField(default="just user")
    main_city = models.CharField(
        max_length=10,
        choices=cities,
        default='SOFIA',
    )

    image = models.ImageField(default='profile_pics/default.png', upload_to='profile_pics')
    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
