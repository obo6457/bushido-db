# Generated by Django 4.1.1 on 2023-05-31 18:25

from django.db import migrations, models
import shortuuid.main


class Migration(migrations.Migration):

    dependencies = [
        ('bushido', '0034_alter_list_id_delete_unitfeat'),
    ]

    operations = [
        migrations.AddField(
            model_name='listunit',
            name='enhancements',
            field=models.ManyToManyField(to='bushido.enhancement'),
        ),
        migrations.AlterField(
            model_name='list',
            name='id',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, editable=False, max_length=20, primary_key=True, serialize=False, unique=True),
        ),
    ]
