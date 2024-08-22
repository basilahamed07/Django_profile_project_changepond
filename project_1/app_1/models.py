from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
# in this project we have three class and names are (introduction), (posts), (about)

class Posts(models.Model):
    post_pics = models.ImageField(upload_to="posts", height_field=None, width_field=None, max_length=None)
    title = models.CharField(max_length=50)
    description  = models.TextField(default="don't have the description ", null=True)
    day = models.DateField()
    time = models.TimeField()
    likes = models.FloatField()
    slug = models.SlugField(default="", editable=False,db_index=True)

    # creating the slug
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self) :
        return f"{self.title} is inserted in time of {self.time}"


class feedback(models.Model):
    name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    message = models.TextField()
    
    def __str__(self):
        return f"{self.name} is added"