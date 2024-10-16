# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class BusinessHolidayViewModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, business_closed: bool=None, holiday_name: str=None, id: str=None, public_holiday_id: int=None):
        """BusinessHolidayViewModel - a model defined in OpenAPI

        :param business_closed: The business_closed of this BusinessHolidayViewModel.
        :param holiday_name: The holiday_name of this BusinessHolidayViewModel.
        :param id: The id of this BusinessHolidayViewModel.
        :param public_holiday_id: The public_holiday_id of this BusinessHolidayViewModel.
        """
        self.openapi_types = {
            'business_closed': bool,
            'holiday_name': str,
            'id': str,
            'public_holiday_id': int
        }

        self.attribute_map = {
            'business_closed': 'businessClosed',
            'holiday_name': 'holidayName',
            'id': 'id',
            'public_holiday_id': 'publicHolidayId'
        }

        self._business_closed = business_closed
        self._holiday_name = holiday_name
        self._id = id
        self._public_holiday_id = public_holiday_id

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BusinessHolidayViewModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BusinessHolidayViewModel of this BusinessHolidayViewModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def business_closed(self):
        """Gets the business_closed of this BusinessHolidayViewModel.


        :return: The business_closed of this BusinessHolidayViewModel.
        :rtype: bool
        """
        return self._business_closed

    @business_closed.setter
    def business_closed(self, business_closed):
        """Sets the business_closed of this BusinessHolidayViewModel.


        :param business_closed: The business_closed of this BusinessHolidayViewModel.
        :type business_closed: bool
        """

        self._business_closed = business_closed

    @property
    def holiday_name(self):
        """Gets the holiday_name of this BusinessHolidayViewModel.


        :return: The holiday_name of this BusinessHolidayViewModel.
        :rtype: str
        """
        return self._holiday_name

    @holiday_name.setter
    def holiday_name(self, holiday_name):
        """Sets the holiday_name of this BusinessHolidayViewModel.


        :param holiday_name: The holiday_name of this BusinessHolidayViewModel.
        :type holiday_name: str
        """

        self._holiday_name = holiday_name

    @property
    def id(self):
        """Gets the id of this BusinessHolidayViewModel.


        :return: The id of this BusinessHolidayViewModel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BusinessHolidayViewModel.


        :param id: The id of this BusinessHolidayViewModel.
        :type id: str
        """

        self._id = id

    @property
    def public_holiday_id(self):
        """Gets the public_holiday_id of this BusinessHolidayViewModel.


        :return: The public_holiday_id of this BusinessHolidayViewModel.
        :rtype: int
        """
        return self._public_holiday_id

    @public_holiday_id.setter
    def public_holiday_id(self, public_holiday_id):
        """Sets the public_holiday_id of this BusinessHolidayViewModel.


        :param public_holiday_id: The public_holiday_id of this BusinessHolidayViewModel.
        :type public_holiday_id: int
        """

        self._public_holiday_id = public_holiday_id
