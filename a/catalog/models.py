from django.db import models

class Rubrics(models.Model):
    name = models.CharField('Рубрики', max_length=1000)
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField('Страна', max_length=1000)
    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField('Регион', max_length=1000)
    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField('Город', max_length=1000)
    def __str__(self):
        return self.name

# Create your models here.
class Company(models.Model):
    rubrics = models.ManyToManyField(Rubrics, blank=True)
    country = models.ForeignKey(Country, null=True, blank=True, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.CASCADE)
    city = models.ForeignKey(City, null=True, blank=True, on_delete=models.CASCADE)
    org_name = models.CharField('Название', max_length=1000, null=True, blank=True)
    address_name = models.CharField('Адрес', max_length=1000, null=True, blank=True)
    address_comment = models.CharField('Адрес коммент', max_length=1000, null=True, blank=True)
    contact_groups_contacts1_text1 = models.CharField('Контакт', max_length=1000, null=True, blank=True)
    contact_groups_contacts1_text2 = models.CharField('Контакт', max_length=1000, null=True, blank=True)
    contact_groups_contacts1_text3 = models.CharField('Контакт', max_length=1000, null=True, blank=True)
    contact_groups_contacts2_text1 = models.CharField('Контакт', max_length=1000, null=True, blank=True)
    contact_groups_contacts2_text2 = models.CharField('Контакт', max_length=1000, null=True, blank=True)
    contact_groups_contacts2_text3 = models.CharField('Контакт', max_length=1000, null=True, blank=True)
    ads_article = models.CharField('Инфо', max_length=1000, null=True, blank=True)
    article_warning = models.CharField('Доп инфо', max_length=1000, null=True, blank=True)
    def __str__(self):
        return self.org_name

class Comment(models.Model):
    company = models.ForeignKey('Company', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=255)
    content = models.TextField()
    is_positive = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)