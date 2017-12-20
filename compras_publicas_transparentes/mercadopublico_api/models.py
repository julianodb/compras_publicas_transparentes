from django.db import models

# Create your models here.
class CompraPublica(models.Model):
    name = models.CharField(max_length=200)
#    pub_date = models.DateTimeField('date published')
#
#    def was_published_recently(self):
#        now = timezone.now()
#        return now - datetime.timedelta(days=1) <= self.pub_date <= now
#
#    def __str__(self):
#        return self.question_text

