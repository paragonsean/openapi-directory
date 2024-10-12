# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class TransactionAuthorisation(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, sca_authentication_data: str=None):
        """TransactionAuthorisation - a model defined in OpenAPI

        :param sca_authentication_data: The sca_authentication_data of this TransactionAuthorisation.
        """
        self.openapi_types = {
            'sca_authentication_data': str
        }

        self.attribute_map = {
            'sca_authentication_data': 'scaAuthenticationData'
        }

        self._sca_authentication_data = sca_authentication_data

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TransactionAuthorisation':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The transactionAuthorisation of this TransactionAuthorisation.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def sca_authentication_data(self):
        """Gets the sca_authentication_data of this TransactionAuthorisation.

        SCA authentication data, depending on the chosen authentication method. If the data is binary, then it is base64 encoded. 

        :return: The sca_authentication_data of this TransactionAuthorisation.
        :rtype: str
        """
        return self._sca_authentication_data

    @sca_authentication_data.setter
    def sca_authentication_data(self, sca_authentication_data):
        """Sets the sca_authentication_data of this TransactionAuthorisation.

        SCA authentication data, depending on the chosen authentication method. If the data is binary, then it is base64 encoded. 

        :param sca_authentication_data: The sca_authentication_data of this TransactionAuthorisation.
        :type sca_authentication_data: str
        """
        if sca_authentication_data is None:
            raise ValueError("Invalid value for `sca_authentication_data`, must not be `None`")

        self._sca_authentication_data = sca_authentication_data
