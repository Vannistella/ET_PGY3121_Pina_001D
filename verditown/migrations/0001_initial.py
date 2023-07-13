# Generated by Django 4.2.2 on 2023-06-18 00:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Categoria')),
                ('nombreCategoria', models.CharField(blank=True, max_length=50, verbose_name='Nombre de Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('sku', models.IntegerField(max_length=8, primary_key=True, serialize=False, verbose_name='SKU')),
                ('nombre', models.CharField(blank=True, max_length=20, verbose_name='Nombre')),
                ('descrip', models.CharField(blank=True, max_length=50, verbose_name='Descripcion')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='imagenes', verbose_name='Imagen')),
                ('precio', models.IntegerField(blank=True, max_length=8, verbose_name='Precio')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='verditown.categoria', verbose_name='Categoria')),
            ],
        ),
    ]
