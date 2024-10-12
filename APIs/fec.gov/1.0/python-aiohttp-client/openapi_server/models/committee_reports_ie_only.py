# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class CommitteeReportsIEOnly(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, beginning_image_number: str=None, committee_id: str=None, committee_name: str=None, committee_type: str=None, coverage_end_date: datetime=None, coverage_start_date: datetime=None, csv_url: str=None, cycle: int=None, document_description: str=None, end_image_number: str=None, fec_file_id: str=None, fec_url: str=None, independent_contributions_period: float=None, independent_expenditures_period: float=None, is_amended: bool=None, means_filed: str=None, pdf_url: str=None, receipt_date: date=None, report_form: str=None, report_type: str=None, report_type_full: str=None, report_year: int=None):
        """CommitteeReportsIEOnly - a model defined in OpenAPI

        :param beginning_image_number: The beginning_image_number of this CommitteeReportsIEOnly.
        :param committee_id: The committee_id of this CommitteeReportsIEOnly.
        :param committee_name: The committee_name of this CommitteeReportsIEOnly.
        :param committee_type: The committee_type of this CommitteeReportsIEOnly.
        :param coverage_end_date: The coverage_end_date of this CommitteeReportsIEOnly.
        :param coverage_start_date: The coverage_start_date of this CommitteeReportsIEOnly.
        :param csv_url: The csv_url of this CommitteeReportsIEOnly.
        :param cycle: The cycle of this CommitteeReportsIEOnly.
        :param document_description: The document_description of this CommitteeReportsIEOnly.
        :param end_image_number: The end_image_number of this CommitteeReportsIEOnly.
        :param fec_file_id: The fec_file_id of this CommitteeReportsIEOnly.
        :param fec_url: The fec_url of this CommitteeReportsIEOnly.
        :param independent_contributions_period: The independent_contributions_period of this CommitteeReportsIEOnly.
        :param independent_expenditures_period: The independent_expenditures_period of this CommitteeReportsIEOnly.
        :param is_amended: The is_amended of this CommitteeReportsIEOnly.
        :param means_filed: The means_filed of this CommitteeReportsIEOnly.
        :param pdf_url: The pdf_url of this CommitteeReportsIEOnly.
        :param receipt_date: The receipt_date of this CommitteeReportsIEOnly.
        :param report_form: The report_form of this CommitteeReportsIEOnly.
        :param report_type: The report_type of this CommitteeReportsIEOnly.
        :param report_type_full: The report_type_full of this CommitteeReportsIEOnly.
        :param report_year: The report_year of this CommitteeReportsIEOnly.
        """
        self.openapi_types = {
            'beginning_image_number': str,
            'committee_id': str,
            'committee_name': str,
            'committee_type': str,
            'coverage_end_date': datetime,
            'coverage_start_date': datetime,
            'csv_url': str,
            'cycle': int,
            'document_description': str,
            'end_image_number': str,
            'fec_file_id': str,
            'fec_url': str,
            'independent_contributions_period': float,
            'independent_expenditures_period': float,
            'is_amended': bool,
            'means_filed': str,
            'pdf_url': str,
            'receipt_date': date,
            'report_form': str,
            'report_type': str,
            'report_type_full': str,
            'report_year': int
        }

        self.attribute_map = {
            'beginning_image_number': 'beginning_image_number',
            'committee_id': 'committee_id',
            'committee_name': 'committee_name',
            'committee_type': 'committee_type',
            'coverage_end_date': 'coverage_end_date',
            'coverage_start_date': 'coverage_start_date',
            'csv_url': 'csv_url',
            'cycle': 'cycle',
            'document_description': 'document_description',
            'end_image_number': 'end_image_number',
            'fec_file_id': 'fec_file_id',
            'fec_url': 'fec_url',
            'independent_contributions_period': 'independent_contributions_period',
            'independent_expenditures_period': 'independent_expenditures_period',
            'is_amended': 'is_amended',
            'means_filed': 'means_filed',
            'pdf_url': 'pdf_url',
            'receipt_date': 'receipt_date',
            'report_form': 'report_form',
            'report_type': 'report_type',
            'report_type_full': 'report_type_full',
            'report_year': 'report_year'
        }

        self._beginning_image_number = beginning_image_number
        self._committee_id = committee_id
        self._committee_name = committee_name
        self._committee_type = committee_type
        self._coverage_end_date = coverage_end_date
        self._coverage_start_date = coverage_start_date
        self._csv_url = csv_url
        self._cycle = cycle
        self._document_description = document_description
        self._end_image_number = end_image_number
        self._fec_file_id = fec_file_id
        self._fec_url = fec_url
        self._independent_contributions_period = independent_contributions_period
        self._independent_expenditures_period = independent_expenditures_period
        self._is_amended = is_amended
        self._means_filed = means_filed
        self._pdf_url = pdf_url
        self._receipt_date = receipt_date
        self._report_form = report_form
        self._report_type = report_type
        self._report_type_full = report_type_full
        self._report_year = report_year

    @classmethod
    def from_dict(cls, dikt: dict) -> 'CommitteeReportsIEOnly':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The CommitteeReportsIEOnly of this CommitteeReportsIEOnly.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def beginning_image_number(self):
        """Gets the beginning_image_number of this CommitteeReportsIEOnly.


        :return: The beginning_image_number of this CommitteeReportsIEOnly.
        :rtype: str
        """
        return self._beginning_image_number

    @beginning_image_number.setter
    def beginning_image_number(self, beginning_image_number):
        """Sets the beginning_image_number of this CommitteeReportsIEOnly.


        :param beginning_image_number: The beginning_image_number of this CommitteeReportsIEOnly.
        :type beginning_image_number: str
        """

        self._beginning_image_number = beginning_image_number

    @property
    def committee_id(self):
        """Gets the committee_id of this CommitteeReportsIEOnly.


        :return: The committee_id of this CommitteeReportsIEOnly.
        :rtype: str
        """
        return self._committee_id

    @committee_id.setter
    def committee_id(self, committee_id):
        """Sets the committee_id of this CommitteeReportsIEOnly.


        :param committee_id: The committee_id of this CommitteeReportsIEOnly.
        :type committee_id: str
        """

        self._committee_id = committee_id

    @property
    def committee_name(self):
        """Gets the committee_name of this CommitteeReportsIEOnly.


        :return: The committee_name of this CommitteeReportsIEOnly.
        :rtype: str
        """
        return self._committee_name

    @committee_name.setter
    def committee_name(self, committee_name):
        """Sets the committee_name of this CommitteeReportsIEOnly.


        :param committee_name: The committee_name of this CommitteeReportsIEOnly.
        :type committee_name: str
        """

        self._committee_name = committee_name

    @property
    def committee_type(self):
        """Gets the committee_type of this CommitteeReportsIEOnly.


        :return: The committee_type of this CommitteeReportsIEOnly.
        :rtype: str
        """
        return self._committee_type

    @committee_type.setter
    def committee_type(self, committee_type):
        """Sets the committee_type of this CommitteeReportsIEOnly.


        :param committee_type: The committee_type of this CommitteeReportsIEOnly.
        :type committee_type: str
        """

        self._committee_type = committee_type

    @property
    def coverage_end_date(self):
        """Gets the coverage_end_date of this CommitteeReportsIEOnly.


        :return: The coverage_end_date of this CommitteeReportsIEOnly.
        :rtype: datetime
        """
        return self._coverage_end_date

    @coverage_end_date.setter
    def coverage_end_date(self, coverage_end_date):
        """Sets the coverage_end_date of this CommitteeReportsIEOnly.


        :param coverage_end_date: The coverage_end_date of this CommitteeReportsIEOnly.
        :type coverage_end_date: datetime
        """

        self._coverage_end_date = coverage_end_date

    @property
    def coverage_start_date(self):
        """Gets the coverage_start_date of this CommitteeReportsIEOnly.


        :return: The coverage_start_date of this CommitteeReportsIEOnly.
        :rtype: datetime
        """
        return self._coverage_start_date

    @coverage_start_date.setter
    def coverage_start_date(self, coverage_start_date):
        """Sets the coverage_start_date of this CommitteeReportsIEOnly.


        :param coverage_start_date: The coverage_start_date of this CommitteeReportsIEOnly.
        :type coverage_start_date: datetime
        """

        self._coverage_start_date = coverage_start_date

    @property
    def csv_url(self):
        """Gets the csv_url of this CommitteeReportsIEOnly.


        :return: The csv_url of this CommitteeReportsIEOnly.
        :rtype: str
        """
        return self._csv_url

    @csv_url.setter
    def csv_url(self, csv_url):
        """Sets the csv_url of this CommitteeReportsIEOnly.


        :param csv_url: The csv_url of this CommitteeReportsIEOnly.
        :type csv_url: str
        """

        self._csv_url = csv_url

    @property
    def cycle(self):
        """Gets the cycle of this CommitteeReportsIEOnly.


        :return: The cycle of this CommitteeReportsIEOnly.
        :rtype: int
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this CommitteeReportsIEOnly.


        :param cycle: The cycle of this CommitteeReportsIEOnly.
        :type cycle: int
        """

        self._cycle = cycle

    @property
    def document_description(self):
        """Gets the document_description of this CommitteeReportsIEOnly.


        :return: The document_description of this CommitteeReportsIEOnly.
        :rtype: str
        """
        return self._document_description

    @document_description.setter
    def document_description(self, document_description):
        """Sets the document_description of this CommitteeReportsIEOnly.


        :param document_description: The document_description of this CommitteeReportsIEOnly.
        :type document_description: str
        """

        self._document_description = document_description

    @property
    def end_image_number(self):
        """Gets the end_image_number of this CommitteeReportsIEOnly.


        :return: The end_image_number of this CommitteeReportsIEOnly.
        :rtype: str
        """
        return self._end_image_number

    @end_image_number.setter
    def end_image_number(self, end_image_number):
        """Sets the end_image_number of this CommitteeReportsIEOnly.


        :param end_image_number: The end_image_number of this CommitteeReportsIEOnly.
        :type end_image_number: str
        """

        self._end_image_number = end_image_number

    @property
    def fec_file_id(self):
        """Gets the fec_file_id of this CommitteeReportsIEOnly.


        :return: The fec_file_id of this CommitteeReportsIEOnly.
        :rtype: str
        """
        return self._fec_file_id

    @fec_file_id.setter
    def fec_file_id(self, fec_file_id):
        """Sets the fec_file_id of this CommitteeReportsIEOnly.


        :param fec_file_id: The fec_file_id of this CommitteeReportsIEOnly.
        :type fec_file_id: str
        """

        self._fec_file_id = fec_file_id

    @property
    def fec_url(self):
        """Gets the fec_url of this CommitteeReportsIEOnly.


        :return: The fec_url of this CommitteeReportsIEOnly.
        :rtype: str
        """
        return self._fec_url

    @fec_url.setter
    def fec_url(self, fec_url):
        """Sets the fec_url of this CommitteeReportsIEOnly.


        :param fec_url: The fec_url of this CommitteeReportsIEOnly.
        :type fec_url: str
        """

        self._fec_url = fec_url

    @property
    def independent_contributions_period(self):
        """Gets the independent_contributions_period of this CommitteeReportsIEOnly.


        :return: The independent_contributions_period of this CommitteeReportsIEOnly.
        :rtype: float
        """
        return self._independent_contributions_period

    @independent_contributions_period.setter
    def independent_contributions_period(self, independent_contributions_period):
        """Sets the independent_contributions_period of this CommitteeReportsIEOnly.


        :param independent_contributions_period: The independent_contributions_period of this CommitteeReportsIEOnly.
        :type independent_contributions_period: float
        """

        self._independent_contributions_period = independent_contributions_period

    @property
    def independent_expenditures_period(self):
        """Gets the independent_expenditures_period of this CommitteeReportsIEOnly.


        :return: The independent_expenditures_period of this CommitteeReportsIEOnly.
        :rtype: float
        """
        return self._independent_expenditures_period

    @independent_expenditures_period.setter
    def independent_expenditures_period(self, independent_expenditures_period):
        """Sets the independent_expenditures_period of this CommitteeReportsIEOnly.


        :param independent_expenditures_period: The independent_expenditures_period of this CommitteeReportsIEOnly.
        :type independent_expenditures_period: float
        """

        self._independent_expenditures_period = independent_expenditures_period

    @property
    def is_amended(self):
        """Gets the is_amended of this CommitteeReportsIEOnly.

         False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment. 

        :return: The is_amended of this CommitteeReportsIEOnly.
        :rtype: bool
        """
        return self._is_amended

    @is_amended.setter
    def is_amended(self, is_amended):
        """Sets the is_amended of this CommitteeReportsIEOnly.

         False indicates that a report is the most recent. True indicates that the report has been superseded by an amendment. 

        :param is_amended: The is_amended of this CommitteeReportsIEOnly.
        :type is_amended: bool
        """

        self._is_amended = is_amended

    @property
    def means_filed(self):
        """Gets the means_filed of this CommitteeReportsIEOnly.

        The method used to file with the FEC, either electronic or on paper.

        :return: The means_filed of this CommitteeReportsIEOnly.
        :rtype: str
        """
        return self._means_filed

    @means_filed.setter
    def means_filed(self, means_filed):
        """Sets the means_filed of this CommitteeReportsIEOnly.

        The method used to file with the FEC, either electronic or on paper.

        :param means_filed: The means_filed of this CommitteeReportsIEOnly.
        :type means_filed: str
        """

        self._means_filed = means_filed

    @property
    def pdf_url(self):
        """Gets the pdf_url of this CommitteeReportsIEOnly.


        :return: The pdf_url of this CommitteeReportsIEOnly.
        :rtype: str
        """
        return self._pdf_url

    @pdf_url.setter
    def pdf_url(self, pdf_url):
        """Sets the pdf_url of this CommitteeReportsIEOnly.


        :param pdf_url: The pdf_url of this CommitteeReportsIEOnly.
        :type pdf_url: str
        """

        self._pdf_url = pdf_url

    @property
    def receipt_date(self):
        """Gets the receipt_date of this CommitteeReportsIEOnly.

        Date the FEC received the electronic or paper record

        :return: The receipt_date of this CommitteeReportsIEOnly.
        :rtype: date
        """
        return self._receipt_date

    @receipt_date.setter
    def receipt_date(self, receipt_date):
        """Sets the receipt_date of this CommitteeReportsIEOnly.

        Date the FEC received the electronic or paper record

        :param receipt_date: The receipt_date of this CommitteeReportsIEOnly.
        :type receipt_date: date
        """

        self._receipt_date = receipt_date

    @property
    def report_form(self):
        """Gets the report_form of this CommitteeReportsIEOnly.


        :return: The report_form of this CommitteeReportsIEOnly.
        :rtype: str
        """
        return self._report_form

    @report_form.setter
    def report_form(self, report_form):
        """Sets the report_form of this CommitteeReportsIEOnly.


        :param report_form: The report_form of this CommitteeReportsIEOnly.
        :type report_form: str
        """

        self._report_form = report_form

    @property
    def report_type(self):
        """Gets the report_type of this CommitteeReportsIEOnly.


        :return: The report_type of this CommitteeReportsIEOnly.
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this CommitteeReportsIEOnly.


        :param report_type: The report_type of this CommitteeReportsIEOnly.
        :type report_type: str
        """

        self._report_type = report_type

    @property
    def report_type_full(self):
        """Gets the report_type_full of this CommitteeReportsIEOnly.


        :return: The report_type_full of this CommitteeReportsIEOnly.
        :rtype: str
        """
        return self._report_type_full

    @report_type_full.setter
    def report_type_full(self, report_type_full):
        """Sets the report_type_full of this CommitteeReportsIEOnly.


        :param report_type_full: The report_type_full of this CommitteeReportsIEOnly.
        :type report_type_full: str
        """

        self._report_type_full = report_type_full

    @property
    def report_year(self):
        """Gets the report_year of this CommitteeReportsIEOnly.


        :return: The report_year of this CommitteeReportsIEOnly.
        :rtype: int
        """
        return self._report_year

    @report_year.setter
    def report_year(self, report_year):
        """Sets the report_year of this CommitteeReportsIEOnly.


        :param report_year: The report_year of this CommitteeReportsIEOnly.
        :type report_year: int
        """

        self._report_year = report_year
