# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CodePushAcquisitionGetAcquisitionStatus200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, message: str=None):
        """CodePushAcquisitionGetAcquisitionStatus200Response - a model defined in OpenAPI

        :param code: The code of this CodePushAcquisitionGetAcquisitionStatus200Response.
        :param message: The message of this CodePushAcquisitionGetAcquisitionStatus200Response.
        """
        self.openapi_types = {
            'code': str,
            'message': str
        }

        self.attribute_map = {
            'code': 'code',
            'message': 'message'
        }

        self._code = code
        self._message = message

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CodePushAcquisitionGetAcquisitionStatus200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The codePushAcquisition_getAcquisitionStatus_200_response of this CodePushAcquisitionGetAcquisitionStatus200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this CodePushAcquisitionGetAcquisitionStatus200Response.

        The code indicating the status

        :return: The code of this CodePushAcquisitionGetAcquisitionStatus200Response.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this CodePushAcquisitionGetAcquisitionStatus200Response.

        The code indicating the status

        :param code: The code of this CodePushAcquisitionGetAcquisitionStatus200Response.
        :type code: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def message(self):
        """Gets the message of this CodePushAcquisitionGetAcquisitionStatus200Response.

        The message indicating the status

        :return: The message of this CodePushAcquisitionGetAcquisitionStatus200Response.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this CodePushAcquisitionGetAcquisitionStatus200Response.

        The message indicating the status

        :param message: The message of this CodePushAcquisitionGetAcquisitionStatus200Response.
        :type message: str
        """
        if message is None:
            raise ValueError("Invalid value for `message`, must not be `None`")

        self._message = message
