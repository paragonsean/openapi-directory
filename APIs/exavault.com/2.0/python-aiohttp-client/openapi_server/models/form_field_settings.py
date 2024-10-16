# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class FormFieldSettings(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, is_required: bool=None, sender_email: bool=None, use_as_folder_name: bool=None, width: float=None):
        """FormFieldSettings - a model defined in OpenAPI

        :param description: The description of this FormFieldSettings.
        :param is_required: The is_required of this FormFieldSettings.
        :param sender_email: The sender_email of this FormFieldSettings.
        :param use_as_folder_name: The use_as_folder_name of this FormFieldSettings.
        :param width: The width of this FormFieldSettings.
        """
        self.openapi_types = {
            'description': str,
            'is_required': bool,
            'sender_email': bool,
            'use_as_folder_name': bool,
            'width': float
        }

        self.attribute_map = {
            'description': 'description',
            'is_required': 'isRequired',
            'sender_email': 'senderEmail',
            'use_as_folder_name': 'useAsFolderName',
            'width': 'width'
        }

        self._description = description
        self._is_required = is_required
        self._sender_email = sender_email
        self._use_as_folder_name = use_as_folder_name
        self._width = width

    @classmethod
    def from_dict(cls, dikt: dict) -> 'FormFieldSettings':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The FormField_settings of this FormFieldSettings.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self):
        """Gets the description of this FormFieldSettings.

        Secondary description of field.

        :return: The description of this FormFieldSettings.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FormFieldSettings.

        Secondary description of field.

        :param description: The description of this FormFieldSettings.
        :type description: str
        """

        self._description = description

    @property
    def is_required(self):
        """Gets the is_required of this FormFieldSettings.

        Whether this field must be completed before form can be submitted

        :return: The is_required of this FormFieldSettings.
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """Sets the is_required of this FormFieldSettings.

        Whether this field must be completed before form can be submitted

        :param is_required: The is_required of this FormFieldSettings.
        :type is_required: bool
        """

        self._is_required = is_required

    @property
    def sender_email(self):
        """Gets the sender_email of this FormFieldSettings.


        :return: The sender_email of this FormFieldSettings.
        :rtype: bool
        """
        return self._sender_email

    @sender_email.setter
    def sender_email(self, sender_email):
        """Sets the sender_email of this FormFieldSettings.


        :param sender_email: The sender_email of this FormFieldSettings.
        :type sender_email: bool
        """

        self._sender_email = sender_email

    @property
    def use_as_folder_name(self):
        """Gets the use_as_folder_name of this FormFieldSettings.

        Whether to place submitted files into a subfolder named the contents of this field. Only takes effect when the `fileDropCreateFolders` parameter on the receive folder is `true`. `isRequired` must be set to `true` if this setting is `true`.

        :return: The use_as_folder_name of this FormFieldSettings.
        :rtype: bool
        """
        return self._use_as_folder_name

    @use_as_folder_name.setter
    def use_as_folder_name(self, use_as_folder_name):
        """Sets the use_as_folder_name of this FormFieldSettings.

        Whether to place submitted files into a subfolder named the contents of this field. Only takes effect when the `fileDropCreateFolders` parameter on the receive folder is `true`. `isRequired` must be set to `true` if this setting is `true`.

        :param use_as_folder_name: The use_as_folder_name of this FormFieldSettings.
        :type use_as_folder_name: bool
        """

        self._use_as_folder_name = use_as_folder_name

    @property
    def width(self):
        """Gets the width of this FormFieldSettings.

        How much of the available width the field should occupy

        :return: The width of this FormFieldSettings.
        :rtype: float
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this FormFieldSettings.

        How much of the available width the field should occupy

        :param width: The width of this FormFieldSettings.
        :type width: float
        """

        self._width = width
