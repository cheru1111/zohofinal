# Generated by Django 4.2.8 on 2024-02-17 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0001_initial'),
        ('Company_Staff', '0008_alter_journaltransactionhistory_company_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalcomment',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.staffdetails'),
        ),
    ]
