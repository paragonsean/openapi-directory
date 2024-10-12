# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
import re
from openapi_server import util


class OriginalVersionDurationVersionVersion(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, duration: str=None, href: str=None, pid: str=None):
        """OriginalVersionDurationVersionVersion - a model defined in OpenAPI

        :param duration: The duration of this OriginalVersionDurationVersionVersion.
        :param href: The href of this OriginalVersionDurationVersionVersion.
        :param pid: The pid of this OriginalVersionDurationVersionVersion.
        """
        self.openapi_types = {
            'duration': str,
            'href': str,
            'pid': str
        }

        self.attribute_map = {
            'duration': 'duration',
            'href': 'href',
            'pid': 'pid'
        }

        self._duration = duration
        self._href = href
        self._pid = pid

    @classmethod
    def from_dict(cls, dikt: dict) -> 'OriginalVersionDurationVersionVersion':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The original_version_duration_version_version of this OriginalVersionDurationVersionVersion.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def duration(self):
        """Gets the duration of this OriginalVersionDurationVersionVersion.


        :return: The duration of this OriginalVersionDurationVersionVersion.
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this OriginalVersionDurationVersionVersion.


        :param duration: The duration of this OriginalVersionDurationVersionVersion.
        :type duration: str
        """
        if duration is not None and not re.search(r'^(-)?P(?:([0-9,.]*)Y)?(?:([0-9,.]*)M)?(?:([0-9,.]*)W)?(?:([0-9,.]*)D)?(?:T(?:([0-9,.]*)H)?(?:([0-9,.]*)M)?(?:([0-9,.]*)S)?)?$', duration):
            raise ValueError("Invalid value for `duration`, must be a follow pattern or equal to `/^(-)?P(?:([0-9,.]*)Y)?(?:([0-9,.]*)M)?(?:([0-9,.]*)W)?(?:([0-9,.]*)D)?(?:T(?:([0-9,.]*)H)?(?:([0-9,.]*)M)?(?:([0-9,.]*)S)?)?$/`")

        self._duration = duration

    @property
    def href(self):
        """Gets the href of this OriginalVersionDurationVersionVersion.


        :return: The href of this OriginalVersionDurationVersionVersion.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this OriginalVersionDurationVersionVersion.


        :param href: The href of this OriginalVersionDurationVersionVersion.
        :type href: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")

        self._href = href

    @property
    def pid(self):
        """Gets the pid of this OriginalVersionDurationVersionVersion.


        :return: The pid of this OriginalVersionDurationVersionVersion.
        :rtype: str
        """
        return self._pid

    @pid.setter
    def pid(self, pid):
        """Sets the pid of this OriginalVersionDurationVersionVersion.


        :param pid: The pid of this OriginalVersionDurationVersionVersion.
        :type pid: str
        """
        if pid is None:
            raise ValueError("Invalid value for `pid`, must not be `None`")
        if pid is not None and not re.search(r'([a-z0-9\.\-]+|.*PID.*)', pid):
            raise ValueError("Invalid value for `pid`, must be a follow pattern or equal to `/([a-z0-9\.\-]+|.*PID.*)/`")

        self._pid = pid
