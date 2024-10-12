# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class InputDateTimeFormat(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, culture: str='en-US', format: str=None, input: str=None):
        """InputDateTimeFormat - a model defined in OpenAPI

        :param culture: The culture of this InputDateTimeFormat.
        :param format: The format of this InputDateTimeFormat.
        :param input: The input of this InputDateTimeFormat.
        """
        self.openapi_types = {
            'culture': str,
            'format': str,
            'input': str
        }

        self.attribute_map = {
            'culture': 'culture',
            'format': 'format',
            'input': 'input'
        }

        self._culture = culture
        self._format = format
        self._input = input

    @classmethod
    def from_dict(cls, dikt: dict) -> 'InputDateTimeFormat':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The inputDateTimeFormat of this InputDateTimeFormat.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def culture(self):
        """Gets the culture of this InputDateTimeFormat.

        Language culture

        :return: The culture of this InputDateTimeFormat.
        :rtype: str
        """
        return self._culture

    @culture.setter
    def culture(self, culture):
        """Sets the culture of this InputDateTimeFormat.

        Language culture

        :param culture: The culture of this InputDateTimeFormat.
        :type culture: str
        """
        allowed_values = ["en-US", "af-ZA", "ar-AE", "ar-BH", "ar-DZ", "ar-EG", "ar-IQ", "ar-JO", "ar-KW", "ar-LB", "ar-LY", "ar-MA", "ar-OM", "ar-QA", "ar-SA", "ar-SY", "ar-TN", "ar-YE", "az-AZ", "be-BY", "bg-BG", "bs-BA", "ca-ES", "cs-CZ", "cy-GB", "da-DK", "de-AT", "de-CH", "de-DE", "de-LI", "de-LU", "el-GR", "en-AU", "en-BZ", "en-CA", "en-CB", "en-GB", "en-IE", "en-JM", "en-NZ", "en-PH", "en-TT", "en-ZA", "en-ZW", "es-AR", "es-BO", "es-CL", "es-CO", "es-CR", "es-DO", "es-EC", "es-ES", "es-GT", "es-HN", "es-MX", "es-NI", "es-PA", "es-PE", "es-PR", "es-PY", "es-SV", "es-UY", "es-VE", "et-EE", "eu-ES", "fa-IR", "fi-FI", "fo-FO", "fr-BE", "fr-CA", "fr-CH", "fr-FR", "fr-LU", "fr-MC", "gl-ES", "gu-IN", "he-IL", "hi-IN", "hr-BA", "hr-HR", "hu-HU", "hy-AM", "id-ID", "is-IS", "it-CH", "it-IT", "ja-JP", "ka-GE", "kk-KZ", "kn-IN", "ko-KR", "ky-KG", "lt-LT", "lv-LV", "mi-NZ", "mn-MN", "mr-IN", "ms-BN", "ms-MY", "mt-MT", "nl-BE", "nl-NL", "nn-NO", "ns-ZA", "pa-IN", "pl-PL", "ps-AR", "pt-BR", "pt-PT", "ro-RO", "ru-RU", "sa-IN", "sk-SK", "sl-SI", "sq-AL", "sr-BA", "sr-SP", "sv-FI", "sv-SE", "sw-KE", "ta-IN", "te-IN", "th-TH", "tl-PH", "tn-ZA", "tr-TR", "uk-UA", "ur-PK", "uz-UZ", "vi-VN", "zh-CN", "zh-HK", "zh-MO", "zh-SG", "zh-TW", "zu-ZA"]  # noqa: E501
        if culture not in allowed_values:
            raise ValueError(
                "Invalid value for `culture` ({0}), must be one of {1}"
                .format(culture, allowed_values)
            )

        self._culture = culture

    @property
    def format(self):
        """Gets the format of this InputDateTimeFormat.

        Output format

        :return: The format of this InputDateTimeFormat.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this InputDateTimeFormat.

        Output format

        :param format: The format of this InputDateTimeFormat.
        :type format: str
        """
        if format is None:
            raise ValueError("Invalid value for `format`, must not be `None`")

        self._format = format

    @property
    def input(self):
        """Gets the input of this InputDateTimeFormat.

        Source date and time

        :return: The input of this InputDateTimeFormat.
        :rtype: str
        """
        return self._input

    @input.setter
    def input(self, input):
        """Sets the input of this InputDateTimeFormat.

        Source date and time

        :param input: The input of this InputDateTimeFormat.
        :type input: str
        """
        if input is None:
            raise ValueError("Invalid value for `input`, must not be `None`")

        self._input = input
