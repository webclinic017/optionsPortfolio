# Generated by Django 3.2.4 on 2021-06-27 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('optionsPF', '0017_butterflyspread_collapsible_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='butterflyspread',
            name='collapsible_tag',
            field=models.CharField(max_length=40),
        ),
    ]
