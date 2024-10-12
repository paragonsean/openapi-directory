# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.query import Query
from openapi_server import util


class RelatedSearchesModule(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, value: List[Query]=None):
        """RelatedSearchesModule - a model defined in OpenAPI

        :param value: The value of this RelatedSearchesModule.
        """
        self.openapi_types = {
            'value': List[Query]
        }

        self.attribute_map = {
            'value': 'value'
        }

        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'RelatedSearchesModule':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The RelatedSearchesModule of this RelatedSearchesModule.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def value(self):
        """Gets the value of this RelatedSearchesModule.

        A list of related searches.

        :return: The value of this RelatedSearchesModule.
        :rtype: List[Query]
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this RelatedSearchesModule.

        A list of related searches.

        :param value: The value of this RelatedSearchesModule.
        :type value: List[Query]
        """

        self._value = value
