#zoho Final
from django.urls import path,re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.static import serve

urlpatterns = [
    # -------------------------------Company section--------------------------------
    path('Company/Dashboard',views.company_dashboard,name='company_dashboard'),
    path('Company/Staff-Request',views.company_staff_request,name='company_staff_request'),
    path('Company/Staff-Request/Accept/<int:pk>',views.staff_request_accept,name='staff_request_accept'),
    path('Company/Staff-Request/Reject/<int:pk>',views.staff_request_reject,name='staff_request_reject'),
    path('Company/All-Staffs',views.company_all_staff,name='company_all_staff'),
    path('Company/Staff-Approval/Cancel/<int:pk>',views.staff_approval_cancel,name='staff_approval_cancel'),
    path('Company/Profile',views.company_profile,name='company_profile'),
    path('Company/Profile-Editpage',views.company_profile_editpage,name='company_profile_editpage'),
    path('Company/Profile/Edit/Basicdetails',views.company_profile_basicdetails_edit,name='company_profile_basicdetails_edit'),
    path('Company/Password_Change',views.company_password_change,name='company_password_change'),
    path('Company/Profile/Edit/Companydetails',views.company_profile_companydetails_edit,name='company_profile_companydetails_edit'),
    path('Company/Module-Editpage',views.company_module_editpage,name='company_module_editpage'),
    path('Company/Module-Edit',views.company_module_edit,name='company_module_edit'),
    path('Company/Renew/Payment_terms',views.company_renew_terms,name='company_renew_terms'),
    path('Company/Notifications',views.company_notifications,name='company_notifications'),
    path('company/messages/read/<int:pk>',views.company_message_read,name='company_message_read'),
    path('Company/Payment_History',views.company_payment_history,name='company_payment_history'),
    path('Company/Trial/Review',views.company_trial_feedback,name='company_trial_feedback'),
    path('Company/Profile/Edit/gsttype',views.company_gsttype_change,name='company_gsttype_change'),


    # -------------------------------Staff section--------------------------------
    path('Staff/Dashboard',views.staff_dashboard,name='staff_dashboard'),
    path('Staff/Profile',views.staff_profile,name='staff_profile'),
    path('Staff/Profile-Editpage',views.staff_profile_editpage,name='staff_profile_editpage'),
    path('Staff/Profile/Edit/details',views.staff_profile_details_edit,name='staff_profile_details_edit'),
    path('Staff/Password_Change',views.staff_password_change,name='staff_password_change'),
    
    # -------------------------------Zoho Modules section--------------------------------
    
     # ------------------------- TINTO urls items  START---------------------

    path('new_items',views.new_items,name='new_items'),
    path('items_list',views.items_list,name='items_list'),
    path('create_item',views.create_item,name='create_item'),
    path('itemsoverview/<int:pk>',views.itemsoverview,name='itemsoverview'),
    path('edititems/<int:pr>',views.edititems,name='edititems'),
    path('item_status_edit/<int:pv>',views.item_status_edit,name='item_status_edit'),
    path('shareItemToEmail/<int:pt>',views.shareItemToEmail,name='shareItemToEmail'),
    path('deleteitem/<int:pl>',views.deleteitem,name='deleteitem'),
    path('add_item_comment/<int:pc>',views.add_item_comment,name='add_item_comment'),
    path('delete_item_comment/<int:ph>/<int:pr>',views.delete_item_comment,name='delete_item_comment'),
    path('add_unit',views.add_unit,name='add_unit'),
    path('unit_dropdown',views.unit_dropdown,name = 'unit_dropdown'),
    path('downloadItemSampleImportFile',views.downloadItemSampleImportFile,name='downloadItemSampleImportFile'),
    path('import_item',views.import_item,name='import_item'),
    path('item_view_sort_by_name/<int:pk>',views.item_view_sort_by_name,name='item_view_sort_by_name'),
    path('item_view_sort_by_hsn/<int:pk>',views.item_view_sort_by_hsn,name='item_view_sort_by_hsn'),
    path('filter_item_view_Active/<int:pk>',views.filter_item_view_Active,name='filter_item_view_Active'),
    path('filter_item_view_inActive/<int:pk>',views.filter_item_view_inActive,name='filter_item_view_inActive'),

    #----------------------------- TINTO urls items  END-----------------------------

    #-------------------------TINTO Chartof accounts urls  START------------------------

    path('chartofaccounts',views.chartofaccounts,name='chartofaccounts'),
    path('addchartofaccounts',views.addchartofaccounts,name='addchartofaccounts'),
    path('create_account',views.create_account,name='create_account'),
    path('chartofaccountsoverview/<int:pk>',views.chartofaccountsoverview,name='chartofaccountsoverview'),
    path('editchartofaccounts/<int:pr>',views.editchartofaccounts,name='editchartofaccounts'),
    path('deleteaccount/<int:pl>',views.deleteaccount,name='deleteaccount'),
    path('acc_status_edit/<int:pv>',views.acc_status_edit,name='acc_status_edit'),
    path('add_account_comment/<int:pc>',views.add_account_comment,name='add_account_comment'),

    path('delete_account_comment/<int:ph>/<int:pr>',views.delete_account_comment,name='delete_account_comment'),
    path('add_account',views.add_account,name='add_account'),
    path('account_dropdown',views.account_dropdown,name = 'account_dropdown'),
    path('account_view_sort_by_name/<int:pk>',views.account_view_sort_by_name,name='account_view_sort_by_name'),
    path('shareaccountToEmail/<int:pt>',views.shareaccountToEmail,name='shareaccountToEmail'),

    #------------------------- TINTO Chartof accounts urls  ENDS----------------------
    
    path('chartofaccountsActive',views.chartofaccountsActive,name='chartofaccountsActive'),
    path('chartofaccountsInactive',views.chartofaccountsInactive,name='chartofaccountsInactive'),
    
    #---------------------------------Payroll employee-----------------------------------
   #--------------------------------------George Mathew---------------------------------
    path('Company/payroll_employee_create',views.payroll_employee_create,name='payroll_employee_create'),
    path('Company/payroll_employee_list',views.employee_list,name='employee_list'),
    path('Company/payroll_employee_overview/<int:pk>',views.employee_overview,name='employee_overview'),
    path('Company/create_employee',views.create_employee,name='create_employee'),
    path('Company/payroll_employee_edit/<int:pk>',views.payroll_employee_edit,name='payroll_employee_edit'),
    path('Company/do_payroll_edit/<int:pk>',views.do_payroll_edit,name='do_payroll_edit'),
    path('Company/add_comment/<int:pk>',views.add_comment,name='add_comment'),
    path('Company/delete_comment/<int:pk>/<int:pi>',views.delete_commet,name='delete_comment'),
    path('Company/delete_employee/<int:pk>',views.delete_employee,name='delete_employee'),
    path('Company/employee_status/<int:pk>',views.employee_status,name='employee_status'),
    path('Company/add_blood',views.add_blood,name='add_blood'),
    path('company/import_payroll_excel',views.import_payroll_excel,name='import_payroll_excel'),
    path('Company/add_file/<int:pk>',views.add_file,name='add_file'),
    path('company/shareemail/<int:pk>',views.shareemail,name='shareemail'),
#----------------------------------------------------end--------------------------------------------------

    path('accounts_asset_filter',views.accounts_asset_filter,name='accounts_asset_filter'),
    path('accounts_liability_filter',views.accounts_liability_filter,name='accounts_liability_filter'),
    path('accounts_equity_filter',views.accounts_equity_filter,name='accounts_equity_filter'),
    path('accounts_income_filter',views.accounts_income_filter,name='accounts_income_filter'),
    path('accounts_expense_filter',views.accounts_expense_filter,name='accounts_expense_filter'),
    
    path('account_view_sort_by_namelist',views.account_view_sort_by_namelist,name='account_view_sort_by_namelist'),
    
    path('account_view_filterActive/<int:ph>',views.account_view_filterActive,name='account_view_filterActive'),
    path('account_view_filterinActive/<int:ph>',views.account_view_filterinActive,name='account_view_filterinActive'),
    
    #---------------- Banking ------------------#
    path('Company/Banking/List',views.bank_list, name='bank_list'),
    path('Company/Banking/Create',views.load_bank_create, name='load_bank_create'),
    path('Company/Banking/Create/Bank',views.bank_create, name='bank_create'),
    path('Company/Banking/Edit/<int:id>',views.bank_edit, name='bank_edit'),
    path('Company/Banking/Edit/Bank/<int:id>',views.load_bank_edit, name='load_bank_edit'),
    path('Company/Banking/View/Bank/<int:id>',views.bank_view, name='bank_view'),
    path('Company/Banking/Bank/Status/<int:id>',views.banking_status, name='banking_status'),
    path('Company/Banking/Bank/File/<int:id>',views.bank_attachfile, name='bank_attachfile'),
    path('Company/Banking/Delete/Bank/<int:id>',views.delete_banking, name='delete_banking'),
    path('Company/Banking/Send/Bank/<int:id>',views.send_bank_transaction, name='send_bank_transaction'),
    path('Company/Banking/Create/Tranaction/<int:id>',views.bank_transaction_create, name='bank_transaction_create'),
    path('Company/Banking/Details/Tranaction',views.load_trans_details, name='load_trans_details'),
    path('Company/Banking/Edit/Tranaction',views.bank_transaction_edit, name='bank_transaction_edit'),
    path('Company/Banking/Delete/Tranaction/<int:id>',views.delete_transaction, name='delete_transaction'),
    path('Company/Banking/History/<int:id>',views.load_bank_history, name='load_bank_history'),
    path('Company/Banking/Transaction/History/<int:id>',views.load_bank_trans_history, name='load_bank_trans_history'),
    
    #----------------------------------------------------------akshay--start--------------------------------------------------------
    #------------price lists-------------------
    path('all_price_lists', views.all_price_lists, name='all_price_lists'),
    path('create_price_list/', views.create_price_list, name='create_price_list'),
    path('price_list_details/<int:price_list_id>/', views.price_list_details, name='price_list_details'),
    path('edit_price_list/<int:price_list_id>/', views.edit_price_list, name='edit_price_list'),
    path('delete_price_list/<int:price_list_id>/', views.delete_price_list, name='delete_price_list'),
    path('toggle_price_list_status/<int:price_list_id>/', views.toggle_price_list_status, name='toggle_price_list_status'),
    path('add_pricelist_comment/<int:price_list_id>/', views.add_pricelist_comment, name='add_pricelist_comment'),
    path('delete_pricelist_comment/<int:comment_id>/<int:price_list_id>/', views.delete_pricelist_comment, name='delete_pricelist_comment'),
    path('email_pricelist/<int:price_list_id>/', views.email_pricelist, name='email_pricelist'),
    path('whatsapp_pricelist/<int:price_list_id>/', views.whatsapp_pricelist, name='whatsapp_pricelist'),
    path('price_list_pdf/<int:price_list_id>/', views.price_list_pdf, name='price_list_pdf'),
    path('attach_file/<int:price_list_id>/', views.attach_file, name='attach_file'),
    path('import_price_list/', views.import_price_list, name='import_price_list'),
    #----------------------------------------------------------akshay--end--------------------------------------------------------
    
    
    #================================manual journal==============================
    path('manual_journal', views.manual_journal, name='manual_journal'),
    path('add_journal/', views.add_journal, name='add_journal'),
    path('journal_overview/<int:journal_id>/', views.journal_overview, name='journal_overview'),
    path('journal',views.journal,name="journal"),
    path('import_journal_list',views.import_journal_list,name='import_journal_list'),
    path('update_journal_status/<int:id>/', views.update_journal_status, name='update_journal_status'),
    path('delete_journal/<int:journal_id>/', views.delete_journal, name='delete_journal'),
    path('add_journal_comment/<int:journal_id>/', views.add_journal_comment, name='add_journal_comment'),
    path('delete_journal_comment/<int:id>/', views.delete_journal_comment, name='delete_journal_comment'),
    path('create_account_jour',views.create_account_jour,name='create_account_jour'),
    path('edit_journal/<int:journal_id>/', views.edit_journal, name='edit_journal'),
    path('downloadJournalSampleImportFile',views.downloadJournalSampleImportFile,name='downloadJournalSampleImportFile'),
    path('downloadAccountSampleImportFile',views.downloadAccountSampleImportFile,name='downloadAccountSampleImportFile'),
    path('email_journal/<int:journal_id>/', views.email_journal, name='email_journal'),
    path('journal_pdf/<int:price_list_id>/', views.journal_pdf, name='journal_pdf'),
    path("check_journal_num_valid",views.check_journal_num_valid,name="check_journal_num_valid"),
    path("check_journal_num_valid2",views.check_journal_num_valid2,name="check_journal_num_valid2"),
    
  
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)