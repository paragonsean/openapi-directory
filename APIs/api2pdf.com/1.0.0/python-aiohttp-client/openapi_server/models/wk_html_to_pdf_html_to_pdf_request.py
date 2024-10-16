# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.wk_html_to_pdf_advanced_options import WkHtmlToPdfAdvancedOptions
from openapi_server import util


class WkHtmlToPdfHtmlToPdfRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, file_name: str=None, html: str=None, inline_pdf: bool=None, options: WkHtmlToPdfAdvancedOptions=None):
        """WkHtmlToPdfHtmlToPdfRequest - a model defined in OpenAPI

        :param file_name: The file_name of this WkHtmlToPdfHtmlToPdfRequest.
        :param html: The html of this WkHtmlToPdfHtmlToPdfRequest.
        :param inline_pdf: The inline_pdf of this WkHtmlToPdfHtmlToPdfRequest.
        :param options: The options of this WkHtmlToPdfHtmlToPdfRequest.
        """
        self.openapi_types = {
            'file_name': str,
            'html': str,
            'inline_pdf': bool,
            'options': WkHtmlToPdfAdvancedOptions
        }

        self.attribute_map = {
            'file_name': 'fileName',
            'html': 'html',
            'inline_pdf': 'inlinePdf',
            'options': 'options'
        }

        self._file_name = file_name
        self._html = html
        self._inline_pdf = inline_pdf
        self._options = options

    @classmethod
    def from_dict(cls, dikt: dict) -> 'WkHtmlToPdfHtmlToPdfRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The WkHtmlToPdfHtmlToPdfRequest of this WkHtmlToPdfHtmlToPdfRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def file_name(self):
        """Gets the file_name of this WkHtmlToPdfHtmlToPdfRequest.


        :return: The file_name of this WkHtmlToPdfHtmlToPdfRequest.
        :rtype: str
        """
        return self._file_name

    @file_name.setter
    def file_name(self, file_name):
        """Sets the file_name of this WkHtmlToPdfHtmlToPdfRequest.


        :param file_name: The file_name of this WkHtmlToPdfHtmlToPdfRequest.
        :type file_name: str
        """

        self._file_name = file_name

    @property
    def html(self):
        """Gets the html of this WkHtmlToPdfHtmlToPdfRequest.


        :return: The html of this WkHtmlToPdfHtmlToPdfRequest.
        :rtype: str
        """
        return self._html

    @html.setter
    def html(self, html):
        """Sets the html of this WkHtmlToPdfHtmlToPdfRequest.


        :param html: The html of this WkHtmlToPdfHtmlToPdfRequest.
        :type html: str
        """
        if html is None:
            raise ValueError("Invalid value for `html`, must not be `None`")

        self._html = html

    @property
    def inline_pdf(self):
        """Gets the inline_pdf of this WkHtmlToPdfHtmlToPdfRequest.


        :return: The inline_pdf of this WkHtmlToPdfHtmlToPdfRequest.
        :rtype: bool
        """
        return self._inline_pdf

    @inline_pdf.setter
    def inline_pdf(self, inline_pdf):
        """Sets the inline_pdf of this WkHtmlToPdfHtmlToPdfRequest.


        :param inline_pdf: The inline_pdf of this WkHtmlToPdfHtmlToPdfRequest.
        :type inline_pdf: bool
        """

        self._inline_pdf = inline_pdf

    @property
    def options(self):
        """Gets the options of this WkHtmlToPdfHtmlToPdfRequest.


        :return: The options of this WkHtmlToPdfHtmlToPdfRequest.
        :rtype: WkHtmlToPdfAdvancedOptions
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this WkHtmlToPdfHtmlToPdfRequest.


        :param options: The options of this WkHtmlToPdfHtmlToPdfRequest.
        :type options: WkHtmlToPdfAdvancedOptions
        """

        self._options = options
