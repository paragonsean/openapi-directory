# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.violated_password_policy import ViolatedPasswordPolicy
from openapi_server import util


class PasswordPolicyViolationResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: int=None, debug_info: str=None, error_code: int=None, message: str=None, violated_password_policies: List[ViolatedPasswordPolicy]=None):
        """PasswordPolicyViolationResponse - a model defined in OpenAPI

        :param code: The code of this PasswordPolicyViolationResponse.
        :param debug_info: The debug_info of this PasswordPolicyViolationResponse.
        :param error_code: The error_code of this PasswordPolicyViolationResponse.
        :param message: The message of this PasswordPolicyViolationResponse.
        :param violated_password_policies: The violated_password_policies of this PasswordPolicyViolationResponse.
        """
        self.openapi_types = {
            'code': int,
            'debug_info': str,
            'error_code': int,
            'message': str,
            'violated_password_policies': List[ViolatedPasswordPolicy]
        }

        self.attribute_map = {
            'code': 'code',
            'debug_info': 'debugInfo',
            'error_code': 'errorCode',
            'message': 'message',
            'violated_password_policies': 'violatedPasswordPolicies'
        }

        self._code = code
        self._debug_info = debug_info
        self._error_code = error_code
        self._message = message
        self._violated_password_policies = violated_password_policies

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PasswordPolicyViolationResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The PasswordPolicyViolationResponse of this PasswordPolicyViolationResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this PasswordPolicyViolationResponse.

        HTTP status code

        :return: The code of this PasswordPolicyViolationResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this PasswordPolicyViolationResponse.

        HTTP status code

        :param code: The code of this PasswordPolicyViolationResponse.
        :type code: int
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def debug_info(self):
        """Gets the debug_info of this PasswordPolicyViolationResponse.

        Debug information

        :return: The debug_info of this PasswordPolicyViolationResponse.
        :rtype: str
        """
        return self._debug_info

    @debug_info.setter
    def debug_info(self, debug_info):
        """Sets the debug_info of this PasswordPolicyViolationResponse.

        Debug information

        :param debug_info: The debug_info of this PasswordPolicyViolationResponse.
        :type debug_info: str
        """

        self._debug_info = debug_info

    @property
    def error_code(self):
        """Gets the error_code of this PasswordPolicyViolationResponse.

        Internal error code

        :return: The error_code of this PasswordPolicyViolationResponse.
        :rtype: int
        """
        return self._error_code

    @error_code.setter
    def error_code(self, error_code):
        """Sets the error_code of this PasswordPolicyViolationResponse.

        Internal error code

        :param error_code: The error_code of this PasswordPolicyViolationResponse.
        :type error_code: int
        """

        self._error_code = error_code

    @property
    def message(self):
        """Gets the message of this PasswordPolicyViolationResponse.

        HTTP status code description

        :return: The message of this PasswordPolicyViolationResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this PasswordPolicyViolationResponse.

        HTTP status code description

        :param message: The message of this PasswordPolicyViolationResponse.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message

    @property
    def violated_password_policies(self):
        """Gets the violated_password_policies of this PasswordPolicyViolationResponse.

        List of violated password policies

        :return: The violated_password_policies of this PasswordPolicyViolationResponse.
        :rtype: List[ViolatedPasswordPolicy]
        """
        return self._violated_password_policies

    @violated_password_policies.setter
    def violated_password_policies(self, violated_password_policies):
        """Sets the violated_password_policies of this PasswordPolicyViolationResponse.

        List of violated password policies

        :param violated_password_policies: The violated_password_policies of this PasswordPolicyViolationResponse.
        :type violated_password_policies: List[ViolatedPasswordPolicy]
        """

        self._violated_password_policies = violated_password_policies
