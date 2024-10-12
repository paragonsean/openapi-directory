# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.image_object import ImageObject
from openapi_server import util


class Query(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, display_text: str=None, search_link: str=None, text: str=None, thumbnail: ImageObject=None, web_search_url: str=None):
        """Query - a model defined in OpenAPI

        :param display_text: The display_text of this Query.
        :param search_link: The search_link of this Query.
        :param text: The text of this Query.
        :param thumbnail: The thumbnail of this Query.
        :param web_search_url: The web_search_url of this Query.
        """
        self.openapi_types = {
            'display_text': str,
            'search_link': str,
            'text': str,
            'thumbnail': ImageObject,
            'web_search_url': str
        }

        self.attribute_map = {
            'display_text': 'displayText',
            'search_link': 'searchLink',
            'text': 'text',
            'thumbnail': 'thumbnail',
            'web_search_url': 'webSearchUrl'
        }

        self._display_text = display_text
        self._search_link = search_link
        self._text = text
        self._thumbnail = thumbnail
        self._web_search_url = web_search_url

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Query':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Query of this Query.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def display_text(self):
        """Gets the display_text of this Query.

        The display version of the query term.

        :return: The display_text of this Query.
        :rtype: str
        """
        return self._display_text

    @display_text.setter
    def display_text(self, display_text):
        """Sets the display_text of this Query.

        The display version of the query term.

        :param display_text: The display_text of this Query.
        :type display_text: str
        """

        self._display_text = display_text

    @property
    def search_link(self):
        """Gets the search_link of this Query.

        The URL that you use to get the results of the related search. Before using the URL, you must append query parameters as appropriate and include the Ocp-Apim-Subscription-Key header. Use this URL if you're displaying the results in your own user interface. Otherwise, use the webSearchUrl URL.

        :return: The search_link of this Query.
        :rtype: str
        """
        return self._search_link

    @search_link.setter
    def search_link(self, search_link):
        """Sets the search_link of this Query.

        The URL that you use to get the results of the related search. Before using the URL, you must append query parameters as appropriate and include the Ocp-Apim-Subscription-Key header. Use this URL if you're displaying the results in your own user interface. Otherwise, use the webSearchUrl URL.

        :param search_link: The search_link of this Query.
        :type search_link: str
        """

        self._search_link = search_link

    @property
    def text(self):
        """Gets the text of this Query.

        The query string. Use this string as the query term in a new search request.

        :return: The text of this Query.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this Query.

        The query string. Use this string as the query term in a new search request.

        :param text: The text of this Query.
        :type text: str
        """
        if text is None:
            raise ValueError("Invalid value for `text`, must not be `None`")

        self._text = text

    @property
    def thumbnail(self):
        """Gets the thumbnail of this Query.


        :return: The thumbnail of this Query.
        :rtype: ImageObject
        """
        return self._thumbnail

    @thumbnail.setter
    def thumbnail(self, thumbnail):
        """Sets the thumbnail of this Query.


        :param thumbnail: The thumbnail of this Query.
        :type thumbnail: ImageObject
        """

        self._thumbnail = thumbnail

    @property
    def web_search_url(self):
        """Gets the web_search_url of this Query.

        The URL that takes the user to the Bing search results page for the query.

        :return: The web_search_url of this Query.
        :rtype: str
        """
        return self._web_search_url

    @web_search_url.setter
    def web_search_url(self, web_search_url):
        """Sets the web_search_url of this Query.

        The URL that takes the user to the Bing search results page for the query.

        :param web_search_url: The web_search_url of this Query.
        :type web_search_url: str
        """

        self._web_search_url = web_search_url
