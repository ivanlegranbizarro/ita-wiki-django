# Generated by Django 4.1.7 on 2023-03-28 13:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Categoría',
                'verbose_name_plural': 'Categorías',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Tema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.ManyToManyField(related_name='tema_categories', to='wiki.category')),
            ],
        ),
        migrations.CreateModel(
            name='Wiki',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('url', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_wikis', to='wiki.category')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_wikis', to=settings.AUTH_USER_MODEL)),
                ('tema', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tema_wikis', to='wiki.tema')),
            ],
            options={
                'verbose_name': 'Recurso',
                'verbose_name_plural': 'Recursos',
                'ordering': ['title'],
            },
        ),
    ]
