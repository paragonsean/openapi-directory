# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class VerificationSms(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id: str=None, sms: str=None, type: str=None, verified: bool=None, verified_at: datetime=None, verified_by: str=None):
        """VerificationSms - a model defined in OpenAPI

        :param id: The id of this VerificationSms.
        :param sms: The sms of this VerificationSms.
        :param type: The type of this VerificationSms.
        :param verified: The verified of this VerificationSms.
        :param verified_at: The verified_at of this VerificationSms.
        :param verified_by: The verified_by of this VerificationSms.
        """
        self.openapi_types = {
            'id': str,
            'sms': str,
            'type': str,
            'verified': bool,
            'verified_at': datetime,
            'verified_by': str
        }

        self.attribute_map = {
            'id': 'id',
            'sms': 'sms',
            'type': 'type',
            'verified': 'verified',
            'verified_at': 'verifiedAt',
            'verified_by': 'verifiedBy'
        }

        self._id = id
        self._sms = sms
        self._type = type
        self._verified = verified
        self._verified_at = verified_at
        self._verified_by = verified_by

    @classmethod
    def from_dict(cls, dikt: dict) -> 'VerificationSms':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The VerificationSms of this VerificationSms.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this VerificationSms.


        :return: The id of this VerificationSms.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VerificationSms.


        :param id: The id of this VerificationSms.
        :type id: str
        """

        self._id = id

    @property
    def sms(self):
        """Gets the sms of this VerificationSms.


        :return: The sms of this VerificationSms.
        :rtype: str
        """
        return self._sms

    @sms.setter
    def sms(self, sms):
        """Sets the sms of this VerificationSms.


        :param sms: The sms of this VerificationSms.
        :type sms: str
        """

        self._sms = sms

    @property
    def type(self):
        """Gets the type of this VerificationSms.


        :return: The type of this VerificationSms.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this VerificationSms.


        :param type: The type of this VerificationSms.
        :type type: str
        """
        allowed_values = ["sms"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def verified(self):
        """Gets the verified of this VerificationSms.


        :return: The verified of this VerificationSms.
        :rtype: bool
        """
        return self._verified

    @verified.setter
    def verified(self, verified):
        """Sets the verified of this VerificationSms.


        :param verified: The verified of this VerificationSms.
        :type verified: bool
        """

        self._verified = verified

    @property
    def verified_at(self):
        """Gets the verified_at of this VerificationSms.


        :return: The verified_at of this VerificationSms.
        :rtype: datetime
        """
        return self._verified_at

    @verified_at.setter
    def verified_at(self, verified_at):
        """Sets the verified_at of this VerificationSms.


        :param verified_at: The verified_at of this VerificationSms.
        :type verified_at: datetime
        """

        self._verified_at = verified_at

    @property
    def verified_by(self):
        """Gets the verified_by of this VerificationSms.


        :return: The verified_by of this VerificationSms.
        :rtype: str
        """
        return self._verified_by

    @verified_by.setter
    def verified_by(self, verified_by):
        """Sets the verified_by of this VerificationSms.


        :param verified_by: The verified_by of this VerificationSms.
        :type verified_by: str
        """

        self._verified_by = verified_by
