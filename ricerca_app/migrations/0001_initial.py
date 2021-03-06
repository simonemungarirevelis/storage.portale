# Generated by Django 3.1.5 on 2021-02-05 15:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CdSList',
            fields=[
                ('regdidid', models.IntegerField(db_column='RegDidId', primary_key=True, serialize=False)),
                ('cdsid', models.IntegerField(blank=True, db_column='CdSId', null=True)),
                ('academicyear', models.IntegerField(blank=True, db_column='AcademicYear', null=True)),
                ('cdsnameit', models.CharField(blank=True, db_column='CdSNameIT', max_length=255, null=True)),
                ('cdsnameeng', models.CharField(blank=True, db_column='CdSNameENG', max_length=255, null=True)),
                ('departmentid', models.CharField(blank=True, db_column='DepartmentId', max_length=40, null=True)),
                ('departmentnameit', models.CharField(blank=True, db_column='DepartmentNameIT', max_length=255, null=True)),
                ('departmentnameeng', models.CharField(blank=True, db_column='DepartmentNameENG', max_length=255, null=True)),
                ('coursetypeid', models.CharField(blank=True, db_column='CourseTypeId', max_length=10, null=True)),
                ('coursetypename', models.CharField(blank=True, db_column='CourseTypeName', max_length=80, null=True)),
                ('courseclassid', models.CharField(blank=True, db_column='CourseClassId', max_length=10, null=True)),
                ('courseclassname', models.CharField(blank=True, db_column='CourseClassName', max_length=255, null=True)),
                ('cdslanguageit', models.CharField(blank=True, db_column='CdsLanguageIT', max_length=100, null=True)),
                ('cdslanguageeng', models.CharField(blank=True, db_column='CdSLanguageENG', max_length=100, null=True)),
                ('cdsduration', models.IntegerField(blank=True, db_column='CdSDuration', null=True)),
                ('cdsects', models.IntegerField(blank=True, db_column='CdSECTS', null=True)),
                ('cdsattendance', models.IntegerField(blank=True, db_column='CdSAttendance', null=True)),
                ('jointdegree', models.CharField(blank=True, db_column='JointDegree', max_length=100, null=True)),
            ],
            options={
                'db_table': 'CDSLIST',
            },
        ),
        migrations.CreateModel(
            name='ComuniAll',
            fields=[
                ('id_comune', models.IntegerField(db_column='ID_COMUNE', primary_key=True, serialize=False)),
                ('ds_comune', models.CharField(blank=True, db_column='DS_COMUNE', max_length=255, null=True)),
                ('cd_catasto', models.CharField(blank=True, db_column='CD_CATASTO', max_length=255, null=True, unique=True)),
                ('cd_istat', models.CharField(blank=True, db_column='CD_ISTAT', max_length=6, null=True)),
                ('dt_costituzione', models.DateTimeField(blank=True, db_column='DT_COSTITUZIONE', null=True)),
                ('dt_cessazione', models.DateTimeField(blank=True, db_column='DT_CESSAZIONE', null=True)),
                ('id_prov', models.IntegerField(blank=True, db_column='ID_PROV', null=True)),
                ('cd_sigla', models.CharField(blank=True, db_column='CD_SIGLA', max_length=2, null=True)),
                ('ds_prov', models.CharField(blank=True, db_column='DS_PROV', max_length=255, null=True)),
                ('id_nazione', models.IntegerField(blank=True, db_column='ID_NAZIONE', null=True)),
                ('cd_iso3166_1_a2_nazione', models.CharField(blank=True, db_column='CD_ISO3166_1_A2_NAZIONE', max_length=2, null=True)),
                ('ds_nazione', models.CharField(blank=True, db_column='DS_NAZIONE', max_length=255, null=True)),
            ],
            options={
                'db_table': 'COMUNI_ALL',
            },
        ),
        migrations.CreateModel(
            name='DidatticaCds',
            fields=[
                ('dt_ins', models.DateTimeField(auto_now_add=True, db_column='DT_INS')),
                ('dt_mod', models.DateTimeField(auto_now=True, db_column='DT_MOD', null=True)),
                ('cds_id', models.IntegerField(db_column='CDS_ID', primary_key=True, serialize=False)),
                ('cds_cod', models.CharField(blank=True, db_column='CDS_COD', max_length=10, null=True)),
                ('nome_cds_it', models.CharField(blank=True, db_column='NOME_CDS_IT', max_length=255, null=True)),
                ('nome_cds_eng', models.CharField(blank=True, db_column='NOME_CDS_ENG', max_length=255, null=True)),
                ('rif_cod', models.CharField(blank=True, db_column='RIF_COD', max_length=10, null=True)),
                ('rif_des', models.CharField(blank=True, db_column='RIF_DES', max_length=40, null=True)),
                ('tipo_corso_cod', models.CharField(blank=True, db_column='TIPO_CORSO_COD', max_length=10, null=True)),
                ('tipo_corso_des', models.CharField(blank=True, db_column='TIPO_CORSO_DES', max_length=80, null=True)),
                ('durata_anni', models.IntegerField(blank=True, db_column='DURATA_ANNI', null=True)),
                ('valore_min', models.IntegerField(blank=True, db_column='VALORE_MIN', null=True)),
                ('tipo_titit_cod', models.CharField(blank=True, db_column='TIPO_TITIT_COD', max_length=10, null=True)),
                ('tipo_titit_des', models.CharField(blank=True, db_column='TIPO_TITIT_DES', max_length=255, null=True)),
                ('min_cfu_comuni', models.IntegerField(blank=True, db_column='MIN_CFU_COMUNI', null=True)),
                ('cfu_max_rico', models.IntegerField(blank=True, db_column='CFU_MAX_RICO', null=True)),
                ('num_max_esami', models.IntegerField(blank=True, db_column='NUM_MAX_ESAMI', null=True)),
                ('perc_min_ore_stu_ind', models.FloatField(blank=True, db_column='PERC_MIN_ORE_STU_IND', null=True)),
                ('perc_max_ore_stu_ind', models.FloatField(blank=True, db_column='PERC_MAX_ORE_STU_IND', null=True)),
                ('tipo_spec_cod', models.CharField(blank=True, db_column='TIPO_SPEC_COD', max_length=10, null=True)),
                ('tipo_spec_des', models.CharField(blank=True, db_column='TIPO_SPEC_DES', max_length=255, null=True)),
                ('scuola_spec_id', models.IntegerField(blank=True, db_column='SCUOLA_SPEC_ID', null=True)),
                ('scuola_spec_des', models.CharField(blank=True, db_column='SCUOLA_SPEC_DES', max_length=255, null=True)),
                ('cla_m_id', models.IntegerField(blank=True, db_column='CLA_M_ID', null=True)),
                ('cla_miur_cod', models.CharField(blank=True, db_column='CLA_MIUR_COD', max_length=10, null=True)),
                ('cla_miur_des', models.CharField(blank=True, db_column='CLA_MIUR_DES', max_length=255, null=True)),
                ('intercla_m_id', models.IntegerField(blank=True, db_column='INTERCLA_M_ID', null=True)),
                ('intercla_miur_cod', models.CharField(blank=True, db_column='INTERCLA_MIUR_COD', max_length=10, null=True)),
                ('intercla_miur_des', models.CharField(blank=True, db_column='INTERCLA_MIUR_DES', max_length=255, null=True)),
                ('codicione', models.CharField(blank=True, db_column='CODICIONE', max_length=255, null=True)),
                ('min_diff_cfu_ord', models.IntegerField(blank=True, db_column='MIN_DIFF_CFU_ORD', null=True)),
                ('sett_post_rif_flg', models.IntegerField(blank=True, db_column='SETT_POST_RIF_FLG', null=True)),
                ('istat_cod', models.CharField(blank=True, db_column='ISTAT_COD', max_length=10, null=True)),
                ('max_punti', models.IntegerField(blank=True, db_column='MAX_PUNTI', null=True)),
                ('um_peso_cod', models.CharField(blank=True, db_column='UM_PESO_COD', max_length=5, null=True)),
                ('um_peso_des', models.CharField(blank=True, db_column='UM_PESO_DES', max_length=40, null=True)),
                ('aa_att_id', models.IntegerField(blank=True, db_column='AA_ATT_ID', null=True)),
                ('data_attivazione', models.DateTimeField(blank=True, db_column='DATA_ATTIVAZIONE', null=True)),
                ('aa_dis_id', models.IntegerField(blank=True, db_column='AA_DIS_ID', null=True)),
                ('url', models.CharField(blank=True, db_column='URL', max_length=255, null=True)),
                ('cds_url_info_web', models.CharField(blank=True, db_column='CDS_URL_INFO_WEB', max_length=255, null=True)),
                ('cds_vis_web_flg', models.IntegerField(blank=True, db_column='CDS_VIS_WEB_FLG', null=True)),
                ('ccs_id', models.IntegerField(blank=True, db_column='CCS_ID', null=True)),
                ('ccs_cod', models.CharField(blank=True, db_column='CCS_COD', max_length=10, null=True)),
                ('ccs_des', models.CharField(blank=True, db_column='CCS_DES', max_length=255, null=True)),
                ('flg_exp_seg_stu', models.IntegerField(blank=True, db_column='FLG_EXP_SEG_STU', null=True)),
                ('data_exp_seg_stu', models.DateTimeField(blank=True, db_column='DATA_EXP_SEG_STU', null=True)),
                ('cdsord_id', models.IntegerField(blank=True, db_column='CDSORD_ID', null=True, unique=True)),
                ('cdsord_cod', models.CharField(blank=True, db_column='CDSORD_COD', max_length=10, null=True)),
                ('aa_ord_id', models.IntegerField(blank=True, db_column='AA_ORD_ID', null=True)),
                ('stato_cdsord_cod', models.CharField(blank=True, db_column='STATO_CDSORD_COD', max_length=5, null=True)),
            ],
            options={
                'db_table': 'DIDATTICA_CDS',
            },
        ),
        migrations.CreateModel(
            name='DidatticaDipartimento',
            fields=[
                ('dt_ins', models.DateTimeField(auto_now_add=True, db_column='DT_INS')),
                ('dt_mod', models.DateTimeField(auto_now=True, db_column='DT_MOD', null=True)),
                ('dip_id', models.IntegerField(db_column='DIP_ID', primary_key=True, serialize=False)),
                ('dip_cod', models.CharField(blank=True, db_column='DIP_COD', max_length=40, null=True)),
                ('dip_des_it', models.CharField(blank=True, db_column='DIP_DES_IT', max_length=255, null=True)),
                ('dip_des_eng', models.CharField(blank=True, db_column='DIP_DES_ENG', max_length=255, null=True)),
                ('dip_nome_breve', models.CharField(blank=True, db_column='DIP_NOME_BREVE', max_length=100, null=True)),
                ('dip_cd_csa', models.CharField(blank=True, db_column='DIP_CD_CSA', max_length=40, null=True)),
                ('miur_dip_id', models.IntegerField(blank=True, db_column='MIUR_DIP_ID', null=True)),
                ('url_pubbl_off_f', models.CharField(blank=True, db_column='URL_PUBBL_OFF_F', max_length=255, null=True)),
                ('dip_vis_web_flg', models.IntegerField(blank=True, db_column='DIP_VIS_WEB_FLG', null=True)),
            ],
            options={
                'verbose_name_plural': 'Didattica Dipartimento',
                'db_table': 'DIDATTICA_DIPARTIMENTO',
            },
        ),
        migrations.CreateModel(
            name='DidatticaRegolamento',
            fields=[
                ('dt_ins', models.DateTimeField(auto_now_add=True, db_column='DT_INS')),
                ('dt_mod', models.DateTimeField(auto_now=True, db_column='DT_MOD', null=True)),
                ('regdid_id', models.IntegerField(db_column='REGDID_ID', primary_key=True, serialize=False)),
                ('aa_reg_did', models.IntegerField(blank=True, db_column='AA_REG_DID', null=True)),
                ('stato_regdid_cod', models.CharField(blank=True, db_column='STATO_REGDID_COD', max_length=5, null=True)),
                ('stato_regdid_des', models.CharField(blank=True, db_column='STATO_REGDID_DES', max_length=40, null=True)),
                ('numero_piani_studio', models.IntegerField(blank=True, db_column='NUMERO_PIANI_STUDIO', null=True)),
                ('anno_scelta_pds', models.IntegerField(blank=True, db_column='ANNO_SCELTA_PDS', null=True)),
                ('modalita_erogazione', models.CharField(blank=True, db_column='MODALITA_EROGAZIONE', max_length=100, null=True)),
                ('frequenza_obbligatoria', models.IntegerField(blank=True, db_column='FREQUENZA_OBBLIGATORIA', null=True)),
                ('titolo_congiunto_cod', models.CharField(blank=True, db_column='TITOLO_CONGIUNTO_COD', max_length=100, null=True)),
                ('cds', models.ForeignKey(blank=True, db_column='CDS_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ricerca_app.didatticacds')),
            ],
            options={
                'db_table': 'DIDATTICA_REGOLAMENTO',
            },
        ),
        migrations.CreateModel(
            name='Personale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_ab', models.IntegerField(db_column='ID_AB')),
                ('cd_esterno', models.CharField(blank=True, db_column='CD_ESTERNO', max_length=60, null=True)),
                ('matricola', models.CharField(db_column='MATRICOLA', max_length=6, unique=True)),
                ('matricola_sp', models.CharField(blank=True, db_column='MATRICOLA_SP', max_length=255, null=True)),
                ('nome', models.CharField(blank=True, db_column='NOME', max_length=100, null=True)),
                ('cognome', models.CharField(blank=True, db_column='COGNOME', max_length=100, null=True)),
                ('middle_name', models.CharField(blank=True, db_column='MIDDLE_NAME', max_length=100, null=True)),
                ('cod_fis', models.CharField(blank=True, db_column='COD_FIS', max_length=16, null=True, unique=True)),
                ('cd_genere', models.CharField(blank=True, db_column='CD_GENERE', max_length=1, null=True)),
                ('dt_nascita', models.DateField(blank=True, db_column='DT_NASCITA', null=True)),
                ('id_comu_nasc', models.IntegerField(blank=True, db_column='ID_COMU_NASC', null=True)),
                ('ds_cittstra_nasc', models.CharField(blank=True, db_column='DS_CITTSTRA_NASC', max_length=255, null=True)),
                ('ds_comune_nasc', models.CharField(blank=True, db_column='DS_COMUNE_NASC', max_length=255, null=True)),
                ('ds_prov_nasc', models.CharField(blank=True, db_column='DS_PROV_NASC', max_length=255, null=True)),
                ('cd_sigla_nasc', models.CharField(blank=True, db_column='CD_SIGLA_NASC', max_length=2, null=True)),
                ('id_nazione_nasc', models.IntegerField(blank=True, db_column='ID_NAZIONE_NASC', null=True)),
                ('ds_nazi_nasc', models.CharField(blank=True, db_column='DS_NAZI_NASC', max_length=100, null=True)),
                ('ds_nazi_breve_nasc', models.CharField(blank=True, db_column='DS_NAZI_BREVE_NASC', max_length=20, null=True)),
                ('id_comu_res', models.IntegerField(blank=True, db_column='ID_COMU_RES', null=True)),
                ('ds_comune_res', models.CharField(blank=True, db_column='DS_COMUNE_RES', max_length=255, null=True)),
                ('cd_cap_res', models.CharField(blank=True, db_column='CD_CAP_RES', max_length=5, null=True)),
                ('indirizzo_res', models.CharField(blank=True, db_column='INDIRIZZO_RES', max_length=255, null=True)),
                ('num_civico_res', models.CharField(blank=True, db_column='NUM_CIVICO_RES', max_length=15, null=True, verbose_name='Numero Civico Residenza')),
                ('cd_sigla_res', models.CharField(blank=True, db_column='CD_SIGLA_RES', max_length=2, null=True)),
                ('id_comu_dom', models.IntegerField(blank=True, db_column='ID_COMU_DOM', null=True)),
                ('ds_comune_dom', models.CharField(blank=True, db_column='DS_COMUNE_DOM', max_length=255, null=True)),
                ('cd_cap_dom', models.CharField(blank=True, db_column='CD_CAP_DOM', max_length=5, null=True)),
                ('indirizzo_dom', models.CharField(blank=True, db_column='INDIRIZZO_DOM', max_length=255, null=True)),
                ('num_civico_dom', models.CharField(blank=True, db_column='NUM_CIVICO_DOM', max_length=15, null=True)),
                ('cd_sigla_dom', models.CharField(blank=True, db_column='CD_SIGLA_DOM', max_length=2, null=True)),
                ('cd_comparto', models.CharField(db_column='CD_COMPARTO', max_length=1)),
                ('ds_comparto', models.CharField(blank=True, db_column='DS_COMPARTO', max_length=40, null=True)),
                ('cd_ruolo', models.CharField(db_column='CD_RUOLO', max_length=4)),
                ('ds_ruolo', models.CharField(blank=True, db_column='DS_RUOLO', max_length=40, null=True)),
                ('ds_ruolo_locale', models.CharField(blank=True, db_column='DS_RUOLO_LOCALE', max_length=40, null=True)),
                ('peso_ruolo', models.DecimalField(blank=True, db_column='PESO_RUOLO', decimal_places=0, max_digits=10, null=True)),
                ('dt_rap_ini', models.DateField(blank=True, db_column='DT_RAP_INI', null=True)),
                ('dt_rap_fin', models.DateField(blank=True, db_column='DT_RAP_FIN', null=True)),
                ('cd_ssd', models.CharField(blank=True, db_column='CD_SSD', max_length=12, null=True)),
                ('ds_ssd', models.CharField(blank=True, db_column='DS_SSD', max_length=100, null=True)),
                ('cd_fac', models.CharField(blank=True, db_column='CD_FAC', max_length=10, null=True)),
                ('ds_fac', models.CharField(blank=True, db_column='DS_FAC', max_length=255, null=True)),
                ('aff_org', models.CharField(blank=True, db_column='AFF_ORG', max_length=6, null=True)),
                ('ds_aff_org', models.CharField(blank=True, db_column='DS_AFF_ORG', max_length=255, null=True)),
                ('ds_aff_org_breve', models.CharField(blank=True, db_column='DS_AFF_ORG_BREVE', max_length=50, null=True)),
                ('aff_org2', models.CharField(blank=True, db_column='AFF_ORG2', max_length=6, null=True)),
                ('ds_aff_org2', models.CharField(blank=True, db_column='DS_AFF_ORG2', max_length=255, null=True)),
                ('ds_aff_org2_breve', models.CharField(blank=True, db_column='DS_AFF_ORG2_BREVE', max_length=50, null=True)),
                ('aff_org3', models.CharField(blank=True, db_column='AFF_ORG3', max_length=6, null=True)),
                ('ds_aff_org3', models.CharField(blank=True, db_column='DS_AFF_ORG3', max_length=255, null=True)),
                ('ds_aff_org3_breve', models.CharField(blank=True, db_column='DS_AFF_ORG3_BREVE', max_length=50, null=True)),
                ('aff_org4', models.CharField(blank=True, db_column='AFF_ORG4', max_length=6, null=True)),
                ('ds_aff_org4', models.CharField(blank=True, db_column='DS_AFF_ORG4', max_length=255, null=True)),
                ('ds_aff_org4_breve', models.CharField(blank=True, db_column='DS_AFF_ORG4_BREVE', max_length=50, null=True)),
                ('sede', models.CharField(blank=True, db_column='SEDE', max_length=6, null=True)),
                ('ds_sede', models.CharField(blank=True, db_column='DS_SEDE', max_length=255, null=True)),
                ('ds_sede_breve', models.CharField(blank=True, db_column='DS_SEDE_BREVE', max_length=50, null=True)),
                ('profilo', models.CharField(blank=True, db_column='PROFILO', max_length=11, null=True)),
                ('ds_profilo', models.CharField(blank=True, db_column='DS_PROFILO', max_length=100, null=True)),
                ('ds_profilo_breve', models.CharField(blank=True, db_column='DS_PROFILO_BREVE', max_length=50, null=True)),
                ('cd_ateneo_corr', models.CharField(blank=True, db_column='CD_ATENEO_CORR', max_length=10, null=True)),
                ('ds_ateneo_corr', models.CharField(blank=True, db_column='DS_ATENEO_CORR', max_length=255, null=True)),
                ('dt_ini_rap_univ', models.DateField(blank=True, db_column='DT_INI_RAP_UNIV', null=True)),
                ('dt_fin_rap_univ', models.DateField(blank=True, db_column='DT_FIN_RAP_UNIV', null=True)),
                ('telrif', models.CharField(blank=True, db_column='TELRIF', max_length=255, null=True)),
                ('email', models.CharField(blank=True, db_column='EMAIL', max_length=255, null=True)),
                ('urlcv', models.CharField(blank=True, db_column='URLCV', max_length=255, null=True)),
                ('fl_docente', models.PositiveIntegerField(blank=True, db_column='FL_DOCENTE', null=True)),
                ('cd_anagrafico', models.CharField(blank=True, db_column='CD_ANAGRAFICO', max_length=20, null=True)),
                ('inquadr', models.CharField(blank=True, db_column='INQUADR', max_length=50, null=True)),
                ('badge', models.CharField(blank=True, db_column='BADGE', max_length=255, null=True)),
                ('tempo', models.CharField(blank=True, db_column='TEMPO', max_length=1, null=True)),
                ('id_contratto', models.IntegerField(blank=True, db_column='ID_CONTRATTO', null=True)),
                ('flg_cessato', models.IntegerField(blank=True, db_column='FLG_CESSATO', null=True)),
                ('dt_ins', models.DateField(db_column='DT_INS')),
                ('dt_mod', models.DateField(blank=True, db_column='DT_MOD', null=True)),
                ('user_ins', models.ForeignKey(blank=True, db_column='USER_INS_ID', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_ins_personale', to=settings.AUTH_USER_MODEL)),
                ('user_mod', models.ForeignKey(blank=True, db_column='USER_MOD_ID', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_mod_personale', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Personale',
                'db_table': 'PERSONALE',
            },
        ),
        migrations.CreateModel(
            name='RicercaAster1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_ins', models.DateTimeField(auto_now_add=True, db_column='DT_INS')),
                ('dt_mod', models.DateTimeField(auto_now=True, db_column='DT_MOD', null=True)),
                ('descrizione', models.TextField(db_column='DESCRIZIONE', max_length=200)),
                ('user_ins', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_ins_aster1', to=settings.AUTH_USER_MODEL)),
                ('user_mod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_mod_aster1', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Aster 1',
                'db_table': 'RICERCA_ASTER1',
                'ordering': ('descrizione',),
            },
        ),
        migrations.CreateModel(
            name='RicercaAster2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_ins', models.DateTimeField(auto_now_add=True, db_column='DT_INS')),
                ('dt_mod', models.DateTimeField(auto_now=True, db_column='DT_MOD', null=True)),
                ('descrizione', models.CharField(db_column='DESCRIZIONE', max_length=200)),
                ('ricerca_aster1', models.ForeignKey(db_column='RICERCA_ASTER1_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='ricerca_app.ricercaaster1')),
                ('user_ins', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_ins_aster2', to=settings.AUTH_USER_MODEL)),
                ('user_mod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_mod_aster2', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Aster 2',
                'db_table': 'RICERCA_ASTER2',
                'ordering': ('ricerca_aster1',),
            },
        ),
        migrations.CreateModel(
            name='RicercaErc1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_ins', models.DateTimeField(auto_now_add=True, db_column='DT_INS')),
                ('dt_mod', models.DateTimeField(auto_now=True, db_column='DT_MOD', null=True)),
                ('cod_erc1', models.CharField(db_column='COD_ERC1', max_length=40, unique=True)),
                ('descrizione', models.TextField(db_column='DESCRIZIONE', max_length=200)),
                ('user_ins', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_ins_erc1', to=settings.AUTH_USER_MODEL)),
                ('user_mod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_mod_erc1', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Erc 1',
                'db_table': 'RICERCA_ERC1',
            },
        ),
        migrations.CreateModel(
            name='RicercaErc2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_ins', models.DateTimeField(auto_now_add=True, db_column='DT_INS')),
                ('dt_mod', models.DateTimeField(auto_now=True, db_column='DT_MOD', null=True)),
                ('cod_erc2', models.CharField(db_column='COD_ERC2', max_length=60, unique=True)),
                ('descrizione', models.TextField(db_column='DESCRIZIONE', max_length=200)),
                ('ricerca_erc1', models.ForeignKey(blank=True, db_column='RICERCA_ERC1_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ricerca_app.ricercaerc1')),
                ('user_ins', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_ins_erc2', to=settings.AUTH_USER_MODEL)),
                ('user_mod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_mod_erc2', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Erc 2',
                'db_table': 'RICERCA_ERC2',
            },
        ),
        migrations.CreateModel(
            name='TerritorioIt',
            fields=[
                ('cd_catasto', models.OneToOneField(db_column='CD_CATASTO', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='ricerca_app.comuniall')),
                ('cd_istat', models.CharField(blank=True, db_column='CD_ISTAT', max_length=6, null=True)),
                ('ds_comune', models.CharField(blank=True, db_column='DS_COMUNE', max_length=255, null=True)),
                ('cd_sigla', models.CharField(blank=True, db_column='CD_SIGLA', max_length=2, null=True)),
                ('ds_provincia', models.CharField(blank=True, db_column='DS_PROVINCIA', max_length=255, null=True)),
                ('cd_770_regio', models.CharField(blank=True, db_column='CD_770_REGIO', max_length=2, null=True)),
                ('ds_regione', models.CharField(blank=True, db_column='DS_REGIONE', max_length=255, null=True)),
            ],
            options={
                'db_table': 'TERRITORIO_IT',
            },
        ),
        migrations.CreateModel(
            name='RicercaLineaBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_ins', models.DateTimeField(auto_now_add=True, db_column='DT_INS')),
                ('dt_mod', models.DateTimeField(auto_now=True, db_column='DT_MOD', null=True)),
                ('descrizione', models.CharField(db_column='DESCRIZIONE', max_length=400)),
                ('descr_pubblicaz_prog_brevetto', models.TextField(blank=True, db_column='DESCR_PUBBLICAZ_PROG_BREVETTO', max_length=1000, null=True)),
                ('anno', models.IntegerField(blank=True, db_column='ANNO', null=True)),
                ('ricerca_erc2', models.ForeignKey(db_column='RICERCA_ERC2_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='ricerca_app.ricercaerc2')),
                ('user_ins', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_ins_lb', to=settings.AUTH_USER_MODEL)),
                ('user_mod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_mod_lb', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Linea di Base',
                'db_table': 'RICERCA_LINEA_BASE',
                'ordering': ('ricerca_erc2',),
            },
        ),
        migrations.CreateModel(
            name='RicercaLineaApplicata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_ins', models.DateTimeField(auto_now_add=True, db_column='DT_INS')),
                ('dt_mod', models.DateTimeField(auto_now=True, db_column='DT_MOD', null=True)),
                ('descrizione', models.CharField(db_column='DESCRIZIONE', max_length=400)),
                ('descr_pubblicaz_prog_brevetto', models.TextField(blank=True, db_column='DESCR_PUBBLICAZ_PROG_BREVETTO', max_length=1000, null=True)),
                ('anno', models.IntegerField(blank=True, db_column='ANNO', null=True)),
                ('ricerca_aster2', models.ForeignKey(db_column='RICERCA_ASTER2_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='ricerca_app.ricercaaster2')),
                ('user_ins', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_ins_la', to=settings.AUTH_USER_MODEL)),
                ('user_mod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_mod_la', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Linea Applicata',
                'db_table': 'RICERCA_LINEA_APPLICATA',
                'ordering': ('ricerca_aster2',),
            },
        ),
        migrations.CreateModel(
            name='RicercaGruppo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_ins', models.DateTimeField(auto_now_add=True, db_column='DT_INS')),
                ('dt_mod', models.DateTimeField(auto_now=True, db_column='DT_MOD', null=True)),
                ('nome', models.CharField(db_column='NOME', max_length=200)),
                ('descrizione', models.TextField(db_column='DESCRIZIONE', max_length=2000)),
                ('user_ins', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_ins_rg', to=settings.AUTH_USER_MODEL)),
                ('user_mod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_mod_rg', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Gruppo di Ricerca',
                'db_table': 'RICERCA_GRUPPO',
                'ordering': ('nome',),
            },
        ),
        migrations.CreateModel(
            name='RicercaDocenteLineaBase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_ins', models.DateTimeField(auto_now_add=True, db_column='DT_INS')),
                ('dt_mod', models.DateTimeField(auto_now=True, db_column='DT_MOD', null=True)),
                ('dt_inizio', models.DateField(blank=True, db_column='DT_INIZIO', null=True)),
                ('dt_fine', models.DateField(blank=True, db_column='DT_FINE', null=True)),
                ('docente', models.ForeignKey(blank=True, db_column='PERSONALE_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ricerca_app.personale')),
                ('ricerca_linea_base', models.ForeignKey(blank=True, db_column='RICERCA_LINEA_BASE_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ricerca_app.ricercalineabase')),
                ('user_ins', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_ins_dlb', to=settings.AUTH_USER_MODEL)),
                ('user_mod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_mod_dlb', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Docente Linea Base',
                'db_table': 'RICERCA_DOCENTE_LINEA_BASE',
            },
        ),
        migrations.CreateModel(
            name='RicercaDocenteLineaApplicata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_ins', models.DateTimeField(auto_now_add=True, db_column='DT_INS')),
                ('dt_mod', models.DateTimeField(auto_now=True, db_column='DT_MOD', null=True)),
                ('dt_inizio', models.DateField(blank=True, db_column='DT_INIZIO', null=True)),
                ('dt_fine', models.DateField(blank=True, db_column='DT_FINE', null=True)),
                ('docente', models.ForeignKey(blank=True, db_column='PERSONALE_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ricerca_app.personale')),
                ('ricerca_linea_applicata', models.ForeignKey(blank=True, db_column='RICERCA_LINEA_APPLICATA_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ricerca_app.ricercalineaapplicata')),
                ('user_ins', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_ins_dla', to=settings.AUTH_USER_MODEL)),
                ('user_mod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_mod_dla', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Docente Linea Applicata',
                'db_table': 'RICERCA_DOCENTE_LINEA_APPLICATA',
            },
        ),
        migrations.CreateModel(
            name='RicercaDocenteGruppo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dt_ins', models.DateTimeField(auto_now_add=True, db_column='DT_INS')),
                ('dt_mod', models.DateTimeField(auto_now=True, db_column='DT_MOD', null=True)),
                ('dt_inizio', models.DateField(blank=True, db_column='DT_INIZIO', null=True)),
                ('dt_fine', models.DateField(blank=True, db_column='DT_FINE', null=True)),
                ('docente', models.ForeignKey(blank=True, db_column='PERSONALE_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ricerca_app.personale')),
                ('ricerca_gruppo', models.ForeignKey(db_column='RICERCA_GRUPPO_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='ricerca_app.ricercagruppo')),
                ('user_ins', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_ins_dg', to=settings.AUTH_USER_MODEL)),
                ('user_mod', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_mod_dg', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Docente Gruppi di Ricerca',
                'db_table': 'RICERCA_DOCENTE_GRUPPO',
                'ordering': ('-dt_fine',),
            },
        ),
        migrations.CreateModel(
            name='DidatticaTestiRegolamento',
            fields=[
                ('txt_id', models.IntegerField(db_column='TXT_ID', primary_key=True, serialize=False)),
                ('tipo_testo_regdid_cod', models.CharField(db_column='TIPO_TESTO_REGDID_COD', max_length=100)),
                ('tipo_testo_regdid_des', models.CharField(blank=True, db_column='TIPO_TESTO_REGDID_DES', max_length=255, null=True)),
                ('clob_txt_ita', models.TextField(blank=True, db_column='CLOB_TXT_ITA', null=True)),
                ('clob_txt_eng', models.TextField(blank=True, db_column='CLOB_TXT_ENG', null=True)),
                ('profilo', models.TextField(blank=True, db_column='PROFILO', null=True)),
                ('profilo_eng', models.TextField(blank=True, db_column='PROFILO_ENG', null=True)),
                ('dt_ins', models.DateTimeField(blank=True, db_column='DT_INS', null=True)),
                ('dt_ins_txt_clob_ita', models.DateTimeField(blank=True, db_column='DT_INS_TXT_CLOB_ITA', null=True)),
                ('dt_ins_txt_clob_eng', models.DateTimeField(blank=True, db_column='DT_INS_TXT_CLOB_ENG', null=True)),
                ('dt_mod', models.DateTimeField(blank=True, db_column='DT_MOD', null=True)),
                ('regdid', models.ForeignKey(db_column='REGDID_ID', on_delete=django.db.models.deletion.DO_NOTHING, to='ricerca_app.didatticaregolamento')),
            ],
            options={
                'db_table': 'DIDATTICA_TESTI_REGOLAMENTO',
            },
        ),
        migrations.CreateModel(
            name='DidatticaCdsLingua',
            fields=[
                ('lin_did_ord_id', models.IntegerField(db_column='LIN_DID_ORD_ID', primary_key=True, serialize=False)),
                ('lingua_id', models.IntegerField(blank=True, db_column='LINGUA_ID', null=True)),
                ('lingua_des_it', models.CharField(blank=True, db_column='LINGUA_DES_IT', max_length=100, null=True)),
                ('iso6392_cod', models.CharField(blank=True, db_column='ISO6392_COD', max_length=3, null=True)),
                ('lingua_des_eng', models.CharField(blank=True, db_column='LINGUA_DES_ENG', max_length=100, null=True)),
                ('cdsord', models.ForeignKey(blank=True, db_column='CDSORD_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ricerca_app.didatticacds', to_field='cdsord_id')),
            ],
            options={
                'db_table': 'DIDATTICA_CDS_LINGUA',
            },
        ),
        migrations.AddField(
            model_name='didatticacds',
            name='dip',
            field=models.ForeignKey(blank=True, db_column='DIP_ID', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='ricerca_app.didatticadipartimento'),
        ),
    ]
