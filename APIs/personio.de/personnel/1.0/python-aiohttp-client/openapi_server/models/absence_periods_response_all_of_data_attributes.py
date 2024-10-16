# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.absence_periods_response_all_of_data_certificate import AbsencePeriodsResponseAllOfDataCertificate
from openapi_server.models.absence_periods_response_all_of_data_employee import AbsencePeriodsResponseAllOfDataEmployee
from openapi_server.models.absence_periods_response_all_of_data_time_off_type import AbsencePeriodsResponseAllOfDataTimeOffType
from openapi_server import util


class AbsencePeriodsResponseAllOfDataAttributes(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, certificate: AbsencePeriodsResponseAllOfDataCertificate=None, created_at: str=None, days_count: float=None, employee: AbsencePeriodsResponseAllOfDataEmployee=None, end_date: str=None, half_day_end: float=None, half_day_start: float=None, id: int=None, start_date: str=None, status: str=None, time_off_type: AbsencePeriodsResponseAllOfDataTimeOffType=None):
        """AbsencePeriodsResponseAllOfDataAttributes - a model defined in OpenAPI

        :param certificate: The certificate of this AbsencePeriodsResponseAllOfDataAttributes.
        :param created_at: The created_at of this AbsencePeriodsResponseAllOfDataAttributes.
        :param days_count: The days_count of this AbsencePeriodsResponseAllOfDataAttributes.
        :param employee: The employee of this AbsencePeriodsResponseAllOfDataAttributes.
        :param end_date: The end_date of this AbsencePeriodsResponseAllOfDataAttributes.
        :param half_day_end: The half_day_end of this AbsencePeriodsResponseAllOfDataAttributes.
        :param half_day_start: The half_day_start of this AbsencePeriodsResponseAllOfDataAttributes.
        :param id: The id of this AbsencePeriodsResponseAllOfDataAttributes.
        :param start_date: The start_date of this AbsencePeriodsResponseAllOfDataAttributes.
        :param status: The status of this AbsencePeriodsResponseAllOfDataAttributes.
        :param time_off_type: The time_off_type of this AbsencePeriodsResponseAllOfDataAttributes.
        """
        self.openapi_types = {
            'certificate': AbsencePeriodsResponseAllOfDataCertificate,
            'created_at': str,
            'days_count': float,
            'employee': AbsencePeriodsResponseAllOfDataEmployee,
            'end_date': str,
            'half_day_end': float,
            'half_day_start': float,
            'id': int,
            'start_date': str,
            'status': str,
            'time_off_type': AbsencePeriodsResponseAllOfDataTimeOffType
        }

        self.attribute_map = {
            'certificate': 'certificate',
            'created_at': 'created_at',
            'days_count': 'days_count',
            'employee': 'employee',
            'end_date': 'end_date',
            'half_day_end': 'half_day_end',
            'half_day_start': 'half_day_start',
            'id': 'id',
            'start_date': 'start_date',
            'status': 'status',
            'time_off_type': 'time_off_type'
        }

        self._certificate = certificate
        self._created_at = created_at
        self._days_count = days_count
        self._employee = employee
        self._end_date = end_date
        self._half_day_end = half_day_end
        self._half_day_start = half_day_start
        self._id = id
        self._start_date = start_date
        self._status = status
        self._time_off_type = time_off_type

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AbsencePeriodsResponseAllOfDataAttributes':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AbsencePeriodsResponse_allOf_data_attributes of this AbsencePeriodsResponseAllOfDataAttributes.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def certificate(self):
        """Gets the certificate of this AbsencePeriodsResponseAllOfDataAttributes.


        :return: The certificate of this AbsencePeriodsResponseAllOfDataAttributes.
        :rtype: AbsencePeriodsResponseAllOfDataCertificate
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this AbsencePeriodsResponseAllOfDataAttributes.


        :param certificate: The certificate of this AbsencePeriodsResponseAllOfDataAttributes.
        :type certificate: AbsencePeriodsResponseAllOfDataCertificate
        """

        self._certificate = certificate

    @property
    def created_at(self):
        """Gets the created_at of this AbsencePeriodsResponseAllOfDataAttributes.


        :return: The created_at of this AbsencePeriodsResponseAllOfDataAttributes.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this AbsencePeriodsResponseAllOfDataAttributes.


        :param created_at: The created_at of this AbsencePeriodsResponseAllOfDataAttributes.
        :type created_at: str
        """

        self._created_at = created_at

    @property
    def days_count(self):
        """Gets the days_count of this AbsencePeriodsResponseAllOfDataAttributes.


        :return: The days_count of this AbsencePeriodsResponseAllOfDataAttributes.
        :rtype: float
        """
        return self._days_count

    @days_count.setter
    def days_count(self, days_count):
        """Sets the days_count of this AbsencePeriodsResponseAllOfDataAttributes.


        :param days_count: The days_count of this AbsencePeriodsResponseAllOfDataAttributes.
        :type days_count: float
        """

        self._days_count = days_count

    @property
    def employee(self):
        """Gets the employee of this AbsencePeriodsResponseAllOfDataAttributes.


        :return: The employee of this AbsencePeriodsResponseAllOfDataAttributes.
        :rtype: AbsencePeriodsResponseAllOfDataEmployee
        """
        return self._employee

    @employee.setter
    def employee(self, employee):
        """Sets the employee of this AbsencePeriodsResponseAllOfDataAttributes.


        :param employee: The employee of this AbsencePeriodsResponseAllOfDataAttributes.
        :type employee: AbsencePeriodsResponseAllOfDataEmployee
        """

        self._employee = employee

    @property
    def end_date(self):
        """Gets the end_date of this AbsencePeriodsResponseAllOfDataAttributes.


        :return: The end_date of this AbsencePeriodsResponseAllOfDataAttributes.
        :rtype: str
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this AbsencePeriodsResponseAllOfDataAttributes.


        :param end_date: The end_date of this AbsencePeriodsResponseAllOfDataAttributes.
        :type end_date: str
        """

        self._end_date = end_date

    @property
    def half_day_end(self):
        """Gets the half_day_end of this AbsencePeriodsResponseAllOfDataAttributes.


        :return: The half_day_end of this AbsencePeriodsResponseAllOfDataAttributes.
        :rtype: float
        """
        return self._half_day_end

    @half_day_end.setter
    def half_day_end(self, half_day_end):
        """Sets the half_day_end of this AbsencePeriodsResponseAllOfDataAttributes.


        :param half_day_end: The half_day_end of this AbsencePeriodsResponseAllOfDataAttributes.
        :type half_day_end: float
        """

        self._half_day_end = half_day_end

    @property
    def half_day_start(self):
        """Gets the half_day_start of this AbsencePeriodsResponseAllOfDataAttributes.


        :return: The half_day_start of this AbsencePeriodsResponseAllOfDataAttributes.
        :rtype: float
        """
        return self._half_day_start

    @half_day_start.setter
    def half_day_start(self, half_day_start):
        """Sets the half_day_start of this AbsencePeriodsResponseAllOfDataAttributes.


        :param half_day_start: The half_day_start of this AbsencePeriodsResponseAllOfDataAttributes.
        :type half_day_start: float
        """

        self._half_day_start = half_day_start

    @property
    def id(self):
        """Gets the id of this AbsencePeriodsResponseAllOfDataAttributes.


        :return: The id of this AbsencePeriodsResponseAllOfDataAttributes.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AbsencePeriodsResponseAllOfDataAttributes.


        :param id: The id of this AbsencePeriodsResponseAllOfDataAttributes.
        :type id: int
        """

        self._id = id

    @property
    def start_date(self):
        """Gets the start_date of this AbsencePeriodsResponseAllOfDataAttributes.


        :return: The start_date of this AbsencePeriodsResponseAllOfDataAttributes.
        :rtype: str
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this AbsencePeriodsResponseAllOfDataAttributes.


        :param start_date: The start_date of this AbsencePeriodsResponseAllOfDataAttributes.
        :type start_date: str
        """

        self._start_date = start_date

    @property
    def status(self):
        """Gets the status of this AbsencePeriodsResponseAllOfDataAttributes.


        :return: The status of this AbsencePeriodsResponseAllOfDataAttributes.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this AbsencePeriodsResponseAllOfDataAttributes.


        :param status: The status of this AbsencePeriodsResponseAllOfDataAttributes.
        :type status: str
        """

        self._status = status

    @property
    def time_off_type(self):
        """Gets the time_off_type of this AbsencePeriodsResponseAllOfDataAttributes.


        :return: The time_off_type of this AbsencePeriodsResponseAllOfDataAttributes.
        :rtype: AbsencePeriodsResponseAllOfDataTimeOffType
        """
        return self._time_off_type

    @time_off_type.setter
    def time_off_type(self, time_off_type):
        """Sets the time_off_type of this AbsencePeriodsResponseAllOfDataAttributes.


        :param time_off_type: The time_off_type of this AbsencePeriodsResponseAllOfDataAttributes.
        :type time_off_type: AbsencePeriodsResponseAllOfDataTimeOffType
        """

        self._time_off_type = time_off_type
