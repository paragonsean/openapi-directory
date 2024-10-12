# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class UpdateProjectMember(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, budget_amount: float=None, cost_amount: float=None, fields_to_update: List[str]=None, project_idfk: int=None, rate_amount: float=None, user_idfk: int=None, can_comment_on_tasks: bool=None, can_create_tasks: bool=None, can_delete_tasks: bool=None, can_update_tasks: bool=None, is_timesheet_allowed: bool=None, is_timesheet_approval_required: bool=None, is_timesheet_approver: bool=None):
        """UpdateProjectMember - a model defined in OpenAPI

        :param budget_amount: The budget_amount of this UpdateProjectMember.
        :param cost_amount: The cost_amount of this UpdateProjectMember.
        :param fields_to_update: The fields_to_update of this UpdateProjectMember.
        :param project_idfk: The project_idfk of this UpdateProjectMember.
        :param rate_amount: The rate_amount of this UpdateProjectMember.
        :param user_idfk: The user_idfk of this UpdateProjectMember.
        :param can_comment_on_tasks: The can_comment_on_tasks of this UpdateProjectMember.
        :param can_create_tasks: The can_create_tasks of this UpdateProjectMember.
        :param can_delete_tasks: The can_delete_tasks of this UpdateProjectMember.
        :param can_update_tasks: The can_update_tasks of this UpdateProjectMember.
        :param is_timesheet_allowed: The is_timesheet_allowed of this UpdateProjectMember.
        :param is_timesheet_approval_required: The is_timesheet_approval_required of this UpdateProjectMember.
        :param is_timesheet_approver: The is_timesheet_approver of this UpdateProjectMember.
        """
        self.openapi_types = {
            'budget_amount': float,
            'cost_amount': float,
            'fields_to_update': List[str],
            'project_idfk': int,
            'rate_amount': float,
            'user_idfk': int,
            'can_comment_on_tasks': bool,
            'can_create_tasks': bool,
            'can_delete_tasks': bool,
            'can_update_tasks': bool,
            'is_timesheet_allowed': bool,
            'is_timesheet_approval_required': bool,
            'is_timesheet_approver': bool
        }

        self.attribute_map = {
            'budget_amount': 'BudgetAmount',
            'cost_amount': 'CostAmount',
            'fields_to_update': 'FieldsToUpdate',
            'project_idfk': 'ProjectIDFK',
            'rate_amount': 'RateAmount',
            'user_idfk': 'UserIDFK',
            'can_comment_on_tasks': 'canCommentOnTasks',
            'can_create_tasks': 'canCreateTasks',
            'can_delete_tasks': 'canDeleteTasks',
            'can_update_tasks': 'canUpdateTasks',
            'is_timesheet_allowed': 'isTimesheetAllowed',
            'is_timesheet_approval_required': 'isTimesheetApprovalRequired',
            'is_timesheet_approver': 'isTimesheetApprover'
        }

        self._budget_amount = budget_amount
        self._cost_amount = cost_amount
        self._fields_to_update = fields_to_update
        self._project_idfk = project_idfk
        self._rate_amount = rate_amount
        self._user_idfk = user_idfk
        self._can_comment_on_tasks = can_comment_on_tasks
        self._can_create_tasks = can_create_tasks
        self._can_delete_tasks = can_delete_tasks
        self._can_update_tasks = can_update_tasks
        self._is_timesheet_allowed = is_timesheet_allowed
        self._is_timesheet_approval_required = is_timesheet_approval_required
        self._is_timesheet_approver = is_timesheet_approver

    @classmethod
    def from_dict(cls, dikt: dict) -> 'UpdateProjectMember':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The UpdateProjectMember of this UpdateProjectMember.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def budget_amount(self):
        """Gets the budget_amount of this UpdateProjectMember.

        A new Budget Amount. Defaults to null.

        :return: The budget_amount of this UpdateProjectMember.
        :rtype: float
        """
        return self._budget_amount

    @budget_amount.setter
    def budget_amount(self, budget_amount):
        """Sets the budget_amount of this UpdateProjectMember.

        A new Budget Amount. Defaults to null.

        :param budget_amount: The budget_amount of this UpdateProjectMember.
        :type budget_amount: float
        """

        self._budget_amount = budget_amount

    @property
    def cost_amount(self):
        """Gets the cost_amount of this UpdateProjectMember.

        A new Cost Amount. Defaults to null.

        :return: The cost_amount of this UpdateProjectMember.
        :rtype: float
        """
        return self._cost_amount

    @cost_amount.setter
    def cost_amount(self, cost_amount):
        """Sets the cost_amount of this UpdateProjectMember.

        A new Cost Amount. Defaults to null.

        :param cost_amount: The cost_amount of this UpdateProjectMember.
        :type cost_amount: float
        """

        self._cost_amount = cost_amount

    @property
    def fields_to_update(self):
        """Gets the fields_to_update of this UpdateProjectMember.

        A string array of field names to be updated.

        :return: The fields_to_update of this UpdateProjectMember.
        :rtype: List[str]
        """
        return self._fields_to_update

    @fields_to_update.setter
    def fields_to_update(self, fields_to_update):
        """Sets the fields_to_update of this UpdateProjectMember.

        A string array of field names to be updated.

        :param fields_to_update: The fields_to_update of this UpdateProjectMember.
        :type fields_to_update: List[str]
        """
        if fields_to_update is None:
            raise ValueError("Invalid value for `fields_to_update`, must not be `None`")

        self._fields_to_update = fields_to_update

    @property
    def project_idfk(self):
        """Gets the project_idfk of this UpdateProjectMember.

        Required. The ProjectID

        :return: The project_idfk of this UpdateProjectMember.
        :rtype: int
        """
        return self._project_idfk

    @project_idfk.setter
    def project_idfk(self, project_idfk):
        """Sets the project_idfk of this UpdateProjectMember.

        Required. The ProjectID

        :param project_idfk: The project_idfk of this UpdateProjectMember.
        :type project_idfk: int
        """
        if project_idfk is None:
            raise ValueError("Invalid value for `project_idfk`, must not be `None`")

        self._project_idfk = project_idfk

    @property
    def rate_amount(self):
        """Gets the rate_amount of this UpdateProjectMember.

        A new Rate Amount. Defaults to null.

        :return: The rate_amount of this UpdateProjectMember.
        :rtype: float
        """
        return self._rate_amount

    @rate_amount.setter
    def rate_amount(self, rate_amount):
        """Sets the rate_amount of this UpdateProjectMember.

        A new Rate Amount. Defaults to null.

        :param rate_amount: The rate_amount of this UpdateProjectMember.
        :type rate_amount: float
        """

        self._rate_amount = rate_amount

    @property
    def user_idfk(self):
        """Gets the user_idfk of this UpdateProjectMember.

        Required. The UserID

        :return: The user_idfk of this UpdateProjectMember.
        :rtype: int
        """
        return self._user_idfk

    @user_idfk.setter
    def user_idfk(self, user_idfk):
        """Sets the user_idfk of this UpdateProjectMember.

        Required. The UserID

        :param user_idfk: The user_idfk of this UpdateProjectMember.
        :type user_idfk: int
        """
        if user_idfk is None:
            raise ValueError("Invalid value for `user_idfk`, must not be `None`")

        self._user_idfk = user_idfk

    @property
    def can_comment_on_tasks(self):
        """Gets the can_comment_on_tasks of this UpdateProjectMember.


        :return: The can_comment_on_tasks of this UpdateProjectMember.
        :rtype: bool
        """
        return self._can_comment_on_tasks

    @can_comment_on_tasks.setter
    def can_comment_on_tasks(self, can_comment_on_tasks):
        """Sets the can_comment_on_tasks of this UpdateProjectMember.


        :param can_comment_on_tasks: The can_comment_on_tasks of this UpdateProjectMember.
        :type can_comment_on_tasks: bool
        """

        self._can_comment_on_tasks = can_comment_on_tasks

    @property
    def can_create_tasks(self):
        """Gets the can_create_tasks of this UpdateProjectMember.


        :return: The can_create_tasks of this UpdateProjectMember.
        :rtype: bool
        """
        return self._can_create_tasks

    @can_create_tasks.setter
    def can_create_tasks(self, can_create_tasks):
        """Sets the can_create_tasks of this UpdateProjectMember.


        :param can_create_tasks: The can_create_tasks of this UpdateProjectMember.
        :type can_create_tasks: bool
        """

        self._can_create_tasks = can_create_tasks

    @property
    def can_delete_tasks(self):
        """Gets the can_delete_tasks of this UpdateProjectMember.


        :return: The can_delete_tasks of this UpdateProjectMember.
        :rtype: bool
        """
        return self._can_delete_tasks

    @can_delete_tasks.setter
    def can_delete_tasks(self, can_delete_tasks):
        """Sets the can_delete_tasks of this UpdateProjectMember.


        :param can_delete_tasks: The can_delete_tasks of this UpdateProjectMember.
        :type can_delete_tasks: bool
        """

        self._can_delete_tasks = can_delete_tasks

    @property
    def can_update_tasks(self):
        """Gets the can_update_tasks of this UpdateProjectMember.


        :return: The can_update_tasks of this UpdateProjectMember.
        :rtype: bool
        """
        return self._can_update_tasks

    @can_update_tasks.setter
    def can_update_tasks(self, can_update_tasks):
        """Sets the can_update_tasks of this UpdateProjectMember.


        :param can_update_tasks: The can_update_tasks of this UpdateProjectMember.
        :type can_update_tasks: bool
        """

        self._can_update_tasks = can_update_tasks

    @property
    def is_timesheet_allowed(self):
        """Gets the is_timesheet_allowed of this UpdateProjectMember.


        :return: The is_timesheet_allowed of this UpdateProjectMember.
        :rtype: bool
        """
        return self._is_timesheet_allowed

    @is_timesheet_allowed.setter
    def is_timesheet_allowed(self, is_timesheet_allowed):
        """Sets the is_timesheet_allowed of this UpdateProjectMember.


        :param is_timesheet_allowed: The is_timesheet_allowed of this UpdateProjectMember.
        :type is_timesheet_allowed: bool
        """

        self._is_timesheet_allowed = is_timesheet_allowed

    @property
    def is_timesheet_approval_required(self):
        """Gets the is_timesheet_approval_required of this UpdateProjectMember.


        :return: The is_timesheet_approval_required of this UpdateProjectMember.
        :rtype: bool
        """
        return self._is_timesheet_approval_required

    @is_timesheet_approval_required.setter
    def is_timesheet_approval_required(self, is_timesheet_approval_required):
        """Sets the is_timesheet_approval_required of this UpdateProjectMember.


        :param is_timesheet_approval_required: The is_timesheet_approval_required of this UpdateProjectMember.
        :type is_timesheet_approval_required: bool
        """

        self._is_timesheet_approval_required = is_timesheet_approval_required

    @property
    def is_timesheet_approver(self):
        """Gets the is_timesheet_approver of this UpdateProjectMember.


        :return: The is_timesheet_approver of this UpdateProjectMember.
        :rtype: bool
        """
        return self._is_timesheet_approver

    @is_timesheet_approver.setter
    def is_timesheet_approver(self, is_timesheet_approver):
        """Sets the is_timesheet_approver of this UpdateProjectMember.


        :param is_timesheet_approver: The is_timesheet_approver of this UpdateProjectMember.
        :type is_timesheet_approver: bool
        """

        self._is_timesheet_approver = is_timesheet_approver
