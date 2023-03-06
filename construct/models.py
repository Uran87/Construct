from django.db import models
from django.urls import reverse
import datetime

# Create your models here.
from django.utils import timezone


class Fence(models.Model):
    fence_text_description = models.TextField()
    fence_name = models.TextField()
    fence_picture = models.ImageField(upload_to='fences')
    fence_slug = models.CharField(max_length=55)
    def __str__(self):
        return self.fence_name





class Requests(models.Model):
    name_customer = models.CharField(max_length=100, verbose_name='Имя клиента')
    text_request = models.TextField(verbose_name='Комментарий')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона')
    request_data = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name_customer +"   "+ self.phone_number




class Cities(models.Model):
    city_name = models.CharField(max_length=250)
    city_name_rod = models.CharField(max_length=250)

    slug_city = models.SlugField(max_length=250, verbose_name='url', unique=True)

    """def get_absolute_url(self):
        return reverse("fences", kwargs={"slug": self.slug_city})"""



class Video(models.Model):
    video_title = models.TextField()
    video_describe = models.TextField()
    video_path = models.TextField()