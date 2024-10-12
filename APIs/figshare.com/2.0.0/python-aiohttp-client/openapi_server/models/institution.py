# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Institution(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, domain: str=None, id: int=None, name: str=None):
        """Institution - a model defined in OpenAPI

        :param domain: The domain of this Institution.
        :param id: The id of this Institution.
        :param name: The name of this Institution.
        """
        self.openapi_types = {
            'domain': str,
            'id': int,
            'name': str
        }

        self.attribute_map = {
            'domain': 'domain',
            'id': 'id',
            'name': 'name'
        }

        self._domain = domain
        self._id = id
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Institution':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Institution of this Institution.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def domain(self):
        """Gets the domain of this Institution.

        Institution domain

        :return: The domain of this Institution.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this Institution.

        Institution domain

        :param domain: The domain of this Institution.
        :type domain: str
        """
        if domain is None:
            raise ValueError("Invalid value for `domain`, must not be `None`")

        self._domain = domain

    @property
    def id(self):
        """Gets the id of this Institution.

        Institution id

        :return: The id of this Institution.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Institution.

        Institution id

        :param id: The id of this Institution.
        :type id: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """Gets the name of this Institution.

        Institution name

        :return: The name of this Institution.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Institution.

        Institution name

        :param name: The name of this Institution.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name
