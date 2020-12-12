# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    admin_id = models.IntegerField(db_column='ADMIN_ID', primary_key=True)  # Field name made lowercase.
    admin_fname = models.CharField(db_column='ADMIN_FNAME', max_length=45)  # Field name made lowercase.
    admin_lname = models.CharField(db_column='ADMIN_LNAME', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'


class AdminHasCustomer(models.Model):
    admin_admin = models.OneToOneField(Admin, models.DO_NOTHING, db_column='ADMIN_ADMIN_ID', primary_key=True)  # Field name made lowercase.
    customer_cust = models.ForeignKey('Customer', models.DO_NOTHING, db_column='CUSTOMER_CUST_ID')  # Field name made lowercase.
    customer_menu_menu_item = models.ForeignKey('Customer', models.DO_NOTHING, db_column='CUSTOMER_MENU_MENU_ITEM_ID', related_name='menuItem')  # Field name made lowercase.
    customer_menu_admin_admin = models.ForeignKey('Customer', models.DO_NOTHING, db_column='CUSTOMER_MENU_ADMIN_ADMIN_ID', related_name='mrnuAdmin')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin_has_customer'
        unique_together = (('admin_admin', 'customer_cust', 'customer_menu_menu_item', 'customer_menu_admin_admin'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Customer(models.Model):
    cust_id = models.IntegerField(db_column='CUST_ID', primary_key=True)  # Field name made lowercase.
    cust_fname = models.CharField(db_column='CUST_FNAME', max_length=45)  # Field name made lowercase.
    cust_lname = models.CharField(db_column='CUST_LNAME', max_length=45)  # Field name made lowercase.
    cust_phone = models.CharField(db_column='CUST_PHONE', max_length=45)  # Field name made lowercase.
    menu_menu_item = models.ForeignKey('Menu', models.DO_NOTHING, db_column='MENU_MENU_ITEM_ID', related_name='menuItem')  # Field name made lowercase.
    menu_admin_admin = models.ForeignKey('Menu', models.DO_NOTHING, db_column='MENU_ADMIN_ADMIN_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'customer'
        unique_together = (('cust_id', 'menu_menu_item', 'menu_admin_admin'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Menu(models.Model):
    menu_item_id = models.IntegerField(db_column='MENU_ITEM_ID', primary_key=True)  # Field name made lowercase.
    #menu_item_name = models.CharField(db_column='MENU_ITEM_NAME', max_length=45)
    menu_quant = models.IntegerField(db_column='MENU_QUANT')  # Field name made lowercase.
    menu_price = models.DecimalField(db_column='MENU_PRICE', max_digits=2, decimal_places=0)  # Field name made lowercase.
    menu_categ = models.CharField(db_column='MENU_CATEG', max_length=45)  # Field name made lowercase.
    menu_cals = models.IntegerField(db_column='MENU_CALS')  # Field name made lowercase.
    admin_admin = models.ForeignKey(Admin, models.DO_NOTHING, db_column='ADMIN_ADMIN_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'menu'
        unique_together = (('menu_item_id', 'admin_admin'),)


class Order(models.Model):
    ord_item_id = models.IntegerField(db_column='ORD_ITEM_ID', primary_key=True)  # Field name made lowercase.
    ord_quant = models.IntegerField(db_column='ORD_QUANT')  # Field name made lowercase.
    customer_cust = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CUSTOMER_CUST_ID')  # Field name made lowercase.
    menu_menu_item = models.ForeignKey(Menu, models.DO_NOTHING, db_column='MENU_MENU_ITEM_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'order'
        unique_together = (('ord_item_id', 'customer_cust', 'menu_menu_item'),)
