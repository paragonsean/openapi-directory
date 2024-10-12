# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.institutional_identification2 import InstitutionalIdentification2
import re
from openapi_server import util


class DebtorAgent7CH(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, bic: str=None, iid: InstitutionalIdentification2=None):
        """DebtorAgent7CH - a model defined in OpenAPI

        :param bic: The bic of this DebtorAgent7CH.
        :param iid: The iid of this DebtorAgent7CH.
        """
        self.openapi_types = {
            'bic': str,
            'iid': InstitutionalIdentification2
        }

        self.attribute_map = {
            'bic': 'bic',
            'iid': 'iid'
        }

        self._bic = bic
        self._iid = iid

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DebtorAgent7CH':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The debtorAgent7-CH of this DebtorAgent7CH.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def bic(self):
        """Gets the bic of this DebtorAgent7CH.

        BICFI 

        :return: The bic of this DebtorAgent7CH.
        :rtype: str
        """
        return self._bic

    @bic.setter
    def bic(self, bic):
        """Sets the bic of this DebtorAgent7CH.

        BICFI 

        :param bic: The bic of this DebtorAgent7CH.
        :type bic: str
        """
        if bic is not None and not re.search(r'[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}', bic):
            raise ValueError("Invalid value for `bic`, must be a follow pattern or equal to `/[A-Z]{6,6}[A-Z2-9][A-NP-Z0-9]([A-Z0-9]{3,3}){0,1}/`")

        self._bic = bic

    @property
    def iid(self):
        """Gets the iid of this DebtorAgent7CH.


        :return: The iid of this DebtorAgent7CH.
        :rtype: InstitutionalIdentification2
        """
        return self._iid

    @iid.setter
    def iid(self, iid):
        """Sets the iid of this DebtorAgent7CH.


        :param iid: The iid of this DebtorAgent7CH.
        :type iid: InstitutionalIdentification2
        """

        self._iid = iid
