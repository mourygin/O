from django.db import models

# Create your models here.
class Stanza(models.Model):
    stanza_nr = models.IntegerField()
    stanza_rn = models.CharField(max_length=16, default='', null=True, blank=True)
    stanza_tx = models.TextField(default='', null=True, blank=True)
    pic_file = models.CharField(max_length=128, default='', null=True, blank=True)
    pic_h = models.IntegerField(default=0)
    pic_v = models.IntegerField(default=0)
