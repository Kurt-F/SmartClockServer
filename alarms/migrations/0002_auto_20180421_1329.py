# Generated by Django 2.0.4 on 2018-04-21 17:29

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('alarms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='alarm',
            name='date',
        ),
        migrations.RemoveField(
            model_name='alarm',
            name='repeat',
        ),
        migrations.AddField(
            model_name='alarm',
            name='friRepeat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='alarm',
            name='monRepeat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='alarm',
            name='satRepeat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='alarm',
            name='sunRepeat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='alarm',
            name='thuRepeat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='alarm',
            name='time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='alarm',
            name='tueRepeat',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='alarm',
            name='wedRepeat',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='alarm',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='alarms.Profile'),
        ),
    ]