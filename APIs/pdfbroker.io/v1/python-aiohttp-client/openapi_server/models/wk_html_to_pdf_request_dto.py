# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class WkHtmlToPdfRequestDto(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, html_base64_string: str=None, resources: Dict[str, str]=None, url: str=None, wk_html_to_pdf_arguments: Dict[str, str]=None):
        """WkHtmlToPdfRequestDto - a model defined in OpenAPI

        :param html_base64_string: The html_base64_string of this WkHtmlToPdfRequestDto.
        :param resources: The resources of this WkHtmlToPdfRequestDto.
        :param url: The url of this WkHtmlToPdfRequestDto.
        :param wk_html_to_pdf_arguments: The wk_html_to_pdf_arguments of this WkHtmlToPdfRequestDto.
        """
        self.openapi_types = {
            'html_base64_string': str,
            'resources': Dict[str, str],
            'url': str,
            'wk_html_to_pdf_arguments': Dict[str, str]
        }

        self.attribute_map = {
            'html_base64_string': 'htmlBase64String',
            'resources': 'resources',
            'url': 'url',
            'wk_html_to_pdf_arguments': 'wkHtmlToPdfArguments'
        }

        self._html_base64_string = html_base64_string
        self._resources = resources
        self._url = url
        self._wk_html_to_pdf_arguments = wk_html_to_pdf_arguments

    @classmethod
    def from_dict(cls, dikt: dict) -> 'WkHtmlToPdfRequestDto':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The WkHtmlToPdfRequestDto of this WkHtmlToPdfRequestDto.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def html_base64_string(self):
        """Gets the html_base64_string of this WkHtmlToPdfRequestDto.

        Base64 encoded string with html. If property Url is set, it will be used, not HtmlBase64String.

        :return: The html_base64_string of this WkHtmlToPdfRequestDto.
        :rtype: str
        """
        return self._html_base64_string

    @html_base64_string.setter
    def html_base64_string(self, html_base64_string):
        """Sets the html_base64_string of this WkHtmlToPdfRequestDto.

        Base64 encoded string with html. If property Url is set, it will be used, not HtmlBase64String.

        :param html_base64_string: The html_base64_string of this WkHtmlToPdfRequestDto.
        :type html_base64_string: str
        """

        self._html_base64_string = html_base64_string

    @property
    def resources(self):
        """Gets the resources of this WkHtmlToPdfRequestDto.

        This is a set of key-value pairs of digital resources like images that is referenced in the HtmlBase64String document. It uses the filename including relative path as key and the data is provided as a Base64 encoded string.

        :return: The resources of this WkHtmlToPdfRequestDto.
        :rtype: Dict[str, str]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        """Sets the resources of this WkHtmlToPdfRequestDto.

        This is a set of key-value pairs of digital resources like images that is referenced in the HtmlBase64String document. It uses the filename including relative path as key and the data is provided as a Base64 encoded string.

        :param resources: The resources of this WkHtmlToPdfRequestDto.
        :type resources: Dict[str, str]
        """

        self._resources = resources

    @property
    def url(self):
        """Gets the url of this WkHtmlToPdfRequestDto.

        The url to generate pdf from. Url has precedence over HtmlBase64String value if both are set.

        :return: The url of this WkHtmlToPdfRequestDto.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WkHtmlToPdfRequestDto.

        The url to generate pdf from. Url has precedence over HtmlBase64String value if both are set.

        :param url: The url of this WkHtmlToPdfRequestDto.
        :type url: str
        """

        self._url = url

    @property
    def wk_html_to_pdf_arguments(self):
        """Gets the wk_html_to_pdf_arguments of this WkHtmlToPdfRequestDto.

        Command line arguments passed to wkhtmltopdf.

        :return: The wk_html_to_pdf_arguments of this WkHtmlToPdfRequestDto.
        :rtype: Dict[str, str]
        """
        return self._wk_html_to_pdf_arguments

    @wk_html_to_pdf_arguments.setter
    def wk_html_to_pdf_arguments(self, wk_html_to_pdf_arguments):
        """Sets the wk_html_to_pdf_arguments of this WkHtmlToPdfRequestDto.

        Command line arguments passed to wkhtmltopdf.

        :param wk_html_to_pdf_arguments: The wk_html_to_pdf_arguments of this WkHtmlToPdfRequestDto.
        :type wk_html_to_pdf_arguments: Dict[str, str]
        """

        self._wk_html_to_pdf_arguments = wk_html_to_pdf_arguments
