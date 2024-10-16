# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class KeywordJobRank(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, domain: str=None, keyword: str=None, localization_code: str=None, localization_zip: str=None, search_engine: str='google'):
        """KeywordJobRank - a model defined in OpenAPI

        :param domain: The domain of this KeywordJobRank.
        :param keyword: The keyword of this KeywordJobRank.
        :param localization_code: The localization_code of this KeywordJobRank.
        :param localization_zip: The localization_zip of this KeywordJobRank.
        :param search_engine: The search_engine of this KeywordJobRank.
        """
        self.openapi_types = {
            'domain': str,
            'keyword': str,
            'localization_code': str,
            'localization_zip': str,
            'search_engine': str
        }

        self.attribute_map = {
            'domain': 'domain',
            'keyword': 'keyword',
            'localization_code': 'localization_code',
            'localization_zip': 'localization_zip',
            'search_engine': 'search_engine'
        }

        self._domain = domain
        self._keyword = keyword
        self._localization_code = localization_code
        self._localization_zip = localization_zip
        self._search_engine = search_engine

    @classmethod
    def from_dict(cls, dikt: dict) -> 'KeywordJobRank':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The KeywordJobRank of this KeywordJobRank.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def domain(self):
        """Gets the domain of this KeywordJobRank.

        The domain you want to check its rank for the keyword entered

        :return: The domain of this KeywordJobRank.
        :rtype: str
        """
        return self._domain

    @domain.setter
    def domain(self, domain):
        """Sets the domain of this KeywordJobRank.

        The domain you want to check its rank for the keyword entered

        :param domain: The domain of this KeywordJobRank.
        :type domain: str
        """

        self._domain = domain

    @property
    def keyword(self):
        """Gets the keyword of this KeywordJobRank.

        keyword (search term)

        :return: The keyword of this KeywordJobRank.
        :rtype: str
        """
        return self._keyword

    @keyword.setter
    def keyword(self, keyword):
        """Sets the keyword of this KeywordJobRank.

        keyword (search term)

        :param keyword: The keyword of this KeywordJobRank.
        :type keyword: str
        """
        if keyword is None:
            raise ValueError("Invalid value for `keyword`, must not be `None`")

        self._keyword = keyword

    @property
    def localization_code(self):
        """Gets the localization_code of this KeywordJobRank.

        A code for the localization, which is a combination of country and language

        :return: The localization_code of this KeywordJobRank.
        :rtype: str
        """
        return self._localization_code

    @localization_code.setter
    def localization_code(self, localization_code):
        """Sets the localization_code of this KeywordJobRank.

        A code for the localization, which is a combination of country and language

        :param localization_code: The localization_code of this KeywordJobRank.
        :type localization_code: str
        """
        allowed_values = ["us", "uk", "au", "br", "be_dutch", "be_french", "ca", "de", "es", "ie", "il", "nl", "sg", "za", "it", "is", "ch", "fr", "se", "at", "dk", "nz", "gr", "in", "ms", "pl", "hk", "id", "ru", "ae", "fi", "pt", "mx", "tr", "cl", "jp", "ar"]  # noqa: E501
        if localization_code not in allowed_values:
            raise ValueError(
                "Invalid value for `localization_code` ({0}), must be one of {1}"
                .format(localization_code, allowed_values)
            )

        self._localization_code = localization_code

    @property
    def localization_zip(self):
        """Gets the localization_zip of this KeywordJobRank.

        option to localize the results per zip code

        :return: The localization_zip of this KeywordJobRank.
        :rtype: str
        """
        return self._localization_zip

    @localization_zip.setter
    def localization_zip(self, localization_zip):
        """Sets the localization_zip of this KeywordJobRank.

        option to localize the results per zip code

        :param localization_zip: The localization_zip of this KeywordJobRank.
        :type localization_zip: str
        """

        self._localization_zip = localization_zip

    @property
    def search_engine(self):
        """Gets the search_engine of this KeywordJobRank.

        google/bing/google_mobile

        :return: The search_engine of this KeywordJobRank.
        :rtype: str
        """
        return self._search_engine

    @search_engine.setter
    def search_engine(self, search_engine):
        """Sets the search_engine of this KeywordJobRank.

        google/bing/google_mobile

        :param search_engine: The search_engine of this KeywordJobRank.
        :type search_engine: str
        """
        allowed_values = ["google", "bing", "google_mobile"]  # noqa: E501
        if search_engine not in allowed_values:
            raise ValueError(
                "Invalid value for `search_engine` ({0}), must be one of {1}"
                .format(search_engine, allowed_values)
            )

        self._search_engine = search_engine
