# Generated by Django 3.0.6 on 2020-06-10 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_auto_20200610_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='agenda.Tipo'),
        ),
    ]
