# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ApiCoreDtoClickStreamHitOsInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, family_id: int=None, family_name: str=None, id: int=None, name: str=None):
        """ApiCoreDtoClickStreamHitOsInfo - a model defined in OpenAPI

        :param family_id: The family_id of this ApiCoreDtoClickStreamHitOsInfo.
        :param family_name: The family_name of this ApiCoreDtoClickStreamHitOsInfo.
        :param id: The id of this ApiCoreDtoClickStreamHitOsInfo.
        :param name: The name of this ApiCoreDtoClickStreamHitOsInfo.
        """
        self.openapi_types = {
            'family_id': int,
            'family_name': str,
            'id': int,
            'name': str
        }

        self.attribute_map = {
            'family_id': 'familyId',
            'family_name': 'familyName',
            'id': 'id',
            'name': 'name'
        }

        self._family_id = family_id
        self._family_name = family_name
        self._id = id
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ApiCoreDtoClickStreamHitOsInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Api.Core.Dto.ClickStream.HitOsInfo of this ApiCoreDtoClickStreamHitOsInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def family_id(self):
        """Gets the family_id of this ApiCoreDtoClickStreamHitOsInfo.


        :return: The family_id of this ApiCoreDtoClickStreamHitOsInfo.
        :rtype: int
        """
        return self._family_id

    @family_id.setter
    def family_id(self, family_id):
        """Sets the family_id of this ApiCoreDtoClickStreamHitOsInfo.


        :param family_id: The family_id of this ApiCoreDtoClickStreamHitOsInfo.
        :type family_id: int
        """

        self._family_id = family_id

    @property
    def family_name(self):
        """Gets the family_name of this ApiCoreDtoClickStreamHitOsInfo.


        :return: The family_name of this ApiCoreDtoClickStreamHitOsInfo.
        :rtype: str
        """
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        """Sets the family_name of this ApiCoreDtoClickStreamHitOsInfo.


        :param family_name: The family_name of this ApiCoreDtoClickStreamHitOsInfo.
        :type family_name: str
        """

        self._family_name = family_name

    @property
    def id(self):
        """Gets the id of this ApiCoreDtoClickStreamHitOsInfo.


        :return: The id of this ApiCoreDtoClickStreamHitOsInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiCoreDtoClickStreamHitOsInfo.


        :param id: The id of this ApiCoreDtoClickStreamHitOsInfo.
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ApiCoreDtoClickStreamHitOsInfo.


        :return: The name of this ApiCoreDtoClickStreamHitOsInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiCoreDtoClickStreamHitOsInfo.


        :param name: The name of this ApiCoreDtoClickStreamHitOsInfo.
        :type name: str
        """

        self._name = name
