# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.identity_properties import IdentityProperties
from openapi_server.models.task_properties_update_parameters import TaskPropertiesUpdateParameters
from openapi_server import util


class TaskUpdateParameters(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, identity: IdentityProperties=None, properties: TaskPropertiesUpdateParameters=None, tags: Dict[str, str]=None):
        """TaskUpdateParameters - a model defined in OpenAPI

        :param identity: The identity of this TaskUpdateParameters.
        :param properties: The properties of this TaskUpdateParameters.
        :param tags: The tags of this TaskUpdateParameters.
        """
        self.openapi_types = {
            'identity': IdentityProperties,
            'properties': TaskPropertiesUpdateParameters,
            'tags': Dict[str, str]
        }

        self.attribute_map = {
            'identity': 'identity',
            'properties': 'properties',
            'tags': 'tags'
        }

        self._identity = identity
        self._properties = properties
        self._tags = tags

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TaskUpdateParameters':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TaskUpdateParameters of this TaskUpdateParameters.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def identity(self):
        """Gets the identity of this TaskUpdateParameters.


        :return: The identity of this TaskUpdateParameters.
        :rtype: IdentityProperties
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this TaskUpdateParameters.


        :param identity: The identity of this TaskUpdateParameters.
        :type identity: IdentityProperties
        """

        self._identity = identity

    @property
    def properties(self):
        """Gets the properties of this TaskUpdateParameters.


        :return: The properties of this TaskUpdateParameters.
        :rtype: TaskPropertiesUpdateParameters
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this TaskUpdateParameters.


        :param properties: The properties of this TaskUpdateParameters.
        :type properties: TaskPropertiesUpdateParameters
        """

        self._properties = properties

    @property
    def tags(self):
        """Gets the tags of this TaskUpdateParameters.

        The ARM resource tags.

        :return: The tags of this TaskUpdateParameters.
        :rtype: Dict[str, str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TaskUpdateParameters.

        The ARM resource tags.

        :param tags: The tags of this TaskUpdateParameters.
        :type tags: Dict[str, str]
        """

        self._tags = tags
