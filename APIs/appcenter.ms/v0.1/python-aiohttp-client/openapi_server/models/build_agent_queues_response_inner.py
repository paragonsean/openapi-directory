# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class BuildAgentQueuesResponseInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, build_definition: str=None, name: str=None):
        """BuildAgentQueuesResponseInner - a model defined in OpenAPI

        :param build_definition: The build_definition of this BuildAgentQueuesResponseInner.
        :param name: The name of this BuildAgentQueuesResponseInner.
        """
        self.openapi_types = {
            'build_definition': str,
            'name': str
        }

        self.attribute_map = {
            'build_definition': 'buildDefinition',
            'name': 'name'
        }

        self._build_definition = build_definition
        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BuildAgentQueuesResponseInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BuildAgentQueuesResponse_inner of this BuildAgentQueuesResponseInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def build_definition(self):
        """Gets the build_definition of this BuildAgentQueuesResponseInner.

        Name of the build definition

        :return: The build_definition of this BuildAgentQueuesResponseInner.
        :rtype: str
        """
        return self._build_definition

    @build_definition.setter
    def build_definition(self, build_definition):
        """Sets the build_definition of this BuildAgentQueuesResponseInner.

        Name of the build definition

        :param build_definition: The build_definition of this BuildAgentQueuesResponseInner.
        :type build_definition: str
        """

        self._build_definition = build_definition

    @property
    def name(self):
        """Gets the name of this BuildAgentQueuesResponseInner.

        Name of the queue

        :return: The name of this BuildAgentQueuesResponseInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BuildAgentQueuesResponseInner.

        Name of the queue

        :param name: The name of this BuildAgentQueuesResponseInner.
        :type name: str
        """

        self._name = name
