# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ResetPasswordModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, locale: str=None, user_name: str=None):
        """ResetPasswordModel - a model defined in OpenAPI

        :param locale: The locale of this ResetPasswordModel.
        :param user_name: The user_name of this ResetPasswordModel.
        """
        self.openapi_types = {
            'locale': str,
            'user_name': str
        }

        self.attribute_map = {
            'locale': 'locale',
            'user_name': 'userName'
        }

        self._locale = locale
        self._user_name = user_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ResetPasswordModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ResetPasswordModel of this ResetPasswordModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def locale(self):
        """Gets the locale of this ResetPasswordModel.

        Supported locales are: \"en-US\", \"en-CA\", and \"fr-CA\"

        :return: The locale of this ResetPasswordModel.
        :rtype: str
        """
        return self._locale

    @locale.setter
    def locale(self, locale):
        """Sets the locale of this ResetPasswordModel.

        Supported locales are: \"en-US\", \"en-CA\", and \"fr-CA\"

        :param locale: The locale of this ResetPasswordModel.
        :type locale: str
        """
        if locale is None:
            raise ValueError("Invalid value for `locale`, must not be `None`")

        self._locale = locale

    @property
    def user_name(self):
        """Gets the user_name of this ResetPasswordModel.


        :return: The user_name of this ResetPasswordModel.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this ResetPasswordModel.


        :param user_name: The user_name of this ResetPasswordModel.
        :type user_name: str
        """
        if user_name is None:
            raise ValueError("Invalid value for `user_name`, must not be `None`")

        self._user_name = user_name
