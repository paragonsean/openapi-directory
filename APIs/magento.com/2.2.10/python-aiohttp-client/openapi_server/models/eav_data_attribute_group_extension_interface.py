# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class EavDataAttributeGroupExtensionInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, attribute_group_code: str=None, sort_order: str=None):
        """EavDataAttributeGroupExtensionInterface - a model defined in OpenAPI

        :param attribute_group_code: The attribute_group_code of this EavDataAttributeGroupExtensionInterface.
        :param sort_order: The sort_order of this EavDataAttributeGroupExtensionInterface.
        """
        self.openapi_types = {
            'attribute_group_code': str,
            'sort_order': str
        }

        self.attribute_map = {
            'attribute_group_code': 'attribute_group_code',
            'sort_order': 'sort_order'
        }

        self._attribute_group_code = attribute_group_code
        self._sort_order = sort_order

    @classmethod
    def from_dict(cls, dikt: dict) -> 'EavDataAttributeGroupExtensionInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The eav-data-attribute-group-extension-interface of this EavDataAttributeGroupExtensionInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def attribute_group_code(self):
        """Gets the attribute_group_code of this EavDataAttributeGroupExtensionInterface.


        :return: The attribute_group_code of this EavDataAttributeGroupExtensionInterface.
        :rtype: str
        """
        return self._attribute_group_code

    @attribute_group_code.setter
    def attribute_group_code(self, attribute_group_code):
        """Sets the attribute_group_code of this EavDataAttributeGroupExtensionInterface.


        :param attribute_group_code: The attribute_group_code of this EavDataAttributeGroupExtensionInterface.
        :type attribute_group_code: str
        """

        self._attribute_group_code = attribute_group_code

    @property
    def sort_order(self):
        """Gets the sort_order of this EavDataAttributeGroupExtensionInterface.


        :return: The sort_order of this EavDataAttributeGroupExtensionInterface.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this EavDataAttributeGroupExtensionInterface.


        :param sort_order: The sort_order of this EavDataAttributeGroupExtensionInterface.
        :type sort_order: str
        """

        self._sort_order = sort_order
