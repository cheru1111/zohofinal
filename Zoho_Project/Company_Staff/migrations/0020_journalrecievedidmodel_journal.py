# Generated by Django 4.2.8 on 2024-03-20 05:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Company_Staff', '0019_vendor_vendorhistory_vendorcontactperson_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalrecievedidmodel',
            name='journal',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.journal'),
        ),
    ]