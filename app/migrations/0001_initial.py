# Generated by Django 4.0.4 on 2022-05-15 22:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_producto', models.CharField(max_length=20)),
                ('precio_producto', models.IntegerField()),
                ('imagen_producto', models.ImageField(null=True, upload_to='Carrito')),
            ],
            options={
                'db_table': 'db_Carrito',
            },
        ),
        migrations.CreateModel(
            name='Comuna',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('comuna', models.CharField(max_length=25)),
            ],
            options={
                'db_table': 'db_comuna',
            },
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_productos', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'db_tipo_producto',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('descripcion', models.CharField(max_length=40)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('create_at', models.DateField(auto_now_add=True)),
                ('update_at', models.DateField(auto_now=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipoproducto')),
            ],
            options={
                'db_table': 'db_producto',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('rut', models.CharField(max_length=30)),
                ('correo', models.CharField(max_length=30)),
                ('numero', models.CharField(max_length=30)),
                ('direccion', models.CharField(max_length=30)),
                ('comuna', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.comuna')),
            ],
            options={
                'db_table': 'db_cliente',
            },
        ),
    ]
