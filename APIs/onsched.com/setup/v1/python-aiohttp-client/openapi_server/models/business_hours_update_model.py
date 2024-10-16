# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.business_hour_input_model import BusinessHourInputModel
from openapi_server import util


class BusinessHoursUpdateModel(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, fri: BusinessHourInputModel=None, mon: BusinessHourInputModel=None, sat: BusinessHourInputModel=None, sun: BusinessHourInputModel=None, thu: BusinessHourInputModel=None, tue: BusinessHourInputModel=None, wed: BusinessHourInputModel=None):
        """BusinessHoursUpdateModel - a model defined in OpenAPI

        :param fri: The fri of this BusinessHoursUpdateModel.
        :param mon: The mon of this BusinessHoursUpdateModel.
        :param sat: The sat of this BusinessHoursUpdateModel.
        :param sun: The sun of this BusinessHoursUpdateModel.
        :param thu: The thu of this BusinessHoursUpdateModel.
        :param tue: The tue of this BusinessHoursUpdateModel.
        :param wed: The wed of this BusinessHoursUpdateModel.
        """
        self.openapi_types = {
            'fri': BusinessHourInputModel,
            'mon': BusinessHourInputModel,
            'sat': BusinessHourInputModel,
            'sun': BusinessHourInputModel,
            'thu': BusinessHourInputModel,
            'tue': BusinessHourInputModel,
            'wed': BusinessHourInputModel
        }

        self.attribute_map = {
            'fri': 'fri',
            'mon': 'mon',
            'sat': 'sat',
            'sun': 'sun',
            'thu': 'thu',
            'tue': 'tue',
            'wed': 'wed'
        }

        self._fri = fri
        self._mon = mon
        self._sat = sat
        self._sun = sun
        self._thu = thu
        self._tue = tue
        self._wed = wed

    @classmethod
    def from_dict(cls, dikt: dict) -> 'BusinessHoursUpdateModel':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The BusinessHoursUpdateModel of this BusinessHoursUpdateModel.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def fri(self):
        """Gets the fri of this BusinessHoursUpdateModel.


        :return: The fri of this BusinessHoursUpdateModel.
        :rtype: BusinessHourInputModel
        """
        return self._fri

    @fri.setter
    def fri(self, fri):
        """Sets the fri of this BusinessHoursUpdateModel.


        :param fri: The fri of this BusinessHoursUpdateModel.
        :type fri: BusinessHourInputModel
        """

        self._fri = fri

    @property
    def mon(self):
        """Gets the mon of this BusinessHoursUpdateModel.


        :return: The mon of this BusinessHoursUpdateModel.
        :rtype: BusinessHourInputModel
        """
        return self._mon

    @mon.setter
    def mon(self, mon):
        """Sets the mon of this BusinessHoursUpdateModel.


        :param mon: The mon of this BusinessHoursUpdateModel.
        :type mon: BusinessHourInputModel
        """

        self._mon = mon

    @property
    def sat(self):
        """Gets the sat of this BusinessHoursUpdateModel.


        :return: The sat of this BusinessHoursUpdateModel.
        :rtype: BusinessHourInputModel
        """
        return self._sat

    @sat.setter
    def sat(self, sat):
        """Sets the sat of this BusinessHoursUpdateModel.


        :param sat: The sat of this BusinessHoursUpdateModel.
        :type sat: BusinessHourInputModel
        """

        self._sat = sat

    @property
    def sun(self):
        """Gets the sun of this BusinessHoursUpdateModel.


        :return: The sun of this BusinessHoursUpdateModel.
        :rtype: BusinessHourInputModel
        """
        return self._sun

    @sun.setter
    def sun(self, sun):
        """Sets the sun of this BusinessHoursUpdateModel.


        :param sun: The sun of this BusinessHoursUpdateModel.
        :type sun: BusinessHourInputModel
        """

        self._sun = sun

    @property
    def thu(self):
        """Gets the thu of this BusinessHoursUpdateModel.


        :return: The thu of this BusinessHoursUpdateModel.
        :rtype: BusinessHourInputModel
        """
        return self._thu

    @thu.setter
    def thu(self, thu):
        """Sets the thu of this BusinessHoursUpdateModel.


        :param thu: The thu of this BusinessHoursUpdateModel.
        :type thu: BusinessHourInputModel
        """

        self._thu = thu

    @property
    def tue(self):
        """Gets the tue of this BusinessHoursUpdateModel.


        :return: The tue of this BusinessHoursUpdateModel.
        :rtype: BusinessHourInputModel
        """
        return self._tue

    @tue.setter
    def tue(self, tue):
        """Sets the tue of this BusinessHoursUpdateModel.


        :param tue: The tue of this BusinessHoursUpdateModel.
        :type tue: BusinessHourInputModel
        """

        self._tue = tue

    @property
    def wed(self):
        """Gets the wed of this BusinessHoursUpdateModel.


        :return: The wed of this BusinessHoursUpdateModel.
        :rtype: BusinessHourInputModel
        """
        return self._wed

    @wed.setter
    def wed(self, wed):
        """Sets the wed of this BusinessHoursUpdateModel.


        :param wed: The wed of this BusinessHoursUpdateModel.
        :type wed: BusinessHourInputModel
        """

        self._wed = wed
