# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Namespace(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, slug: str=None):
        """Namespace - a model defined in OpenAPI

        :param id: The id of this Namespace.
        :param name: The name of this Namespace.
        :param slug: The slug of this Namespace.
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'slug': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'slug': 'slug'
        }

        self._id = id
        self._name = name
        self._slug = slug

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Namespace':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The namespace of this Namespace.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Namespace.


        :return: The id of this Namespace.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Namespace.


        :param id: The id of this Namespace.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Namespace.


        :return: The name of this Namespace.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Namespace.


        :param name: The name of this Namespace.
        :type name: str
        """

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this Namespace.


        :return: The slug of this Namespace.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Namespace.


        :param slug: The slug of this Namespace.
        :type slug: str
        """

        self._slug = slug
