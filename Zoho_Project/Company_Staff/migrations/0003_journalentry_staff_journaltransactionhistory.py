# Generated by Django 4.2.8 on 2024-02-14 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0001_initial'),
        ('Company_Staff', '0002_journal_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='journalentry',
            name='staff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.staffdetails'),
        ),
        migrations.CreateModel(
            name='JournalTransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('action', models.CharField(choices=[('Created', 'Created'), ('Edited', 'Edited')], max_length=10, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('journal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.journalentry')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.staffdetails')),
            ],
        ),
    ]
