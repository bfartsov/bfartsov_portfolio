from django.db import models
from PIL import Image


class Banner(models.Model):
    img = models.ImageField(upload_to="photos/%Y/%m/%d/")
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class About(models.Model):
    farts_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)

    title = models.CharField(max_length=200)
    about = models.TextField(max_length=255)
    img = models.ImageField(upload_to='photos/about/%Y/%m/%d')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.img.path)
        output_size = (960, 960)
        resized_image = image.resize(output_size)
        resized_image.save(self.img.path)
        super().save(*args, **kwargs)


class Skill_Section(models.Model):
    title = models.CharField(max_length=150)
    sub_title = models.CharField(max_length=150)
    skills = models.ManyToManyField('Skill')

    def __str__(self):
        return self.title


class Skill(models.Model):
    skill = models.CharField(max_length=150)
    prosent = models.IntegerField()

    def __str__(self):
        return self.skill


class PortFolio(models.Model):
    title = models.CharField(max_length=150)
    img = models.ImageField(upload_to='photos/portfolio/%Y/%m/%d')
    thumb = models.ImageField(upload_to='photos/portfolio/%Y/%m/%d')
    about = models.TextField(max_length=255)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title
