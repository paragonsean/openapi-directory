# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.model_field import ModelField
from openapi_server import util


class Serprequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, fields: List[ModelField]=None, format: str=None, name: str=None, page_num: int=1, proxy: str=None, type: str=None, url: str=None):
        """Serprequest - a model defined in OpenAPI

        :param fields: The fields of this Serprequest.
        :param format: The format of this Serprequest.
        :param name: The name of this Serprequest.
        :param page_num: The page_num of this Serprequest.
        :param proxy: The proxy of this Serprequest.
        :param type: The type of this Serprequest.
        :param url: The url of this Serprequest.
        """
        self.openapi_types = {
            'fields': List[ModelField],
            'format': str,
            'name': str,
            'page_num': int,
            'proxy': str,
            'type': str,
            'url': str
        }

        self.attribute_map = {
            'fields': 'fields',
            'format': 'format',
            'name': 'name',
            'page_num': 'pageNum',
            'proxy': 'proxy',
            'type': 'type',
            'url': 'url'
        }

        self._fields = fields
        self._format = format
        self._name = name
        self._page_num = page_num
        self._proxy = proxy
        self._type = type
        self._url = url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Serprequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The serprequest of this Serprequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def fields(self):
        """Gets the fields of this Serprequest.

        Specify CSS selectors (patterns) used to gather data from Search Engine Result Pages.  Ready-to-use payloads for collecting search results from the most popular Search Engines are available. These payloads are customizable, though. 

        :return: The fields of this Serprequest.
        :rtype: List[ModelField]
        """
        return self._fields

    @fields.setter
    def fields(self, fields):
        """Sets the fields of this Serprequest.

        Specify CSS selectors (patterns) used to gather data from Search Engine Result Pages.  Ready-to-use payloads for collecting search results from the most popular Search Engines are available. These payloads are customizable, though. 

        :param fields: The fields of this Serprequest.
        :type fields: List[ModelField]
        """

        self._fields = fields

    @property
    def format(self):
        """Gets the format of this Serprequest.

        Extracted data is returned either in CSV, MS Excel, JSON, JSON(Lines) or XML format.

        :return: The format of this Serprequest.
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Serprequest.

        Extracted data is returned either in CSV, MS Excel, JSON, JSON(Lines) or XML format.

        :param format: The format of this Serprequest.
        :type format: str
        """
        allowed_values = ["csv", "json", "jsonl", "excel", "xml"]  # noqa: E501
        if format not in allowed_values:
            raise ValueError(
                "Invalid value for `format` ({0}), must be one of {1}"
                .format(format, allowed_values)
            )

        self._format = format

    @property
    def name(self):
        """Gets the name of this Serprequest.

        Collection name.

        :return: The name of this Serprequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Serprequest.

        Collection name.

        :param name: The name of this Serprequest.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def page_num(self):
        """Gets the page_num of this Serprequest.

        Specify number of pages to crawl.

        :return: The page_num of this Serprequest.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        """Sets the page_num of this Serprequest.

        Specify number of pages to crawl.

        :param page_num: The page_num of this Serprequest.
        :type page_num: int
        """

        self._page_num = page_num

    @property
    def proxy(self):
        """Gets the proxy of this Serprequest.

        Always specify proxy for sending SERP requests. Add choosen [country ISO code](https://en.wikipedia.org/wiki/ISO_3166-2) to `country-` value to send requests through a proxy in the specified country. Use `country-any` to use random geo-targets.

        :return: The proxy of this Serprequest.
        :rtype: str
        """
        return self._proxy

    @proxy.setter
    def proxy(self, proxy):
        """Sets the proxy of this Serprequest.

        Always specify proxy for sending SERP requests. Add choosen [country ISO code](https://en.wikipedia.org/wiki/ISO_3166-2) to `country-` value to send requests through a proxy in the specified country. Use `country-any` to use random geo-targets.

        :param proxy: The proxy of this Serprequest.
        :type proxy: str
        """
        if proxy is None:
            raise ValueError("Invalid value for `proxy`, must not be `None`")

        self._proxy = proxy

    @property
    def type(self):
        """Gets the type of this Serprequest.

        For SERP requests you should _always_ use `chrome` type to fetch content with a Headless chrome browser

        :return: The type of this Serprequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Serprequest.

        For SERP requests you should _always_ use `chrome` type to fetch content with a Headless chrome browser

        :param type: The type of this Serprequest.
        :type type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

    @property
    def url(self):
        """Gets the url of this Serprequest.

        url holds the link to a Search Engine to use, and other optional parameters like languages or country.

        :return: The url of this Serprequest.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this Serprequest.

        url holds the link to a Search Engine to use, and other optional parameters like languages or country.

        :param url: The url of this Serprequest.
        :type url: str
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")

        self._url = url
