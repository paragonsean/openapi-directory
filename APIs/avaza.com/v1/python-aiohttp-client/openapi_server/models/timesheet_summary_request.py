# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class TimesheetSummaryRequest(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, entry_date_from: datetime=None, entry_date_to: datetime=None, group_by: List[str]=None, project_id: int=None, user_id: List[int]=None, is_billable: bool=None, is_invoiced: bool=None):
        """TimesheetSummaryRequest - a model defined in OpenAPI

        :param entry_date_from: The entry_date_from of this TimesheetSummaryRequest.
        :param entry_date_to: The entry_date_to of this TimesheetSummaryRequest.
        :param group_by: The group_by of this TimesheetSummaryRequest.
        :param project_id: The project_id of this TimesheetSummaryRequest.
        :param user_id: The user_id of this TimesheetSummaryRequest.
        :param is_billable: The is_billable of this TimesheetSummaryRequest.
        :param is_invoiced: The is_invoiced of this TimesheetSummaryRequest.
        """
        self.openapi_types = {
            'entry_date_from': datetime,
            'entry_date_to': datetime,
            'group_by': List[str],
            'project_id': int,
            'user_id': List[int],
            'is_billable': bool,
            'is_invoiced': bool
        }

        self.attribute_map = {
            'entry_date_from': 'EntryDateFrom',
            'entry_date_to': 'EntryDateTo',
            'group_by': 'GroupBy',
            'project_id': 'ProjectID',
            'user_id': 'UserID',
            'is_billable': 'isBillable',
            'is_invoiced': 'isInvoiced'
        }

        self._entry_date_from = entry_date_from
        self._entry_date_to = entry_date_to
        self._group_by = group_by
        self._project_id = project_id
        self._user_id = user_id
        self._is_billable = is_billable
        self._is_invoiced = is_invoiced

    @classmethod
    def from_dict(cls, dikt: dict) -> 'TimesheetSummaryRequest':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The TimesheetSummaryRequest of this TimesheetSummaryRequest.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def entry_date_from(self):
        """Gets the entry_date_from of this TimesheetSummaryRequest.

        (Required) Filter for timesheets greater or equal to the specified date. e.g. 2019-01-25. You can optionally include a time component, otherwise it assumes 00:00

        :return: The entry_date_from of this TimesheetSummaryRequest.
        :rtype: datetime
        """
        return self._entry_date_from

    @entry_date_from.setter
    def entry_date_from(self, entry_date_from):
        """Sets the entry_date_from of this TimesheetSummaryRequest.

        (Required) Filter for timesheets greater or equal to the specified date. e.g. 2019-01-25. You can optionally include a time component, otherwise it assumes 00:00

        :param entry_date_from: The entry_date_from of this TimesheetSummaryRequest.
        :type entry_date_from: datetime
        """

        self._entry_date_from = entry_date_from

    @property
    def entry_date_to(self):
        """Gets the entry_date_to of this TimesheetSummaryRequest.

        (Required) Filter for timesheets with an entry date smaller or equal to the specified  date. e.g. 2019-01-25. You can optionally include a time component, otherwise it assumes 00:00

        :return: The entry_date_to of this TimesheetSummaryRequest.
        :rtype: datetime
        """
        return self._entry_date_to

    @entry_date_to.setter
    def entry_date_to(self, entry_date_to):
        """Sets the entry_date_to of this TimesheetSummaryRequest.

        (Required) Filter for timesheets with an entry date smaller or equal to the specified  date. e.g. 2019-01-25. You can optionally include a time component, otherwise it assumes 00:00

        :param entry_date_to: The entry_date_to of this TimesheetSummaryRequest.
        :type entry_date_to: datetime
        """

        self._entry_date_to = entry_date_to

    @property
    def group_by(self):
        """Gets the group_by of this TimesheetSummaryRequest.

        (Optional) Combine one, two or three levels of Grouping. Combine these possible grouping values: \"Customer\", \"Project\", \"Category\", \"User\", \"Task\", \"Year\", \"Month\", \"Day\", \"Week\".

        :return: The group_by of this TimesheetSummaryRequest.
        :rtype: List[str]
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        """Sets the group_by of this TimesheetSummaryRequest.

        (Optional) Combine one, two or three levels of Grouping. Combine these possible grouping values: \"Customer\", \"Project\", \"Category\", \"User\", \"Task\", \"Year\", \"Month\", \"Day\", \"Week\".

        :param group_by: The group_by of this TimesheetSummaryRequest.
        :type group_by: List[str]
        """

        self._group_by = group_by

    @property
    def project_id(self):
        """Gets the project_id of this TimesheetSummaryRequest.

        (Optional) Filter by Project

        :return: The project_id of this TimesheetSummaryRequest.
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TimesheetSummaryRequest.

        (Optional) Filter by Project

        :param project_id: The project_id of this TimesheetSummaryRequest.
        :type project_id: int
        """

        self._project_id = project_id

    @property
    def user_id(self):
        """Gets the user_id of this TimesheetSummaryRequest.

        (Optional) Defaults to the current user. Provide one or more UserIDs of Users whose timesheets should be retrieved. If the current user doesn't have impersonation rights, then they will only see their own data.

        :return: The user_id of this TimesheetSummaryRequest.
        :rtype: List[int]
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this TimesheetSummaryRequest.

        (Optional) Defaults to the current user. Provide one or more UserIDs of Users whose timesheets should be retrieved. If the current user doesn't have impersonation rights, then they will only see their own data.

        :param user_id: The user_id of this TimesheetSummaryRequest.
        :type user_id: List[int]
        """

        self._user_id = user_id

    @property
    def is_billable(self):
        """Gets the is_billable of this TimesheetSummaryRequest.

        (Optional) Filter by the billable status of Timesheets.

        :return: The is_billable of this TimesheetSummaryRequest.
        :rtype: bool
        """
        return self._is_billable

    @is_billable.setter
    def is_billable(self, is_billable):
        """Sets the is_billable of this TimesheetSummaryRequest.

        (Optional) Filter by the billable status of Timesheets.

        :param is_billable: The is_billable of this TimesheetSummaryRequest.
        :type is_billable: bool
        """

        self._is_billable = is_billable

    @property
    def is_invoiced(self):
        """Gets the is_invoiced of this TimesheetSummaryRequest.

        (Optional) Filter for timesheets by whether they have been Invoiced or not.

        :return: The is_invoiced of this TimesheetSummaryRequest.
        :rtype: bool
        """
        return self._is_invoiced

    @is_invoiced.setter
    def is_invoiced(self, is_invoiced):
        """Sets the is_invoiced of this TimesheetSummaryRequest.

        (Optional) Filter for timesheets by whether they have been Invoiced or not.

        :param is_invoiced: The is_invoiced of this TimesheetSummaryRequest.
        :type is_invoiced: bool
        """

        self._is_invoiced = is_invoiced
