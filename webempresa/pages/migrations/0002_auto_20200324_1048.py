# Generated by Django 3.0.4 on 2020-03-24 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='page',
            options={'ordering': ['order', 'title'], 'verbose_name': 'pagina', 'verbose_name_plural': 'paginas'},
        ),
        migrations.AddField(
            model_name='page',
            name='order',
            field=models.PositiveSmallIntegerField(default=0, verbose_name='Orden'),
        ),
    ]
