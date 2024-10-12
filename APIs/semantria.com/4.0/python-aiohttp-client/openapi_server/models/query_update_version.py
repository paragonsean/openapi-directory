# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class QueryUpdateVersion(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, name: str=None, query: str=None):
        """QueryUpdateVersion - a model defined in OpenAPI

        :param id: The id of this QueryUpdateVersion.
        :param name: The name of this QueryUpdateVersion.
        :param query: The query of this QueryUpdateVersion.
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'query': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'query': 'query'
        }

        self._id = id
        self._name = name
        self._query = query

    @classmethod
    def from_dict(cls, dikt: dict) -> 'QueryUpdateVersion':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Query_UpdateVersion of this QueryUpdateVersion.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this QueryUpdateVersion.

        Unique query identifier

        :return: The id of this QueryUpdateVersion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueryUpdateVersion.

        Unique query identifier

        :param id: The id of this QueryUpdateVersion.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def name(self):
        """Gets the name of this QueryUpdateVersion.

        Query name

        :return: The name of this QueryUpdateVersion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QueryUpdateVersion.

        Query name

        :param name: The name of this QueryUpdateVersion.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def query(self):
        """Gets the query of this QueryUpdateVersion.

        Boolean query used for content categorization

        :return: The query of this QueryUpdateVersion.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this QueryUpdateVersion.

        Boolean query used for content categorization

        :param query: The query of this QueryUpdateVersion.
        :type query: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")

        self._query = query
