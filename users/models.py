from django.db import models
from  PIL import Image
from django.contrib.auth.models import User
from django.db.models.signals import post_save  

# Create your models here.

class Profile(models.Model):
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    user = models.OneToOneField(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.user.username

    #reducing the image size
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)



#signals
def profile_create(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(profile_create, sender=User)


def save_profile(sender, instance, **kwargs):
    instance.profile.save()

post_save.connect(save_profile, sender=User)