from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.TextField()
    content = models.TextField()

    
    def __str__(self):
        # if self.title:
        return str(self.id) +"_"+ self.title
        # else:
            # return self.id