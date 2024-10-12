# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class BillDocumentLink(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, media_type: str=None, url: str=None):
        """BillDocumentLink - a model defined in OpenAPI

        :param media_type: The media_type of this BillDocumentLink.
        :param url: The url of this BillDocumentLink.
        """
        self.openapi_types = {
            'media_type': str,
            'url': str
        }

        self.attribute_map = {
            'media_type': 'media_type',
            'url': 'url'
        }

        self._media_type = media_type
        self._url = url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BillDocumentLink':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BillDocumentLink of this BillDocumentLink.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def media_type(self):
        """Gets the media_type of this BillDocumentLink.


        :return: The media_type of this BillDocumentLink.
        :rtype: str
        """
        return self._media_type

    @media_type.setter
    def media_type(self, media_type):
        """Sets the media_type of this BillDocumentLink.


        :param media_type: The media_type of this BillDocumentLink.
        :type media_type: str
        """
        if media_type is None:
            raise ValueError("Invalid value for `media_type`, must not be `None`")

        self._media_type = media_type

    @property
    def url(self):
        """Gets the url of this BillDocumentLink.


        :return: The url of this BillDocumentLink.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this BillDocumentLink.


        :param url: The url of this BillDocumentLink.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")

        self._url = url
