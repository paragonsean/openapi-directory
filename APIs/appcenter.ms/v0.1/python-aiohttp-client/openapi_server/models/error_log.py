# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.analytics_generic_log_flow200_response_logs_inner_device import AnalyticsGenericLogFlow200ResponseLogsInnerDevice
from openapi_server import util


class ErrorLog(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, app_launch_toffset: int=None, id: str=None, session_id: str=None, device: AnalyticsGenericLogFlow200ResponseLogsInnerDevice=None, install_id: str=None, timestamp: datetime=None, type: str=None):
        """ErrorLog - a model defined in OpenAPI

        :param app_launch_toffset: The app_launch_toffset of this ErrorLog.
        :param id: The id of this ErrorLog.
        :param session_id: The session_id of this ErrorLog.
        :param device: The device of this ErrorLog.
        :param install_id: The install_id of this ErrorLog.
        :param timestamp: The timestamp of this ErrorLog.
        :param type: The type of this ErrorLog.
        """
        self.openapi_types = {
            'app_launch_toffset': int,
            'id': str,
            'session_id': str,
            'device': AnalyticsGenericLogFlow200ResponseLogsInnerDevice,
            'install_id': str,
            'timestamp': datetime,
            'type': str
        }

        self.attribute_map = {
            'app_launch_toffset': 'app_launch_toffset',
            'id': 'id',
            'session_id': 'session_id',
            'device': 'device',
            'install_id': 'install_id',
            'timestamp': 'timestamp',
            'type': 'type'
        }

        self._app_launch_toffset = app_launch_toffset
        self._id = id
        self._session_id = session_id
        self._device = device
        self._install_id = install_id
        self._timestamp = timestamp
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ErrorLog':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ErrorLog of this ErrorLog.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_launch_toffset(self):
        """Gets the app_launch_toffset of this ErrorLog.

        Corresponds to the number of milliseconds elapsed between the time the error occurred and the app was launched. 

        :return: The app_launch_toffset of this ErrorLog.
        :rtype: int
        """
        return self._app_launch_toffset

    @app_launch_toffset.setter
    def app_launch_toffset(self, app_launch_toffset):
        """Sets the app_launch_toffset of this ErrorLog.

        Corresponds to the number of milliseconds elapsed between the time the error occurred and the app was launched. 

        :param app_launch_toffset: The app_launch_toffset of this ErrorLog.
        :type app_launch_toffset: int
        """

        self._app_launch_toffset = app_launch_toffset

    @property
    def id(self):
        """Gets the id of this ErrorLog.

        Error identifier.

        :return: The id of this ErrorLog.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ErrorLog.

        Error identifier.

        :param id: The id of this ErrorLog.
        :type id: str
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id

    @property
    def session_id(self):
        """Gets the session_id of this ErrorLog.

        Session ID. 

        :return: The session_id of this ErrorLog.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this ErrorLog.

        Session ID. 

        :param session_id: The session_id of this ErrorLog.
        :type session_id: str
        """
        if session_id is None:
            raise ValueError("Invalid value for `session_id`, must not be `None`")

        self._session_id = session_id

    @property
    def device(self):
        """Gets the device of this ErrorLog.


        :return: The device of this ErrorLog.
        :rtype: AnalyticsGenericLogFlow200ResponseLogsInnerDevice
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this ErrorLog.


        :param device: The device of this ErrorLog.
        :type device: AnalyticsGenericLogFlow200ResponseLogsInnerDevice
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")

        self._device = device

    @property
    def install_id(self):
        """Gets the install_id of this ErrorLog.

        Install ID. 

        :return: The install_id of this ErrorLog.
        :rtype: str
        """
        return self._install_id

    @install_id.setter
    def install_id(self, install_id):
        """Sets the install_id of this ErrorLog.

        Install ID. 

        :param install_id: The install_id of this ErrorLog.
        :type install_id: str
        """
        if install_id is None:
            raise ValueError("Invalid value for `install_id`, must not be `None`")

        self._install_id = install_id

    @property
    def timestamp(self):
        """Gets the timestamp of this ErrorLog.

        Log creation timestamp. 

        :return: The timestamp of this ErrorLog.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ErrorLog.

        Log creation timestamp. 

        :param timestamp: The timestamp of this ErrorLog.
        :type timestamp: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp

    @property
    def type(self):
        """Gets the type of this ErrorLog.

        Log type. 

        :return: The type of this ErrorLog.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ErrorLog.

        Log type. 

        :param type: The type of this ErrorLog.
        :type type: str
        """
        allowed_values = ["event", "page", "start_session", "error", "push_installation", "start_service", "custom_properties"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
