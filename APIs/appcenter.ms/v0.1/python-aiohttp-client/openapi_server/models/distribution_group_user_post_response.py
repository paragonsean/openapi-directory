# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DistributionGroupUserPostResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, invite_pending: bool=None, message: str=None, status: int=None, user_email: str=None):
        """DistributionGroupUserPostResponse - a model defined in OpenAPI

        :param code: The code of this DistributionGroupUserPostResponse.
        :param invite_pending: The invite_pending of this DistributionGroupUserPostResponse.
        :param message: The message of this DistributionGroupUserPostResponse.
        :param status: The status of this DistributionGroupUserPostResponse.
        :param user_email: The user_email of this DistributionGroupUserPostResponse.
        """
        self.openapi_types = {
            'code': str,
            'invite_pending': bool,
            'message': str,
            'status': int,
            'user_email': str
        }

        self.attribute_map = {
            'code': 'code',
            'invite_pending': 'invite_pending',
            'message': 'message',
            'status': 'status',
            'user_email': 'user_email'
        }

        self._code = code
        self._invite_pending = invite_pending
        self._message = message
        self._status = status
        self._user_email = user_email

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DistributionGroupUserPostResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The DistributionGroupUserPostResponse of this DistributionGroupUserPostResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this DistributionGroupUserPostResponse.

        The code of the result

        :return: The code of this DistributionGroupUserPostResponse.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this DistributionGroupUserPostResponse.

        The code of the result

        :param code: The code of this DistributionGroupUserPostResponse.
        :type code: str
        """

        self._code = code

    @property
    def invite_pending(self):
        """Gets the invite_pending of this DistributionGroupUserPostResponse.

        Whether the has accepted the invite. Available when an invite is pending, and the value will be \"true\".

        :return: The invite_pending of this DistributionGroupUserPostResponse.
        :rtype: bool
        """
        return self._invite_pending

    @invite_pending.setter
    def invite_pending(self, invite_pending):
        """Sets the invite_pending of this DistributionGroupUserPostResponse.

        Whether the has accepted the invite. Available when an invite is pending, and the value will be \"true\".

        :param invite_pending: The invite_pending of this DistributionGroupUserPostResponse.
        :type invite_pending: bool
        """

        self._invite_pending = invite_pending

    @property
    def message(self):
        """Gets the message of this DistributionGroupUserPostResponse.

        The message of the result

        :return: The message of this DistributionGroupUserPostResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DistributionGroupUserPostResponse.

        The message of the result

        :param message: The message of this DistributionGroupUserPostResponse.
        :type message: str
        """

        self._message = message

    @property
    def status(self):
        """Gets the status of this DistributionGroupUserPostResponse.

        The status code of the result

        :return: The status of this DistributionGroupUserPostResponse.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this DistributionGroupUserPostResponse.

        The status code of the result

        :param status: The status of this DistributionGroupUserPostResponse.
        :type status: int
        """
        if status is None:
            raise ValueError("Invalid value for `status`, must not be `None`")

        self._status = status

    @property
    def user_email(self):
        """Gets the user_email of this DistributionGroupUserPostResponse.

        The email of the user

        :return: The user_email of this DistributionGroupUserPostResponse.
        :rtype: str
        """
        return self._user_email

    @user_email.setter
    def user_email(self, user_email):
        """Sets the user_email of this DistributionGroupUserPostResponse.

        The email of the user

        :param user_email: The user_email of this DistributionGroupUserPostResponse.
        :type user_email: str
        """

        self._user_email = user_email
