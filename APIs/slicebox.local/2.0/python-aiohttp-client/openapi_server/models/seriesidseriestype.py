# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.seriestype import Seriestype
from openapi_server import util


class Seriesidseriestype(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, seriesid: int=None, seriestype: Seriestype=None):
        """Seriesidseriestype - a model defined in OpenAPI

        :param seriesid: The seriesid of this Seriesidseriestype.
        :param seriestype: The seriestype of this Seriesidseriestype.
        """
        self.openapi_types = {
            'seriesid': int,
            'seriestype': Seriestype
        }

        self.attribute_map = {
            'seriesid': 'seriesid',
            'seriestype': 'seriestype'
        }

        self._seriesid = seriesid
        self._seriestype = seriestype

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Seriesidseriestype':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The seriesidseriestype of this Seriesidseriestype.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def seriesid(self):
        """Gets the seriesid of this Seriesidseriestype.


        :return: The seriesid of this Seriesidseriestype.
        :rtype: int
        """
        return self._seriesid

    @seriesid.setter
    def seriesid(self, seriesid):
        """Sets the seriesid of this Seriesidseriestype.


        :param seriesid: The seriesid of this Seriesidseriestype.
        :type seriesid: int
        """

        self._seriesid = seriesid

    @property
    def seriestype(self):
        """Gets the seriestype of this Seriesidseriestype.


        :return: The seriestype of this Seriesidseriestype.
        :rtype: Seriestype
        """
        return self._seriestype

    @seriestype.setter
    def seriestype(self, seriestype):
        """Sets the seriestype of this Seriesidseriestype.


        :param seriestype: The seriestype of this Seriesidseriestype.
        :type seriestype: Seriestype
        """

        self._seriestype = seriestype
