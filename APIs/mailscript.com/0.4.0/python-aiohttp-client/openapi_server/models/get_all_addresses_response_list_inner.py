# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.address import Address
from openapi_server import util


class GetAllAddressesResponseListInner(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, created_at: datetime=None, created_by: str=None, display_name: str=None, id: str=None, owner: str=None):
        """GetAllAddressesResponseListInner - a model defined in OpenAPI

        :param created_at: The created_at of this GetAllAddressesResponseListInner.
        :param created_by: The created_by of this GetAllAddressesResponseListInner.
        :param display_name: The display_name of this GetAllAddressesResponseListInner.
        :param id: The id of this GetAllAddressesResponseListInner.
        :param owner: The owner of this GetAllAddressesResponseListInner.
        """
        self.openapi_types = {
            'created_at': datetime,
            'created_by': str,
            'display_name': str,
            'id': str,
            'owner': str
        }

        self.attribute_map = {
            'created_at': 'createdAt',
            'created_by': 'createdBy',
            'display_name': 'displayName',
            'id': 'id',
            'owner': 'owner'
        }

        self._created_at = created_at
        self._created_by = created_by
        self._display_name = display_name
        self._id = id
        self._owner = owner

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GetAllAddressesResponseListInner':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GetAllAddressesResponse_list_inner of this GetAllAddressesResponseListInner.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def created_at(self):
        """Gets the created_at of this GetAllAddressesResponseListInner.


        :return: The created_at of this GetAllAddressesResponseListInner.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this GetAllAddressesResponseListInner.


        :param created_at: The created_at of this GetAllAddressesResponseListInner.
        :type created_at: datetime
        """
        if created_at is None:
            raise ValueError("Invalid value for `created_at`, must not be `None`")

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this GetAllAddressesResponseListInner.


        :return: The created_by of this GetAllAddressesResponseListInner.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this GetAllAddressesResponseListInner.


        :param created_by: The created_by of this GetAllAddressesResponseListInner.
        :type created_by: str
        """
        if created_by is None:
            raise ValueError("Invalid value for `created_by`, must not be `None`")

        self._created_by = created_by

    @property
    def display_name(self):
        """Gets the display_name of this GetAllAddressesResponseListInner.


        :return: The display_name of this GetAllAddressesResponseListInner.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this GetAllAddressesResponseListInner.


        :param display_name: The display_name of this GetAllAddressesResponseListInner.
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this GetAllAddressesResponseListInner.


        :return: The id of this GetAllAddressesResponseListInner.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this GetAllAddressesResponseListInner.


        :param id: The id of this GetAllAddressesResponseListInner.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def owner(self):
        """Gets the owner of this GetAllAddressesResponseListInner.


        :return: The owner of this GetAllAddressesResponseListInner.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this GetAllAddressesResponseListInner.


        :param owner: The owner of this GetAllAddressesResponseListInner.
        :type owner: str
        """
        if owner is None:
            raise ValueError("Invalid value for `owner`, must not be `None`")

        self._owner = owner
