import itertools
import operator

from functools import reduce
from rest_framework import generics, permissions
from rest_framework.response import Response
from django.db.models import Q, Prefetch

from .filters import *
from .serializers import *


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


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ #

class ApiEndpoint(generics.GenericAPIView):
    def get(self, obj):
        queryset = self.get_queryset()

        # TODO: pagination custom
        # page = self.paginate_queryset(queryset)
        # if page is not None:
        #     serializer = self.get_serializer(page, many=True)
        #     return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @staticmethod
    def build_filter_chain(params_dict, query_params):
        return reduce(operator.and_,
                      [Q(**{v: query_params.get(k)}) for (k, v) in params_dict.items() if query_params.get(k)],
                      Q())


class ApiCdSList(ApiEndpoint):
    description = ''
    serializer_class = CdSListSerializer
    filter_backends = [ApiCdsListFilter]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({'language': str(self.request.query_params.get('language', 'it')).lower()})
        return context

    def get_queryset(self):
        language = str(self.request.query_params.get('language', 'it')).lower()

        didatticacds_params_to_query_field = {
            'coursetype': 'tipo_corso_cod',
            'courseclassid': 'cla_miur_cod',
            'courseclassname': 'cla_miur_des__iexact',
            # 'courseclassgroup': ... unspecified atm
            'departmentid': 'dip__dip_cod',
            'departmentname': f'dip__dip_des_{ language == "it" and "it" or "eng" }__iexact',
        }

        didatticaregolamento_params_to_query_field = {
            'academicyear': 'aa_reg_did',
            'jointdegree': 'titolo_congiunto_cod',
        }

        didatticacdslingua_params_to_query_field = {
            'cdslanguage': 'iso6392_cod__iexact',
        }
        values_to_return = ('didatticaregolamento__regdid_id', 'cds_id')

        keywords = set(self.request.query_params.get('keywords', '').split(','))
        items = DidatticaCds.objects\
            .filter(reduce(operator.and_,
                           [Q(**{f'nome_cds_{ language == "it" and "it" or "eng"}__icontains': e}) for e in keywords],
                           Q()))\
            .filter(self.build_filter_chain(didatticacds_params_to_query_field,
                                            self.request.query_params))\
            .select_related('dip')\
            .prefetch_related(*[Prefetch('didatticaregolamento_set',
                                         queryset=DidatticaRegolamento.objects.filter(stato_regdid_cod='A').filter(
                                             self.build_filter_chain(
                                                 didatticaregolamento_params_to_query_field,
                                                 self.request.query_params))),
                                Prefetch('didatticacdslingua_set',
                                         queryset=DidatticaCdsLingua.objects.filter(
                                             self.build_filter_chain(
                                                 didatticacdslingua_params_to_query_field,
                                                 self.request.query_params)))
                                ])\
        .all()#.values('didatticaregolamento__regdid_id',
        #                        'didatticaregolamento__aa_reg_did',
        #                        'didatticaregolamento__frequenza_obbligatoria',
        #                        'dip__dip_cod',
        #                        'dip__dip_des_it',
        #                        'dip__dip_des_eng',
        #                        'didatticacdslingua__iso6392_cod',
        #                        'cds_id',
        #                        'nome_cds_it',
        #                        'nome_cds_eng',
        #                        'tipo_corso_cod',
        #                        'cla_miur_cod',
        #                        'cla_miur_des',
        #                        'durata_anni',
        #                        'valore_min').distinct()
        # print(len(items)) #535
        # return items

        res_set = set() #103
        for e in items:
            res_set |= set(itertools.product(*[
                [e],
                list(e.didatticaregolamento_set.all()),
                list(e.didatticacdslingua_set.all()),
            ]))

        print(len(res_set))
        return res_set


# class ApiCdSListView(ApiResourceList):
#     description = ''
#     serializer_class = CdSListSerializerView
#     filter_backends = [ApiCdsListFilter]
#
#     def get_serializer_context(self):
#         context = super().get_serializer_context()
#         context.update({'language': self.request.query_params.get('language', 'it')})
#         return context
#
#     def get_queryset(self):
#         # browser's Accept-Language header
#         # [?] no way to force it in the URL?
#         # language = self.request.LANGUAGE_CODE
#         # alternatively, get it from a parameter for now
#         language = self.request.query_params.get('language', 'it')
#
#         # all 'non-service' parameters but `keywords' (treated differently)
#         input_params = {k: self.request.query_params.get(k) for k in [
#             'academicyear',
#             'departmentid',
#             'departmentname',
#             'coursetype',
#             'courseclassid',
#             'courseclassname',
#             'cdslanguage',
#             'jointdegree',
#         ]}
#
#         # first filtering
#         items = CdSList.objects.filter(
#             **{k: v for (k, v) in input_params.items() if v})
#
#         # refine the selection if `keywords' is a non-empty list of keywords
#         input_param_keywords = self.request.query_params.get('keywords')
#         if input_param_keywords:
#             kw = input_param_keywords.split(',')
#
#             # choose Italian as both default and fallback option, English otherwise
#             if language is None or str(language).lower() == 'it':
#                 items = items.filter(
#                     reduce(operator.and_,
#                            [Q(cdsnameit__icontains=e) for e in kw])
#                 )
#             else:
#                 items = items.filter(
#                     reduce(operator.and_,
#                            [Q(cdsnameeng__icontains=e) for e in kw])
#                 )
#
#         return items
