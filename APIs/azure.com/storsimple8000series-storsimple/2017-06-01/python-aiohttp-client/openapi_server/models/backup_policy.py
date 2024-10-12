# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.backup_policy_properties import BackupPolicyProperties
from openapi_server import util


class BackupPolicy(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, properties: BackupPolicyProperties=None, id: str=None, kind: str=None, name: str=None, type: str=None):
        """BackupPolicy - a model defined in OpenAPI

        :param properties: The properties of this BackupPolicy.
        :param id: The id of this BackupPolicy.
        :param kind: The kind of this BackupPolicy.
        :param name: The name of this BackupPolicy.
        :param type: The type of this BackupPolicy.
        """
        self.openapi_types = {
            'properties': BackupPolicyProperties,
            'id': str,
            'kind': str,
            'name': str,
            'type': str
        }

        self.attribute_map = {
            'properties': 'properties',
            'id': 'id',
            'kind': 'kind',
            'name': 'name',
            'type': 'type'
        }

        self._properties = properties
        self._id = id
        self._kind = kind
        self._name = name
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BackupPolicy':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BackupPolicy of this BackupPolicy.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def properties(self):
        """Gets the properties of this BackupPolicy.


        :return: The properties of this BackupPolicy.
        :rtype: BackupPolicyProperties
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this BackupPolicy.


        :param properties: The properties of this BackupPolicy.
        :type properties: BackupPolicyProperties
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")

        self._properties = properties

    @property
    def id(self):
        """Gets the id of this BackupPolicy.

        The path ID that uniquely identifies the object.

        :return: The id of this BackupPolicy.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BackupPolicy.

        The path ID that uniquely identifies the object.

        :param id: The id of this BackupPolicy.
        :type id: str
        """

        self._id = id

    @property
    def kind(self):
        """Gets the kind of this BackupPolicy.

        The Kind of the object. Currently only Series8000 is supported

        :return: The kind of this BackupPolicy.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this BackupPolicy.

        The Kind of the object. Currently only Series8000 is supported

        :param kind: The kind of this BackupPolicy.
        :type kind: str
        """
        allowed_values = ["Series8000"]  # noqa: E501
        if kind not in allowed_values:
            raise ValueError(
                "Invalid value for `kind` ({0}), must be one of {1}"
                .format(kind, allowed_values)
            )

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this BackupPolicy.

        The name of the object.

        :return: The name of this BackupPolicy.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BackupPolicy.

        The name of the object.

        :param name: The name of this BackupPolicy.
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this BackupPolicy.

        The hierarchical type of the object.

        :return: The type of this BackupPolicy.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BackupPolicy.

        The hierarchical type of the object.

        :param type: The type of this BackupPolicy.
        :type type: str
        """

        self._type = type
