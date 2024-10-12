# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Property1(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, key: str=None, section: str=None, value: str=None):
        """Property1 - a model defined in OpenAPI

        :param key: The key of this Property1.
        :param section: The section of this Property1.
        :param value: The value of this Property1.
        """
        self.openapi_types = {
            'key': str,
            'section': str,
            'value': str
        }

        self.attribute_map = {
            'key': 'key',
            'section': 'section',
            'value': 'value'
        }

        self._key = key
        self._section = section
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Property1':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The property_1 of this Property1.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def key(self):
        """Gets the key of this Property1.

        The key of the property. For <strong>rtsp</strong>, valid values are <strong>debugRtspSession</strong>, <strong>maxRtcpWaitTime</strong>, <strong>avSyncMethod</strong>, <strong>rtspValidationFrequency</strong>, <strong>rtpTransportMode</strong>, <strong>rtspFilterUnknownTracks</strong>, <strong>rtpIgnoreSpropParameterSets</strong>, and <strong>rtpIgnoreProfileLevelId</strong>. For <strong>cupertino</strong>, valid values are <strong>cupertinoEnableProgramDateTime</strong>, <strong>cupertinoEnableId3ProgramDateTime</strong>, and <strong>cupertinoProgramDateTimeOffset</strong>.

        :return: The key of this Property1.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this Property1.

        The key of the property. For <strong>rtsp</strong>, valid values are <strong>debugRtspSession</strong>, <strong>maxRtcpWaitTime</strong>, <strong>avSyncMethod</strong>, <strong>rtspValidationFrequency</strong>, <strong>rtpTransportMode</strong>, <strong>rtspFilterUnknownTracks</strong>, <strong>rtpIgnoreSpropParameterSets</strong>, and <strong>rtpIgnoreProfileLevelId</strong>. For <strong>cupertino</strong>, valid values are <strong>cupertinoEnableProgramDateTime</strong>, <strong>cupertinoEnableId3ProgramDateTime</strong>, and <strong>cupertinoProgramDateTimeOffset</strong>.

        :param key: The key of this Property1.
        :type key: str
        """
        if key is None:
            raise ValueError("Invalid value for `key`, must not be `None`")

        self._key = key

    @property
    def section(self):
        """Gets the section of this Property1.

        The section of the transcoder configuration table that contains the property. Valid values are <strong>rtsp</strong> and <strong>cupertino</strong>.

        :return: The section of this Property1.
        :rtype: str
        """
        return self._section

    @section.setter
    def section(self, section):
        """Sets the section of this Property1.

        The section of the transcoder configuration table that contains the property. Valid values are <strong>rtsp</strong> and <strong>cupertino</strong>.

        :param section: The section of this Property1.
        :type section: str
        """
        if section is None:
            raise ValueError("Invalid value for `section`, must not be `None`")

        self._section = section

    @property
    def value(self):
        """Gets the value of this Property1.

        The value of the property. For <strong>debugRtspSession</strong>, <strong>avSyncMethod</strong>, <strong>rtspFilterUnknownTracks</strong>, <strong>rtpIgnoreSpropParameterSets</strong>, <strong>rtpIgnoreProfileLevelId</strong>, <strong>cupertinoEnableProgramDateTime</strong>, and <strong>cupertinoEnableId3ProgramDateTime</strong>, valid values are <strong>true</strong> or <strong>false</strong>. <strong>maxRtcpWaitTime</strong> must be <strong>0</strong> (ms, off) or greater. The default is <strong>2000</strong>. Valid values for <strong>rtpTransportMode</strong> are <strong>udp</strong> or <strong>interleave</strong> (the default). <strong>rtspValidationFrequency</strong> must be <strong>0</strong> (ms, off) or greater. The default is <strong>15000</strong>. <strong>cupertinoProgramDateTimeOffset</strong> must be an integer, positive or negative. The default is <strong>0</strong> (ms).

        :return: The value of this Property1.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Property1.

        The value of the property. For <strong>debugRtspSession</strong>, <strong>avSyncMethod</strong>, <strong>rtspFilterUnknownTracks</strong>, <strong>rtpIgnoreSpropParameterSets</strong>, <strong>rtpIgnoreProfileLevelId</strong>, <strong>cupertinoEnableProgramDateTime</strong>, and <strong>cupertinoEnableId3ProgramDateTime</strong>, valid values are <strong>true</strong> or <strong>false</strong>. <strong>maxRtcpWaitTime</strong> must be <strong>0</strong> (ms, off) or greater. The default is <strong>2000</strong>. Valid values for <strong>rtpTransportMode</strong> are <strong>udp</strong> or <strong>interleave</strong> (the default). <strong>rtspValidationFrequency</strong> must be <strong>0</strong> (ms, off) or greater. The default is <strong>15000</strong>. <strong>cupertinoProgramDateTimeOffset</strong> must be an integer, positive or negative. The default is <strong>0</strong> (ms).

        :param value: The value of this Property1.
        :type value: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

        self._value = value
