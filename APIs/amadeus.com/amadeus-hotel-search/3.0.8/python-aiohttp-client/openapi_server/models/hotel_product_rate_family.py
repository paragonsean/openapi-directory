# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
import re
from openapi_server import util


class HotelProductRateFamily(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, code: str=None, type: str=None):
        """HotelProductRateFamily - a model defined in OpenAPI

        :param code: The code of this HotelProductRateFamily.
        :param type: The type of this HotelProductRateFamily.
        """
        self.openapi_types = {
            'code': str,
            'type': str
        }

        self.attribute_map = {
            'code': 'code',
            'type': 'type'
        }

        self._code = code
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'HotelProductRateFamily':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The HotelProduct_RateFamily of this HotelProductRateFamily.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def code(self):
        """Gets the code of this HotelProductRateFamily.

        The estimated rate family (PRO,FAM,GOV)

        :return: The code of this HotelProductRateFamily.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this HotelProductRateFamily.

        The estimated rate family (PRO,FAM,GOV)

        :param code: The code of this HotelProductRateFamily.
        :type code: str
        """
        if code is not None and not re.search(r'[A-Z0-9]{3}', code):
            raise ValueError("Invalid value for `code`, must be a follow pattern or equal to `/[A-Z0-9]{3}/`")

        self._code = code

    @property
    def type(self):
        """Gets the type of this HotelProductRateFamily.

        The type of the rate (public=P, negotiated=N, conditional=C)

        :return: The type of this HotelProductRateFamily.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HotelProductRateFamily.

        The type of the rate (public=P, negotiated=N, conditional=C)

        :param type: The type of this HotelProductRateFamily.
        :type type: str
        """
        if type is not None and not re.search(r'[PNC]', type):
            raise ValueError("Invalid value for `type`, must be a follow pattern or equal to `/[PNC]/`")

        self._type = type
