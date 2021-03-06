# Generated by Django 4.0.3 on 2022-03-19 23:09

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DuckModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(default='')),
                ('species', models.CharField(choices=[('Indian Runner Duck', 'Indian Runner'), ('Mallard Duck', 'Mallard'), ('Pekin Duck', 'Pekin'), ('Khaki Campbell', 'Khaki Campbell'), ('Buff', 'Buff'), ('Magpie', 'Magpie')], max_length=60)),
                ('age', models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(20), django.core.validators.MinValueValidator(1)])),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
