from django.db import connection
from django.test import TestCase, Client
from django.urls import reverse

from .util_test import ContextUnitTest, CdsListUnitTest


class ApiCdSListUnitTest(TestCase):

    def setUp(self):
        super().setUp()
        connection.cursor().execute("CREATE TABLE CDSLIST("
                                    "RegDidId int(11) PRIMARY KEY,"
                                    "CdSId int(11),"
                                    "AcademicYear int(11),"
                                    "CdSNameIT varchar(255),"
                                    "CdSNameENG varchar(255),"
                                    "DepartmentId varchar(40),"
                                    "DepartmentNameIT varchar(255),"
                                    "DepartmentNameENG varchar(255),"
                                    "CourseTypeId varchar(10),"
                                    "CourseTypeName varchar(80),"
                                    "CourseClassId varchar(10),"
                                    "CourseClassName varchar(255),"
                                    "CdsLanguageIT varchar(100),"
                                    "CdSLanguageENG varchar(100),"
                                    "CdSDuration int(11),"
                                    "CdSECTS int(11),"
                                    "CdSAttendance int(1),"
                                    "JointDegree varchar(100)"
                                    ");")

    def tearDown(self):
        connection.cursor().execute("DROP TABLE CDSLIST")

    def test_apicdslist(self):
        req = Client()
        user = ContextUnitTest.create_user(username='staff',
                                           is_staff=True)
        CdsListUnitTest.create_cdslist()
        url = reverse('ricerca:cdslist')

        # check url
        res = req.get(url)
        assert res.status_code == 200

        # GET
        data = {'academicyear': 2020}
        res = req.get(url, data=data)
        assert res.json()[0]['regdidid'] == 1
