# Generated by Django 4.2.2 on 2023-06-23 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citasmd', '0002_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_paciente', models.IntegerField(null=True)),
                ('Pac_nomb', models.CharField(max_length=20, null=True)),
                ('Pac_Apellido', models.CharField(max_length=20, null=True)),
                ('Pac_edad', models.IntegerField(null=True)),
                ('correo', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
