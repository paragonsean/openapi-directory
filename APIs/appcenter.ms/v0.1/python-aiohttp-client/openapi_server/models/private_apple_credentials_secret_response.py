# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PrivateAppleCredentialsSecretResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: object=None, display_name: str=None, id: str=None, is2_fa: bool=None, is_valid: bool=None, service_type: str=None):
        """PrivateAppleCredentialsSecretResponse - a model defined in OpenAPI

        :param data: The data of this PrivateAppleCredentialsSecretResponse.
        :param display_name: The display_name of this PrivateAppleCredentialsSecretResponse.
        :param id: The id of this PrivateAppleCredentialsSecretResponse.
        :param is2_fa: The is2_fa of this PrivateAppleCredentialsSecretResponse.
        :param is_valid: The is_valid of this PrivateAppleCredentialsSecretResponse.
        :param service_type: The service_type of this PrivateAppleCredentialsSecretResponse.
        """
        self.openapi_types = {
            'data': object,
            'display_name': str,
            'id': str,
            'is2_fa': bool,
            'is_valid': bool,
            'service_type': str
        }

        self.attribute_map = {
            'data': 'data',
            'display_name': 'displayName',
            'id': 'id',
            'is2_fa': 'is2FA',
            'is_valid': 'isValid',
            'service_type': 'serviceType'
        }

        self._data = data
        self._display_name = display_name
        self._id = id
        self._is2_fa = is2_fa
        self._is_valid = is_valid
        self._service_type = service_type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PrivateAppleCredentialsSecretResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PrivateAppleCredentialsSecretResponse of this PrivateAppleCredentialsSecretResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this PrivateAppleCredentialsSecretResponse.

        apple secret details

        :return: The data of this PrivateAppleCredentialsSecretResponse.
        :rtype: object
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this PrivateAppleCredentialsSecretResponse.

        apple secret details

        :param data: The data of this PrivateAppleCredentialsSecretResponse.
        :type data: object
        """
        if data is None:
            raise ValueError("Invalid value for `data`, must not be `None`")

        self._data = data

    @property
    def display_name(self):
        """Gets the display_name of this PrivateAppleCredentialsSecretResponse.

        display name of shared connection

        :return: The display_name of this PrivateAppleCredentialsSecretResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PrivateAppleCredentialsSecretResponse.

        display name of shared connection

        :param display_name: The display_name of this PrivateAppleCredentialsSecretResponse.
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def id(self):
        """Gets the id of this PrivateAppleCredentialsSecretResponse.

        id of the shared connection

        :return: The id of this PrivateAppleCredentialsSecretResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PrivateAppleCredentialsSecretResponse.

        id of the shared connection

        :param id: The id of this PrivateAppleCredentialsSecretResponse.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def is2_fa(self):
        """Gets the is2_fa of this PrivateAppleCredentialsSecretResponse.

        if the account is a 2FA account or not

        :return: The is2_fa of this PrivateAppleCredentialsSecretResponse.
        :rtype: bool
        """
        return self._is2_fa

    @is2_fa.setter
    def is2_fa(self, is2_fa):
        """Sets the is2_fa of this PrivateAppleCredentialsSecretResponse.

        if the account is a 2FA account or not

        :param is2_fa: The is2_fa of this PrivateAppleCredentialsSecretResponse.
        :type is2_fa: bool
        """

        self._is2_fa = is2_fa

    @property
    def is_valid(self):
        """Gets the is_valid of this PrivateAppleCredentialsSecretResponse.

        whether the credentials are valid or not

        :return: The is_valid of this PrivateAppleCredentialsSecretResponse.
        :rtype: bool
        """
        return self._is_valid

    @is_valid.setter
    def is_valid(self, is_valid):
        """Sets the is_valid of this PrivateAppleCredentialsSecretResponse.

        whether the credentials are valid or not

        :param is_valid: The is_valid of this PrivateAppleCredentialsSecretResponse.
        :type is_valid: bool
        """

        self._is_valid = is_valid

    @property
    def service_type(self):
        """Gets the service_type of this PrivateAppleCredentialsSecretResponse.

        service type of shared connection can be apple|gitlab|googleplay|jira|applecertificate

        :return: The service_type of this PrivateAppleCredentialsSecretResponse.
        :rtype: str
        """
        return self._service_type

    @service_type.setter
    def service_type(self, service_type):
        """Sets the service_type of this PrivateAppleCredentialsSecretResponse.

        service type of shared connection can be apple|gitlab|googleplay|jira|applecertificate

        :param service_type: The service_type of this PrivateAppleCredentialsSecretResponse.
        :type service_type: str
        """
        allowed_values = ["apple", "jira", "googleplay", "gitlab"]  # noqa: E501
        if service_type not in allowed_values:
            raise ValueError(
                "Invalid value for `service_type` ({0}), must be one of {1}"
                .format(service_type, allowed_values)
            )

        self._service_type = service_type
