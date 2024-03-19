# Generated by Django 4.2.8 on 2024-03-19 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Register_Login', '0001_initial'),
        ('Company_Staff', '0018_alter_journal_attachment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('vendor_display_name', models.CharField(blank=True, max_length=255, null=True)),
                ('vendor_email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(default='', max_length=15)),
                ('phone', models.CharField(default='', max_length=15)),
                ('company_name', models.CharField(blank=True, max_length=255, null=True)),
                ('skype_name_number', models.CharField(blank=True, max_length=255, null=True)),
                ('designation', models.CharField(blank=True, max_length=255, null=True)),
                ('department', models.CharField(blank=True, max_length=255, null=True)),
                ('website', models.URLField(blank=True, default='', null=True)),
                ('gst_treatment', models.CharField(blank=True, max_length=255, null=True)),
                ('gst_number', models.CharField(blank=True, max_length=20, null=True)),
                ('pan_number', models.CharField(blank=True, max_length=20, null=True)),
                ('currency', models.CharField(blank=True, max_length=255, null=True)),
                ('opening_balance_type', models.CharField(blank=True, max_length=255, null=True)),
                ('opening_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('current_balance', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('credit_limit', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
                ('source_of_supply', models.CharField(blank=True, max_length=255, null=True)),
                ('billing_attention', models.CharField(blank=True, max_length=255, null=True)),
                ('billing_address', models.TextField(blank=True, null=True)),
                ('billing_city', models.CharField(blank=True, max_length=255, null=True)),
                ('billing_state', models.CharField(blank=True, max_length=255, null=True)),
                ('billing_country', models.CharField(blank=True, max_length=255, null=True)),
                ('billing_pin_code', models.CharField(blank=True, max_length=10, null=True)),
                ('billing_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('billing_fax', models.CharField(blank=True, max_length=15, null=True)),
                ('shipping_attention', models.CharField(blank=True, max_length=255, null=True)),
                ('shipping_address', models.TextField(blank=True, null=True)),
                ('shipping_city', models.CharField(blank=True, max_length=255, null=True)),
                ('shipping_state', models.CharField(blank=True, max_length=255, null=True)),
                ('shipping_country', models.CharField(blank=True, max_length=255, null=True)),
                ('shipping_pin_code', models.CharField(blank=True, max_length=10, null=True)),
                ('shipping_phone', models.CharField(blank=True, max_length=15, null=True)),
                ('shipping_fax', models.CharField(blank=True, max_length=15, null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('vendor_status', models.CharField(blank=True, max_length=10, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('payment_term', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Company_Staff.company_payment_term')),
            ],
        ),
        migrations.CreateModel(
            name='VendorHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('action', models.CharField(blank=True, max_length=200, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='VendorContactPerson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('work_phone', models.CharField(max_length=15)),
                ('mobile', models.CharField(max_length=15)),
                ('skype_name_number', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('vendor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor_remarks_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remarks', models.CharField(max_length=500)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor_mail_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail_from', models.TextField(max_length=300)),
                ('mail_to', models.TextField(max_length=300)),
                ('subject', models.TextField(max_length=250)),
                ('content', models.TextField(max_length=900)),
                ('mail_date', models.DateTimeField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor_doc_upload_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=200)),
                ('document', models.FileField(upload_to='doc/')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.vendor')),
            ],
        ),
        migrations.CreateModel(
            name='Vendor_comments_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('vendor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.vendor')),
            ],
        ),
    ]