# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.spell_check_response_tokens_inner import SpellCheckResponseTokensInner
from openapi_server import util


class SpellCheckResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, corrected_text_html: str=None, tokens: List[SpellCheckResponseTokensInner]=None):
        """SpellCheckResponse - a model defined in OpenAPI

        :param corrected_text_html: The corrected_text_html of this SpellCheckResponse.
        :param tokens: The tokens of this SpellCheckResponse.
        """
        self.openapi_types = {
            'corrected_text_html': str,
            'tokens': List[SpellCheckResponseTokensInner]
        }

        self.attribute_map = {
            'corrected_text_html': 'corrected_text_html',
            'tokens': 'tokens'
        }

        self._corrected_text_html = corrected_text_html
        self._tokens = tokens

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SpellCheckResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SpellCheckResponse of this SpellCheckResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def corrected_text_html(self):
        """Gets the corrected_text_html of this SpellCheckResponse.

        The corrected text for the entire search term (multiple words/tokens), where misspelled tokens are replaced with the correct texts and html tags <b><i>

        :return: The corrected_text_html of this SpellCheckResponse.
        :rtype: str
        """
        return self._corrected_text_html

    @corrected_text_html.setter
    def corrected_text_html(self, corrected_text_html):
        """Sets the corrected_text_html of this SpellCheckResponse.

        The corrected text for the entire search term (multiple words/tokens), where misspelled tokens are replaced with the correct texts and html tags <b><i>

        :param corrected_text_html: The corrected_text_html of this SpellCheckResponse.
        :type corrected_text_html: str
        """
        if corrected_text_html is None:
            raise ValueError("Invalid value for `corrected_text_html`, must not be `None`")

        self._corrected_text_html = corrected_text_html

    @property
    def tokens(self):
        """Gets the tokens of this SpellCheckResponse.

        The word in the text query string that is not spelled correctly

        :return: The tokens of this SpellCheckResponse.
        :rtype: List[SpellCheckResponseTokensInner]
        """
        return self._tokens

    @tokens.setter
    def tokens(self, tokens):
        """Sets the tokens of this SpellCheckResponse.

        The word in the text query string that is not spelled correctly

        :param tokens: The tokens of this SpellCheckResponse.
        :type tokens: List[SpellCheckResponseTokensInner]
        """
        if tokens is None:
            raise ValueError("Invalid value for `tokens`, must not be `None`")

        self._tokens = tokens
