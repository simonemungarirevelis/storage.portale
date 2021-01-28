from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import (DidatticaCds, DidatticaCdsLingua, DidatticaRegolamento, DidatticaDipartimento)


class ContextUnitTest(TestCase):

    @classmethod
    def create_user(cls, **kwargs):
        data = {'username': 'foo',
                'first_name': 'foo',
                'last_name': 'bar',
                'email': 'that@mail.org'}
        for k, v in kwargs.items():
            data[k] = v
        user = get_user_model().objects.create(**data)
        return user


class DidatticaCdsUnitTest(TestCase):

    @classmethod
    def create_didatticaCds(cls, **kwargs):
        data = {
            'cds_id': 1,
            'nome_cds_it': 'informatica',
            'nome_cds_eng': 'computerscience',
            'dip_id': 1,
            'tipo_corso_cod': '1',
            'cla_miur_cod': '1',
            'cla_miur_des': 'laurea in informatica',
            'cdsduration': 3,
            'cdsects': 180,
            'cdsord_id': 1,
        }
        for k, v in kwargs.items():
            data[k] = v

        obj = DidatticaCds.objects.create(**data)
        return obj

class DidatticaCdsLinguaUnitTest(TestCase):

    @classmethod
    def create_didatticaCdsLingua(cls, **kwargs):
        data = {
            'lin_did_ord_id': 1,
            'iso6392_cod': 'ita',
        }
        for k, v in kwargs.items():
            data[k] = v

        obj = DidatticaCdsLingua.objects.create(**data)
        return obj

class DidatticaRegolamentoUnitTest(TestCase):

    @classmethod
    def create_didatticaRegolamento(cls, **kwargs):
        data = {
            'regdid_id': 1,
            'cds_id' : 1,
            'aa_reg_did': 2020,
            'frequenza_obbligatoria': 0,
            'titolo_congiunto_cod': 'N',
        }
        for k, v in kwargs.items():
            data[k] = v

        obj = DidatticaRegolamento.objects.create(**data)
        return obj

class DidatticaDipartimentoUnitTest(TestCase):

    @classmethod
    def create_didatticaDipartimento(cls, **kwargs):
        data = {
            'dip_id': 1,
            'dip_cod': '1',
            'dip_des_it': 'matematica e informatica',
            'dip_des_eng': 'math and computer science'
        }
        for k, v in kwargs.items():
            data[k] = v

        obj = DidatticaDipartimento.objects.create(**data)
        return obj