# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class Transmitter(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, alt: float=1, bwi: float=0.1, frq: float=868, lat: float=38.916, lon: float=1.448, txw: float=0.1):
        """Transmitter - a model defined in OpenAPI

        :param alt: The alt of this Transmitter.
        :param bwi: The bwi of this Transmitter.
        :param frq: The frq of this Transmitter.
        :param lat: The lat of this Transmitter.
        :param lon: The lon of this Transmitter.
        :param txw: The txw of this Transmitter.
        """
        self.openapi_types = {
            'alt': float,
            'bwi': float,
            'frq': float,
            'lat': float,
            'lon': float,
            'txw': float
        }

        self.attribute_map = {
            'alt': 'alt',
            'bwi': 'bwi',
            'frq': 'frq',
            'lat': 'lat',
            'lon': 'lon',
            'txw': 'txw'
        }

        self._alt = alt
        self._bwi = bwi
        self._frq = frq
        self._lat = lat
        self._lon = lon
        self._txw = txw

    @classmethod
    def from_dict(cls, dikt: dict) -> 'Transmitter':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The Transmitter of this Transmitter.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def alt(self):
        """Gets the alt of this Transmitter.

        Altitude above ground level in metres OR feet

        :return: The alt of this Transmitter.
        :rtype: float
        """
        return self._alt

    @alt.setter
    def alt(self, alt):
        """Sets the alt of this Transmitter.

        Altitude above ground level in metres OR feet

        :param alt: The alt of this Transmitter.
        :type alt: float
        """
        if alt is not None and alt > 60000:
            raise ValueError("Invalid value for `alt`, must be a value less than or equal to `60000`")
        if alt is not None and alt < 0.1:
            raise ValueError("Invalid value for `alt`, must be a value greater than or equal to `0.1`")

        self._alt = alt

    @property
    def bwi(self):
        """Gets the bwi of this Transmitter.

        Bandwidth in MHz. 1MHz has a noise floor of -114dBm. 10MHz = -104dBm, 20MHz = -101dBm

        :return: The bwi of this Transmitter.
        :rtype: float
        """
        return self._bwi

    @bwi.setter
    def bwi(self, bwi):
        """Sets the bwi of this Transmitter.

        Bandwidth in MHz. 1MHz has a noise floor of -114dBm. 10MHz = -104dBm, 20MHz = -101dBm

        :param bwi: The bwi of this Transmitter.
        :type bwi: float
        """
        if bwi is not None and bwi > 100:
            raise ValueError("Invalid value for `bwi`, must be a value less than or equal to `100`")
        if bwi is not None and bwi < 0.1:
            raise ValueError("Invalid value for `bwi`, must be a value greater than or equal to `0.1`")

        self._bwi = bwi

    @property
    def frq(self):
        """Gets the frq of this Transmitter.

        Centre frequency in megahertz

        :return: The frq of this Transmitter.
        :rtype: float
        """
        return self._frq

    @frq.setter
    def frq(self, frq):
        """Sets the frq of this Transmitter.

        Centre frequency in megahertz

        :param frq: The frq of this Transmitter.
        :type frq: float
        """
        if frq is not None and frq > 100000:
            raise ValueError("Invalid value for `frq`, must be a value less than or equal to `100000`")
        if frq is not None and frq < 1:
            raise ValueError("Invalid value for `frq`, must be a value greater than or equal to `1`")

        self._frq = frq

    @property
    def lat(self):
        """Gets the lat of this Transmitter.

        Latitude in decimal degrees

        :return: The lat of this Transmitter.
        :rtype: float
        """
        return self._lat

    @lat.setter
    def lat(self, lat):
        """Sets the lat of this Transmitter.

        Latitude in decimal degrees

        :param lat: The lat of this Transmitter.
        :type lat: float
        """
        if lat is not None and lat > 89:
            raise ValueError("Invalid value for `lat`, must be a value less than or equal to `89`")
        if lat is not None and lat < -89:
            raise ValueError("Invalid value for `lat`, must be a value greater than or equal to `-89`")

        self._lat = lat

    @property
    def lon(self):
        """Gets the lon of this Transmitter.

        Longitude in decimal degrees

        :return: The lon of this Transmitter.
        :rtype: float
        """
        return self._lon

    @lon.setter
    def lon(self, lon):
        """Sets the lon of this Transmitter.

        Longitude in decimal degrees

        :param lon: The lon of this Transmitter.
        :type lon: float
        """
        if lon is not None and lon > 180:
            raise ValueError("Invalid value for `lon`, must be a value less than or equal to `180`")
        if lon is not None and lon < -180:
            raise ValueError("Invalid value for `lon`, must be a value greater than or equal to `-180`")

        self._lon = lon

    @property
    def txw(self):
        """Gets the txw of this Transmitter.

        Transmitter power in watts before the antenna

        :return: The txw of this Transmitter.
        :rtype: float
        """
        return self._txw

    @txw.setter
    def txw(self, txw):
        """Sets the txw of this Transmitter.

        Transmitter power in watts before the antenna

        :param txw: The txw of this Transmitter.
        :type txw: float
        """
        if txw is not None and txw > 2000000:
            raise ValueError("Invalid value for `txw`, must be a value less than or equal to `2000000`")
        if txw is not None and txw < 0.001:
            raise ValueError("Invalid value for `txw`, must be a value greater than or equal to `0.001`")

        self._txw = txw
