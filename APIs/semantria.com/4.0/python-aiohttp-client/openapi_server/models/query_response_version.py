# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class QueryResponseVersion(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, modified: str=None, name: str=None, query: str=None):
        """QueryResponseVersion - a model defined in OpenAPI

        :param id: The id of this QueryResponseVersion.
        :param modified: The modified of this QueryResponseVersion.
        :param name: The name of this QueryResponseVersion.
        :param query: The query of this QueryResponseVersion.
        """
        self.openapi_types = {
            'id': str,
            'modified': str,
            'name': str,
            'query': str
        }

        self.attribute_map = {
            'id': 'id',
            'modified': 'modified',
            'name': 'name',
            'query': 'query'
        }

        self._id = id
        self._modified = modified
        self._name = name
        self._query = query

    @classmethod
    def from_dict(cls, dikt: dict) -> 'QueryResponseVersion':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Query_ResponseVersion of this QueryResponseVersion.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this QueryResponseVersion.

        Unique query identifier

        :return: The id of this QueryResponseVersion.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this QueryResponseVersion.

        Unique query identifier

        :param id: The id of this QueryResponseVersion.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def modified(self):
        """Gets the modified of this QueryResponseVersion.

        The timestamp of the latest update of the record. Creation date of update didn't occur

        :return: The modified of this QueryResponseVersion.
        :rtype: str
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this QueryResponseVersion.

        The timestamp of the latest update of the record. Creation date of update didn't occur

        :param modified: The modified of this QueryResponseVersion.
        :type modified: str
        """
        if modified is None:
            raise ValueError("Invalid value for `modified`, must not be `None`")

        self._modified = modified

    @property
    def name(self):
        """Gets the name of this QueryResponseVersion.

        Query name

        :return: The name of this QueryResponseVersion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this QueryResponseVersion.

        Query name

        :param name: The name of this QueryResponseVersion.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def query(self):
        """Gets the query of this QueryResponseVersion.

        Boolean query used for content categorization

        :return: The query of this QueryResponseVersion.
        :rtype: str
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this QueryResponseVersion.

        Boolean query used for content categorization

        :param query: The query of this QueryResponseVersion.
        :type query: str
        """
        if query is None:
            raise ValueError("Invalid value for `query`, must not be `None`")

        self._query = query
