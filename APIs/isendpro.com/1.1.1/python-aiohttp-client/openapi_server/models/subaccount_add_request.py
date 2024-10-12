# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class SubaccountAddRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, keyid: str=None, sub_account_edit: str=None, sub_account_login: str=None, sub_account_password: str=None):
        """SubaccountAddRequest - a model defined in OpenAPI

        :param keyid: The keyid of this SubaccountAddRequest.
        :param sub_account_edit: The sub_account_edit of this SubaccountAddRequest.
        :param sub_account_login: The sub_account_login of this SubaccountAddRequest.
        :param sub_account_password: The sub_account_password of this SubaccountAddRequest.
        """
        self.openapi_types = {
            'keyid': str,
            'sub_account_edit': str,
            'sub_account_login': str,
            'sub_account_password': str
        }

        self.attribute_map = {
            'keyid': 'keyid',
            'sub_account_edit': 'subAccountEdit',
            'sub_account_login': 'subAccountLogin',
            'sub_account_password': 'subAccountPassword'
        }

        self._keyid = keyid
        self._sub_account_edit = sub_account_edit
        self._sub_account_login = sub_account_login
        self._sub_account_password = sub_account_password

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SubaccountAddRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SubaccountAddRequest of this SubaccountAddRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def keyid(self):
        """Gets the keyid of this SubaccountAddRequest.


        :return: The keyid of this SubaccountAddRequest.
        :rtype: str
        """
        return self._keyid

    @keyid.setter
    def keyid(self, keyid):
        """Sets the keyid of this SubaccountAddRequest.


        :param keyid: The keyid of this SubaccountAddRequest.
        :type keyid: str
        """
        if keyid is None:
            raise ValueError("Invalid value for `keyid`, must not be `None`")

        self._keyid = keyid

    @property
    def sub_account_edit(self):
        """Gets the sub_account_edit of this SubaccountAddRequest.


        :return: The sub_account_edit of this SubaccountAddRequest.
        :rtype: str
        """
        return self._sub_account_edit

    @sub_account_edit.setter
    def sub_account_edit(self, sub_account_edit):
        """Sets the sub_account_edit of this SubaccountAddRequest.


        :param sub_account_edit: The sub_account_edit of this SubaccountAddRequest.
        :type sub_account_edit: str
        """
        allowed_values = ["addAccount"]  # noqa: E501
        if sub_account_edit not in allowed_values:
            raise ValueError(
                "Invalid value for `sub_account_edit` ({0}), must be one of {1}"
                .format(sub_account_edit, allowed_values)
            )

        self._sub_account_edit = sub_account_edit

    @property
    def sub_account_login(self):
        """Gets the sub_account_login of this SubaccountAddRequest.


        :return: The sub_account_login of this SubaccountAddRequest.
        :rtype: str
        """
        return self._sub_account_login

    @sub_account_login.setter
    def sub_account_login(self, sub_account_login):
        """Sets the sub_account_login of this SubaccountAddRequest.


        :param sub_account_login: The sub_account_login of this SubaccountAddRequest.
        :type sub_account_login: str
        """
        if sub_account_login is None:
            raise ValueError("Invalid value for `sub_account_login`, must not be `None`")

        self._sub_account_login = sub_account_login

    @property
    def sub_account_password(self):
        """Gets the sub_account_password of this SubaccountAddRequest.


        :return: The sub_account_password of this SubaccountAddRequest.
        :rtype: str
        """
        return self._sub_account_password

    @sub_account_password.setter
    def sub_account_password(self, sub_account_password):
        """Sets the sub_account_password of this SubaccountAddRequest.


        :param sub_account_password: The sub_account_password of this SubaccountAddRequest.
        :type sub_account_password: str
        """
        if sub_account_password is None:
            raise ValueError("Invalid value for `sub_account_password`, must not be `None`")

        self._sub_account_password = sub_account_password
