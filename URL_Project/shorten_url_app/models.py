from django.db import models

# URL object (model) for storing info on users' URLs
class URL(models.Model):
    #specify fields (primary key by default, autoincremented)
    url_text = models.CharField(max_length=300)
    short_url_text = models.CharField(max_length=100, default=None)
    pub_date = models.DateTimeField('Date published')

    def __str__(self):   #to display text value
        return self.url_text