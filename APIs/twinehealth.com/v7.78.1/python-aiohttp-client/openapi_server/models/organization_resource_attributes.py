# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class OrganizationResourceAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, name: str=None):
        """OrganizationResourceAttributes - a model defined in OpenAPI

        :param name: The name of this OrganizationResourceAttributes.
        """
        self.openapi_types = {
            'name': str
        }

        self.attribute_map = {
            'name': 'name'
        }

        self._name = name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OrganizationResourceAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The OrganizationResource_attributes of this OrganizationResourceAttributes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def name(self):
        """Gets the name of this OrganizationResourceAttributes.


        :return: The name of this OrganizationResourceAttributes.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationResourceAttributes.


        :param name: The name of this OrganizationResourceAttributes.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name
