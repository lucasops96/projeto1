from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey 

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    # Aqui começam os campos para a relação genérica
    # Representa o model que queremos encaixar aqui
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    # Representa o id da linha do model descrito acima
    object_id = models.CharField()
    # Um campo que representa a relação genérica que conhece os
    # campos acima (content_type e object_id)
    content_object = GenericForeignKey('content_type','object_id')


