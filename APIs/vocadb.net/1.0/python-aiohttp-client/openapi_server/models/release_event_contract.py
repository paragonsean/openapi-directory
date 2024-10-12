# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.entry_status import EntryStatus
from openapi_server.models.event_category import EventCategory
from openapi_server.models.release_event_series_contract import ReleaseEventSeriesContract
from openapi_server.models.song_list_base_contract import SongListBaseContract
from openapi_server.models.venue_contract import VenueContract
from openapi_server import util


class ReleaseEventContract(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, additional_names: str=None, category: EventCategory=None, custom_name: bool=None, _date: datetime=None, deleted: bool=None, description: str=None, end_date: datetime=None, has_venue_or_venue_name: bool=None, id: int=None, inherited_category: EventCategory=None, name: str=None, picture_mime: str=None, series: ReleaseEventSeriesContract=None, song_list: SongListBaseContract=None, status: EntryStatus=None, url_slug: str=None, venue: VenueContract=None, venue_name: str=None, version: int=None):
        """ReleaseEventContract - a model defined in OpenAPI

        :param additional_names: The additional_names of this ReleaseEventContract.
        :param category: The category of this ReleaseEventContract.
        :param custom_name: The custom_name of this ReleaseEventContract.
        :param _date: The _date of this ReleaseEventContract.
        :param deleted: The deleted of this ReleaseEventContract.
        :param description: The description of this ReleaseEventContract.
        :param end_date: The end_date of this ReleaseEventContract.
        :param has_venue_or_venue_name: The has_venue_or_venue_name of this ReleaseEventContract.
        :param id: The id of this ReleaseEventContract.
        :param inherited_category: The inherited_category of this ReleaseEventContract.
        :param name: The name of this ReleaseEventContract.
        :param picture_mime: The picture_mime of this ReleaseEventContract.
        :param series: The series of this ReleaseEventContract.
        :param song_list: The song_list of this ReleaseEventContract.
        :param status: The status of this ReleaseEventContract.
        :param url_slug: The url_slug of this ReleaseEventContract.
        :param venue: The venue of this ReleaseEventContract.
        :param venue_name: The venue_name of this ReleaseEventContract.
        :param version: The version of this ReleaseEventContract.
        """
        self.openapi_types = {
            'additional_names': str,
            'category': EventCategory,
            'custom_name': bool,
            '_date': datetime,
            'deleted': bool,
            'description': str,
            'end_date': datetime,
            'has_venue_or_venue_name': bool,
            'id': int,
            'inherited_category': EventCategory,
            'name': str,
            'picture_mime': str,
            'series': ReleaseEventSeriesContract,
            'song_list': SongListBaseContract,
            'status': EntryStatus,
            'url_slug': str,
            'venue': VenueContract,
            'venue_name': str,
            'version': int
        }

        self.attribute_map = {
            'additional_names': 'additionalNames',
            'category': 'category',
            'custom_name': 'customName',
            '_date': 'date',
            'deleted': 'deleted',
            'description': 'description',
            'end_date': 'endDate',
            'has_venue_or_venue_name': 'hasVenueOrVenueName',
            'id': 'id',
            'inherited_category': 'inheritedCategory',
            'name': 'name',
            'picture_mime': 'pictureMime',
            'series': 'series',
            'song_list': 'songList',
            'status': 'status',
            'url_slug': 'urlSlug',
            'venue': 'venue',
            'venue_name': 'venueName',
            'version': 'version'
        }

        self._additional_names = additional_names
        self._category = category
        self._custom_name = custom_name
        self.__date = _date
        self._deleted = deleted
        self._description = description
        self._end_date = end_date
        self._has_venue_or_venue_name = has_venue_or_venue_name
        self._id = id
        self._inherited_category = inherited_category
        self._name = name
        self._picture_mime = picture_mime
        self._series = series
        self._song_list = song_list
        self._status = status
        self._url_slug = url_slug
        self._venue = venue
        self._venue_name = venue_name
        self._version = version

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ReleaseEventContract':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ReleaseEventContract of this ReleaseEventContract.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def additional_names(self):
        """Gets the additional_names of this ReleaseEventContract.


        :return: The additional_names of this ReleaseEventContract.
        :rtype: str
        """
        return self._additional_names

    @additional_names.setter
    def additional_names(self, additional_names):
        """Sets the additional_names of this ReleaseEventContract.


        :param additional_names: The additional_names of this ReleaseEventContract.
        :type additional_names: str
        """

        self._additional_names = additional_names

    @property
    def category(self):
        """Gets the category of this ReleaseEventContract.


        :return: The category of this ReleaseEventContract.
        :rtype: EventCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this ReleaseEventContract.


        :param category: The category of this ReleaseEventContract.
        :type category: EventCategory
        """

        self._category = category

    @property
    def custom_name(self):
        """Gets the custom_name of this ReleaseEventContract.


        :return: The custom_name of this ReleaseEventContract.
        :rtype: bool
        """
        return self._custom_name

    @custom_name.setter
    def custom_name(self, custom_name):
        """Sets the custom_name of this ReleaseEventContract.


        :param custom_name: The custom_name of this ReleaseEventContract.
        :type custom_name: bool
        """

        self._custom_name = custom_name

    @property
    def _date(self):
        """Gets the _date of this ReleaseEventContract.


        :return: The _date of this ReleaseEventContract.
        :rtype: datetime
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ReleaseEventContract.


        :param _date: The _date of this ReleaseEventContract.
        :type _date: datetime
        """

        self.__date = _date

    @property
    def deleted(self):
        """Gets the deleted of this ReleaseEventContract.


        :return: The deleted of this ReleaseEventContract.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this ReleaseEventContract.


        :param deleted: The deleted of this ReleaseEventContract.
        :type deleted: bool
        """

        self._deleted = deleted

    @property
    def description(self):
        """Gets the description of this ReleaseEventContract.


        :return: The description of this ReleaseEventContract.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReleaseEventContract.


        :param description: The description of this ReleaseEventContract.
        :type description: str
        """

        self._description = description

    @property
    def end_date(self):
        """Gets the end_date of this ReleaseEventContract.


        :return: The end_date of this ReleaseEventContract.
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ReleaseEventContract.


        :param end_date: The end_date of this ReleaseEventContract.
        :type end_date: datetime
        """

        self._end_date = end_date

    @property
    def has_venue_or_venue_name(self):
        """Gets the has_venue_or_venue_name of this ReleaseEventContract.


        :return: The has_venue_or_venue_name of this ReleaseEventContract.
        :rtype: bool
        """
        return self._has_venue_or_venue_name

    @has_venue_or_venue_name.setter
    def has_venue_or_venue_name(self, has_venue_or_venue_name):
        """Sets the has_venue_or_venue_name of this ReleaseEventContract.


        :param has_venue_or_venue_name: The has_venue_or_venue_name of this ReleaseEventContract.
        :type has_venue_or_venue_name: bool
        """

        self._has_venue_or_venue_name = has_venue_or_venue_name

    @property
    def id(self):
        """Gets the id of this ReleaseEventContract.


        :return: The id of this ReleaseEventContract.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ReleaseEventContract.


        :param id: The id of this ReleaseEventContract.
        :type id: int
        """

        self._id = id

    @property
    def inherited_category(self):
        """Gets the inherited_category of this ReleaseEventContract.


        :return: The inherited_category of this ReleaseEventContract.
        :rtype: EventCategory
        """
        return self._inherited_category

    @inherited_category.setter
    def inherited_category(self, inherited_category):
        """Sets the inherited_category of this ReleaseEventContract.


        :param inherited_category: The inherited_category of this ReleaseEventContract.
        :type inherited_category: EventCategory
        """

        self._inherited_category = inherited_category

    @property
    def name(self):
        """Gets the name of this ReleaseEventContract.


        :return: The name of this ReleaseEventContract.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReleaseEventContract.


        :param name: The name of this ReleaseEventContract.
        :type name: str
        """

        self._name = name

    @property
    def picture_mime(self):
        """Gets the picture_mime of this ReleaseEventContract.


        :return: The picture_mime of this ReleaseEventContract.
        :rtype: str
        """
        return self._picture_mime

    @picture_mime.setter
    def picture_mime(self, picture_mime):
        """Sets the picture_mime of this ReleaseEventContract.


        :param picture_mime: The picture_mime of this ReleaseEventContract.
        :type picture_mime: str
        """

        self._picture_mime = picture_mime

    @property
    def series(self):
        """Gets the series of this ReleaseEventContract.


        :return: The series of this ReleaseEventContract.
        :rtype: ReleaseEventSeriesContract
        """
        return self._series

    @series.setter
    def series(self, series):
        """Sets the series of this ReleaseEventContract.


        :param series: The series of this ReleaseEventContract.
        :type series: ReleaseEventSeriesContract
        """

        self._series = series

    @property
    def song_list(self):
        """Gets the song_list of this ReleaseEventContract.


        :return: The song_list of this ReleaseEventContract.
        :rtype: SongListBaseContract
        """
        return self._song_list

    @song_list.setter
    def song_list(self, song_list):
        """Sets the song_list of this ReleaseEventContract.


        :param song_list: The song_list of this ReleaseEventContract.
        :type song_list: SongListBaseContract
        """

        self._song_list = song_list

    @property
    def status(self):
        """Gets the status of this ReleaseEventContract.


        :return: The status of this ReleaseEventContract.
        :rtype: EntryStatus
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ReleaseEventContract.


        :param status: The status of this ReleaseEventContract.
        :type status: EntryStatus
        """

        self._status = status

    @property
    def url_slug(self):
        """Gets the url_slug of this ReleaseEventContract.


        :return: The url_slug of this ReleaseEventContract.
        :rtype: str
        """
        return self._url_slug

    @url_slug.setter
    def url_slug(self, url_slug):
        """Sets the url_slug of this ReleaseEventContract.


        :param url_slug: The url_slug of this ReleaseEventContract.
        :type url_slug: str
        """

        self._url_slug = url_slug

    @property
    def venue(self):
        """Gets the venue of this ReleaseEventContract.


        :return: The venue of this ReleaseEventContract.
        :rtype: VenueContract
        """
        return self._venue

    @venue.setter
    def venue(self, venue):
        """Sets the venue of this ReleaseEventContract.


        :param venue: The venue of this ReleaseEventContract.
        :type venue: VenueContract
        """

        self._venue = venue

    @property
    def venue_name(self):
        """Gets the venue_name of this ReleaseEventContract.


        :return: The venue_name of this ReleaseEventContract.
        :rtype: str
        """
        return self._venue_name

    @venue_name.setter
    def venue_name(self, venue_name):
        """Sets the venue_name of this ReleaseEventContract.


        :param venue_name: The venue_name of this ReleaseEventContract.
        :type venue_name: str
        """

        self._venue_name = venue_name

    @property
    def version(self):
        """Gets the version of this ReleaseEventContract.


        :return: The version of this ReleaseEventContract.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ReleaseEventContract.


        :param version: The version of this ReleaseEventContract.
        :type version: int
        """

        self._version = version
