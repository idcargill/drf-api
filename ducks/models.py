from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

class Species(models.TextChoices):
  INDIAN_RUNNER   = 'Indian Runner Duck'
  MALLARD         = 'Mallard Duck'
  PEKIN           = 'Pekin Duck'
  KHAKI_CAMPBELL  = 'Khaki Campbell'
  BUFF            = 'Buff'
  MAGPIE          = 'Magpie'

class DuckModel(models.Model):
  owner           = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
  name            = models.CharField(max_length=30)
  description     = models.TextField(default='')
  species         = models.CharField(choices=Species.choices, max_length=60)
  age             = models.IntegerField(default=1, validators=[MaxValueValidator(20), MinValueValidator(1)])

  
  def __str__(self):
    return f'{self.id} {self.species} {self.name}    Owner: {self.owner}'


