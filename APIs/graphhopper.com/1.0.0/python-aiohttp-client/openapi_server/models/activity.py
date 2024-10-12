# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.response_address import ResponseAddress
from openapi_server import util


class Activity(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, address: ResponseAddress=None, arr_date_time: datetime=None, arr_time: int=None, distance: int=None, driving_time: int=None, end_date_time: datetime=None, end_time: int=None, id: str=None, load_after: List[int]=None, load_before: List[int]=None, location_id: str=None, preparation_time: int=None, type: str=None, waiting_time: int=None):
        """Activity - a model defined in OpenAPI

        :param address: The address of this Activity.
        :param arr_date_time: The arr_date_time of this Activity.
        :param arr_time: The arr_time of this Activity.
        :param distance: The distance of this Activity.
        :param driving_time: The driving_time of this Activity.
        :param end_date_time: The end_date_time of this Activity.
        :param end_time: The end_time of this Activity.
        :param id: The id of this Activity.
        :param load_after: The load_after of this Activity.
        :param load_before: The load_before of this Activity.
        :param location_id: The location_id of this Activity.
        :param preparation_time: The preparation_time of this Activity.
        :param type: The type of this Activity.
        :param waiting_time: The waiting_time of this Activity.
        """
        self.openapi_types = {
            'address': ResponseAddress,
            'arr_date_time': datetime,
            'arr_time': int,
            'distance': int,
            'driving_time': int,
            'end_date_time': datetime,
            'end_time': int,
            'id': str,
            'load_after': List[int],
            'load_before': List[int],
            'location_id': str,
            'preparation_time': int,
            'type': str,
            'waiting_time': int
        }

        self.attribute_map = {
            'address': 'address',
            'arr_date_time': 'arr_date_time',
            'arr_time': 'arr_time',
            'distance': 'distance',
            'driving_time': 'driving_time',
            'end_date_time': 'end_date_time',
            'end_time': 'end_time',
            'id': 'id',
            'load_after': 'load_after',
            'load_before': 'load_before',
            'location_id': 'location_id',
            'preparation_time': 'preparation_time',
            'type': 'type',
            'waiting_time': 'waiting_time'
        }

        self._address = address
        self._arr_date_time = arr_date_time
        self._arr_time = arr_time
        self._distance = distance
        self._driving_time = driving_time
        self._end_date_time = end_date_time
        self._end_time = end_time
        self._id = id
        self._load_after = load_after
        self._load_before = load_before
        self._location_id = location_id
        self._preparation_time = preparation_time
        self._type = type
        self._waiting_time = waiting_time

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Activity':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Activity of this Activity.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def address(self):
        """Gets the address of this Activity.


        :return: The address of this Activity.
        :rtype: ResponseAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Activity.


        :param address: The address of this Activity.
        :type address: ResponseAddress
        """

        self._address = address

    @property
    def arr_date_time(self):
        """Gets the arr_date_time of this Activity.

        Arrival date time with offset like this 1970-01-01T01:00+01:00. If you do not use time-dependent optimization, this is `null`.

        :return: The arr_date_time of this Activity.
        :rtype: datetime
        """
        return self._arr_date_time

    @arr_date_time.setter
    def arr_date_time(self, arr_date_time):
        """Sets the arr_date_time of this Activity.

        Arrival date time with offset like this 1970-01-01T01:00+01:00. If you do not use time-dependent optimization, this is `null`.

        :param arr_date_time: The arr_date_time of this Activity.
        :type arr_date_time: datetime
        """

        self._arr_date_time = arr_date_time

    @property
    def arr_time(self):
        """Gets the arr_time of this Activity.

        Arrival time at this activity in seconds. If type is `start`, this is not available (since it makes no sense to have `arr_time` at start). However, `end_time` is available and actually means \\\"departure time\\\" at start location. It is important to note that `arr_time` does not necessarily mean \\\"start of underlying activity\\\", it solely means arrival time at activity location. If this activity has no time windows and if there are no further preparation times, `arr_time` is equal to activity start time.

        :return: The arr_time of this Activity.
        :rtype: int
        """
        return self._arr_time

    @arr_time.setter
    def arr_time(self, arr_time):
        """Sets the arr_time of this Activity.

        Arrival time at this activity in seconds. If type is `start`, this is not available (since it makes no sense to have `arr_time` at start). However, `end_time` is available and actually means \\\"departure time\\\" at start location. It is important to note that `arr_time` does not necessarily mean \\\"start of underlying activity\\\", it solely means arrival time at activity location. If this activity has no time windows and if there are no further preparation times, `arr_time` is equal to activity start time.

        :param arr_time: The arr_time of this Activity.
        :type arr_time: int
        """

        self._arr_time = arr_time

    @property
    def distance(self):
        """Gets the distance of this Activity.

        cumulated distance from start to this activity in m

        :return: The distance of this Activity.
        :rtype: int
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        """Sets the distance of this Activity.

        cumulated distance from start to this activity in m

        :param distance: The distance of this Activity.
        :type distance: int
        """

        self._distance = distance

    @property
    def driving_time(self):
        """Gets the driving_time of this Activity.

        cumulated driving time from start to this driver activity in seconds

        :return: The driving_time of this Activity.
        :rtype: int
        """
        return self._driving_time

    @driving_time.setter
    def driving_time(self, driving_time):
        """Sets the driving_time of this Activity.

        cumulated driving time from start to this driver activity in seconds

        :param driving_time: The driving_time of this Activity.
        :type driving_time: int
        """

        self._driving_time = driving_time

    @property
    def end_date_time(self):
        """Gets the end_date_time of this Activity.

        End date time with offset like this 1970-01-01T01:00+01:00. If you do not use time-dependent optimization, this is `null`.

        :return: The end_date_time of this Activity.
        :rtype: datetime
        """
        return self._end_date_time

    @end_date_time.setter
    def end_date_time(self, end_date_time):
        """Sets the end_date_time of this Activity.

        End date time with offset like this 1970-01-01T01:00+01:00. If you do not use time-dependent optimization, this is `null`.

        :param end_date_time: The end_date_time of this Activity.
        :type end_date_time: datetime
        """

        self._end_date_time = end_date_time

    @property
    def end_time(self):
        """Gets the end_time of this Activity.

        End time of and thus departure time at this activity. If type is `end`, this is not available (since it makes no sense to have an `end_time` at end) `end_time` at each activity is equal to the departure time at the activity location.

        :return: The end_time of this Activity.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        """Sets the end_time of this Activity.

        End time of and thus departure time at this activity. If type is `end`, this is not available (since it makes no sense to have an `end_time` at end) `end_time` at each activity is equal to the departure time at the activity location.

        :param end_time: The end_time of this Activity.
        :type end_time: int
        """

        self._end_time = end_time

    @property
    def id(self):
        """Gets the id of this Activity.

        Id referring to the underlying service or shipment, i.e. the shipment or service this activity belongs to

        :return: The id of this Activity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Activity.

        Id referring to the underlying service or shipment, i.e. the shipment or service this activity belongs to

        :param id: The id of this Activity.
        :type id: str
        """

        self._id = id

    @property
    def load_after(self):
        """Gets the load_after of this Activity.

        Array with size/capacity dimensions after this activity

        :return: The load_after of this Activity.
        :rtype: List[int]
        """
        return self._load_after

    @load_after.setter
    def load_after(self, load_after):
        """Sets the load_after of this Activity.

        Array with size/capacity dimensions after this activity

        :param load_after: The load_after of this Activity.
        :type load_after: List[int]
        """

        self._load_after = load_after

    @property
    def load_before(self):
        """Gets the load_before of this Activity.

        Array with size/capacity dimensions before this activity

        :return: The load_before of this Activity.
        :rtype: List[int]
        """
        return self._load_before

    @load_before.setter
    def load_before(self, load_before):
        """Sets the load_before of this Activity.

        Array with size/capacity dimensions before this activity

        :param load_before: The load_before of this Activity.
        :type load_before: List[int]
        """

        self._load_before = load_before

    @property
    def location_id(self):
        """Gets the location_id of this Activity.

        Id that refers to address

        :return: The location_id of this Activity.
        :rtype: str
        """
        return self._location_id

    @location_id.setter
    def location_id(self, location_id):
        """Sets the location_id of this Activity.

        Id that refers to address

        :param location_id: The location_id of this Activity.
        :type location_id: str
        """

        self._location_id = location_id

    @property
    def preparation_time(self):
        """Gets the preparation_time of this Activity.

        preparation time at this activity in seconds

        :return: The preparation_time of this Activity.
        :rtype: int
        """
        return self._preparation_time

    @preparation_time.setter
    def preparation_time(self, preparation_time):
        """Sets the preparation_time of this Activity.

        preparation time at this activity in seconds

        :param preparation_time: The preparation_time of this Activity.
        :type preparation_time: int
        """

        self._preparation_time = preparation_time

    @property
    def type(self):
        """Gets the type of this Activity.

        type of activity

        :return: The type of this Activity.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Activity.

        type of activity

        :param type: The type of this Activity.
        :type type: str
        """
        allowed_values = ["start", "end", "service", "pickupShipment", "deliverShipment", "pickup", "delivery", "break"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def waiting_time(self):
        """Gets the waiting_time of this Activity.

        Waiting time at this activity in seconds. A waiting time can occur if the activity has at least one time window. If `arr_time` < `time_window.earliest` a waiting time of `time_window_earliest` - `arr_time` occurs.

        :return: The waiting_time of this Activity.
        :rtype: int
        """
        return self._waiting_time

    @waiting_time.setter
    def waiting_time(self, waiting_time):
        """Sets the waiting_time of this Activity.

        Waiting time at this activity in seconds. A waiting time can occur if the activity has at least one time window. If `arr_time` < `time_window.earliest` a waiting time of `time_window_earliest` - `arr_time` occurs.

        :param waiting_time: The waiting_time of this Activity.
        :type waiting_time: int
        """

        self._waiting_time = waiting_time
