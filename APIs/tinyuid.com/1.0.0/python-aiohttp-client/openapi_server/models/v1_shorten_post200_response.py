# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class V1ShortenPost200Response(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, result_url: str=None):
        """V1ShortenPost200Response - a model defined in OpenAPI

        :param result_url: The result_url of this V1ShortenPost200Response.
        """
        self.openapi_types = {
            'result_url': str
        }

        self.attribute_map = {
            'result_url': 'result_url'
        }

        self._result_url = result_url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'V1ShortenPost200Response':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The _v1_shorten_post_200_response of this V1ShortenPost200Response.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def result_url(self):
        """Gets the result_url of this V1ShortenPost200Response.

        Short link

        :return: The result_url of this V1ShortenPost200Response.
        :rtype: str
        """
        return self._result_url

    @result_url.setter
    def result_url(self, result_url):
        """Sets the result_url of this V1ShortenPost200Response.

        Short link

        :param result_url: The result_url of this V1ShortenPost200Response.
        :type result_url: str
        """
        if result_url is None:
            raise ValueError("Invalid value for `result_url`, must not be `None`")

        self._result_url = result_url
