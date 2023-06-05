# Generated by Django 4.1.1 on 2022-10-12 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bushido', '0011_unit_kifeats'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='UnitTrait',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('X', models.CharField(default='0', max_length=3)),
                ('Y', models.CharField(default='0', max_length=3)),
                ('descriptor', models.CharField(default='', max_length=10)),
                ('trait', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bushido.trait')),
                ('unit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bushido.unit')),
            ],
        ),
        migrations.AddField(
            model_name='unit',
            name='traits',
            field=models.ManyToManyField(through='bushido.UnitTrait', to='bushido.trait'),
        ),
    ]