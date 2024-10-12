# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.entry_status import EntryStatus
from openapi_server.models.entry_thumb_for_api_contract import EntryThumbForApiContract
from openapi_server.models.event_category import EventCategory
from openapi_server.models.localized_string_contract import LocalizedStringContract
from openapi_server.models.release_event_for_api_contract import ReleaseEventForApiContract
from openapi_server.models.web_link_for_api_contract import WebLinkForApiContract
from openapi_server import util


class ReleaseEventSeriesForApiContract(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, additional_names: str=None, category: EventCategory=None, description: str=None, events: List[ReleaseEventForApiContract]=None, id: int=None, main_picture: EntryThumbForApiContract=None, name: str=None, names: List[LocalizedStringContract]=None, status: EntryStatus=None, url_slug: str=None, version: int=None, web_links: List[WebLinkForApiContract]=None):
        """ReleaseEventSeriesForApiContract - a model defined in OpenAPI

        :param additional_names: The additional_names of this ReleaseEventSeriesForApiContract.
        :param category: The category of this ReleaseEventSeriesForApiContract.
        :param description: The description of this ReleaseEventSeriesForApiContract.
        :param events: The events of this ReleaseEventSeriesForApiContract.
        :param id: The id of this ReleaseEventSeriesForApiContract.
        :param main_picture: The main_picture of this ReleaseEventSeriesForApiContract.
        :param name: The name of this ReleaseEventSeriesForApiContract.
        :param names: The names of this ReleaseEventSeriesForApiContract.
        :param status: The status of this ReleaseEventSeriesForApiContract.
        :param url_slug: The url_slug of this ReleaseEventSeriesForApiContract.
        :param version: The version of this ReleaseEventSeriesForApiContract.
        :param web_links: The web_links of this ReleaseEventSeriesForApiContract.
        """
        self.openapi_types = {
            'additional_names': str,
            'category': EventCategory,
            'description': str,
            'events': List[ReleaseEventForApiContract],
            'id': int,
            'main_picture': EntryThumbForApiContract,
            'name': str,
            'names': List[LocalizedStringContract],
            'status': EntryStatus,
            'url_slug': str,
            'version': int,
            'web_links': List[WebLinkForApiContract]
        }

        self.attribute_map = {
            'additional_names': 'additionalNames',
            'category': 'category',
            'description': 'description',
            'events': 'events',
            'id': 'id',
            'main_picture': 'mainPicture',
            'name': 'name',
            'names': 'names',
            'status': 'status',
            'url_slug': 'urlSlug',
            'version': 'version',
            'web_links': 'webLinks'
        }

        self._additional_names = additional_names
        self._category = category
        self._description = description
        self._events = events
        self._id = id
        self._main_picture = main_picture
        self._name = name
        self._names = names
        self._status = status
        self._url_slug = url_slug
        self._version = version
        self._web_links = web_links

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ReleaseEventSeriesForApiContract':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ReleaseEventSeriesForApiContract of this ReleaseEventSeriesForApiContract.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def additional_names(self):
        """Gets the additional_names of this ReleaseEventSeriesForApiContract.


        :return: The additional_names of this ReleaseEventSeriesForApiContract.
        :rtype: str
        """
        return self._additional_names

    @additional_names.setter
    def additional_names(self, additional_names):
        """Sets the additional_names of this ReleaseEventSeriesForApiContract.


        :param additional_names: The additional_names of this ReleaseEventSeriesForApiContract.
        :type additional_names: str
        """

        self._additional_names = additional_names

    @property
    def category(self):
        """Gets the category of this ReleaseEventSeriesForApiContract.


        :return: The category of this ReleaseEventSeriesForApiContract.
        :rtype: EventCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ReleaseEventSeriesForApiContract.


        :param category: The category of this ReleaseEventSeriesForApiContract.
        :type category: EventCategory
        """

        self._category = category

    @property
    def description(self):
        """Gets the description of this ReleaseEventSeriesForApiContract.


        :return: The description of this ReleaseEventSeriesForApiContract.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReleaseEventSeriesForApiContract.


        :param description: The description of this ReleaseEventSeriesForApiContract.
        :type description: str
        """

        self._description = description

    @property
    def events(self):
        """Gets the events of this ReleaseEventSeriesForApiContract.


        :return: The events of this ReleaseEventSeriesForApiContract.
        :rtype: List[ReleaseEventForApiContract]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this ReleaseEventSeriesForApiContract.


        :param events: The events of this ReleaseEventSeriesForApiContract.
        :type events: List[ReleaseEventForApiContract]
        """

        self._events = events

    @property
    def id(self):
        """Gets the id of this ReleaseEventSeriesForApiContract.


        :return: The id of this ReleaseEventSeriesForApiContract.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReleaseEventSeriesForApiContract.


        :param id: The id of this ReleaseEventSeriesForApiContract.
        :type id: int
        """

        self._id = id

    @property
    def main_picture(self):
        """Gets the main_picture of this ReleaseEventSeriesForApiContract.


        :return: The main_picture of this ReleaseEventSeriesForApiContract.
        :rtype: EntryThumbForApiContract
        """
        return self._main_picture

    @main_picture.setter
    def main_picture(self, main_picture):
        """Sets the main_picture of this ReleaseEventSeriesForApiContract.


        :param main_picture: The main_picture of this ReleaseEventSeriesForApiContract.
        :type main_picture: EntryThumbForApiContract
        """

        self._main_picture = main_picture

    @property
    def name(self):
        """Gets the name of this ReleaseEventSeriesForApiContract.


        :return: The name of this ReleaseEventSeriesForApiContract.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReleaseEventSeriesForApiContract.


        :param name: The name of this ReleaseEventSeriesForApiContract.
        :type name: str
        """

        self._name = name

    @property
    def names(self):
        """Gets the names of this ReleaseEventSeriesForApiContract.


        :return: The names of this ReleaseEventSeriesForApiContract.
        :rtype: List[LocalizedStringContract]
        """
        return self._names

    @names.setter
    def names(self, names):
        """Sets the names of this ReleaseEventSeriesForApiContract.


        :param names: The names of this ReleaseEventSeriesForApiContract.
        :type names: List[LocalizedStringContract]
        """

        self._names = names

    @property
    def status(self):
        """Gets the status of this ReleaseEventSeriesForApiContract.


        :return: The status of this ReleaseEventSeriesForApiContract.
        :rtype: EntryStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ReleaseEventSeriesForApiContract.


        :param status: The status of this ReleaseEventSeriesForApiContract.
        :type status: EntryStatus
        """

        self._status = status

    @property
    def url_slug(self):
        """Gets the url_slug of this ReleaseEventSeriesForApiContract.


        :return: The url_slug of this ReleaseEventSeriesForApiContract.
        :rtype: str
        """
        return self._url_slug

    @url_slug.setter
    def url_slug(self, url_slug):
        """Sets the url_slug of this ReleaseEventSeriesForApiContract.


        :param url_slug: The url_slug of this ReleaseEventSeriesForApiContract.
        :type url_slug: str
        """

        self._url_slug = url_slug

    @property
    def version(self):
        """Gets the version of this ReleaseEventSeriesForApiContract.


        :return: The version of this ReleaseEventSeriesForApiContract.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ReleaseEventSeriesForApiContract.


        :param version: The version of this ReleaseEventSeriesForApiContract.
        :type version: int
        """

        self._version = version

    @property
    def web_links(self):
        """Gets the web_links of this ReleaseEventSeriesForApiContract.


        :return: The web_links of this ReleaseEventSeriesForApiContract.
        :rtype: List[WebLinkForApiContract]
        """
        return self._web_links

    @web_links.setter
    def web_links(self, web_links):
        """Sets the web_links of this ReleaseEventSeriesForApiContract.


        :param web_links: The web_links of this ReleaseEventSeriesForApiContract.
        :type web_links: List[WebLinkForApiContract]
        """

        self._web_links = web_links
