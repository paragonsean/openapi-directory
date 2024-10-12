# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class PointPointDailyMorningWindData(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, angle: float=None, dir: file=None, gusts: float=None, speed: float=None):
        """PointPointDailyMorningWindData - a model defined in OpenAPI

        :param angle: The angle of this PointPointDailyMorningWindData.
        :param dir: The dir of this PointPointDailyMorningWindData.
        :param gusts: The gusts of this PointPointDailyMorningWindData.
        :param speed: The speed of this PointPointDailyMorningWindData.
        """
        self.openapi_types = {
            'angle': float,
            'dir': file,
            'gusts': float,
            'speed': float
        }

        self.attribute_map = {
            'angle': 'angle',
            'dir': 'dir',
            'gusts': 'gusts',
            'speed': 'speed'
        }

        self._angle = angle
        self._dir = dir
        self._gusts = gusts
        self._speed = speed

    @classmethod
    def from_dict(cls, dikt: dict) -> 'PointPointDailyMorningWindData':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Point_PointDailyMorningWindData of this PointPointDailyMorningWindData.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def angle(self):
        """Gets the angle of this PointPointDailyMorningWindData.

        Morning wind direction angle in degrees, 180° means wind from the south. Unit: degrees

        :return: The angle of this PointPointDailyMorningWindData.
        :rtype: float
        """
        return self._angle

    @angle.setter
    def angle(self, angle):
        """Sets the angle of this PointPointDailyMorningWindData.

        Morning wind direction angle in degrees, 180° means wind from the south. Unit: degrees

        :param angle: The angle of this PointPointDailyMorningWindData.
        :type angle: float
        """

        self._angle = angle

    @property
    def dir(self):
        """Gets the dir of this PointPointDailyMorningWindData.

        Morning wind direction in `N`, `NNE`, `NE`, ..., `NNW` format. Unit: 16dir

        :return: The dir of this PointPointDailyMorningWindData.
        :rtype: file
        """
        return self._dir

    @dir.setter
    def dir(self, dir):
        """Sets the dir of this PointPointDailyMorningWindData.

        Morning wind direction in `N`, `NNE`, `NE`, ..., `NNW` format. Unit: 16dir

        :param dir: The dir of this PointPointDailyMorningWindData.
        :type dir: file
        """

        self._dir = dir

    @property
    def gusts(self):
        """Gets the gusts of this PointPointDailyMorningWindData.

        Units: metric = m/s, us = mph, uk = mph, ca = km/h

        :return: The gusts of this PointPointDailyMorningWindData.
        :rtype: float
        """
        return self._gusts

    @gusts.setter
    def gusts(self, gusts):
        """Sets the gusts of this PointPointDailyMorningWindData.

        Units: metric = m/s, us = mph, uk = mph, ca = km/h

        :param gusts: The gusts of this PointPointDailyMorningWindData.
        :type gusts: float
        """

        self._gusts = gusts

    @property
    def speed(self):
        """Gets the speed of this PointPointDailyMorningWindData.

        Units: metric = m/s, us = mph, uk = mph, ca = km/h

        :return: The speed of this PointPointDailyMorningWindData.
        :rtype: float
        """
        return self._speed

    @speed.setter
    def speed(self, speed):
        """Sets the speed of this PointPointDailyMorningWindData.

        Units: metric = m/s, us = mph, uk = mph, ca = km/h

        :param speed: The speed of this PointPointDailyMorningWindData.
        :type speed: float
        """

        self._speed = speed
