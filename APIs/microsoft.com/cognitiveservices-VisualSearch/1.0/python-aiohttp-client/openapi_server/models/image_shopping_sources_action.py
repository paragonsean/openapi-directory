# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.aggregate_offer import AggregateOffer
from openapi_server.models.image_action import ImageAction
from openapi_server.models.image_object import ImageObject
from openapi_server.models.thing import Thing
from openapi_server import util


class ImageShoppingSourcesAction(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, data: AggregateOffer=None, type: str=None, action_type: str=None, display_name: str=None, is_top_action: bool=None, result: List[Thing]=None, service_url: str=None, date_published: str=None, provider: List[Thing]=None, text: str=None, thumbnail_url: str=None, alternate_name: str=None, bing_id: str=None, description: str=None, image: ImageObject=None, name: str=None, url: str=None, read_link: str=None, web_search_url: str=None, id: str=None):
        """ImageShoppingSourcesAction - a model defined in OpenAPI

        :param data: The data of this ImageShoppingSourcesAction.
        :param type: The type of this ImageShoppingSourcesAction.
        :param action_type: The action_type of this ImageShoppingSourcesAction.
        :param display_name: The display_name of this ImageShoppingSourcesAction.
        :param is_top_action: The is_top_action of this ImageShoppingSourcesAction.
        :param result: The result of this ImageShoppingSourcesAction.
        :param service_url: The service_url of this ImageShoppingSourcesAction.
        :param date_published: The date_published of this ImageShoppingSourcesAction.
        :param provider: The provider of this ImageShoppingSourcesAction.
        :param text: The text of this ImageShoppingSourcesAction.
        :param thumbnail_url: The thumbnail_url of this ImageShoppingSourcesAction.
        :param alternate_name: The alternate_name of this ImageShoppingSourcesAction.
        :param bing_id: The bing_id of this ImageShoppingSourcesAction.
        :param description: The description of this ImageShoppingSourcesAction.
        :param image: The image of this ImageShoppingSourcesAction.
        :param name: The name of this ImageShoppingSourcesAction.
        :param url: The url of this ImageShoppingSourcesAction.
        :param read_link: The read_link of this ImageShoppingSourcesAction.
        :param web_search_url: The web_search_url of this ImageShoppingSourcesAction.
        :param id: The id of this ImageShoppingSourcesAction.
        """
        self.openapi_types = {
            'data': AggregateOffer,
            'type': str,
            'action_type': str,
            'display_name': str,
            'is_top_action': bool,
            'result': List[Thing],
            'service_url': str,
            'date_published': str,
            'provider': List[Thing],
            'text': str,
            'thumbnail_url': str,
            'alternate_name': str,
            'bing_id': str,
            'description': str,
            'image': ImageObject,
            'name': str,
            'url': str,
            'read_link': str,
            'web_search_url': str,
            'id': str
        }

        self.attribute_map = {
            'data': 'data',
            'type': '_type',
            'action_type': 'actionType',
            'display_name': 'displayName',
            'is_top_action': 'isTopAction',
            'result': 'result',
            'service_url': 'serviceUrl',
            'date_published': 'datePublished',
            'provider': 'provider',
            'text': 'text',
            'thumbnail_url': 'thumbnailUrl',
            'alternate_name': 'alternateName',
            'bing_id': 'bingId',
            'description': 'description',
            'image': 'image',
            'name': 'name',
            'url': 'url',
            'read_link': 'readLink',
            'web_search_url': 'webSearchUrl',
            'id': 'id'
        }

        self._data = data
        self._type = type
        self._action_type = action_type
        self._display_name = display_name
        self._is_top_action = is_top_action
        self._result = result
        self._service_url = service_url
        self._date_published = date_published
        self._provider = provider
        self._text = text
        self._thumbnail_url = thumbnail_url
        self._alternate_name = alternate_name
        self._bing_id = bing_id
        self._description = description
        self._image = image
        self._name = name
        self._url = url
        self._read_link = read_link
        self._web_search_url = web_search_url
        self._id = id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ImageShoppingSourcesAction':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ImageShoppingSourcesAction of this ImageShoppingSourcesAction.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def data(self):
        """Gets the data of this ImageShoppingSourcesAction.


        :return: The data of this ImageShoppingSourcesAction.
        :rtype: AggregateOffer
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this ImageShoppingSourcesAction.


        :param data: The data of this ImageShoppingSourcesAction.
        :type data: AggregateOffer
        """

        self._data = data

    @property
    def type(self):
        """Gets the type of this ImageShoppingSourcesAction.


        :return: The type of this ImageShoppingSourcesAction.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ImageShoppingSourcesAction.


        :param type: The type of this ImageShoppingSourcesAction.
        :type type: str
        """

        self._type = type

    @property
    def action_type(self):
        """Gets the action_type of this ImageShoppingSourcesAction.

        A string representing the type of action.

        :return: The action_type of this ImageShoppingSourcesAction.
        :rtype: str
        """
        return self._action_type

    @action_type.setter
    def action_type(self, action_type):
        """Sets the action_type of this ImageShoppingSourcesAction.

        A string representing the type of action.

        :param action_type: The action_type of this ImageShoppingSourcesAction.
        :type action_type: str
        """

        self._action_type = action_type

    @property
    def display_name(self):
        """Gets the display_name of this ImageShoppingSourcesAction.

        A display name for the action.

        :return: The display_name of this ImageShoppingSourcesAction.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ImageShoppingSourcesAction.

        A display name for the action.

        :param display_name: The display_name of this ImageShoppingSourcesAction.
        :type display_name: str
        """

        self._display_name = display_name

    @property
    def is_top_action(self):
        """Gets the is_top_action of this ImageShoppingSourcesAction.

        A Boolean representing whether this result is the top action.

        :return: The is_top_action of this ImageShoppingSourcesAction.
        :rtype: bool
        """
        return self._is_top_action

    @is_top_action.setter
    def is_top_action(self, is_top_action):
        """Sets the is_top_action of this ImageShoppingSourcesAction.

        A Boolean representing whether this result is the top action.

        :param is_top_action: The is_top_action of this ImageShoppingSourcesAction.
        :type is_top_action: bool
        """

        self._is_top_action = is_top_action

    @property
    def result(self):
        """Gets the result of this ImageShoppingSourcesAction.

        The result produced in the action.

        :return: The result of this ImageShoppingSourcesAction.
        :rtype: List[Thing]
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this ImageShoppingSourcesAction.

        The result produced in the action.

        :param result: The result of this ImageShoppingSourcesAction.
        :type result: List[Thing]
        """

        self._result = result

    @property
    def service_url(self):
        """Gets the service_url of this ImageShoppingSourcesAction.

        Use this URL to get additional data to determine how to take the appropriate action. For example, the serviceUrl might return JSON along with an image URL.

        :return: The service_url of this ImageShoppingSourcesAction.
        :rtype: str
        """
        return self._service_url

    @service_url.setter
    def service_url(self, service_url):
        """Sets the service_url of this ImageShoppingSourcesAction.

        Use this URL to get additional data to determine how to take the appropriate action. For example, the serviceUrl might return JSON along with an image URL.

        :param service_url: The service_url of this ImageShoppingSourcesAction.
        :type service_url: str
        """

        self._service_url = service_url

    @property
    def date_published(self):
        """Gets the date_published of this ImageShoppingSourcesAction.

        The date on which the CreativeWork was published.

        :return: The date_published of this ImageShoppingSourcesAction.
        :rtype: str
        """
        return self._date_published

    @date_published.setter
    def date_published(self, date_published):
        """Sets the date_published of this ImageShoppingSourcesAction.

        The date on which the CreativeWork was published.

        :param date_published: The date_published of this ImageShoppingSourcesAction.
        :type date_published: str
        """

        self._date_published = date_published

    @property
    def provider(self):
        """Gets the provider of this ImageShoppingSourcesAction.

        The source of the creative work.

        :return: The provider of this ImageShoppingSourcesAction.
        :rtype: List[Thing]
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ImageShoppingSourcesAction.

        The source of the creative work.

        :param provider: The provider of this ImageShoppingSourcesAction.
        :type provider: List[Thing]
        """

        self._provider = provider

    @property
    def text(self):
        """Gets the text of this ImageShoppingSourcesAction.

        Text content of this creative work.

        :return: The text of this ImageShoppingSourcesAction.
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ImageShoppingSourcesAction.

        Text content of this creative work.

        :param text: The text of this ImageShoppingSourcesAction.
        :type text: str
        """

        self._text = text

    @property
    def thumbnail_url(self):
        """Gets the thumbnail_url of this ImageShoppingSourcesAction.

        The URL to a thumbnail of the item.

        :return: The thumbnail_url of this ImageShoppingSourcesAction.
        :rtype: str
        """
        return self._thumbnail_url

    @thumbnail_url.setter
    def thumbnail_url(self, thumbnail_url):
        """Sets the thumbnail_url of this ImageShoppingSourcesAction.

        The URL to a thumbnail of the item.

        :param thumbnail_url: The thumbnail_url of this ImageShoppingSourcesAction.
        :type thumbnail_url: str
        """

        self._thumbnail_url = thumbnail_url

    @property
    def alternate_name(self):
        """Gets the alternate_name of this ImageShoppingSourcesAction.

        An alias for the item.

        :return: The alternate_name of this ImageShoppingSourcesAction.
        :rtype: str
        """
        return self._alternate_name

    @alternate_name.setter
    def alternate_name(self, alternate_name):
        """Sets the alternate_name of this ImageShoppingSourcesAction.

        An alias for the item.

        :param alternate_name: The alternate_name of this ImageShoppingSourcesAction.
        :type alternate_name: str
        """

        self._alternate_name = alternate_name

    @property
    def bing_id(self):
        """Gets the bing_id of this ImageShoppingSourcesAction.

        An ID that uniquely identifies this item.

        :return: The bing_id of this ImageShoppingSourcesAction.
        :rtype: str
        """
        return self._bing_id

    @bing_id.setter
    def bing_id(self, bing_id):
        """Sets the bing_id of this ImageShoppingSourcesAction.

        An ID that uniquely identifies this item.

        :param bing_id: The bing_id of this ImageShoppingSourcesAction.
        :type bing_id: str
        """

        self._bing_id = bing_id

    @property
    def description(self):
        """Gets the description of this ImageShoppingSourcesAction.

        A short description of the item.

        :return: The description of this ImageShoppingSourcesAction.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ImageShoppingSourcesAction.

        A short description of the item.

        :param description: The description of this ImageShoppingSourcesAction.
        :type description: str
        """

        self._description = description

    @property
    def image(self):
        """Gets the image of this ImageShoppingSourcesAction.


        :return: The image of this ImageShoppingSourcesAction.
        :rtype: ImageObject
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this ImageShoppingSourcesAction.


        :param image: The image of this ImageShoppingSourcesAction.
        :type image: ImageObject
        """

        self._image = image

    @property
    def name(self):
        """Gets the name of this ImageShoppingSourcesAction.

        The name of the thing represented by this object.

        :return: The name of this ImageShoppingSourcesAction.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ImageShoppingSourcesAction.

        The name of the thing represented by this object.

        :param name: The name of this ImageShoppingSourcesAction.
        :type name: str
        """

        self._name = name

    @property
    def url(self):
        """Gets the url of this ImageShoppingSourcesAction.

        The URL to get more information about the thing represented by this object.

        :return: The url of this ImageShoppingSourcesAction.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this ImageShoppingSourcesAction.

        The URL to get more information about the thing represented by this object.

        :param url: The url of this ImageShoppingSourcesAction.
        :type url: str
        """

        self._url = url

    @property
    def read_link(self):
        """Gets the read_link of this ImageShoppingSourcesAction.

        The URL that returns this resource. To use the URL, append query parameters as appropriate and include the Ocp-Apim-Subscription-Key header.

        :return: The read_link of this ImageShoppingSourcesAction.
        :rtype: str
        """
        return self._read_link

    @read_link.setter
    def read_link(self, read_link):
        """Sets the read_link of this ImageShoppingSourcesAction.

        The URL that returns this resource. To use the URL, append query parameters as appropriate and include the Ocp-Apim-Subscription-Key header.

        :param read_link: The read_link of this ImageShoppingSourcesAction.
        :type read_link: str
        """

        self._read_link = read_link

    @property
    def web_search_url(self):
        """Gets the web_search_url of this ImageShoppingSourcesAction.

        The URL to Bing's search result for this item.

        :return: The web_search_url of this ImageShoppingSourcesAction.
        :rtype: str
        """
        return self._web_search_url

    @web_search_url.setter
    def web_search_url(self, web_search_url):
        """Sets the web_search_url of this ImageShoppingSourcesAction.

        The URL to Bing's search result for this item.

        :param web_search_url: The web_search_url of this ImageShoppingSourcesAction.
        :type web_search_url: str
        """

        self._web_search_url = web_search_url

    @property
    def id(self):
        """Gets the id of this ImageShoppingSourcesAction.

        A String identifier.

        :return: The id of this ImageShoppingSourcesAction.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ImageShoppingSourcesAction.

        A String identifier.

        :param id: The id of this ImageShoppingSourcesAction.
        :type id: str
        """

        self._id = id
