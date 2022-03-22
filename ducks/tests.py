from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import DuckModel

class TestDuck(TestCase):

  @classmethod
  def setUpTest(cls):
    user = get_user_model().objects.create_user(username='tester', password='pass')
    user.save()

    duck = DuckModel.objects.create(name='McQuack', owner=user, description='a duck', age=5, species='Magpie')
    duck.save()

  def test_duck_model(self):
    duck = DuckModel.objects.get(id=1)
    # owner = str(duck.owner)
    name = str(duck.name)
    description = duck.description
    age = duck.age

    # self.assertEqual(owner, 'tester')
    self.assertEqual(name, 'McQuack')
    self.assertEqual(description, 'a duck')
    self.assertEqual(age, 5)
