# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class InvoiceAttachment(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: int=None, invoice_id: int=None, link: str=None, obfuscated_file_name: str=None, original_file_name: str=None, size: int=None, type: str=None):
        """InvoiceAttachment - a model defined in OpenAPI

        :param id: The id of this InvoiceAttachment.
        :param invoice_id: The invoice_id of this InvoiceAttachment.
        :param link: The link of this InvoiceAttachment.
        :param obfuscated_file_name: The obfuscated_file_name of this InvoiceAttachment.
        :param original_file_name: The original_file_name of this InvoiceAttachment.
        :param size: The size of this InvoiceAttachment.
        :param type: The type of this InvoiceAttachment.
        """
        self.openapi_types = {
            'id': int,
            'invoice_id': int,
            'link': str,
            'obfuscated_file_name': str,
            'original_file_name': str,
            'size': int,
            'type': str
        }

        self.attribute_map = {
            'id': 'Id',
            'invoice_id': 'InvoiceId',
            'link': 'Link',
            'obfuscated_file_name': 'ObfuscatedFileName',
            'original_file_name': 'OriginalFileName',
            'size': 'Size',
            'type': 'Type'
        }

        self._id = id
        self._invoice_id = invoice_id
        self._link = link
        self._obfuscated_file_name = obfuscated_file_name
        self._original_file_name = original_file_name
        self._size = size
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InvoiceAttachment':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The InvoiceAttachment of this InvoiceAttachment.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this InvoiceAttachment.


        :return: The id of this InvoiceAttachment.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InvoiceAttachment.


        :param id: The id of this InvoiceAttachment.
        :type id: int
        """

        self._id = id

    @property
    def invoice_id(self):
        """Gets the invoice_id of this InvoiceAttachment.


        :return: The invoice_id of this InvoiceAttachment.
        :rtype: int
        """
        return self._invoice_id

    @invoice_id.setter
    def invoice_id(self, invoice_id):
        """Sets the invoice_id of this InvoiceAttachment.


        :param invoice_id: The invoice_id of this InvoiceAttachment.
        :type invoice_id: int
        """

        self._invoice_id = invoice_id

    @property
    def link(self):
        """Gets the link of this InvoiceAttachment.


        :return: The link of this InvoiceAttachment.
        :rtype: str
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this InvoiceAttachment.


        :param link: The link of this InvoiceAttachment.
        :type link: str
        """

        self._link = link

    @property
    def obfuscated_file_name(self):
        """Gets the obfuscated_file_name of this InvoiceAttachment.


        :return: The obfuscated_file_name of this InvoiceAttachment.
        :rtype: str
        """
        return self._obfuscated_file_name

    @obfuscated_file_name.setter
    def obfuscated_file_name(self, obfuscated_file_name):
        """Sets the obfuscated_file_name of this InvoiceAttachment.


        :param obfuscated_file_name: The obfuscated_file_name of this InvoiceAttachment.
        :type obfuscated_file_name: str
        """

        self._obfuscated_file_name = obfuscated_file_name

    @property
    def original_file_name(self):
        """Gets the original_file_name of this InvoiceAttachment.


        :return: The original_file_name of this InvoiceAttachment.
        :rtype: str
        """
        return self._original_file_name

    @original_file_name.setter
    def original_file_name(self, original_file_name):
        """Sets the original_file_name of this InvoiceAttachment.


        :param original_file_name: The original_file_name of this InvoiceAttachment.
        :type original_file_name: str
        """

        self._original_file_name = original_file_name

    @property
    def size(self):
        """Gets the size of this InvoiceAttachment.


        :return: The size of this InvoiceAttachment.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this InvoiceAttachment.


        :param size: The size of this InvoiceAttachment.
        :type size: int
        """

        self._size = size

    @property
    def type(self):
        """Gets the type of this InvoiceAttachment.


        :return: The type of this InvoiceAttachment.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InvoiceAttachment.


        :param type: The type of this InvoiceAttachment.
        :type type: str
        """
        allowed_values = ["External", "Uploaded"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
