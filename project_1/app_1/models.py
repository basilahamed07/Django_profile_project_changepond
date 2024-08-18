from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
# in this project we have three class and names are (introduction), (posts), (about)

class Introduction(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    degree = models.CharField(max_length=20)
    certification = models.TextField()
    #profile_pic = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    full_name = models.CharField(max_length=100, editable=False)
    
    #creating the full name
    def save(self,*args, **kwargs):
        self.full_name = f"{self.first_name} {self.last_name}"
        super().save(*args,**kwargs)

    #returning the full name 
    def __str__(self):
        return f"{self.full_name} data inserted :)"

class Posts(models.Model):
    # post_pics = models.ImageField(_(""), upload_to=None, height_field=None, width_field=None, max_length=None)
    title = models.CharField(max_length=50)
    description  = models.TextField(default="don't have the description ", null=True)
    day = models.DateField()
    time = models.TimeField()
    starts = models.FloatField()
    slug = models.SlugField(default="", editable=False)

    # creating the slug
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    def __str__(self) :
        return f"{self.title} is inserted in time of {self.time}"
    

class About(models.Model):

    services_list = (
        ("cybersecurity", "cybersecurity"),
        ("clousaecurity", "clousaecurity"),
        ("pentesting", "pentesting"),
        ("hacking", "hacking"),
    ) 

    name = models.CharField(max_length=100)
    phone = models.IntegerField(null=False, blank=False, unique=True)
    services = models.CharField(choices=services_list, default="hacking", max_length=100)

    def __str__(self) :
        return f"thankyou {self.name} contact you shortly"