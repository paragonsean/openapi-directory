# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None, _false: str=None):
        """LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner - a model defined in OpenAPI

        :param name: The name of this LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner.
        :param _false: The _false of this LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner.
        """
        self.openapi_types = {
            'name': str,
            '_false': str
        }

        self.attribute_map = {
            'name': 'name',
            '_false': 'false'
        }

        self._name = name
        self.__false = _false

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _legal_search__get_default_response_advisory_opinions_inner_ao_citations_inner of this LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner.


        :return: The name of this LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner.


        :param name: The name of this LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner.
        :type name: str
        """

        self._name = name

    @property
    def _false(self):
        """Gets the _false of this LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner.


        :return: The _false of this LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner.
        :rtype: str
        """
        return self.__false

    @_false.setter
    def _false(self, _false):
        """Sets the _false of this LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner.


        :param _false: The _false of this LegalSearchGetDefaultResponseAdvisoryOpinionsInnerAoCitationsInner.
        :type _false: str
        """

        self.__false = _false
