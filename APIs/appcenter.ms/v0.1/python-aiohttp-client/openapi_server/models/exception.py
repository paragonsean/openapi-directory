# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.exception_frames_inner import ExceptionFramesInner
from openapi_server import util


class Exception(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, frames: List[ExceptionFramesInner]=None, inner_exceptions: List[Exception]=None, platform: str=None, reason: str=None, relevant: bool=None, type: str=None):
        """Exception - a model defined in OpenAPI

        :param frames: The frames of this Exception.
        :param inner_exceptions: The inner_exceptions of this Exception.
        :param platform: The platform of this Exception.
        :param reason: The reason of this Exception.
        :param relevant: The relevant of this Exception.
        :param type: The type of this Exception.
        """
        self.openapi_types = {
            'frames': List[ExceptionFramesInner],
            'inner_exceptions': List[Exception],
            'platform': str,
            'reason': str,
            'relevant': bool,
            'type': str
        }

        self.attribute_map = {
            'frames': 'frames',
            'inner_exceptions': 'inner_exceptions',
            'platform': 'platform',
            'reason': 'reason',
            'relevant': 'relevant',
            'type': 'type'
        }

        self._frames = frames
        self._inner_exceptions = inner_exceptions
        self._platform = platform
        self._reason = reason
        self._relevant = relevant
        self._type = type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Exception':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Exception of this Exception.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def frames(self):
        """Gets the frames of this Exception.

        frames of the excetpion

        :return: The frames of this Exception.
        :rtype: List[ExceptionFramesInner]
        """
        return self._frames

    @frames.setter
    def frames(self, frames):
        """Sets the frames of this Exception.

        frames of the excetpion

        :param frames: The frames of this Exception.
        :type frames: List[ExceptionFramesInner]
        """
        if frames is None:
            raise ValueError("Invalid value for `frames`, must not be `None`")

        self._frames = frames

    @property
    def inner_exceptions(self):
        """Gets the inner_exceptions of this Exception.


        :return: The inner_exceptions of this Exception.
        :rtype: List[Exception]
        """
        return self._inner_exceptions

    @inner_exceptions.setter
    def inner_exceptions(self, inner_exceptions):
        """Sets the inner_exceptions of this Exception.


        :param inner_exceptions: The inner_exceptions of this Exception.
        :type inner_exceptions: List[Exception]
        """

        self._inner_exceptions = inner_exceptions

    @property
    def platform(self):
        """Gets the platform of this Exception.

        SDK/Platform this thread is beeing generated from

        :return: The platform of this Exception.
        :rtype: str
        """
        return self._platform

    @platform.setter
    def platform(self, platform):
        """Sets the platform of this Exception.

        SDK/Platform this thread is beeing generated from

        :param platform: The platform of this Exception.
        :type platform: str
        """
        allowed_values = ["ios", "android", "xamarin", "react-native", "ndk", "unity", "other"]  # noqa: E501
        if platform not in allowed_values:
            raise ValueError(
                "Invalid value for `platform` ({0}), must be one of {1}"
                .format(platform, allowed_values)
            )

        self._platform = platform

    @property
    def reason(self):
        """Gets the reason of this Exception.

        Reason of the exception

        :return: The reason of this Exception.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this Exception.

        Reason of the exception

        :param reason: The reason of this Exception.
        :type reason: str
        """

        self._reason = reason

    @property
    def relevant(self):
        """Gets the relevant of this Exception.

        relevant exception (crashed)

        :return: The relevant of this Exception.
        :rtype: bool
        """
        return self._relevant

    @relevant.setter
    def relevant(self, relevant):
        """Sets the relevant of this Exception.

        relevant exception (crashed)

        :param relevant: The relevant of this Exception.
        :type relevant: bool
        """

        self._relevant = relevant

    @property
    def type(self):
        """Gets the type of this Exception.

        Type of the exception (NSSomethingException, NullPointerException)

        :return: The type of this Exception.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Exception.

        Type of the exception (NSSomethingException, NullPointerException)

        :param type: The type of this Exception.
        :type type: str
        """

        self._type = type
