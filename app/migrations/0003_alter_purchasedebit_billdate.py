# Generated by Django 4.2.6 on 2024-04-27 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_history_date_alter_purchasedebit_billdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasedebit',
            name='billdate',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
