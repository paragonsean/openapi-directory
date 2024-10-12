# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ApiCoreDtoClickStreamHitSource(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, name: str=None, param: str=None):
        """ApiCoreDtoClickStreamHitSource - a model defined in OpenAPI

        :param id: The id of this ApiCoreDtoClickStreamHitSource.
        :param name: The name of this ApiCoreDtoClickStreamHitSource.
        :param param: The param of this ApiCoreDtoClickStreamHitSource.
        """
        self.openapi_types = {
            'id': int,
            'name': str,
            'param': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'param': 'param'
        }

        self._id = id
        self._name = name
        self._param = param

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ApiCoreDtoClickStreamHitSource':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Api.Core.Dto.ClickStream.HitSource of this ApiCoreDtoClickStreamHitSource.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this ApiCoreDtoClickStreamHitSource.


        :return: The id of this ApiCoreDtoClickStreamHitSource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiCoreDtoClickStreamHitSource.


        :param id: The id of this ApiCoreDtoClickStreamHitSource.
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ApiCoreDtoClickStreamHitSource.


        :return: The name of this ApiCoreDtoClickStreamHitSource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiCoreDtoClickStreamHitSource.


        :param name: The name of this ApiCoreDtoClickStreamHitSource.
        :type name: str
        """

        self._name = name

    @property
    def param(self):
        """Gets the param of this ApiCoreDtoClickStreamHitSource.


        :return: The param of this ApiCoreDtoClickStreamHitSource.
        :rtype: str
        """
        return self._param

    @param.setter
    def param(self, param):
        """Sets the param of this ApiCoreDtoClickStreamHitSource.


        :param param: The param of this ApiCoreDtoClickStreamHitSource.
        :type param: str
        """

        self._param = param
