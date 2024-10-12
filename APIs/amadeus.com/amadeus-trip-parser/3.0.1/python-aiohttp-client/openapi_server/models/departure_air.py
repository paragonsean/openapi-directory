# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class DepartureAir(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, check_in_end_time: str=None, iata_code: str=None, local_date_time: str=None, terminal: str=None):
        """DepartureAir - a model defined in OpenAPI

        :param check_in_end_time: The check_in_end_time of this DepartureAir.
        :param iata_code: The iata_code of this DepartureAir.
        :param local_date_time: The local_date_time of this DepartureAir.
        :param terminal: The terminal of this DepartureAir.
        """
        self.openapi_types = {
            'check_in_end_time': str,
            'iata_code': str,
            'local_date_time': str,
            'terminal': str
        }

        self.attribute_map = {
            'check_in_end_time': 'checkInEndTime',
            'iata_code': 'iataCode',
            'local_date_time': 'localDateTime',
            'terminal': 'terminal'
        }

        self._check_in_end_time = check_in_end_time
        self._iata_code = iata_code
        self._local_date_time = local_date_time
        self._terminal = terminal

    @classmethod
    def from_dict(cls, dikt: dict) -> 'DepartureAir':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The departureAir of this DepartureAir.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def check_in_end_time(self):
        """Gets the check_in_end_time of this DepartureAir.


        :return: The check_in_end_time of this DepartureAir.
        :rtype: str
        """
        return self._check_in_end_time

    @check_in_end_time.setter
    def check_in_end_time(self, check_in_end_time):
        """Sets the check_in_end_time of this DepartureAir.


        :param check_in_end_time: The check_in_end_time of this DepartureAir.
        :type check_in_end_time: str
        """

        self._check_in_end_time = check_in_end_time

    @property
    def iata_code(self):
        """Gets the iata_code of this DepartureAir.

        IATA Airport code

        :return: The iata_code of this DepartureAir.
        :rtype: str
        """
        return self._iata_code

    @iata_code.setter
    def iata_code(self, iata_code):
        """Sets the iata_code of this DepartureAir.

        IATA Airport code

        :param iata_code: The iata_code of this DepartureAir.
        :type iata_code: str
        """

        self._iata_code = iata_code

    @property
    def local_date_time(self):
        """Gets the local_date_time of this DepartureAir.

        Local schedule dateTime of the departure or arrival. Conversion of dateTime in local date time.

        :return: The local_date_time of this DepartureAir.
        :rtype: str
        """
        return self._local_date_time

    @local_date_time.setter
    def local_date_time(self, local_date_time):
        """Sets the local_date_time of this DepartureAir.

        Local schedule dateTime of the departure or arrival. Conversion of dateTime in local date time.

        :param local_date_time: The local_date_time of this DepartureAir.
        :type local_date_time: str
        """

        self._local_date_time = local_date_time

    @property
    def terminal(self):
        """Gets the terminal of this DepartureAir.

        Terminal name / number

        :return: The terminal of this DepartureAir.
        :rtype: str
        """
        return self._terminal

    @terminal.setter
    def terminal(self, terminal):
        """Sets the terminal of this DepartureAir.

        Terminal name / number

        :param terminal: The terminal of this DepartureAir.
        :type terminal: str
        """

        self._terminal = terminal
