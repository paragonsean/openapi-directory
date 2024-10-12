# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class TaxonomyTopic(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, type: str=None):
        """TaxonomyTopic - a model defined in OpenAPI

        :param id: The id of this TaxonomyTopic.
        :param type: The type of this TaxonomyTopic.
        """
        self.openapi_types = {
            'id': str,
            'type': str
        }

        self.attribute_map = {
            'id': 'id',
            'type': 'type'
        }

        self._id = id
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TaxonomyTopic':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TaxonomyTopic of this TaxonomyTopic.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this TaxonomyTopic.

        Unique taxonomy topic identifier

        :return: The id of this TaxonomyTopic.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TaxonomyTopic.

        Unique taxonomy topic identifier

        :param id: The id of this TaxonomyTopic.
        :type id: str
        """

        self._id = id

    @property
    def type(self):
        """Gets the type of this TaxonomyTopic.

        Type of the topic (category or query) associated with the certain taxonomy node

        :return: The type of this TaxonomyTopic.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TaxonomyTopic.

        Type of the topic (category or query) associated with the certain taxonomy node

        :param type: The type of this TaxonomyTopic.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type
