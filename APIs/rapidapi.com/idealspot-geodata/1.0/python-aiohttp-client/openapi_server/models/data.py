# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.parameters import Parameters
from openapi_server import util


class Data(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, groups: List[str]=None, id: str=None, name: str=None, parameters: Parameters=None, periods: List[str]=None, slug: str=None, version: str=None):
        """Data - a model defined in OpenAPI

        :param description: The description of this Data.
        :param groups: The groups of this Data.
        :param id: The id of this Data.
        :param name: The name of this Data.
        :param parameters: The parameters of this Data.
        :param periods: The periods of this Data.
        :param slug: The slug of this Data.
        :param version: The version of this Data.
        """
        self.openapi_types = {
            'description': str,
            'groups': List[str],
            'id': str,
            'name': str,
            'parameters': Parameters,
            'periods': List[str],
            'slug': str,
            'version': str
        }

        self.attribute_map = {
            'description': 'description',
            'groups': 'groups',
            'id': 'id',
            'name': 'name',
            'parameters': 'parameters',
            'periods': 'periods',
            'slug': 'slug',
            'version': 'version'
        }

        self._description = description
        self._groups = groups
        self._id = id
        self._name = name
        self._parameters = parameters
        self._periods = periods
        self._slug = slug
        self._version = version

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Data':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Data of this Data.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this Data.


        :return: The description of this Data.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Data.


        :param description: The description of this Data.
        :type description: str
        """
        if description is None:
            raise ValueError("Invalid value for `description`, must not be `None`")

        self._description = description

    @property
    def groups(self):
        """Gets the groups of this Data.


        :return: The groups of this Data.
        :rtype: List[str]
        """
        return self._groups

    @groups.setter
    def groups(self, groups):
        """Sets the groups of this Data.


        :param groups: The groups of this Data.
        :type groups: List[str]
        """
        if groups is None:
            raise ValueError("Invalid value for `groups`, must not be `None`")

        self._groups = groups

    @property
    def id(self):
        """Gets the id of this Data.


        :return: The id of this Data.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Data.


        :param id: The id of this Data.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """Gets the name of this Data.


        :return: The name of this Data.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Data.


        :param name: The name of this Data.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def parameters(self):
        """Gets the parameters of this Data.


        :return: The parameters of this Data.
        :rtype: Parameters
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        """Sets the parameters of this Data.


        :param parameters: The parameters of this Data.
        :type parameters: Parameters
        """
        if parameters is None:
            raise ValueError("Invalid value for `parameters`, must not be `None`")

        self._parameters = parameters

    @property
    def periods(self):
        """Gets the periods of this Data.


        :return: The periods of this Data.
        :rtype: List[str]
        """
        return self._periods

    @periods.setter
    def periods(self, periods):
        """Sets the periods of this Data.


        :param periods: The periods of this Data.
        :type periods: List[str]
        """
        if periods is None:
            raise ValueError("Invalid value for `periods`, must not be `None`")

        self._periods = periods

    @property
    def slug(self):
        """Gets the slug of this Data.


        :return: The slug of this Data.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Data.


        :param slug: The slug of this Data.
        :type slug: str
        """
        if slug is None:
            raise ValueError("Invalid value for `slug`, must not be `None`")

        self._slug = slug

    @property
    def version(self):
        """Gets the version of this Data.


        :return: The version of this Data.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Data.


        :param version: The version of this Data.
        :type version: str
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")

        self._version = version
