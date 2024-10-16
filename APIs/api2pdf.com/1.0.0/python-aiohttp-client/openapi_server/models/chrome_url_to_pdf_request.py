# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.chrome_advanced_options import ChromeAdvancedOptions
from openapi_server import util


class ChromeUrlToPdfRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, file_name: str=None, inline_pdf: bool=None, options: ChromeAdvancedOptions=None, url: str=None):
        """ChromeUrlToPdfRequest - a model defined in OpenAPI

        :param file_name: The file_name of this ChromeUrlToPdfRequest.
        :param inline_pdf: The inline_pdf of this ChromeUrlToPdfRequest.
        :param options: The options of this ChromeUrlToPdfRequest.
        :param url: The url of this ChromeUrlToPdfRequest.
        """
        self.openapi_types = {
            'file_name': str,
            'inline_pdf': bool,
            'options': ChromeAdvancedOptions,
            'url': str
        }

        self.attribute_map = {
            'file_name': 'fileName',
            'inline_pdf': 'inlinePdf',
            'options': 'options',
            'url': 'url'
        }

        self._file_name = file_name
        self._inline_pdf = inline_pdf
        self._options = options
        self._url = url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ChromeUrlToPdfRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ChromeUrlToPdfRequest of this ChromeUrlToPdfRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def file_name(self):
        """Gets the file_name of this ChromeUrlToPdfRequest.


        :return: The file_name of this ChromeUrlToPdfRequest.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this ChromeUrlToPdfRequest.


        :param file_name: The file_name of this ChromeUrlToPdfRequest.
        :type file_name: str
        """

        self._file_name = file_name

    @property
    def inline_pdf(self):
        """Gets the inline_pdf of this ChromeUrlToPdfRequest.


        :return: The inline_pdf of this ChromeUrlToPdfRequest.
        :rtype: bool
        """
        return self._inline_pdf

    @inline_pdf.setter
    def inline_pdf(self, inline_pdf):
        """Sets the inline_pdf of this ChromeUrlToPdfRequest.


        :param inline_pdf: The inline_pdf of this ChromeUrlToPdfRequest.
        :type inline_pdf: bool
        """

        self._inline_pdf = inline_pdf

    @property
    def options(self):
        """Gets the options of this ChromeUrlToPdfRequest.


        :return: The options of this ChromeUrlToPdfRequest.
        :rtype: ChromeAdvancedOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this ChromeUrlToPdfRequest.


        :param options: The options of this ChromeUrlToPdfRequest.
        :type options: ChromeAdvancedOptions
        """

        self._options = options

    @property
    def url(self):
        """Gets the url of this ChromeUrlToPdfRequest.


        :return: The url of this ChromeUrlToPdfRequest.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ChromeUrlToPdfRequest.


        :param url: The url of this ChromeUrlToPdfRequest.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")

        self._url = url
