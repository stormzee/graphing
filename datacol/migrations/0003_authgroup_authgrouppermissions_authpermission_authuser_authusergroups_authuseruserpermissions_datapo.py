# Generated by Django 3.2.9 on 2021-11-29 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('datacol', '0002_auto_20211129_2312'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Datapoints',
            fields=[
                ('country', models.IntegerField()),
                ('feature', models.CharField(max_length=80)),
                ('var_code', models.IntegerField(primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=80)),
            ],
            options={
                'db_table': 'datapoints',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.PositiveSmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Features',
            fields=[
                ('feature', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=255)),
                ('datapoint', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'features',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SafetyCase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('case_id', models.CharField(blank=True, max_length=255, null=True)),
                ('case_age', models.CharField(blank=True, max_length=255, null=True)),
                ('case_bcg', models.CharField(blank=True, max_length=255, null=True)),
                ('case_bcg_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_carer_age', models.CharField(blank=True, max_length=255, null=True)),
                ('case_carer_edu', models.CharField(blank=True, max_length=255, null=True)),
                ('case_carer_mob', models.CharField(blank=True, max_length=255, null=True)),
                ('case_carer_rel', models.CharField(blank=True, max_length=255, null=True)),
                ('case_carer_rlgn', models.CharField(blank=True, max_length=255, null=True)),
                ('case_carer_rsp', models.CharField(blank=True, max_length=255, null=True)),
                ('case_carer_wrk', models.CharField(blank=True, max_length=255, null=True)),
                ('case_carer_yob', models.CharField(blank=True, max_length=255, null=True)),
                ('case_cdist', models.CharField(blank=True, max_length=255, null=True)),
                ('case_cluster', models.CharField(blank=True, max_length=255, null=True)),
                ('case_country', models.CharField(blank=True, max_length=255, null=True)),
                ('case_doa', models.CharField(blank=True, max_length=255, null=True)),
                ('case_dob', models.CharField(blank=True, max_length=255, null=True)),
                ('case_doi', models.CharField(blank=True, max_length=255, null=True)),
                ('case_doo', models.CharField(blank=True, max_length=255, null=True)),
                ('case_dov', models.CharField(blank=True, max_length=255, null=True)),
                ('case_gender', models.CharField(blank=True, max_length=255, null=True)),
                ('case_gpslat', models.CharField(blank=True, max_length=255, null=True)),
                ('case_gpslong', models.CharField(blank=True, max_length=255, null=True)),
                ('case_hepb', models.CharField(blank=True, max_length=255, null=True)),
                ('case_hepb_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_hh_id', models.CharField(blank=True, max_length=255, null=True)),
                ('case_hh_size', models.CharField(blank=True, max_length=255, null=True)),
                ('case_hh_und5', models.CharField(blank=True, max_length=255, null=True)),
                ('case_hosp', models.CharField(blank=True, max_length=255, null=True)),
                ('case_illdays', models.CharField(blank=True, max_length=255, null=True)),
                ('case_ipv', models.CharField(blank=True, max_length=255, null=True)),
                ('case_ipv_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_meas1', models.CharField(blank=True, max_length=255, null=True)),
                ('case_meas1_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_meas2', models.CharField(blank=True, max_length=255, null=True)),
                ('case_meas2_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_menga', models.CharField(blank=True, max_length=255, null=True)),
                ('case_menga_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_net_bsick', models.CharField(blank=True, max_length=255, null=True)),
                ('case_net_night', models.CharField(blank=True, max_length=255, null=True)),
                ('case_opv0', models.CharField(blank=True, max_length=255, null=True)),
                ('case_opv0_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_opv1', models.CharField(blank=True, max_length=255, null=True)),
                ('case_opv1_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_opv2', models.CharField(blank=True, max_length=255, null=True)),
                ('case_opv2_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_opv3', models.CharField(blank=True, max_length=255, null=True)),
                ('case_opv3_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_outcome', models.CharField(blank=True, max_length=255, null=True)),
                ('case_pcv1', models.CharField(blank=True, max_length=255, null=True)),
                ('case_pcv1_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_pcv2', models.CharField(blank=True, max_length=255, null=True)),
                ('case_pcv2_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_pcv3', models.CharField(blank=True, max_length=255, null=True)),
                ('case_pcv3_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_penta1', models.CharField(blank=True, max_length=255, null=True)),
                ('case_penta1_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_penta2', models.CharField(blank=True, max_length=255, null=True)),
                ('case_penta2_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_penta3', models.CharField(blank=True, max_length=255, null=True)),
                ('case_penta3_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_bcg', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_hepb', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_ipv', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_meas1', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_meas2', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_menga', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_opv0', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_opv1', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_opv2', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_opv3', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_pcv1', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_pcv2', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_pcv3', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_penta1', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_penta2', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_penta3', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_rota1', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_rota2', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_rota3', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_rtss1', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_rtss2', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_rtss3', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_rtss4', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rec_yfever', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rota1', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rota1_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rota2', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rota2_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rota3', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rota3_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rtss1', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rtss1_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rtss2', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rtss2_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rtss3', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rtss3_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rtss4', models.CharField(blank=True, max_length=255, null=True)),
                ('case_rtss4_date', models.CharField(blank=True, max_length=255, null=True)),
                ('case_sdist', models.CharField(blank=True, max_length=255, null=True)),
                ('case_sleep_num', models.CharField(blank=True, max_length=255, null=True)),
                ('case_tov', models.CharField(blank=True, max_length=255, null=True)),
                ('case_vacc_lpoint', models.CharField(blank=True, max_length=255, null=True)),
                ('case_vacc_photo', models.CharField(blank=True, max_length=255, null=True)),
                ('case_vacc_rpoint', models.CharField(blank=True, max_length=255, null=True)),
                ('case_yfever', models.CharField(blank=True, max_length=255, null=True)),
                ('case_yfever_date', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'safety_case',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SafetyControls',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('control_id', models.CharField(blank=True, max_length=255, null=True)),
                ('case_age', models.CharField(blank=True, max_length=255, null=True)),
                ('case_cluster', models.CharField(blank=True, max_length=255, null=True)),
                ('case_country', models.CharField(blank=True, max_length=255, null=True)),
                ('case_doa', models.CharField(blank=True, max_length=255, null=True)),
                ('case_dob', models.CharField(blank=True, max_length=255, null=True)),
                ('case_doi', models.CharField(blank=True, max_length=255, null=True)),
                ('case_doo', models.CharField(blank=True, max_length=255, null=True)),
                ('case_gender', models.CharField(blank=True, max_length=255, null=True)),
                ('case_hosp', models.CharField(blank=True, max_length=255, null=True)),
                ('case_id', models.CharField(blank=True, max_length=255, null=True)),
                ('case_illdays', models.CharField(blank=True, max_length=255, null=True)),
                ('case_outcome', models.CharField(blank=True, max_length=255, null=True)),
                ('control_age', models.CharField(blank=True, max_length=255, null=True)),
                ('control_bcg', models.CharField(blank=True, max_length=255, null=True)),
                ('control_bcg_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_carer_age', models.CharField(blank=True, max_length=255, null=True)),
                ('control_carer_edu', models.CharField(blank=True, max_length=255, null=True)),
                ('control_carer_mob', models.CharField(blank=True, max_length=255, null=True)),
                ('control_carer_rel', models.CharField(blank=True, max_length=255, null=True)),
                ('control_carer_rlgn', models.CharField(blank=True, max_length=255, null=True)),
                ('control_carer_rsp', models.CharField(blank=True, max_length=255, null=True)),
                ('control_carer_wrk', models.CharField(blank=True, max_length=255, null=True)),
                ('control_carer_yob', models.CharField(blank=True, max_length=255, null=True)),
                ('control_cdist', models.CharField(blank=True, max_length=255, null=True)),
                ('control_cluster', models.CharField(blank=True, max_length=255, null=True)),
                ('control_country', models.CharField(blank=True, max_length=255, null=True)),
                ('control_dob', models.CharField(blank=True, max_length=255, null=True)),
                ('control_dov', models.CharField(blank=True, max_length=255, null=True)),
                ('control_gender', models.CharField(blank=True, max_length=255, null=True)),
                ('control_gpslat', models.CharField(blank=True, max_length=255, null=True)),
                ('control_gpslong', models.CharField(blank=True, max_length=255, null=True)),
                ('control_hepb', models.CharField(blank=True, max_length=255, null=True)),
                ('control_hepb_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_hh_id', models.CharField(blank=True, max_length=255, null=True)),
                ('control_hh_size', models.CharField(blank=True, max_length=255, null=True)),
                ('control_hh_und5', models.CharField(blank=True, max_length=255, null=True)),
                ('control_ipv', models.CharField(blank=True, max_length=255, null=True)),
                ('control_ipv_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_meas1', models.CharField(blank=True, max_length=255, null=True)),
                ('control_meas1_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_meas2', models.CharField(blank=True, max_length=255, null=True)),
                ('control_meas2_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_menga', models.CharField(blank=True, max_length=255, null=True)),
                ('control_menga_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_net_bsick', models.CharField(blank=True, max_length=255, null=True)),
                ('control_net_night', models.CharField(blank=True, max_length=255, null=True)),
                ('control_opv0', models.CharField(blank=True, max_length=255, null=True)),
                ('control_opv0_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_opv1', models.CharField(blank=True, max_length=255, null=True)),
                ('control_opv1_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_opv2', models.CharField(blank=True, max_length=255, null=True)),
                ('control_opv2_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_opv3', models.CharField(blank=True, max_length=255, null=True)),
                ('control_opv3_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_pcv1', models.CharField(blank=True, max_length=255, null=True)),
                ('control_pcv1_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_pcv2', models.CharField(blank=True, max_length=255, null=True)),
                ('control_pcv2_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_pcv3', models.CharField(blank=True, max_length=255, null=True)),
                ('control_pcv3_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_penta1', models.CharField(blank=True, max_length=255, null=True)),
                ('control_penta1_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_penta2', models.CharField(blank=True, max_length=255, null=True)),
                ('control_penta2_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_penta3', models.CharField(blank=True, max_length=255, null=True)),
                ('control_penta3_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_bcg', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_hepb', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_ipv', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_meas1', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_meas2', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_menga', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_opv0', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_opv1', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_opv2', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_opv3', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_pcv1', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_pcv2', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_pcv3', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_penta1', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_penta2', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_penta3', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_rota1', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_rota2', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_rota3', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_rtss1', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_rtss2', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_rtss3', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_rtss4', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rec_yfever', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rota1', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rota1_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rota2', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rota2_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rota3', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rota3_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rtss1', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rtss1_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rtss2', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rtss2_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rtss3', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rtss3_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rtss4', models.CharField(blank=True, max_length=255, null=True)),
                ('control_rtss4_date', models.CharField(blank=True, max_length=255, null=True)),
                ('control_sdist', models.CharField(blank=True, max_length=255, null=True)),
                ('control_sleep_num', models.CharField(blank=True, max_length=255, null=True)),
                ('control_tov', models.CharField(blank=True, max_length=255, null=True)),
                ('control_vacc_lpoint', models.CharField(blank=True, max_length=255, null=True)),
                ('control_vacc_photo', models.CharField(blank=True, max_length=255, null=True)),
                ('control_vacc_rpoint', models.CharField(blank=True, max_length=255, null=True)),
                ('control_yfever', models.CharField(blank=True, max_length=255, null=True)),
                ('control_yfever_date', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'db_table': 'safety_controls',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SafetyListing',
            fields=[
                ('case_id', models.CharField(max_length=80, primary_key=True, serialize=False)),
                ('case_age', models.IntegerField(blank=True, null=True)),
                ('case_cluster', models.IntegerField(blank=True, null=True)),
                ('case_country', models.IntegerField(blank=True, null=True)),
                ('case_doa', models.DateField(blank=True, null=True)),
                ('case_dob', models.DateField(blank=True, null=True)),
                ('case_doi', models.DateField(blank=True, null=True)),
                ('case_doo', models.DateField(blank=True, null=True)),
                ('case_gender', models.IntegerField(blank=True, null=True)),
                ('case_hosp', models.IntegerField(blank=True, null=True)),
                ('case_illdays', models.IntegerField(blank=True, null=True)),
                ('case_outcome', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'safety_listing',
                'managed': False,
            },
        ),
    ]
