# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.failover_group_update_properties import FailoverGroupUpdateProperties
from openapi_server import util


class FailoverGroupUpdate(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, properties: FailoverGroupUpdateProperties=None, tags: Dict[str, str]=None):
        """FailoverGroupUpdate - a model defined in OpenAPI

        :param properties: The properties of this FailoverGroupUpdate.
        :param tags: The tags of this FailoverGroupUpdate.
        """
        self.openapi_types = {
            'properties': FailoverGroupUpdateProperties,
            'tags': Dict[str, str]
        }

        self.attribute_map = {
            'properties': 'properties',
            'tags': 'tags'
        }

        self._properties = properties
        self._tags = tags

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FailoverGroupUpdate':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FailoverGroupUpdate of this FailoverGroupUpdate.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def properties(self):
        """Gets the properties of this FailoverGroupUpdate.


        :return: The properties of this FailoverGroupUpdate.
        :rtype: FailoverGroupUpdateProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this FailoverGroupUpdate.


        :param properties: The properties of this FailoverGroupUpdate.
        :type properties: FailoverGroupUpdateProperties
        """

        self._properties = properties

    @property
    def tags(self):
        """Gets the tags of this FailoverGroupUpdate.

        Resource tags.

        :return: The tags of this FailoverGroupUpdate.
        :rtype: Dict[str, str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this FailoverGroupUpdate.

        Resource tags.

        :param tags: The tags of this FailoverGroupUpdate.
        :type tags: Dict[str, str]
        """

        self._tags = tags
