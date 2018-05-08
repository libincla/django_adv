from django.db import models

# Create your models here.

# publisher ==> chubanshe
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=60)
    website = models.URLField()
    
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']

class Author(models.Model):

    salutation = models.CharField(max_length=50)
    name = models.CharField(max_length=200, blank=True)
    email = models.EmailField()
    headshot = models.ImageField(upload_to='author_headshots', blank=True, null=True)

 
    def __str__(self):
        return self.name



# book manager



class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    authors = models.ManyToManyField('Author')
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True, null=True)
    num_pages = models.IntegerField(blank=True, null=True)
    #objects  = BookManager()``

    def __str__(self):
        return self.title




class MaleManager(models.Manager):
    def get_queryset(self):
        return super(MaleManager, self).get_queryset().filter(gender='M')

class FemaleManager(models.Manager):
    def get_queryset(self):
        return super(FemaleManager, self).get_queryset().filter(gender='F')

class Person(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices = (('M', 'Male'), ('F', 'Female')))
 
    people = models.Manager()
    men = MaleManager()
    women = FemaleManager()

    def __str__(self):
        return u'%s %s' % (self.first_name, self.last_name)

    def baby_boomer_status(self):
        import datetime
        if self.birth_date < datetime.date(1940, 1, 1):
            return 'pre-boomer'
        elif self.birth_date < datetime.date(1966, 1, 1):
            return 'heihei boomer'
        else:
            return 'post-boomer'
    def _get_full_name(self):
        return '%s %s' % (self.first_name, self.last_name)

    full_name = property(_get_full_name)


class Blog(models.Model):
    name = models.CharField(max_length=300)
    tagline = models.TextField()
 
    def save(self, *args, **kwargs):
        if self.name == 'libin':
            return
        else:
            super(Blog, self).save(*args, **kwargs)
    def __str__(self):
        return self.name
