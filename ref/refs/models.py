from django.db import models

# Create your models here.
class Color(models.Model):

    color_text = models.CharField(max_length=50)

    def __str__(self):
        return self.color_text
    

class  Ref(models.Model):

    STATUS = (
        ('ativa', 'Ativa'),
        ('desativada', 'Desativada'),
    )

    reference = models.CharField(max_length=20)
    description = models.TextField()
    color_text = models.ForeignKey(Color, on_delete=models.CASCADE)
    status = models.CharField(
        max_length=10,
        choices=STATUS,
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.reference
