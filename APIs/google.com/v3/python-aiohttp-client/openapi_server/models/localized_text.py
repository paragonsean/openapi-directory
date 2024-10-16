# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class LocalizedText(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, language_code: str=None, text: str=None):
        """LocalizedText - a model defined in OpenAPI

        :param language_code: The language_code of this LocalizedText.
        :param text: The text of this LocalizedText.
        """
        self.openapi_types = {
            'language_code': str,
            'text': str
        }

        self.attribute_map = {
            'language_code': 'languageCode',
            'text': 'text'
        }

        self._language_code = language_code
        self._text = text

    @classmethod
    def from_dict(cls, dikt: dict) -> 'LocalizedText':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The LocalizedText of this LocalizedText.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def language_code(self):
        """Gets the language_code of this LocalizedText.

        The text's BCP-47 language code, such as \"en-US\" or \"sr-Latn\". For more information, see http://www.unicode.org/reports/tr35/#Unicode_locale_identifier.

        :return: The language_code of this LocalizedText.
        :rtype: str
        """
        return self._language_code

    @language_code.setter
    def language_code(self, language_code):
        """Sets the language_code of this LocalizedText.

        The text's BCP-47 language code, such as \"en-US\" or \"sr-Latn\". For more information, see http://www.unicode.org/reports/tr35/#Unicode_locale_identifier.

        :param language_code: The language_code of this LocalizedText.
        :type language_code: str
        """

        self._language_code = language_code

    @property
    def text(self):
        """Gets the text of this LocalizedText.

        Localized string in the language corresponding to `language_code' below.

        :return: The text of this LocalizedText.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this LocalizedText.

        Localized string in the language corresponding to `language_code' below.

        :param text: The text of this LocalizedText.
        :type text: str
        """

        self._text = text
