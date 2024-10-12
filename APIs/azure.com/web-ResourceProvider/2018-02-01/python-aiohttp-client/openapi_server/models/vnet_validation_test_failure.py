# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class VnetValidationTestFailure(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, properties: object=None, id: str=None, kind: str=None, name: str=None, type: str=None):
        """VnetValidationTestFailure - a model defined in OpenAPI

        :param properties: The properties of this VnetValidationTestFailure.
        :param id: The id of this VnetValidationTestFailure.
        :param kind: The kind of this VnetValidationTestFailure.
        :param name: The name of this VnetValidationTestFailure.
        :param type: The type of this VnetValidationTestFailure.
        """
        self.openapi_types = {
            'properties': object,
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
    def from_dict(cls, dikt: dict) -> 'VnetValidationTestFailure':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The VnetValidationTestFailure of this VnetValidationTestFailure.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def properties(self):
        """Gets the properties of this VnetValidationTestFailure.

        VnetValidationTestFailure resource specific properties

        :return: The properties of this VnetValidationTestFailure.
        :rtype: object
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this VnetValidationTestFailure.

        VnetValidationTestFailure resource specific properties

        :param properties: The properties of this VnetValidationTestFailure.
        :type properties: object
        """

        self._properties = properties

    @property
    def id(self):
        """Gets the id of this VnetValidationTestFailure.

        Resource Id.

        :return: The id of this VnetValidationTestFailure.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VnetValidationTestFailure.

        Resource Id.

        :param id: The id of this VnetValidationTestFailure.
        :type id: str
        """

        self._id = id

    @property
    def kind(self):
        """Gets the kind of this VnetValidationTestFailure.

        Kind of resource.

        :return: The kind of this VnetValidationTestFailure.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this VnetValidationTestFailure.

        Kind of resource.

        :param kind: The kind of this VnetValidationTestFailure.
        :type kind: str
        """

        self._kind = kind

    @property
    def name(self):
        """Gets the name of this VnetValidationTestFailure.

        Resource Name.

        :return: The name of this VnetValidationTestFailure.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this VnetValidationTestFailure.

        Resource Name.

        :param name: The name of this VnetValidationTestFailure.
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this VnetValidationTestFailure.

        Resource type.

        :return: The type of this VnetValidationTestFailure.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VnetValidationTestFailure.

        Resource type.

        :param type: The type of this VnetValidationTestFailure.
        :type type: str
        """

        self._type = type
