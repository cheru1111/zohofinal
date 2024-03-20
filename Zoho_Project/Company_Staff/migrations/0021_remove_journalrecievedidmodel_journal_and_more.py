# Generated by Django 4.2.8 on 2024-03-20 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0020_journalrecievedidmodel_journal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='journalrecievedidmodel',
            name='journal',
        ),
        migrations.AddField(
            model_name='journal',
            name='journal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.journalrecievedidmodel'),
        ),
    ]