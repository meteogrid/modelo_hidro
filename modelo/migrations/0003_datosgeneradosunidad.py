# Generated by Django 2.1.4 on 2018-12-13 16:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0002_calculomodelo_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatosGeneradosUnidad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField()),
                ('Pcp', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Etp', models.DecimalField(decimal_places=2, max_digits=6)),
                ('Unidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='modelo.UnidadHidrologica')),
            ],
        ),
    ]
