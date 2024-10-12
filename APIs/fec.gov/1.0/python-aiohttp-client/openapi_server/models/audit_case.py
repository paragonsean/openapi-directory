# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.audit_case_category_relation import AuditCaseCategoryRelation
from openapi_server import util


class AuditCase(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, audit_case_id: str=None, audit_id: int=None, candidate_id: str=None, candidate_name: str=None, committee_description: str=None, committee_designation: str=None, committee_id: str=None, committee_name: str=None, committee_type: str=None, cycle: int=None, far_release_date: date=None, link_to_report: str=None, primary_category_list: List[AuditCaseCategoryRelation]=None):
        """AuditCase - a model defined in OpenAPI

        :param audit_case_id: The audit_case_id of this AuditCase.
        :param audit_id: The audit_id of this AuditCase.
        :param candidate_id: The candidate_id of this AuditCase.
        :param candidate_name: The candidate_name of this AuditCase.
        :param committee_description: The committee_description of this AuditCase.
        :param committee_designation: The committee_designation of this AuditCase.
        :param committee_id: The committee_id of this AuditCase.
        :param committee_name: The committee_name of this AuditCase.
        :param committee_type: The committee_type of this AuditCase.
        :param cycle: The cycle of this AuditCase.
        :param far_release_date: The far_release_date of this AuditCase.
        :param link_to_report: The link_to_report of this AuditCase.
        :param primary_category_list: The primary_category_list of this AuditCase.
        """
        self.openapi_types = {
            'audit_case_id': str,
            'audit_id': int,
            'candidate_id': str,
            'candidate_name': str,
            'committee_description': str,
            'committee_designation': str,
            'committee_id': str,
            'committee_name': str,
            'committee_type': str,
            'cycle': int,
            'far_release_date': date,
            'link_to_report': str,
            'primary_category_list': List[AuditCaseCategoryRelation]
        }

        self.attribute_map = {
            'audit_case_id': 'audit_case_id',
            'audit_id': 'audit_id',
            'candidate_id': 'candidate_id',
            'candidate_name': 'candidate_name',
            'committee_description': 'committee_description',
            'committee_designation': 'committee_designation',
            'committee_id': 'committee_id',
            'committee_name': 'committee_name',
            'committee_type': 'committee_type',
            'cycle': 'cycle',
            'far_release_date': 'far_release_date',
            'link_to_report': 'link_to_report',
            'primary_category_list': 'primary_category_list'
        }

        self._audit_case_id = audit_case_id
        self._audit_id = audit_id
        self._candidate_id = candidate_id
        self._candidate_name = candidate_name
        self._committee_description = committee_description
        self._committee_designation = committee_designation
        self._committee_id = committee_id
        self._committee_name = committee_name
        self._committee_type = committee_type
        self._cycle = cycle
        self._far_release_date = far_release_date
        self._link_to_report = link_to_report
        self._primary_category_list = primary_category_list

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AuditCase':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AuditCase of this AuditCase.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def audit_case_id(self):
        """Gets the audit_case_id of this AuditCase.


        :return: The audit_case_id of this AuditCase.
        :rtype: str
        """
        return self._audit_case_id

    @audit_case_id.setter
    def audit_case_id(self, audit_case_id):
        """Sets the audit_case_id of this AuditCase.


        :param audit_case_id: The audit_case_id of this AuditCase.
        :type audit_case_id: str
        """

        self._audit_case_id = audit_case_id

    @property
    def audit_id(self):
        """Gets the audit_id of this AuditCase.


        :return: The audit_id of this AuditCase.
        :rtype: int
        """
        return self._audit_id

    @audit_id.setter
    def audit_id(self, audit_id):
        """Sets the audit_id of this AuditCase.


        :param audit_id: The audit_id of this AuditCase.
        :type audit_id: int
        """

        self._audit_id = audit_id

    @property
    def candidate_id(self):
        """Gets the candidate_id of this AuditCase.


        :return: The candidate_id of this AuditCase.
        :rtype: str
        """
        return self._candidate_id

    @candidate_id.setter
    def candidate_id(self, candidate_id):
        """Sets the candidate_id of this AuditCase.


        :param candidate_id: The candidate_id of this AuditCase.
        :type candidate_id: str
        """

        self._candidate_id = candidate_id

    @property
    def candidate_name(self):
        """Gets the candidate_name of this AuditCase.


        :return: The candidate_name of this AuditCase.
        :rtype: str
        """
        return self._candidate_name

    @candidate_name.setter
    def candidate_name(self, candidate_name):
        """Sets the candidate_name of this AuditCase.


        :param candidate_name: The candidate_name of this AuditCase.
        :type candidate_name: str
        """

        self._candidate_name = candidate_name

    @property
    def committee_description(self):
        """Gets the committee_description of this AuditCase.


        :return: The committee_description of this AuditCase.
        :rtype: str
        """
        return self._committee_description

    @committee_description.setter
    def committee_description(self, committee_description):
        """Sets the committee_description of this AuditCase.


        :param committee_description: The committee_description of this AuditCase.
        :type committee_description: str
        """

        self._committee_description = committee_description

    @property
    def committee_designation(self):
        """Gets the committee_designation of this AuditCase.


        :return: The committee_designation of this AuditCase.
        :rtype: str
        """
        return self._committee_designation

    @committee_designation.setter
    def committee_designation(self, committee_designation):
        """Sets the committee_designation of this AuditCase.


        :param committee_designation: The committee_designation of this AuditCase.
        :type committee_designation: str
        """

        self._committee_designation = committee_designation

    @property
    def committee_id(self):
        """Gets the committee_id of this AuditCase.


        :return: The committee_id of this AuditCase.
        :rtype: str
        """
        return self._committee_id

    @committee_id.setter
    def committee_id(self, committee_id):
        """Sets the committee_id of this AuditCase.


        :param committee_id: The committee_id of this AuditCase.
        :type committee_id: str
        """

        self._committee_id = committee_id

    @property
    def committee_name(self):
        """Gets the committee_name of this AuditCase.


        :return: The committee_name of this AuditCase.
        :rtype: str
        """
        return self._committee_name

    @committee_name.setter
    def committee_name(self, committee_name):
        """Sets the committee_name of this AuditCase.


        :param committee_name: The committee_name of this AuditCase.
        :type committee_name: str
        """

        self._committee_name = committee_name

    @property
    def committee_type(self):
        """Gets the committee_type of this AuditCase.


        :return: The committee_type of this AuditCase.
        :rtype: str
        """
        return self._committee_type

    @committee_type.setter
    def committee_type(self, committee_type):
        """Sets the committee_type of this AuditCase.


        :param committee_type: The committee_type of this AuditCase.
        :type committee_type: str
        """

        self._committee_type = committee_type

    @property
    def cycle(self):
        """Gets the cycle of this AuditCase.


        :return: The cycle of this AuditCase.
        :rtype: int
        """
        return self._cycle

    @cycle.setter
    def cycle(self, cycle):
        """Sets the cycle of this AuditCase.


        :param cycle: The cycle of this AuditCase.
        :type cycle: int
        """

        self._cycle = cycle

    @property
    def far_release_date(self):
        """Gets the far_release_date of this AuditCase.


        :return: The far_release_date of this AuditCase.
        :rtype: date
        """
        return self._far_release_date

    @far_release_date.setter
    def far_release_date(self, far_release_date):
        """Sets the far_release_date of this AuditCase.


        :param far_release_date: The far_release_date of this AuditCase.
        :type far_release_date: date
        """

        self._far_release_date = far_release_date

    @property
    def link_to_report(self):
        """Gets the link_to_report of this AuditCase.

         URL for retrieving the PDF document 

        :return: The link_to_report of this AuditCase.
        :rtype: str
        """
        return self._link_to_report

    @link_to_report.setter
    def link_to_report(self, link_to_report):
        """Sets the link_to_report of this AuditCase.

         URL for retrieving the PDF document 

        :param link_to_report: The link_to_report of this AuditCase.
        :type link_to_report: str
        """

        self._link_to_report = link_to_report

    @property
    def primary_category_list(self):
        """Gets the primary_category_list of this AuditCase.


        :return: The primary_category_list of this AuditCase.
        :rtype: List[AuditCaseCategoryRelation]
        """
        return self._primary_category_list

    @primary_category_list.setter
    def primary_category_list(self, primary_category_list):
        """Sets the primary_category_list of this AuditCase.


        :param primary_category_list: The primary_category_list of this AuditCase.
        :type primary_category_list: List[AuditCaseCategoryRelation]
        """

        self._primary_category_list = primary_category_list
