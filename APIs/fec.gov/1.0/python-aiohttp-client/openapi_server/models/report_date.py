# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class ReportDate(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, create_date: date=None, due_date: date=None, report_type: str=None, report_type_full: str=None, report_year: int=None, update_date: date=None):
        """ReportDate - a model defined in OpenAPI

        :param create_date: The create_date of this ReportDate.
        :param due_date: The due_date of this ReportDate.
        :param report_type: The report_type of this ReportDate.
        :param report_type_full: The report_type_full of this ReportDate.
        :param report_year: The report_year of this ReportDate.
        :param update_date: The update_date of this ReportDate.
        """
        self.openapi_types = {
            'create_date': date,
            'due_date': date,
            'report_type': str,
            'report_type_full': str,
            'report_year': int,
            'update_date': date
        }

        self.attribute_map = {
            'create_date': 'create_date',
            'due_date': 'due_date',
            'report_type': 'report_type',
            'report_type_full': 'report_type_full',
            'report_year': 'report_year',
            'update_date': 'update_date'
        }

        self._create_date = create_date
        self._due_date = due_date
        self._report_type = report_type
        self._report_type_full = report_type_full
        self._report_year = report_year
        self._update_date = update_date

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ReportDate':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ReportDate of this ReportDate.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def create_date(self):
        """Gets the create_date of this ReportDate.

        Date the record was created

        :return: The create_date of this ReportDate.
        :rtype: date
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this ReportDate.

        Date the record was created

        :param create_date: The create_date of this ReportDate.
        :type create_date: date
        """

        self._create_date = create_date

    @property
    def due_date(self):
        """Gets the due_date of this ReportDate.

        Date the report is due

        :return: The due_date of this ReportDate.
        :rtype: date
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this ReportDate.

        Date the report is due

        :param due_date: The due_date of this ReportDate.
        :type due_date: date
        """

        self._due_date = due_date

    @property
    def report_type(self):
        """Gets the report_type of this ReportDate.


        :return: The report_type of this ReportDate.
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this ReportDate.


        :param report_type: The report_type of this ReportDate.
        :type report_type: str
        """

        self._report_type = report_type

    @property
    def report_type_full(self):
        """Gets the report_type_full of this ReportDate.


        :return: The report_type_full of this ReportDate.
        :rtype: str
        """
        return self._report_type_full

    @report_type_full.setter
    def report_type_full(self, report_type_full):
        """Sets the report_type_full of this ReportDate.


        :param report_type_full: The report_type_full of this ReportDate.
        :type report_type_full: str
        """

        self._report_type_full = report_type_full

    @property
    def report_year(self):
        """Gets the report_year of this ReportDate.

         Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date. 

        :return: The report_year of this ReportDate.
        :rtype: int
        """
        return self._report_year

    @report_year.setter
    def report_year(self, report_year):
        """Sets the report_year of this ReportDate.

         Forms with coverage date -      year from the coverage ending date. Forms without coverage date -      year from the receipt date. 

        :param report_year: The report_year of this ReportDate.
        :type report_year: int
        """

        self._report_year = report_year

    @property
    def update_date(self):
        """Gets the update_date of this ReportDate.

        Date the record was updated

        :return: The update_date of this ReportDate.
        :rtype: date
        """
        return self._update_date

    @update_date.setter
    def update_date(self, update_date):
        """Sets the update_date of this ReportDate.

        Date the record was updated

        :param update_date: The update_date of this ReportDate.
        :type update_date: date
        """

        self._update_date = update_date
