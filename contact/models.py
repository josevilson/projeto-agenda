from django.db import models
from django.utils import timezone

# Create your models here.
# first_name (string), last_name(string
# email (email) created_date(date), description (text)

# ----
# category (foreign key), show (boolean), owner(foreign key))
# picture (image)
# CASCATE DELETA TODAS OS CONTATOS LINKADOS EM CATEGORY
# SET_NULL DEIXA EM BRANCO


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'


class Contact(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, blank=True)
    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
