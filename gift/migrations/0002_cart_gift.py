# Generated by Django 4.1.1 on 2022-09-05 08:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gift', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='gift',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='giftt', to='gift.gift'),
        ),
    ]
