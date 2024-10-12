# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.legal_search_get_default_response_adrs_inner_dispositions_inner_citations_inner import LegalSearchGetDefaultResponseAdrsInnerDispositionsInnerCitationsInner
from openapi_server import util


class LegalSearchGetDefaultResponseAdrsInnerDispositionsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, citations: List[LegalSearchGetDefaultResponseAdrsInnerDispositionsInnerCitationsInner]=None, disposition: str=None, penalty: float=None, respondent: str=None):
        """LegalSearchGetDefaultResponseAdrsInnerDispositionsInner - a model defined in OpenAPI

        :param citations: The citations of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.
        :param disposition: The disposition of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.
        :param penalty: The penalty of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.
        :param respondent: The respondent of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.
        """
        self.openapi_types = {
            'citations': List[LegalSearchGetDefaultResponseAdrsInnerDispositionsInnerCitationsInner],
            'disposition': str,
            'penalty': float,
            'respondent': str
        }

        self.attribute_map = {
            'citations': 'citations',
            'disposition': 'disposition',
            'penalty': 'penalty',
            'respondent': 'respondent'
        }

        self._citations = citations
        self._disposition = disposition
        self._penalty = penalty
        self._respondent = respondent

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LegalSearchGetDefaultResponseAdrsInnerDispositionsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _legal_search__get_default_response_adrs_inner_dispositions_inner of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def citations(self):
        """Gets the citations of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.


        :return: The citations of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.
        :rtype: List[LegalSearchGetDefaultResponseAdrsInnerDispositionsInnerCitationsInner]
        """
        return self._citations

    @citations.setter
    def citations(self, citations):
        """Sets the citations of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.


        :param citations: The citations of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.
        :type citations: List[LegalSearchGetDefaultResponseAdrsInnerDispositionsInnerCitationsInner]
        """

        self._citations = citations

    @property
    def disposition(self):
        """Gets the disposition of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.


        :return: The disposition of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.
        :rtype: str
        """
        return self._disposition

    @disposition.setter
    def disposition(self, disposition):
        """Sets the disposition of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.


        :param disposition: The disposition of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.
        :type disposition: str
        """

        self._disposition = disposition

    @property
    def penalty(self):
        """Gets the penalty of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.


        :return: The penalty of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.
        :rtype: float
        """
        return self._penalty

    @penalty.setter
    def penalty(self, penalty):
        """Sets the penalty of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.


        :param penalty: The penalty of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.
        :type penalty: float
        """

        self._penalty = penalty

    @property
    def respondent(self):
        """Gets the respondent of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.


        :return: The respondent of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.
        :rtype: str
        """
        return self._respondent

    @respondent.setter
    def respondent(self, respondent):
        """Sets the respondent of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.


        :param respondent: The respondent of this LegalSearchGetDefaultResponseAdrsInnerDispositionsInner.
        :type respondent: str
        """

        self._respondent = respondent
