from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import (CdSList)


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


class CdsListUnitTest(TestCase):

    @classmethod
    def create_cdslist(cls, **kwargs):
        data = {
            'regdidid': 1,
            'cdsid': 1,
            'academicyear': 2020,
            'cdsnameit': 'informatica',
            'cdsnameeng': 'computerscience',
            'departmentid': '1',
            'departmentnameit': 'matematicainformatica',
            'departmentnameeng': 'mathcomputerscience',
            'coursetypeid': '1',
            'coursetypename': 'laurea',
            'courseclassid': '1',
            'courseclassname': 'laurea in informatica',
            'cdslanguageit': 'italiano',
            'cdslanguageeng': 'italian',
            'cdsduration': 3,
            'cdsects': 180,
            'cdsattendance': 0,
            'jointdegree': 'N',
        }
        for k, v in kwargs.items():
            data[k] = v

        obj = CdSList.objects.create(**data)
        return obj
