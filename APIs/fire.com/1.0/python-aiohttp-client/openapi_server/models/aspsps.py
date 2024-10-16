# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.aspsp import Aspsp
from openapi_server import util


class Aspsps(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, aspsps: List[Aspsp]=None, total: int=None):
        """Aspsps - a model defined in OpenAPI

        :param aspsps: The aspsps of this Aspsps.
        :param total: The total of this Aspsps.
        """
        self.openapi_types = {
            'aspsps': List[Aspsp],
            'total': int
        }

        self.attribute_map = {
            'aspsps': 'aspsps',
            'total': 'total'
        }

        self._aspsps = aspsps
        self._total = total

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Aspsps':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The aspsps of this Aspsps.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def aspsps(self):
        """Gets the aspsps of this Aspsps.


        :return: The aspsps of this Aspsps.
        :rtype: List[Aspsp]
        """
        return self._aspsps

    @aspsps.setter
    def aspsps(self, aspsps):
        """Sets the aspsps of this Aspsps.


        :param aspsps: The aspsps of this Aspsps.
        :type aspsps: List[Aspsp]
        """

        self._aspsps = aspsps

    @property
    def total(self):
        """Gets the total of this Aspsps.

        The total number of ASPSPs in the list.

        :return: The total of this Aspsps.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this Aspsps.

        The total number of ASPSPs in the list.

        :param total: The total of this Aspsps.
        :type total: int
        """

        self._total = total
