# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class VerifySmsRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, sms: str=None):
        """VerifySmsRequest - a model defined in OpenAPI

        :param code: The code of this VerifySmsRequest.
        :param sms: The sms of this VerifySmsRequest.
        """
        self.openapi_types = {
            'code': str,
            'sms': str
        }

        self.attribute_map = {
            'code': 'code',
            'sms': 'sms'
        }

        self._code = code
        self._sms = sms

    @classmethod
    def from_dict(cls, dikt: dict) -> 'VerifySmsRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The VerifySmsRequest of this VerifySmsRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this VerifySmsRequest.


        :return: The code of this VerifySmsRequest.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this VerifySmsRequest.


        :param code: The code of this VerifySmsRequest.
        :type code: str
        """
        if code is None:
            raise ValueError("Invalid value for `code`, must not be `None`")

        self._code = code

    @property
    def sms(self):
        """Gets the sms of this VerifySmsRequest.


        :return: The sms of this VerifySmsRequest.
        :rtype: str
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this VerifySmsRequest.


        :param sms: The sms of this VerifySmsRequest.
        :type sms: str
        """
        if sms is None:
            raise ValueError("Invalid value for `sms`, must not be `None`")

        self._sms = sms
