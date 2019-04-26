from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField( max_length=150)
    publication_date = models.DateField("Date")
    body_text = models.TextField(("input text"))
    image = models.ImageField(("image input"), upload_to='images/', height_field=None, width_field=None, max_length=None)


    def summary(self):
        return self.body_text[:150]