from rest_framework import serializers

from .models import *


class PersonaleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Personale
        # Todo add @properties to Model to hanlde childs elements
        fields = ['nome', 'cognome', ]  # 'matricola', 'cod_fis']
        #  fields = '__all__'


class RicercaAster1Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RicercaAster1
        fields = ['descrizione', ]


class RicercaAster2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RicercaAster2
        fields = ['descrizione', ]


class RicercaErc1Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RicercaErc1
        fields = ['cod_erc1', 'descrizione', ]


class RicercaErc2Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RicercaErc2
        fields = ['cod_erc2', 'descrizione', 'ricerca_erc1']


class RicercaDocenteGruppoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RicercaDocenteGruppo
        fields = ['docente', 'ricerca_gruppo', 'dt_inizio', 'dt_fine']


class RicercaDocenteLineaApplicataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RicercaDocenteLineaApplicata
        fields = ['docente', 'ricerca_linea_applicata', 'dt_inizio', 'dt_fine']


class RicercaDocenteLineaBaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RicercaDocenteLineaBase
        fields = ['docente', 'ricerca_linea_base', 'dt_inizio', 'dt_fine']


class RicercaGruppoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RicercaGruppo
        fields = ['nome', 'descrizione']


class RicercaLineaApplicataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RicercaLineaApplicata
        fields = ['descrizione', 'ricerca_aster2',
                  'descr_pubblicaz_prog_brevetto', 'anno']


class RicercaLineaBaseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RicercaLineaBase
        fields = ['descrizione', 'ricerca_erc2',
                  'descr_pubblicaz_prog_brevetto', 'anno']


# ------------------------------------- #

# class DidatticaDipartimentoSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = DidatticaDipartimento
#         fields = ['dip_id', 'dip_cod', 'dip_nome_breve', 'dip_des_it']
#
#
# class DidatticaCdsInDipartimentoListSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = DidatticaCds
#         fields = ['cds_id', 'cds_cod', 'nome_cds_it', 'dip_id']
#
#
# class DidatticaCdsSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = DidatticaCds
#         fields = ['cds_id', 'cds_cod', 'nome_cds_it', 'dip_id']
#
#
# # class DidatticaLinguePerCdsListSerializer(serializers.HyperlinkedModelSerializer):
# class DidatticaLinguePerCdsListSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = DidatticaCdsLingua
#         fields = ['cdsord', 'lingua_des_it', 'lingua_des_eng']


class CdSListSerializer(serializers.Serializer):
    def to_representation(self, instance):
        cds, reg, lingua = instance[:3]
        data = super().to_representation(instance)
        data.update(self.to_dict(cds, reg, lingua,
                                 str(self.context['request'].LANGUAGE_CODE)))
                                 # str(self.context['language'])))
        return data

    def create(self, validated_data):
        super().create(validated_data)

    def update(self, instance, validated_data):
        super().update(instance, validated_data)

    @staticmethod
    def to_dict(cds: DidatticaCds,
                reg: DidatticaRegolamento,
                cds_lang: DidatticaCdsLingua,
                req_lang='en'):
        return {
            'RegDidId': reg.regdid_id,
            'CdSId': reg.cds_id,
            'AcademicYear': reg.aa_reg_did,
            'CdSName': cds.nome_cds_it if req_lang == 'it' or cds.nome_cds_eng is None else cds.nome_cds_eng,
            'DepartmentId': cds.dip.dip_cod,
            'DepartmentName': cds.dip.dip_des_it if req_lang == 'it' or cds.dip.dip_des_eng is None else cds.dip.dip_des_eng,
            'CourseType': cds.tipo_corso_cod,
            'CourseClassId': cds.cla_miur_cod,
            'CourseClassName': cds.cla_miur_des,
            'CdSLanguage': cds_lang.iso6392_cod,
            'CdSDuration': cds.durata_anni,
            'CdSECTS': cds.valore_min,
            'CdSAttendance': reg.frequenza_obbligatoria
        }
