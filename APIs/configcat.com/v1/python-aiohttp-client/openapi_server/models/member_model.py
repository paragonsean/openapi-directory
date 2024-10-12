# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class MemberModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, email: str=None, full_name: str=None, permission_group_id: int=None, product_id: str=None, user_id: str=None):
        """MemberModel - a model defined in OpenAPI

        :param email: The email of this MemberModel.
        :param full_name: The full_name of this MemberModel.
        :param permission_group_id: The permission_group_id of this MemberModel.
        :param product_id: The product_id of this MemberModel.
        :param user_id: The user_id of this MemberModel.
        """
        self.openapi_types = {
            'email': str,
            'full_name': str,
            'permission_group_id': int,
            'product_id': str,
            'user_id': str
        }

        self.attribute_map = {
            'email': 'email',
            'full_name': 'fullName',
            'permission_group_id': 'permissionGroupId',
            'product_id': 'productId',
            'user_id': 'userId'
        }

        self._email = email
        self._full_name = full_name
        self._permission_group_id = permission_group_id
        self._product_id = product_id
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'MemberModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The MemberModel of this MemberModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def email(self):
        """Gets the email of this MemberModel.


        :return: The email of this MemberModel.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this MemberModel.


        :param email: The email of this MemberModel.
        :type email: str
        """

        self._email = email

    @property
    def full_name(self):
        """Gets the full_name of this MemberModel.


        :return: The full_name of this MemberModel.
        :rtype: str
        """
        return self._full_name

    @full_name.setter
    def full_name(self, full_name):
        """Sets the full_name of this MemberModel.


        :param full_name: The full_name of this MemberModel.
        :type full_name: str
        """

        self._full_name = full_name

    @property
    def permission_group_id(self):
        """Gets the permission_group_id of this MemberModel.


        :return: The permission_group_id of this MemberModel.
        :rtype: int
        """
        return self._permission_group_id

    @permission_group_id.setter
    def permission_group_id(self, permission_group_id):
        """Sets the permission_group_id of this MemberModel.


        :param permission_group_id: The permission_group_id of this MemberModel.
        :type permission_group_id: int
        """

        self._permission_group_id = permission_group_id

    @property
    def product_id(self):
        """Gets the product_id of this MemberModel.


        :return: The product_id of this MemberModel.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this MemberModel.


        :param product_id: The product_id of this MemberModel.
        :type product_id: str
        """

        self._product_id = product_id

    @property
    def user_id(self):
        """Gets the user_id of this MemberModel.


        :return: The user_id of this MemberModel.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this MemberModel.


        :param user_id: The user_id of this MemberModel.
        :type user_id: str
        """

        self._user_id = user_id
