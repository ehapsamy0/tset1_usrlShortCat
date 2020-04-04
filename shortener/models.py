from django.db import models
from .utils import code_generator, create_shortcode
from django.conf import settings

# Create your models here.


SHORTCODE_MAX = getattr(settings,"SHORTCODE_MAX",15)
#           OR
#SHORTCODE_MAX = settings.SHORTCODE_MAX


class KirrURLManager(models.Manager):
    def all(self,*args,**kwargs):
        qs_main = super(KirrURLManager,self).all(*args,**kwargs)
        qs = qs_main.filter(active=True)
        return qs
    def refresh_shortcode(self,items=None):
        qs = KirrURL.objects.filter(id__gte=1)
        if items is not None and isinstance(items,int):
            qs = qs.order_by('-id')[:items]
        new_code = 0
        for q in qs:
            q.shortcode = create_shortcode(q)
            q.save()
            new_code += 1
            return "new_code made: {i}".format(i=new_code)

class KirrURL(models.Model):
    url = models.CharField(max_length=222,)
    shortcode = models.CharField(max_length=SHORTCODE_MAX,unique=True,blank=True)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    #empty_datetime = models.DateTimeField(auto_now=True)
    #shortcode = models.CharField(max_length=220,null=True)
    #shortcode = models.CharField(max_length=220,default = 'cfeddulteshortcode')

    objects = KirrURLManager()
    same_random = KirrURLManager()
    def save(self,*args,**kwargs):
        if self.shortcode is None or self.shortcode =="":
            self.shortcode = code_generator()
        super(KirrURL,self).save(*args,**kwargs)

    #class Meta:
    #    ordering = '-id'


    #def my_save(self):
    #    self.save()

    def __str__(self):
        return str(self.url)
    ''' here if you use python 2
    def __unicode__(self):
        return str(self.url)
    
    '''