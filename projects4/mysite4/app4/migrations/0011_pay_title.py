# Generated by Django 4.2.6 on 2023-11-17 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app4', '0010_remove_pay_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='pay',
            name='title',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='app4.food'),
            preserve_default=False,
        ),
    ]