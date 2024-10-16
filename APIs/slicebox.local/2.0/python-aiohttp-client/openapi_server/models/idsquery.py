# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Idsquery(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, ids: List[int]=None):
        """Idsquery - a model defined in OpenAPI

        :param ids: The ids of this Idsquery.
        """
        self.openapi_types = {
            'ids': List[int]
        }

        self.attribute_map = {
            'ids': 'ids'
        }

        self._ids = ids

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Idsquery':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The idsquery of this Idsquery.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def ids(self):
        """Gets the ids of this Idsquery.


        :return: The ids of this Idsquery.
        :rtype: List[int]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        """Sets the ids of this Idsquery.


        :param ids: The ids of this Idsquery.
        :type ids: List[int]
        """
        if ids is None:
            raise ValueError("Invalid value for `ids`, must not be `None`")

        self._ids = ids
