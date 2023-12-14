# Generated by Django 4.2.5 on 2023-12-12 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ui', '0013_delete_data_delete_datatest_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
        migrations.AlterField(
            model_name='calculate_data',
            name='density',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='calculate_data',
            name='id_ig_ratio',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='calculate_data',
            name='nitrogen',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='calculate_data',
            name='oxygen',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='calculate_data',
            name='ph',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='calculate_data',
            name='predicted_value',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='calculate_data',
            name='ssa',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='calculate_data',
            name='sulphur',
            field=models.CharField(max_length=150),
        ),
    ]
