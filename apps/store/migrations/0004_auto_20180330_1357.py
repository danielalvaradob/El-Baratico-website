# Generated by Django 2.0.3 on 2018-03-30 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20180330_1604'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'ordering': ('descripcion',), 'verbose_name': 'categoria', 'verbose_name_plural': 'categorias'},
        ),
        migrations.AlterModelOptions(
            name='producto',
            options={'ordering': ('-nombre',)},
        ),
        migrations.AddField(
            model_name='categoria',
            name='slug',
            field=models.SlugField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='slug',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='producto',
            name='stock',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='categoria',
            name='descripcion',
            field=models.CharField(db_index=True, max_length=100),
        ),
        migrations.AlterIndexTogether(
            name='producto',
            index_together={('id', 'slug')},
        ),
    ]