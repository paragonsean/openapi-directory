# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.consent import Consent
from openapi_server.models.date_range import DateRange
from openapi_server.models.key_material import KeyMaterial
from openapi_server import util


class HIPHIRequestHiRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, consent: Consent=None, data_push_url: str=None, date_range: DateRange=None, key_material: KeyMaterial=None):
        """HIPHIRequestHiRequest - a model defined in OpenAPI

        :param consent: The consent of this HIPHIRequestHiRequest.
        :param data_push_url: The data_push_url of this HIPHIRequestHiRequest.
        :param date_range: The date_range of this HIPHIRequestHiRequest.
        :param key_material: The key_material of this HIPHIRequestHiRequest.
        """
        self.openapi_types = {
            'consent': Consent,
            'data_push_url': str,
            'date_range': DateRange,
            'key_material': KeyMaterial
        }

        self.attribute_map = {
            'consent': 'consent',
            'data_push_url': 'dataPushUrl',
            'date_range': 'dateRange',
            'key_material': 'keyMaterial'
        }

        self._consent = consent
        self._data_push_url = data_push_url
        self._date_range = date_range
        self._key_material = key_material

    @classmethod
    def from_dict(cls, dikt: dict) -> 'HIPHIRequestHiRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The HIPHIRequest_hiRequest of this HIPHIRequestHiRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def consent(self):
        """Gets the consent of this HIPHIRequestHiRequest.


        :return: The consent of this HIPHIRequestHiRequest.
        :rtype: Consent
        """
        return self._consent

    @consent.setter
    def consent(self, consent):
        """Sets the consent of this HIPHIRequestHiRequest.


        :param consent: The consent of this HIPHIRequestHiRequest.
        :type consent: Consent
        """
        if consent is None:
            raise ValueError("Invalid value for `consent`, must not be `None`")

        self._consent = consent

    @property
    def data_push_url(self):
        """Gets the data_push_url of this HIPHIRequestHiRequest.


        :return: The data_push_url of this HIPHIRequestHiRequest.
        :rtype: str
        """
        return self._data_push_url

    @data_push_url.setter
    def data_push_url(self, data_push_url):
        """Sets the data_push_url of this HIPHIRequestHiRequest.


        :param data_push_url: The data_push_url of this HIPHIRequestHiRequest.
        :type data_push_url: str
        """
        if data_push_url is None:
            raise ValueError("Invalid value for `data_push_url`, must not be `None`")

        self._data_push_url = data_push_url

    @property
    def date_range(self):
        """Gets the date_range of this HIPHIRequestHiRequest.


        :return: The date_range of this HIPHIRequestHiRequest.
        :rtype: DateRange
        """
        return self._date_range

    @date_range.setter
    def date_range(self, date_range):
        """Sets the date_range of this HIPHIRequestHiRequest.


        :param date_range: The date_range of this HIPHIRequestHiRequest.
        :type date_range: DateRange
        """
        if date_range is None:
            raise ValueError("Invalid value for `date_range`, must not be `None`")

        self._date_range = date_range

    @property
    def key_material(self):
        """Gets the key_material of this HIPHIRequestHiRequest.


        :return: The key_material of this HIPHIRequestHiRequest.
        :rtype: KeyMaterial
        """
        return self._key_material

    @key_material.setter
    def key_material(self, key_material):
        """Sets the key_material of this HIPHIRequestHiRequest.


        :param key_material: The key_material of this HIPHIRequestHiRequest.
        :type key_material: KeyMaterial
        """
        if key_material is None:
            raise ValueError("Invalid value for `key_material`, must not be `None`")

        self._key_material = key_material
