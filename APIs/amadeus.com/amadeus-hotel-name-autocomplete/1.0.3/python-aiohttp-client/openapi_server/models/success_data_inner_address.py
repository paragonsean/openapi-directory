# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
import re
from openapi_server import util


class SuccessDataInnerAddress(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, city_name: str=None, country_code: str=None, state_code: str=None):
        """SuccessDataInnerAddress - a model defined in OpenAPI

        :param city_name: The city_name of this SuccessDataInnerAddress.
        :param country_code: The country_code of this SuccessDataInnerAddress.
        :param state_code: The state_code of this SuccessDataInnerAddress.
        """
        self.openapi_types = {
            'city_name': str,
            'country_code': str,
            'state_code': str
        }

        self.attribute_map = {
            'city_name': 'cityName',
            'country_code': 'countryCode',
            'state_code': 'stateCode'
        }

        self._city_name = city_name
        self._country_code = country_code
        self._state_code = state_code

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SuccessDataInnerAddress':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Success_data_inner_address of this SuccessDataInnerAddress.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def city_name(self):
        """Gets the city_name of this SuccessDataInnerAddress.

        The name of the city to which the location belongs to.

        :return: The city_name of this SuccessDataInnerAddress.
        :rtype: str
        """
        return self._city_name

    @city_name.setter
    def city_name(self, city_name):
        """Sets the city_name of this SuccessDataInnerAddress.

        The name of the city to which the location belongs to.

        :param city_name: The city_name of this SuccessDataInnerAddress.
        :type city_name: str
        """
        if city_name is None:
            raise ValueError("Invalid value for `city_name`, must not be `None`")
        if city_name is not None and len(city_name) > 105:
            raise ValueError("Invalid value for `city_name`, length must be less than or equal to `105`")
        if city_name is not None and len(city_name) < 1:
            raise ValueError("Invalid value for `city_name`, length must be greater than or equal to `1`")
        if city_name is not None and not re.search(r'^[A-Za-z0-9 - ]+', city_name):
            raise ValueError("Invalid value for `city_name`, must be a follow pattern or equal to `/^[A-Za-z0-9 - ]+/`")

        self._city_name = city_name

    @property
    def country_code(self):
        """Gets the country_code of this SuccessDataInnerAddress.

        The countrycode to which the location belongs to.

        :return: The country_code of this SuccessDataInnerAddress.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this SuccessDataInnerAddress.

        The countrycode to which the location belongs to.

        :param country_code: The country_code of this SuccessDataInnerAddress.
        :type country_code: str
        """
        if country_code is None:
            raise ValueError("Invalid value for `country_code`, must not be `None`")
        if country_code is not None and len(country_code) > 2:
            raise ValueError("Invalid value for `country_code`, length must be less than or equal to `2`")
        if country_code is not None and len(country_code) < 2:
            raise ValueError("Invalid value for `country_code`, length must be greater than or equal to `2`")
        if country_code is not None and not re.search(r'^[A-Z]+', country_code):
            raise ValueError("Invalid value for `country_code`, must be a follow pattern or equal to `/^[A-Z]+/`")

        self._country_code = country_code

    @property
    def state_code(self):
        """Gets the state_code of this SuccessDataInnerAddress.

        The statecode to which the location belongs to.

        :return: The state_code of this SuccessDataInnerAddress.
        :rtype: str
        """
        return self._state_code

    @state_code.setter
    def state_code(self, state_code):
        """Sets the state_code of this SuccessDataInnerAddress.

        The statecode to which the location belongs to.

        :param state_code: The state_code of this SuccessDataInnerAddress.
        :type state_code: str
        """
        if state_code is not None and len(state_code) > 2:
            raise ValueError("Invalid value for `state_code`, length must be less than or equal to `2`")
        if state_code is not None and len(state_code) < 2:
            raise ValueError("Invalid value for `state_code`, length must be greater than or equal to `2`")
        if state_code is not None and not re.search(r'^[A-Z]+', state_code):
            raise ValueError("Invalid value for `state_code`, must be a follow pattern or equal to `/^[A-Z]+/`")

        self._state_code = state_code
