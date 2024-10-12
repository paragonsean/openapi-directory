# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.translate_translated_text import TranslateTranslatedText
from openapi_server import util


class Translate(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, translated_text: TranslateTranslatedText=None):
        """Translate - a model defined in OpenAPI

        :param translated_text: The translated_text of this Translate.
        """
        self.openapi_types = {
            'translated_text': TranslateTranslatedText
        }

        self.attribute_map = {
            'translated_text': 'translatedText'
        }

        self._translated_text = translated_text

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Translate':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The translate of this Translate.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def translated_text(self):
        """Gets the translated_text of this Translate.


        :return: The translated_text of this Translate.
        :rtype: TranslateTranslatedText
        """
        return self._translated_text

    @translated_text.setter
    def translated_text(self, translated_text):
        """Sets the translated_text of this Translate.


        :param translated_text: The translated_text of this Translate.
        :type translated_text: TranslateTranslatedText
        """

        self._translated_text = translated_text
