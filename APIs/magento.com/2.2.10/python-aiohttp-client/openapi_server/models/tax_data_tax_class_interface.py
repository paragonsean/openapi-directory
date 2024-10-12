# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class TaxDataTaxClassInterface(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, class_id: int=None, class_name: str=None, class_type: str=None, extension_attributes: object=None):
        """TaxDataTaxClassInterface - a model defined in OpenAPI

        :param class_id: The class_id of this TaxDataTaxClassInterface.
        :param class_name: The class_name of this TaxDataTaxClassInterface.
        :param class_type: The class_type of this TaxDataTaxClassInterface.
        :param extension_attributes: The extension_attributes of this TaxDataTaxClassInterface.
        """
        self.openapi_types = {
            'class_id': int,
            'class_name': str,
            'class_type': str,
            'extension_attributes': object
        }

        self.attribute_map = {
            'class_id': 'class_id',
            'class_name': 'class_name',
            'class_type': 'class_type',
            'extension_attributes': 'extension_attributes'
        }

        self._class_id = class_id
        self._class_name = class_name
        self._class_type = class_type
        self._extension_attributes = extension_attributes

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TaxDataTaxClassInterface':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The tax-data-tax-class-interface of this TaxDataTaxClassInterface.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def class_id(self):
        """Gets the class_id of this TaxDataTaxClassInterface.

        Tax class ID.

        :return: The class_id of this TaxDataTaxClassInterface.
        :rtype: int
        """
        return self._class_id

    @class_id.setter
    def class_id(self, class_id):
        """Sets the class_id of this TaxDataTaxClassInterface.

        Tax class ID.

        :param class_id: The class_id of this TaxDataTaxClassInterface.
        :type class_id: int
        """

        self._class_id = class_id

    @property
    def class_name(self):
        """Gets the class_name of this TaxDataTaxClassInterface.

        Tax class name.

        :return: The class_name of this TaxDataTaxClassInterface.
        :rtype: str
        """
        return self._class_name

    @class_name.setter
    def class_name(self, class_name):
        """Sets the class_name of this TaxDataTaxClassInterface.

        Tax class name.

        :param class_name: The class_name of this TaxDataTaxClassInterface.
        :type class_name: str
        """
        if class_name is None:
            raise ValueError("Invalid value for `class_name`, must not be `None`")

        self._class_name = class_name

    @property
    def class_type(self):
        """Gets the class_type of this TaxDataTaxClassInterface.

        Tax class type.

        :return: The class_type of this TaxDataTaxClassInterface.
        :rtype: str
        """
        return self._class_type

    @class_type.setter
    def class_type(self, class_type):
        """Sets the class_type of this TaxDataTaxClassInterface.

        Tax class type.

        :param class_type: The class_type of this TaxDataTaxClassInterface.
        :type class_type: str
        """
        if class_type is None:
            raise ValueError("Invalid value for `class_type`, must not be `None`")

        self._class_type = class_type

    @property
    def extension_attributes(self):
        """Gets the extension_attributes of this TaxDataTaxClassInterface.

        ExtensionInterface class for @see \\Magento\\Tax\\Api\\Data\\TaxClassInterface

        :return: The extension_attributes of this TaxDataTaxClassInterface.
        :rtype: object
        """
        return self._extension_attributes

    @extension_attributes.setter
    def extension_attributes(self, extension_attributes):
        """Sets the extension_attributes of this TaxDataTaxClassInterface.

        ExtensionInterface class for @see \\Magento\\Tax\\Api\\Data\\TaxClassInterface

        :param extension_attributes: The extension_attributes of this TaxDataTaxClassInterface.
        :type extension_attributes: object
        """

        self._extension_attributes = extension_attributes
