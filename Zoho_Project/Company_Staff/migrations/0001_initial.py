# Generated by Django 4.2.8 on 2024-02-09 08:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Register_Login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bnk_name', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('bnk_branch', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('bnk_acno', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('bnk_ifsc', models.CharField(blank=True, default='', max_length=220, null=True)),
                ('bnk_bal_type', models.CharField(choices=[('Credit', 'Credit'), ('Debit', 'Debit')], default='Debit', max_length=220)),
                ('bnk_opnbal', models.FloatField(blank=True, null=True)),
                ('bnk_bal', models.FloatField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('document', models.FileField(blank=True, null=True, upload_to='bank/')),
                ('status', models.TextField(default='Active')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='BankTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trans_cur_amount', models.FloatField(blank=True, null=True)),
                ('trans_amount', models.FloatField(blank=True, null=True)),
                ('trans_adj_amount', models.FloatField(blank=True, null=True)),
                ('trans_adj_date', models.DateField(blank=True, null=True)),
                ('trans_type', models.CharField(choices=[('Opening Balance', 'Opening Balance'), ('Bank to Bank', 'Bank to Bank'), ('Bank to Cash', 'Bank to Cash'), ('Cash to Bank', 'Cash to Bank'), ('Bank Adjustment', 'Bank Adjustment')], max_length=220)),
                ('trans_adj_type', models.CharField(choices=[('', ''), ('Balance Increase', 'Balance Increase'), ('Balance Decrease', 'Balance Decrease')], max_length=220)),
                ('trans_desc', models.CharField(blank=True, max_length=220, null=True)),
                ('bank_to_bank_no', models.PositiveIntegerField(blank=True, null=True)),
                ('banking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.banking')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='Bloodgroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Blood_group', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Chart_of_Accounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(blank=True, max_length=255, null=True)),
                ('account_name', models.CharField(blank=True, max_length=255, null=True)),
                ('account_description', models.CharField(blank=True, max_length=255, null=True)),
                ('account_number', models.CharField(blank=True, max_length=255, null=True)),
                ('account_code', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(blank=True, default='Active', max_length=255, null=True)),
                ('Create_status', models.CharField(blank=True, default='added', max_length=255, null=True)),
                ('sub_account', models.CharField(blank=True, max_length=255, null=True)),
                ('parent_account', models.CharField(blank=True, max_length=255, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='Company_Payment_Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('term_name', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('days', models.IntegerField(default=0, null=True)),
                ('status', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_type', models.CharField(blank=True, max_length=220, null=True)),
                ('title', models.CharField(blank=True, max_length=220, null=True)),
                ('first_name', models.CharField(blank=True, max_length=220, null=True)),
                ('last_name', models.CharField(blank=True, max_length=220, null=True)),
                ('customer_display_name', models.CharField(blank=True, max_length=220, null=True)),
                ('company_name', models.CharField(blank=True, max_length=220, null=True)),
                ('customer_email', models.EmailField(max_length=255, null=True)),
                ('customer_phone', models.CharField(blank=True, max_length=220, null=True)),
                ('customer_mobile', models.CharField(blank=True, max_length=220, null=True)),
                ('skype', models.CharField(blank=True, max_length=220, null=True)),
                ('designation', models.CharField(blank=True, max_length=220, null=True)),
                ('department', models.CharField(blank=True, max_length=220, null=True)),
                ('website', models.CharField(blank=True, max_length=220, null=True)),
                ('GST_treatement', models.CharField(blank=True, max_length=220, null=True)),
                ('GST_number', models.CharField(blank=True, max_length=220, null=True)),
                ('PAN_number', models.CharField(blank=True, max_length=220, null=True)),
                ('place_of_supply', models.CharField(blank=True, max_length=220, null=True)),
                ('tax_preference', models.CharField(blank=True, max_length=220, null=True)),
                ('currency', models.CharField(blank=True, max_length=220, null=True)),
                ('opening_balance_type', models.CharField(blank=True, max_length=220, null=True)),
                ('opening_balance', models.FloatField(blank=True, null=True)),
                ('credit_limit', models.FloatField(blank=True, null=True)),
                ('price_list', models.CharField(blank=True, max_length=220, null=True)),
                ('portal_language', models.CharField(blank=True, max_length=220, null=True)),
                ('facebook', models.CharField(blank=True, max_length=220, null=True)),
                ('twitter', models.CharField(blank=True, max_length=220, null=True)),
                ('current_balance', models.FloatField(blank=True, null=True)),
                ('billing_attention', models.CharField(blank=True, max_length=220, null=True)),
                ('billing_address', models.CharField(blank=True, max_length=220, null=True)),
                ('billing_city', models.CharField(blank=True, max_length=220, null=True)),
                ('billing_state', models.CharField(blank=True, max_length=220, null=True)),
                ('billing_country', models.CharField(blank=True, max_length=220, null=True)),
                ('billing_pincode', models.CharField(blank=True, max_length=220, null=True)),
                ('billing_mobile', models.CharField(blank=True, max_length=220, null=True)),
                ('billing_fax', models.CharField(blank=True, max_length=220, null=True)),
                ('shipping_attention', models.CharField(blank=True, max_length=220, null=True)),
                ('shipping_address', models.CharField(blank=True, max_length=220, null=True)),
                ('shipping_city', models.CharField(blank=True, max_length=220, null=True)),
                ('shipping_state', models.CharField(blank=True, max_length=220, null=True)),
                ('shipping_country', models.CharField(blank=True, max_length=220, null=True)),
                ('shipping_pincode', models.CharField(blank=True, max_length=220, null=True)),
                ('shipping_mobile', models.CharField(blank=True, max_length=220, null=True)),
                ('shipping_fax', models.CharField(blank=True, max_length=220, null=True)),
                ('remarks', models.CharField(blank=True, max_length=220, null=True)),
                ('customer_status', models.CharField(blank=True, max_length=220, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('company_payment_terms', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.company_payment_term')),
                ('login_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_type', models.CharField(max_length=255)),
                ('item_name', models.CharField(max_length=255)),
                ('hsn_code', models.IntegerField(blank=True, null=True)),
                ('tax_reference', models.CharField(max_length=255, null=True)),
                ('intrastate_tax', models.IntegerField(blank=True, null=True)),
                ('interstate_tax', models.IntegerField(blank=True, null=True)),
                ('selling_price', models.IntegerField(blank=True, null=True)),
                ('sales_account', models.CharField(max_length=255)),
                ('sales_description', models.CharField(max_length=255)),
                ('purchase_price', models.IntegerField(blank=True, null=True)),
                ('purchase_account', models.CharField(max_length=255)),
                ('purchase_description', models.CharField(max_length=255)),
                ('minimum_stock_to_maintain', models.IntegerField(blank=True, null=True)),
                ('activation_tag', models.CharField(default='active', max_length=255)),
                ('inventory_account', models.CharField(max_length=255, null=True)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('opening_stock', models.IntegerField(blank=True, default=0, null=True)),
                ('current_stock', models.IntegerField(blank=True, default=0, null=True)),
                ('opening_stock_per_unit', models.IntegerField(blank=True, null=True)),
                ('type', models.CharField(blank=True, max_length=255, null=True)),
                ('track_inventory', models.IntegerField(blank=True, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='Journal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('journal_no', models.CharField(max_length=255, null=True)),
                ('reference_no', models.IntegerField(null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('currency', models.CharField(max_length=255, null=True)),
                ('journal_type', models.CharField(max_length=255, null=True)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='attachments/')),
                ('total_debit', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('total_credit', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('debit_difference', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('credit_difference', models.DecimalField(decimal_places=2, default=0, max_digits=10, null=True)),
                ('status', models.CharField(blank=True, choices=[('draft', 'Draft'), ('save', 'Save')], max_length=255, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
            ],
        ),
        migrations.CreateModel(
            name='JournalRecievedIdModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pattern', models.CharField(max_length=255, null=True)),
                ('ref_number', models.CharField(max_length=255, null=True)),
                ('jn_rec_number', models.CharField(max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='payroll_employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('alias', models.CharField(max_length=100, null=True)),
                ('image', models.ImageField(null=True, upload_to='image/')),
                ('joindate', models.DateField(null=True)),
                ('salary_type', models.CharField(default='Fixed', max_length=100, null=True)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('emp_number', models.CharField(max_length=100, null=True)),
                ('designation', models.CharField(max_length=100, null=True)),
                ('location', models.CharField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=100, null=True)),
                ('dob', models.DateField(null=True)),
                ('age', models.PositiveIntegerField(default=0)),
                ('blood', models.CharField(max_length=10, null=True)),
                ('parent', models.CharField(max_length=100, null=True)),
                ('spouse_name', models.CharField(max_length=100, null=True)),
                ('address', models.CharField(max_length=250, null=True)),
                ('permanent_address', models.CharField(max_length=250, null=True)),
                ('Phone', models.BigIntegerField(null=True)),
                ('emergency_phone', models.BigIntegerField(blank=True, default=1, null=True)),
                ('email', models.EmailField(max_length=255, null=True)),
                ('Income_tax_no', models.CharField(max_length=255, null=True)),
                ('Aadhar', models.CharField(default='', max_length=250, null=True)),
                ('UAN', models.CharField(max_length=255, null=True)),
                ('PFN', models.CharField(max_length=255, null=True)),
                ('PRAN', models.CharField(max_length=255, null=True)),
                ('status', models.CharField(default='Active', max_length=200, null=True)),
                ('isTDS', models.CharField(max_length=200, null=True)),
                ('TDS_percentage', models.IntegerField(default=0, null=True)),
                ('salaryrange', models.CharField(choices=[('1-10', '1-10'), ('10-15', '10-15'), ('15-31', '15-31')], default='1-10', max_length=10, null=True)),
                ('amountperhr', models.IntegerField(blank=True, default=0, null=True)),
                ('workhr', models.IntegerField(blank=True, default=0, null=True)),
                ('uploaded_file', models.FileField(null=True, upload_to='images/')),
                ('acc_no', models.CharField(max_length=255, null=True)),
                ('IFSC', models.CharField(max_length=100, null=True)),
                ('bank_name', models.CharField(max_length=100, null=True)),
                ('branch', models.CharField(max_length=100, null=True)),
                ('transaction_type', models.CharField(max_length=100, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='PriceList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('type', models.CharField(choices=[('Sales', 'Sales'), ('Purchase', 'Purchase')], max_length=10, null=True)),
                ('item_rate_type', models.CharField(choices=[('Percentage', 'Percentage'), ('Each Item', 'Each Item')], max_length=15, null=True)),
                ('description', models.TextField(null=True)),
                ('percentage_type', models.CharField(blank=True, choices=[('Markup', 'Markup'), ('Markdown', 'Markdown')], max_length=10, null=True)),
                ('percentage_value', models.IntegerField(blank=True, null=True)),
                ('round_off', models.CharField(choices=[('Never Mind', 'Never Mind'), ('Nearest Whole Number', 'Nearest Whole Number'), ('0.99', '0.99'), ('0.50', '0.50'), ('0.49', '0.49')], max_length=20, null=True)),
                ('currency', models.CharField(choices=[('Indian Rupee', 'Indian Rupee')], max_length=20, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], default='Active', max_length=10)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='price_list_attachment/')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_name', models.CharField(max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
            ],
        ),
        migrations.CreateModel(
            name='PriceListTransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('action', models.CharField(choices=[('Created', 'Created'), ('Edited', 'Edited')], max_length=10, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('price_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.pricelist')),
            ],
        ),
        migrations.CreateModel(
            name='PriceListItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standard_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('custom_rate', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.items')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('price_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.pricelist')),
            ],
        ),
        migrations.CreateModel(
            name='PriceListComment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date_added', models.DateField(auto_now_add=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('price_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.pricelist')),
            ],
        ),
        migrations.CreateModel(
            name='payroll_employee_comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255, null=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.payroll_employee')),
                ('login_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='JournalEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('contact', models.CharField(max_length=200, null=True)),
                ('debits', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('credits', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('journal', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.journal')),
                ('login', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='Items_comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, max_length=255, null=True)),
                ('Items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.items')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('logindetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.AddField(
            model_name='items',
            name='unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.unit'),
        ),
        migrations.CreateModel(
            name='Item_Transaction_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(null=True)),
                ('action', models.CharField(default='Created', max_length=255)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.items')),
                ('logindetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='employee_history',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(auto_now=True, null=True)),
                ('Action', models.CharField(max_length=255, null=True)),
                ('company', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.payroll_employee')),
                ('login_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action', models.CharField(blank=True, max_length=220, null=True)),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.customer')),
                ('login_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='CustomerContactPersons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=220, null=True)),
                ('first_name', models.CharField(blank=True, max_length=220, null=True)),
                ('last_name', models.CharField(blank=True, max_length=220, null=True)),
                ('email', models.EmailField(blank=True, max_length=220, null=True)),
                ('work_phone', models.CharField(blank=True, max_length=220, null=True)),
                ('mobile', models.CharField(blank=True, max_length=220, null=True)),
                ('skype', models.CharField(blank=True, max_length=220, null=True)),
                ('designation', models.CharField(blank=True, max_length=220, null=True)),
                ('department', models.CharField(blank=True, max_length=220, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.customer')),
                ('login_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='CompanyRepeatEvery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repeat_every', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('repeat_type', models.CharField(blank=True, default='', max_length=100, null=True)),
                ('duration', models.IntegerField(default=0, null=True)),
                ('days', models.IntegerField(default=0, null=True)),
                ('company', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
            ],
        ),
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.CharField(max_length=255, null=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.payroll_employee')),
                ('login_details', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='Chart_of_Accounts_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateField(null=True)),
                ('action', models.CharField(default='Created', max_length=255)),
                ('chart_of_accounts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.chart_of_accounts')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('logindetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='chart_of_accounts_comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.CharField(blank=True, max_length=255, null=True)),
                ('chart_of_accounts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.chart_of_accounts')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('logindetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
        migrations.CreateModel(
            name='BankTransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hist_cur_amount', models.FloatField(blank=True, null=True)),
                ('hist_amount', models.FloatField(blank=True, null=True)),
                ('hist_adj_amount', models.FloatField(blank=True, null=True)),
                ('hist_adj_date', models.DateField(auto_now_add=True, null=True)),
                ('hist_action', models.CharField(choices=[('Created', 'Created'), ('Updated', 'Updated')], max_length=220)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
                ('transaction', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.banktransaction')),
            ],
        ),
        migrations.CreateModel(
            name='BankingHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hist_adj_amount', models.FloatField(blank=True, null=True)),
                ('hist_adj_date', models.DateField(auto_now_add=True, null=True)),
                ('hist_action', models.CharField(choices=[('Created', 'Created'), ('Updated', 'Updated')], max_length=220)),
                ('banking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Company_Staff.banking')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Register_Login.companydetails')),
                ('login_details', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Register_Login.logindetails')),
            ],
        ),
    ]
