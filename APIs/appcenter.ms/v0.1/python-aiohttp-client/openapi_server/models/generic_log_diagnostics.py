# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.analytics_generic_log_flow200_response_logs_inner_device import AnalyticsGenericLogFlow200ResponseLogsInnerDevice
from openapi_server import util


class GenericLogDiagnostics(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, device: AnalyticsGenericLogFlow200ResponseLogsInnerDevice=None, event_id: str=None, event_name: str=None, install_id: str=None, message_id: str=None, properties: Dict[str, str]=None, session_id: str=None, timestamp: datetime=None, type: str=None):
        """GenericLogDiagnostics - a model defined in OpenAPI

        :param device: The device of this GenericLogDiagnostics.
        :param event_id: The event_id of this GenericLogDiagnostics.
        :param event_name: The event_name of this GenericLogDiagnostics.
        :param install_id: The install_id of this GenericLogDiagnostics.
        :param message_id: The message_id of this GenericLogDiagnostics.
        :param properties: The properties of this GenericLogDiagnostics.
        :param session_id: The session_id of this GenericLogDiagnostics.
        :param timestamp: The timestamp of this GenericLogDiagnostics.
        :param type: The type of this GenericLogDiagnostics.
        """
        self.openapi_types = {
            'device': AnalyticsGenericLogFlow200ResponseLogsInnerDevice,
            'event_id': str,
            'event_name': str,
            'install_id': str,
            'message_id': str,
            'properties': Dict[str, str],
            'session_id': str,
            'timestamp': datetime,
            'type': str
        }

        self.attribute_map = {
            'device': 'device',
            'event_id': 'event_id',
            'event_name': 'event_name',
            'install_id': 'install_id',
            'message_id': 'message_id',
            'properties': 'properties',
            'session_id': 'session_id',
            'timestamp': 'timestamp',
            'type': 'type'
        }

        self._device = device
        self._event_id = event_id
        self._event_name = event_name
        self._install_id = install_id
        self._message_id = message_id
        self._properties = properties
        self._session_id = session_id
        self._timestamp = timestamp
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'GenericLogDiagnostics':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The GenericLog_Diagnostics of this GenericLogDiagnostics.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def device(self):
        """Gets the device of this GenericLogDiagnostics.


        :return: The device of this GenericLogDiagnostics.
        :rtype: AnalyticsGenericLogFlow200ResponseLogsInnerDevice
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this GenericLogDiagnostics.


        :param device: The device of this GenericLogDiagnostics.
        :type device: AnalyticsGenericLogFlow200ResponseLogsInnerDevice
        """
        if device is None:
            raise ValueError("Invalid value for `device`, must not be `None`")

        self._device = device

    @property
    def event_id(self):
        """Gets the event_id of this GenericLogDiagnostics.

        Event ID. 

        :return: The event_id of this GenericLogDiagnostics.
        :rtype: str
        """
        return self._event_id

    @event_id.setter
    def event_id(self, event_id):
        """Sets the event_id of this GenericLogDiagnostics.

        Event ID. 

        :param event_id: The event_id of this GenericLogDiagnostics.
        :type event_id: str
        """

        self._event_id = event_id

    @property
    def event_name(self):
        """Gets the event_name of this GenericLogDiagnostics.

        Event name. 

        :return: The event_name of this GenericLogDiagnostics.
        :rtype: str
        """
        return self._event_name

    @event_name.setter
    def event_name(self, event_name):
        """Sets the event_name of this GenericLogDiagnostics.

        Event name. 

        :param event_name: The event_name of this GenericLogDiagnostics.
        :type event_name: str
        """

        self._event_name = event_name

    @property
    def install_id(self):
        """Gets the install_id of this GenericLogDiagnostics.

        Install ID. 

        :return: The install_id of this GenericLogDiagnostics.
        :rtype: str
        """
        return self._install_id

    @install_id.setter
    def install_id(self, install_id):
        """Sets the install_id of this GenericLogDiagnostics.

        Install ID. 

        :param install_id: The install_id of this GenericLogDiagnostics.
        :type install_id: str
        """
        if install_id is None:
            raise ValueError("Invalid value for `install_id`, must not be `None`")

        self._install_id = install_id

    @property
    def message_id(self):
        """Gets the message_id of this GenericLogDiagnostics.

        Message ID. 

        :return: The message_id of this GenericLogDiagnostics.
        :rtype: str
        """
        return self._message_id

    @message_id.setter
    def message_id(self, message_id):
        """Sets the message_id of this GenericLogDiagnostics.

        Message ID. 

        :param message_id: The message_id of this GenericLogDiagnostics.
        :type message_id: str
        """

        self._message_id = message_id

    @property
    def properties(self):
        """Gets the properties of this GenericLogDiagnostics.

        event specific properties. 

        :return: The properties of this GenericLogDiagnostics.
        :rtype: Dict[str, str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this GenericLogDiagnostics.

        event specific properties. 

        :param properties: The properties of this GenericLogDiagnostics.
        :type properties: Dict[str, str]
        """

        self._properties = properties

    @property
    def session_id(self):
        """Gets the session_id of this GenericLogDiagnostics.

        Session ID. 

        :return: The session_id of this GenericLogDiagnostics.
        :rtype: str
        """
        return self._session_id

    @session_id.setter
    def session_id(self, session_id):
        """Sets the session_id of this GenericLogDiagnostics.

        Session ID. 

        :param session_id: The session_id of this GenericLogDiagnostics.
        :type session_id: str
        """

        self._session_id = session_id

    @property
    def timestamp(self):
        """Gets the timestamp of this GenericLogDiagnostics.

        Log creation timestamp. 

        :return: The timestamp of this GenericLogDiagnostics.
        :rtype: datetime
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this GenericLogDiagnostics.

        Log creation timestamp. 

        :param timestamp: The timestamp of this GenericLogDiagnostics.
        :type timestamp: datetime
        """
        if timestamp is None:
            raise ValueError("Invalid value for `timestamp`, must not be `None`")

        self._timestamp = timestamp

    @property
    def type(self):
        """Gets the type of this GenericLogDiagnostics.

        Log type. 

        :return: The type of this GenericLogDiagnostics.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this GenericLogDiagnostics.

        Log type. 

        :param type: The type of this GenericLogDiagnostics.
        :type type: str
        """
        allowed_values = ["event", "page", "start_session", "error", "push_installation", "start_service", "custom_properties"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"
                .format(type, allowed_values)
            )

        self._type = type
