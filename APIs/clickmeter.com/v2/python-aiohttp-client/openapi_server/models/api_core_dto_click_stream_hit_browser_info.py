# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ApiCoreDtoClickStreamHitBrowserInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, browser_type: str=None, family_id: int=None, family_name: str=None, id: int=None, name: str=None):
        """ApiCoreDtoClickStreamHitBrowserInfo - a model defined in OpenAPI

        :param browser_type: The browser_type of this ApiCoreDtoClickStreamHitBrowserInfo.
        :param family_id: The family_id of this ApiCoreDtoClickStreamHitBrowserInfo.
        :param family_name: The family_name of this ApiCoreDtoClickStreamHitBrowserInfo.
        :param id: The id of this ApiCoreDtoClickStreamHitBrowserInfo.
        :param name: The name of this ApiCoreDtoClickStreamHitBrowserInfo.
        """
        self.openapi_types = {
            'browser_type': str,
            'family_id': int,
            'family_name': str,
            'id': int,
            'name': str
        }

        self.attribute_map = {
            'browser_type': 'browserType',
            'family_id': 'familyId',
            'family_name': 'familyName',
            'id': 'id',
            'name': 'name'
        }

        self._browser_type = browser_type
        self._family_id = family_id
        self._family_name = family_name
        self._id = id
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ApiCoreDtoClickStreamHitBrowserInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Api.Core.Dto.ClickStream.HitBrowserInfo of this ApiCoreDtoClickStreamHitBrowserInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def browser_type(self):
        """Gets the browser_type of this ApiCoreDtoClickStreamHitBrowserInfo.


        :return: The browser_type of this ApiCoreDtoClickStreamHitBrowserInfo.
        :rtype: str
        """
        return self._browser_type

    @browser_type.setter
    def browser_type(self, browser_type):
        """Sets the browser_type of this ApiCoreDtoClickStreamHitBrowserInfo.


        :param browser_type: The browser_type of this ApiCoreDtoClickStreamHitBrowserInfo.
        :type browser_type: str
        """

        self._browser_type = browser_type

    @property
    def family_id(self):
        """Gets the family_id of this ApiCoreDtoClickStreamHitBrowserInfo.


        :return: The family_id of this ApiCoreDtoClickStreamHitBrowserInfo.
        :rtype: int
        """
        return self._family_id

    @family_id.setter
    def family_id(self, family_id):
        """Sets the family_id of this ApiCoreDtoClickStreamHitBrowserInfo.


        :param family_id: The family_id of this ApiCoreDtoClickStreamHitBrowserInfo.
        :type family_id: int
        """

        self._family_id = family_id

    @property
    def family_name(self):
        """Gets the family_name of this ApiCoreDtoClickStreamHitBrowserInfo.


        :return: The family_name of this ApiCoreDtoClickStreamHitBrowserInfo.
        :rtype: str
        """
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        """Sets the family_name of this ApiCoreDtoClickStreamHitBrowserInfo.


        :param family_name: The family_name of this ApiCoreDtoClickStreamHitBrowserInfo.
        :type family_name: str
        """

        self._family_name = family_name

    @property
    def id(self):
        """Gets the id of this ApiCoreDtoClickStreamHitBrowserInfo.


        :return: The id of this ApiCoreDtoClickStreamHitBrowserInfo.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApiCoreDtoClickStreamHitBrowserInfo.


        :param id: The id of this ApiCoreDtoClickStreamHitBrowserInfo.
        :type id: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this ApiCoreDtoClickStreamHitBrowserInfo.


        :return: The name of this ApiCoreDtoClickStreamHitBrowserInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApiCoreDtoClickStreamHitBrowserInfo.


        :param name: The name of this ApiCoreDtoClickStreamHitBrowserInfo.
        :type name: str
        """

        self._name = name
