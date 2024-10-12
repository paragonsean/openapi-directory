# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SubmissionEntryToInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, address: str=None, fields: List[str]=None, id: str=None, name: str=None, type: str=None):
        """SubmissionEntryToInner - a model defined in OpenAPI

        :param address: The address of this SubmissionEntryToInner.
        :param fields: The fields of this SubmissionEntryToInner.
        :param id: The id of this SubmissionEntryToInner.
        :param name: The name of this SubmissionEntryToInner.
        :param type: The type of this SubmissionEntryToInner.
        """
        self.openapi_types = {
            'address': str,
            'fields': List[str],
            'id': str,
            'name': str,
            'type': str
        }

        self.attribute_map = {
            'address': 'address',
            'fields': 'fields',
            'id': 'id',
            'name': 'name',
            'type': 'type'
        }

        self._address = address
        self._fields = fields
        self._id = id
        self._name = name
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SubmissionEntryToInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SubmissionEntry_to_inner of this SubmissionEntryToInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self):
        """Gets the address of this SubmissionEntryToInner.

        The phone number of the recipient.  It must be supplied if the `type` is INTERNATIONAL

        :return: The address of this SubmissionEntryToInner.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SubmissionEntryToInner.

        The phone number of the recipient.  It must be supplied if the `type` is INTERNATIONAL

        :param address: The address of this SubmissionEntryToInner.
        :type address: str
        """

        self._address = address

    @property
    def fields(self):
        """Gets the fields of this SubmissionEntryToInner.

        Custom fields that can be used in the message body. A value can be given if the `type` is INTERNATIONAL  Read the [body templates section](#tag/Message) for more information. 

        :return: The fields of this SubmissionEntryToInner.
        :rtype: List[str]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this SubmissionEntryToInner.

        Custom fields that can be used in the message body. A value can be given if the `type` is INTERNATIONAL  Read the [body templates section](#tag/Message) for more information. 

        :param fields: The fields of this SubmissionEntryToInner.
        :type fields: List[str]
        """

        self._fields = fields

    @property
    def id(self):
        """Gets the id of this SubmissionEntryToInner.

        The id of a group in your phonebook.  A value can be given if the `type` is GROUP.

        :return: The id of this SubmissionEntryToInner.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubmissionEntryToInner.

        The id of a group in your phonebook.  A value can be given if the `type` is GROUP.

        :param id: The id of this SubmissionEntryToInner.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SubmissionEntryToInner.

        The name of a group in your phonebook. A value can be given if the `type` is GROUP.

        :return: The name of this SubmissionEntryToInner.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubmissionEntryToInner.

        The name of a group in your phonebook. A value can be given if the `type` is GROUP.

        :param name: The name of this SubmissionEntryToInner.
        :type name: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this SubmissionEntryToInner.

        Type of the recipient. The default value is INTERNATIONAL.

        :return: The type of this SubmissionEntryToInner.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SubmissionEntryToInner.

        Type of the recipient. The default value is INTERNATIONAL.

        :param type: The type of this SubmissionEntryToInner.
        :type type: str
        """
        allowed_values = ["INTERNATIONAL", "GROUP"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
