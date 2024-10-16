# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.refund import Refund
from openapi_server import util


class EmbeddedRefunds(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, refunds: List[Refund]=None):
        """EmbeddedRefunds - a model defined in OpenAPI

        :param refunds: The refunds of this EmbeddedRefunds.
        """
        self.openapi_types = {
            'refunds': List[Refund]
        }

        self.attribute_map = {
            'refunds': 'refunds'
        }

        self._refunds = refunds

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EmbeddedRefunds':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The EmbeddedRefunds of this EmbeddedRefunds.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def refunds(self):
        """Gets the refunds of this EmbeddedRefunds.


        :return: The refunds of this EmbeddedRefunds.
        :rtype: List[Refund]
        """
        return self._refunds

    @refunds.setter
    def refunds(self, refunds):
        """Sets the refunds of this EmbeddedRefunds.


        :param refunds: The refunds of this EmbeddedRefunds.
        :type refunds: List[Refund]
        """

        self._refunds = refunds
