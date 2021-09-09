# Generated by Django 3.2.5 on 2021-09-08 14:36

import autoslug.fields
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60, unique_for_month='pub_date')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='title')),
                ('article', models.TextField()),
                ('share', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('views', models.IntegerField(validators=[django.core.validators.MinValueValidator(0)])),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='writer', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]