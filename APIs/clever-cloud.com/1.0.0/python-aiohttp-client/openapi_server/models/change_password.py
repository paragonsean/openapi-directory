# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ChangePassword(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, new_password: str=None, old_password: str=None):
        """ChangePassword - a model defined in OpenAPI

        :param new_password: The new_password of this ChangePassword.
        :param old_password: The old_password of this ChangePassword.
        """
        self.openapi_types = {
            'new_password': str,
            'old_password': str
        }

        self.attribute_map = {
            'new_password': 'newPassword',
            'old_password': 'oldPassword'
        }

        self._new_password = new_password
        self._old_password = old_password

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ChangePassword':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Change_Password of this ChangePassword.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def new_password(self):
        """Gets the new_password of this ChangePassword.


        :return: The new_password of this ChangePassword.
        :rtype: str
        """
        return self._new_password

    @new_password.setter
    def new_password(self, new_password):
        """Sets the new_password of this ChangePassword.


        :param new_password: The new_password of this ChangePassword.
        :type new_password: str
        """
        if new_password is None:
            raise ValueError("Invalid value for `new_password`, must not be `None`")

        self._new_password = new_password

    @property
    def old_password(self):
        """Gets the old_password of this ChangePassword.


        :return: The old_password of this ChangePassword.
        :rtype: str
        """
        return self._old_password

    @old_password.setter
    def old_password(self, old_password):
        """Sets the old_password of this ChangePassword.


        :param old_password: The old_password of this ChangePassword.
        :type old_password: str
        """
        if old_password is None:
            raise ValueError("Invalid value for `old_password`, must not be `None`")

        self._old_password = old_password
