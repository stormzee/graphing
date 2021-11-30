from django.db import models


# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
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
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Datapoints(models.Model):
    country = models.IntegerField()
    feature = models.CharField(max_length=80)
    var_code = models.IntegerField(primary_key=True)
    label = models.CharField(max_length=80)

    class Meta:
        managed = False
        db_table = 'datapoints'
        unique_together = (('var_code', 'country', 'feature'),)


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
    id = models.BigAutoField(primary_key=True)
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


class Features(models.Model):
    feature = models.CharField(primary_key=True, max_length=255)
    description = models.CharField(max_length=255)
    datapoint = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'features'


class SafetyCase(models.Model):
    case_id = models.CharField(max_length=255, blank=True, null=True)
    case_age = models.CharField(max_length=255, blank=True, null=True)
    case_bcg = models.CharField(max_length=255, blank=True, null=True)
    case_bcg_date = models.CharField(max_length=255, blank=True, null=True)
    case_carer_age = models.CharField(max_length=255, blank=True, null=True)
    case_carer_edu = models.CharField(max_length=255, blank=True, null=True)
    case_carer_mob = models.CharField(max_length=255, blank=True, null=True)
    case_carer_rel = models.CharField(max_length=255, blank=True, null=True)
    case_carer_rlgn = models.CharField(max_length=255, blank=True, null=True)
    case_carer_rsp = models.CharField(max_length=255, blank=True, null=True)
    case_carer_wrk = models.CharField(max_length=255, blank=True, null=True)
    case_carer_yob = models.CharField(max_length=255, blank=True, null=True)
    case_cdist = models.CharField(max_length=255, blank=True, null=True)
    case_cluster = models.CharField(max_length=255, blank=True, null=True)
    case_country = models.CharField(max_length=255, blank=True, null=True)
    case_doa = models.CharField(max_length=255, blank=True, null=True)
    case_dob = models.CharField(max_length=255, blank=True, null=True)
    case_doi = models.CharField(max_length=255, blank=True, null=True)
    case_doo = models.CharField(max_length=255, blank=True, null=True)
    case_dov = models.CharField(max_length=255, blank=True, null=True)
    case_gender = models.CharField(max_length=255, blank=True, null=True)
    case_gpslat = models.CharField(max_length=255, blank=True, null=True)
    case_gpslong = models.CharField(max_length=255, blank=True, null=True)
    case_hepb = models.CharField(max_length=255, blank=True, null=True)
    case_hepb_date = models.CharField(max_length=255, blank=True, null=True)
    case_hh_id = models.CharField(max_length=255, blank=True, null=True)
    case_hh_size = models.CharField(max_length=255, blank=True, null=True)
    case_hh_und5 = models.CharField(max_length=255, blank=True, null=True)
    case_hosp = models.CharField(max_length=255, blank=True, null=True)
    case_illdays = models.CharField(max_length=255, blank=True, null=True)
    case_ipv = models.CharField(max_length=255, blank=True, null=True)
    case_ipv_date = models.CharField(max_length=255, blank=True, null=True)
    case_meas1 = models.CharField(max_length=255, blank=True, null=True)
    case_meas1_date = models.CharField(max_length=255, blank=True, null=True)
    case_meas2 = models.CharField(max_length=255, blank=True, null=True)
    case_meas2_date = models.CharField(max_length=255, blank=True, null=True)
    case_menga = models.CharField(max_length=255, blank=True, null=True)
    case_menga_date = models.CharField(max_length=255, blank=True, null=True)
    case_net_bsick = models.CharField(max_length=255, blank=True, null=True)
    case_net_night = models.CharField(max_length=255, blank=True, null=True)
    case_opv0 = models.CharField(max_length=255, blank=True, null=True)
    case_opv0_date = models.CharField(max_length=255, blank=True, null=True)
    case_opv1 = models.CharField(max_length=255, blank=True, null=True)
    case_opv1_date = models.CharField(max_length=255, blank=True, null=True)
    case_opv2 = models.CharField(max_length=255, blank=True, null=True)
    case_opv2_date = models.CharField(max_length=255, blank=True, null=True)
    case_opv3 = models.CharField(max_length=255, blank=True, null=True)
    case_opv3_date = models.CharField(max_length=255, blank=True, null=True)
    case_outcome = models.CharField(max_length=255, blank=True, null=True)
    case_pcv1 = models.CharField(max_length=255, blank=True, null=True)
    case_pcv1_date = models.CharField(max_length=255, blank=True, null=True)
    case_pcv2 = models.CharField(max_length=255, blank=True, null=True)
    case_pcv2_date = models.CharField(max_length=255, blank=True, null=True)
    case_pcv3 = models.CharField(max_length=255, blank=True, null=True)
    case_pcv3_date = models.CharField(max_length=255, blank=True, null=True)
    case_penta1 = models.CharField(max_length=255, blank=True, null=True)
    case_penta1_date = models.CharField(max_length=255, blank=True, null=True)
    case_penta2 = models.CharField(max_length=255, blank=True, null=True)
    case_penta2_date = models.CharField(max_length=255, blank=True, null=True)
    case_penta3 = models.CharField(max_length=255, blank=True, null=True)
    case_penta3_date = models.CharField(max_length=255, blank=True, null=True)
    case_rec_bcg = models.CharField(max_length=255, blank=True, null=True)
    case_rec_hepb = models.CharField(max_length=255, blank=True, null=True)
    case_rec_ipv = models.CharField(max_length=255, blank=True, null=True)
    case_rec_meas1 = models.CharField(max_length=255, blank=True, null=True)
    case_rec_meas2 = models.CharField(max_length=255, blank=True, null=True)
    case_rec_menga = models.CharField(max_length=255, blank=True, null=True)
    case_rec_opv0 = models.CharField(max_length=255, blank=True, null=True)
    case_rec_opv1 = models.CharField(max_length=255, blank=True, null=True)
    case_rec_opv2 = models.CharField(max_length=255, blank=True, null=True)
    case_rec_opv3 = models.CharField(max_length=255, blank=True, null=True)
    case_rec_pcv1 = models.CharField(max_length=255, blank=True, null=True)
    case_rec_pcv2 = models.CharField(max_length=255, blank=True, null=True)
    case_rec_pcv3 = models.CharField(max_length=255, blank=True, null=True)
    case_rec_penta1 = models.CharField(max_length=255, blank=True, null=True)
    case_rec_penta2 = models.CharField(max_length=255, blank=True, null=True)
    case_rec_penta3 = models.CharField(max_length=255, blank=True, null=True)
    case_rec_rota1 = models.CharField(max_length=255, blank=True, null=True)
    case_rec_rota2 = models.CharField(max_length=255, blank=True, null=True)
    case_rec_rota3 = models.CharField(max_length=255, blank=True, null=True)
    case_rec_rtss1 = models.CharField(max_length=255, blank=True, null=True)
    case_rec_rtss2 = models.CharField(max_length=255, blank=True, null=True)
    case_rec_rtss3 = models.CharField(max_length=255, blank=True, null=True)
    case_rec_rtss4 = models.CharField(max_length=255, blank=True, null=True)
    case_rec_yfever = models.CharField(max_length=255, blank=True, null=True)
    case_rota1 = models.CharField(max_length=255, blank=True, null=True)
    case_rota1_date = models.CharField(max_length=255, blank=True, null=True)
    case_rota2 = models.CharField(max_length=255, blank=True, null=True)
    case_rota2_date = models.CharField(max_length=255, blank=True, null=True)
    case_rota3 = models.CharField(max_length=255, blank=True, null=True)
    case_rota3_date = models.CharField(max_length=255, blank=True, null=True)
    case_rtss1 = models.CharField(max_length=255, blank=True, null=True)
    case_rtss1_date = models.CharField(max_length=255, blank=True, null=True)
    case_rtss2 = models.CharField(max_length=255, blank=True, null=True)
    case_rtss2_date = models.CharField(max_length=255, blank=True, null=True)
    case_rtss3 = models.CharField(max_length=255, blank=True, null=True)
    case_rtss3_date = models.CharField(max_length=255, blank=True, null=True)
    case_rtss4 = models.CharField(max_length=255, blank=True, null=True)
    case_rtss4_date = models.CharField(max_length=255, blank=True, null=True)
    case_sdist = models.CharField(max_length=255, blank=True, null=True)
    case_sleep_num = models.CharField(max_length=255, blank=True, null=True)
    case_tov = models.CharField(max_length=255, blank=True, null=True)
    case_vacc_lpoint = models.CharField(max_length=255, blank=True, null=True)
    case_vacc_photo = models.CharField(max_length=255, blank=True, null=True)
    case_vacc_rpoint = models.CharField(max_length=255, blank=True, null=True)
    case_yfever = models.CharField(max_length=255, blank=True, null=True)
    case_yfever_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'safety_case'


class SafetyControls(models.Model):
    control_id = models.CharField(max_length=255, blank=True, null=True)
    case_age = models.CharField(max_length=255, blank=True, null=True)
    case_cluster = models.CharField(max_length=255, blank=True, null=True)
    case_country = models.CharField(max_length=255, blank=True, null=True)
    case_doa = models.CharField(max_length=255, blank=True, null=True)
    case_dob = models.CharField(max_length=255, blank=True, null=True)
    case_doi = models.CharField(max_length=255, blank=True, null=True)
    case_doo = models.CharField(max_length=255, blank=True, null=True)
    case_gender = models.CharField(max_length=255, blank=True, null=True)
    case_hosp = models.CharField(max_length=255, blank=True, null=True)
    case_id = models.CharField(max_length=255, blank=True, null=True)
    case_illdays = models.CharField(max_length=255, blank=True, null=True)
    case_outcome = models.CharField(max_length=255, blank=True, null=True)
    control_age = models.CharField(max_length=255, blank=True, null=True)
    control_bcg = models.CharField(max_length=255, blank=True, null=True)
    control_bcg_date = models.CharField(max_length=255, blank=True, null=True)
    control_carer_age = models.CharField(max_length=255, blank=True, null=True)
    control_carer_edu = models.CharField(max_length=255, blank=True, null=True)
    control_carer_mob = models.CharField(max_length=255, blank=True, null=True)
    control_carer_rel = models.CharField(max_length=255, blank=True, null=True)
    control_carer_rlgn = models.CharField(max_length=255, blank=True, null=True)
    control_carer_rsp = models.CharField(max_length=255, blank=True, null=True)
    control_carer_wrk = models.CharField(max_length=255, blank=True, null=True)
    control_carer_yob = models.CharField(max_length=255, blank=True, null=True)
    control_cdist = models.CharField(max_length=255, blank=True, null=True)
    control_cluster = models.CharField(max_length=255, blank=True, null=True)
    control_country = models.CharField(max_length=255, blank=True, null=True)
    control_dob = models.CharField(max_length=255, blank=True, null=True)
    control_dov = models.CharField(max_length=255, blank=True, null=True)
    control_gender = models.CharField(max_length=255, blank=True, null=True)
    control_gpslat = models.CharField(max_length=255, blank=True, null=True)
    control_gpslong = models.CharField(max_length=255, blank=True, null=True)
    control_hepb = models.CharField(max_length=255, blank=True, null=True)
    control_hepb_date = models.CharField(max_length=255, blank=True, null=True)
    control_hh_id = models.CharField(max_length=255, blank=True, null=True)
    control_hh_size = models.CharField(max_length=255, blank=True, null=True)
    control_hh_und5 = models.CharField(max_length=255, blank=True, null=True)
    control_ipv = models.CharField(max_length=255, blank=True, null=True)
    control_ipv_date = models.CharField(max_length=255, blank=True, null=True)
    control_meas1 = models.CharField(max_length=255, blank=True, null=True)
    control_meas1_date = models.CharField(max_length=255, blank=True, null=True)
    control_meas2 = models.CharField(max_length=255, blank=True, null=True)
    control_meas2_date = models.CharField(max_length=255, blank=True, null=True)
    control_menga = models.CharField(max_length=255, blank=True, null=True)
    control_menga_date = models.CharField(max_length=255, blank=True, null=True)
    control_net_bsick = models.CharField(max_length=255, blank=True, null=True)
    control_net_night = models.CharField(max_length=255, blank=True, null=True)
    control_opv0 = models.CharField(max_length=255, blank=True, null=True)
    control_opv0_date = models.CharField(max_length=255, blank=True, null=True)
    control_opv1 = models.CharField(max_length=255, blank=True, null=True)
    control_opv1_date = models.CharField(max_length=255, blank=True, null=True)
    control_opv2 = models.CharField(max_length=255, blank=True, null=True)
    control_opv2_date = models.CharField(max_length=255, blank=True, null=True)
    control_opv3 = models.CharField(max_length=255, blank=True, null=True)
    control_opv3_date = models.CharField(max_length=255, blank=True, null=True)
    control_pcv1 = models.CharField(max_length=255, blank=True, null=True)
    control_pcv1_date = models.CharField(max_length=255, blank=True, null=True)
    control_pcv2 = models.CharField(max_length=255, blank=True, null=True)
    control_pcv2_date = models.CharField(max_length=255, blank=True, null=True)
    control_pcv3 = models.CharField(max_length=255, blank=True, null=True)
    control_pcv3_date = models.CharField(max_length=255, blank=True, null=True)
    control_penta1 = models.CharField(max_length=255, blank=True, null=True)
    control_penta1_date = models.CharField(max_length=255, blank=True, null=True)
    control_penta2 = models.CharField(max_length=255, blank=True, null=True)
    control_penta2_date = models.CharField(max_length=255, blank=True, null=True)
    control_penta3 = models.CharField(max_length=255, blank=True, null=True)
    control_penta3_date = models.CharField(max_length=255, blank=True, null=True)
    control_rec_bcg = models.CharField(max_length=255, blank=True, null=True)
    control_rec_hepb = models.CharField(max_length=255, blank=True, null=True)
    control_rec_ipv = models.CharField(max_length=255, blank=True, null=True)
    control_rec_meas1 = models.CharField(max_length=255, blank=True, null=True)
    control_rec_meas2 = models.CharField(max_length=255, blank=True, null=True)
    control_rec_menga = models.CharField(max_length=255, blank=True, null=True)
    control_rec_opv0 = models.CharField(max_length=255, blank=True, null=True)
    control_rec_opv1 = models.CharField(max_length=255, blank=True, null=True)
    control_rec_opv2 = models.CharField(max_length=255, blank=True, null=True)
    control_rec_opv3 = models.CharField(max_length=255, blank=True, null=True)
    control_rec_pcv1 = models.CharField(max_length=255, blank=True, null=True)
    control_rec_pcv2 = models.CharField(max_length=255, blank=True, null=True)
    control_rec_pcv3 = models.CharField(max_length=255, blank=True, null=True)
    control_rec_penta1 = models.CharField(max_length=255, blank=True, null=True)
    control_rec_penta2 = models.CharField(max_length=255, blank=True, null=True)
    control_rec_penta3 = models.CharField(max_length=255, blank=True, null=True)
    control_rec_rota1 = models.CharField(max_length=255, blank=True, null=True)
    control_rec_rota2 = models.CharField(max_length=255, blank=True, null=True)
    control_rec_rota3 = models.CharField(max_length=255, blank=True, null=True)
    control_rec_rtss1 = models.CharField(max_length=255, blank=True, null=True)
    control_rec_rtss2 = models.CharField(max_length=255, blank=True, null=True)
    control_rec_rtss3 = models.CharField(max_length=255, blank=True, null=True)
    control_rec_rtss4 = models.CharField(max_length=255, blank=True, null=True)
    control_rec_yfever = models.CharField(max_length=255, blank=True, null=True)
    control_rota1 = models.CharField(max_length=255, blank=True, null=True)
    control_rota1_date = models.CharField(max_length=255, blank=True, null=True)
    control_rota2 = models.CharField(max_length=255, blank=True, null=True)
    control_rota2_date = models.CharField(max_length=255, blank=True, null=True)
    control_rota3 = models.CharField(max_length=255, blank=True, null=True)
    control_rota3_date = models.CharField(max_length=255, blank=True, null=True)
    control_rtss1 = models.CharField(max_length=255, blank=True, null=True)
    control_rtss1_date = models.CharField(max_length=255, blank=True, null=True)
    control_rtss2 = models.CharField(max_length=255, blank=True, null=True)
    control_rtss2_date = models.CharField(max_length=255, blank=True, null=True)
    control_rtss3 = models.CharField(max_length=255, blank=True, null=True)
    control_rtss3_date = models.CharField(max_length=255, blank=True, null=True)
    control_rtss4 = models.CharField(max_length=255, blank=True, null=True)
    control_rtss4_date = models.CharField(max_length=255, blank=True, null=True)
    control_sdist = models.CharField(max_length=255, blank=True, null=True)
    control_sleep_num = models.CharField(max_length=255, blank=True, null=True)
    control_tov = models.CharField(max_length=255, blank=True, null=True)
    control_vacc_lpoint = models.CharField(max_length=255, blank=True, null=True)
    control_vacc_photo = models.CharField(max_length=255, blank=True, null=True)
    control_vacc_rpoint = models.CharField(max_length=255, blank=True, null=True)
    control_yfever = models.CharField(max_length=255, blank=True, null=True)
    control_yfever_date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'safety_controls'


class SafetyListing(models.Model):
    case_id = models.CharField(primary_key=True, max_length=80)
    case_age = models.IntegerField(blank=True, null=True)
    case_cluster = models.IntegerField(blank=True, null=True)
    case_country = models.IntegerField(blank=True, null=True)
    case_doa = models.DateField(blank=True, null=True)
    case_dob = models.DateField(blank=True, null=True)
    case_doi = models.DateField(blank=True, null=True)
    case_doo = models.DateField(blank=True, null=True)
    case_gender = models.IntegerField(blank=True, null=True)
    case_hosp = models.IntegerField(blank=True, null=True)
    case_illdays = models.IntegerField(blank=True, null=True)
    case_outcome = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'safety_listing'


class Metrics_view(models.Model):
    sn = models.CharField(primary_key=True, max_length=50)
    country = models.CharField( max_length=255, blank=True, null=True)
    feature = models.CharField(max_length=255, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    # category = models.CharField(max_length=255, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    card = models.IntegerField(blank=True, null=True)
    has_card = models.IntegerField(blank=True, null=True)
    recall = models.IntegerField(blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'metrics_view_home_checkvacc'
    
    # def __str__(self):
    #     return self.name


