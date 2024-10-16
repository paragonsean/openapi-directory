# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.reconciliation_report_validation_issue import ReconciliationReportValidationIssue
from openapi_server import util


class ValidateReconciliationReportResponse(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, issues: List[ReconciliationReportValidationIssue]=None, successful_record_count: int=None):
        """ValidateReconciliationReportResponse - a model defined in OpenAPI

        :param issues: The issues of this ValidateReconciliationReportResponse.
        :param successful_record_count: The successful_record_count of this ValidateReconciliationReportResponse.
        """
        self.openapi_types = {
            'issues': List[ReconciliationReportValidationIssue],
            'successful_record_count': int
        }

        self.attribute_map = {
            'issues': 'issues',
            'successful_record_count': 'successfulRecordCount'
        }

        self._issues = issues
        self._successful_record_count = successful_record_count

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ValidateReconciliationReportResponse':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ValidateReconciliationReportResponse of this ValidateReconciliationReportResponse.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def issues(self):
        """Gets the issues of this ValidateReconciliationReportResponse.

        Issues that were encountered when validating the file.

        :return: The issues of this ValidateReconciliationReportResponse.
        :rtype: List[ReconciliationReportValidationIssue]
        """
        return self._issues

    @issues.setter
    def issues(self, issues):
        """Sets the issues of this ValidateReconciliationReportResponse.

        Issues that were encountered when validating the file.

        :param issues: The issues of this ValidateReconciliationReportResponse.
        :type issues: List[ReconciliationReportValidationIssue]
        """

        self._issues = issues

    @property
    def successful_record_count(self):
        """Gets the successful_record_count of this ValidateReconciliationReportResponse.

        The number of commission records that were successfully validated.

        :return: The successful_record_count of this ValidateReconciliationReportResponse.
        :rtype: int
        """
        return self._successful_record_count

    @successful_record_count.setter
    def successful_record_count(self, successful_record_count):
        """Sets the successful_record_count of this ValidateReconciliationReportResponse.

        The number of commission records that were successfully validated.

        :param successful_record_count: The successful_record_count of this ValidateReconciliationReportResponse.
        :type successful_record_count: int
        """

        self._successful_record_count = successful_record_count
