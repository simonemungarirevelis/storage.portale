from django.shortcuts import render
from rest_framework import generics, viewsets, permissions

from . models import *
from . serializers import *


# permissions.IsAuthenticatedOrReadOnly
# allow authenticated users to perform any request. Requests for
# unauthorised users will only be permitted if the request method is
# one of the "safe" methods; GET, HEAD or OPTIONS

class ApiResourceList(generics.ListCreateAPIView):
    permission_classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
    allowed_methods = ('GET',)

    def perform_create(self, serializer):
        serializer.save(user_ins=self.request.user)


class ApiResourceDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    allowed_methods = ('GET',)

    def perform_update(self, serializer):
        serializer.save(user_mod=self.request.user)

# =================================================


class ApiPersonaleList(ApiResourceList):
    description = 'Available Personale, Professors and Researchers'
    queryset = Personale.objects.all()
    serializer_class = PersonaleSerializer


class ApiPersonaleDetail(ApiResourceDetail):
    description = 'Detail of Persona'
    queryset = Personale.objects.all()
    serializer_class = PersonaleSerializer


# =================================================

class ApiRicercaAster1List(ApiResourceList):
    description = 'Available Aster 1'
    queryset = RicercaAster1.objects.all()
    serializer_class = RicercaAster1Serializer


class ApiRicercaAster1Detail(ApiResourceDetail):
    description = 'Aster 1 Details'
    queryset = RicercaAster1.objects.all()
    serializer_class = RicercaAster1Serializer


# =================================================

class ApiRicercaAster2List(ApiResourceList):
    description = 'Available Aster 2'
    queryset = RicercaAster2.objects.all()
    serializer_class = RicercaAster2Serializer


class ApiRicercaAster2Detail(ApiResourceDetail):
    description = 'Aster 2 Details'
    queryset = RicercaAster2.objects.all()
    serializer_class = RicercaAster2Serializer


# =================================================

class ApiRicercaErc1List(ApiResourceList):
    description = 'Available Erc 1'
    queryset = RicercaErc1.objects.all()
    serializer_class = RicercaErc1Serializer


class ApiRicercaErc1Detail(ApiResourceDetail):
    description = 'Erc 1 Details'
    queryset = RicercaErc1.objects.all()
    serializer_class = RicercaErc1Serializer


# =================================================

class ApiRicercaErc2List(ApiResourceList):
    description = 'Available Erc 2'
    queryset = RicercaErc2.objects.all()
    serializer_class = RicercaErc2Serializer


class ApiRicercaErc2Detail(ApiResourceDetail):
    description = 'Erc 2 Details'
    queryset = RicercaErc2.objects.all()
    serializer_class = RicercaErc2Serializer


# =================================================

class ApiRicercaDocenteGruppoList(ApiResourceList):
    description = 'List of Professors/Researchers in which Research Groups'
    queryset = RicercaDocenteGruppo.objects.all()
    serializer_class = RicercaDocenteGruppoSerializer


class ApiRicercaDocenteGruppoDetail(ApiResourceDetail):
    description = 'Details of Professors/Researchers in which Research Groups'
    queryset = RicercaDocenteGruppo.objects.all()
    serializer_class = RicercaDocenteGruppoSerializer


# =================================================

class ApiRicercaDocenteLineaApplicataList(ApiResourceList):
    description = 'List of Professors/Researchers and Applied Lines'
    queryset = RicercaDocenteLineaApplicata.objects.all()
    serializer_class = RicercaDocenteLineaApplicataSerializer


class ApiRicercaDocenteLineaApplicataDetail(ApiResourceDetail):
    description = 'Details of a Professor/Researcher in an Applied Line'
    queryset = RicercaDocenteLineaApplicata.objects.all()
    serializer_class = RicercaDocenteLineaApplicataSerializer


# =================================================

class ApiRicercaDocenteLineaBaseList(ApiResourceList):
    description = 'List of Base Lines'
    queryset = RicercaDocenteLineaBase.objects.all()
    serializer_class = RicercaDocenteLineaBaseSerializer


class ApiRicercaDocenteLineaBaseDetail(ApiResourceDetail):
    description = 'Details about a Base Line'
    queryset = RicercaDocenteLineaBase.objects.all()
    serializer_class = RicercaDocenteLineaBaseSerializer


# =================================================

class ApiRicercaGruppoList(ApiResourceList):
    description = 'List of Research Groups'
    queryset = RicercaGruppo.objects.all()
    serializer_class = RicercaGruppoSerializer


class ApiRicercaGruppoDetail(ApiResourceDetail):
    description = 'Details of a Research Group'
    queryset = RicercaGruppo.objects.all()
    serializer_class = RicercaGruppoSerializer


# =================================================

class ApiRicercaLineaApplicataList(ApiResourceList):
    description = 'List of Applied Lines'
    queryset = RicercaLineaApplicata.objects.all()
    serializer_class = RicercaLineaApplicataSerializer


class ApiRicercaLineaApplicataDetail(ApiResourceDetail):
    description = 'Detail of an Applied Line'
    queryset = RicercaLineaApplicata.objects.all()
    serializer_class = RicercaLineaApplicataSerializer


# =================================================

class ApiRicercaLineaBaseList(ApiResourceList):
    description = 'List of Base Lines'
    queryset = RicercaLineaBase.objects.all()
    serializer_class = RicercaLineaBaseSerializer


class ApiRicercaLineaBaseDetail(ApiResourceDetail):
    description = 'Details of a Base Line'
    queryset = RicercaLineaBase.objects.all()
    serializer_class = RicercaLineaBaseSerializer


# =================================================

# TODO:
#  - Paginazione: aggiungere paginatore (custom?) a classi astratte || aggiungere paginatore a settings
#  - admin CRUD classi nuove

# class ApiDidatticaDipartimentoList(ApiResourceList):
#     description = 'Set of all Dipartimenti'
#     queryset = DidatticaDipartimento.objects.all()
#     serializer_class = DidatticaDipartimentoSerializer
#
#
# class ApiDidatticaDipartimentoDetail(ApiResourceDetail):
#     description = 'Detail of Dipartimento'
#     queryset = DidatticaDipartimento.objects.all()
#     serializer_class = DidatticaDipartimentoSerializer
#
#
# class ApiDidatticaCdsList(ApiResourceList):
#     description = 'Set of all CDS'
#     queryset = DidatticaCds.objects.all()
#     serializer_class = DidatticaCdsSerializer
#
#
# class ApiDidatticaCdsDetail(ApiResourceDetail):
#     description = 'Detail of CDS'
#     queryset = DidatticaCds.objects.all()
#     serializer_class = DidatticaCdsSerializer
#
#
# class ApiDidatticaCdsInDipartimentoList(ApiResourceList):
#     description = 'Set of all CDS in a Dipartimento'
#     serializer_class = DidatticaCdsInDipartimentoListSerializer
#
#     def get_queryset(self):
#         if self.kwargs.get('pk', None):
#             return DidatticaCds.objects.filter(dip_id=self.kwargs['pk'])
#         return DidatticaCds.objects.all()
#
#
# class ApiDidatticaLinguePerCdsList(ApiResourceList):
#     description = 'Set of all languages a CDS is provided in'
#     serializer_class = DidatticaLinguePerCdsListSerializer
#
#     def get_queryset(self):
#         if self.kwargs.get('pk', None):
#             return DidatticaCdsLingua.objects.filter(cdsord__cds_id=self.kwargs['pk'])
#         return DidatticaCdsLingua.objects.all()

import operator
from functools import reduce
from django.db.models import Q
from rest_framework import filters


class ApiCdSList(ApiResourceList):
    description = ''
    serializer_class = CdSListSerializer

    filter_backends = [filters.SearchFilter]
    search_fields=['academicyear', 'departmentid']

    # def get_serializer(self, *args, **kwargs):
    #     ...

    def get_queryset(self):
        # all 'non-service' parameters but `keywords' (treated differently)
        input_params = {k: self.request.GET.get(k) for k in [
            'academicyear',
            'departmentid',
            'departmentname',
            'coursetype',
            'courseclassid',
            'courseclassname',
            'cdslanguage',
            'jointdegree',
        ]}

        # first filtering
        items = CdSList.objects.filter(**{k: v for (k, v) in input_params.items()
                                          if v})

        # refine the selection if `keywords' is a non-empty list of keywords
        input_param_keywords = self.request.GET.get('keywords')
        if input_param_keywords:
            kw = input_param_keywords.split(',')  # FIXME: cover all usual methods?
            language = self.request.GET.get('language')

            # choose Italian as both default and fallback option, English otherwise
            if language is None or str(language).upper() == 'IT':
                items = items.filter(
                    reduce(operator.and_, [Q(cdsnameit__icontains=e) for e in kw])
                )
            else:
                items = items.filter(
                    reduce(operator.and_, [Q(cdsnameeng__icontains=e) for e in kw])
                )

        # TODO: questione orderby:order

        return items

