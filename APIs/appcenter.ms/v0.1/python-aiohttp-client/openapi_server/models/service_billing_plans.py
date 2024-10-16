# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.billing_aggregated_information_get_by_app200_response_billing_plans_build_service_current_billing_period import BillingAggregatedInformationGetByApp200ResponseBillingPlansBuildServiceCurrentBillingPeriod
from openapi_server import util


class ServiceBillingPlans(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, can_select_trial_plan: bool=None, current_billing_period: BillingAggregatedInformationGetByApp200ResponseBillingPlansBuildServiceCurrentBillingPeriod=None, last_trial_plan_expiration_time: str=None):
        """ServiceBillingPlans - a model defined in OpenAPI

        :param can_select_trial_plan: The can_select_trial_plan of this ServiceBillingPlans.
        :param current_billing_period: The current_billing_period of this ServiceBillingPlans.
        :param last_trial_plan_expiration_time: The last_trial_plan_expiration_time of this ServiceBillingPlans.
        """
        self.openapi_types = {
            'can_select_trial_plan': bool,
            'current_billing_period': BillingAggregatedInformationGetByApp200ResponseBillingPlansBuildServiceCurrentBillingPeriod,
            'last_trial_plan_expiration_time': str
        }

        self.attribute_map = {
            'can_select_trial_plan': 'canSelectTrialPlan',
            'current_billing_period': 'currentBillingPeriod',
            'last_trial_plan_expiration_time': 'lastTrialPlanExpirationTime'
        }

        self._can_select_trial_plan = can_select_trial_plan
        self._current_billing_period = current_billing_period
        self._last_trial_plan_expiration_time = last_trial_plan_expiration_time

    @classmethod
    def from_dict(cls, dikt: dict) -> 'ServiceBillingPlans':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The ServiceBillingPlans of this ServiceBillingPlans.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def can_select_trial_plan(self):
        """Gets the can_select_trial_plan of this ServiceBillingPlans.

        Can customer select trial plan for that service (if it exists)?

        :return: The can_select_trial_plan of this ServiceBillingPlans.
        :rtype: bool
        """
        return self._can_select_trial_plan

    @can_select_trial_plan.setter
    def can_select_trial_plan(self, can_select_trial_plan):
        """Sets the can_select_trial_plan of this ServiceBillingPlans.

        Can customer select trial plan for that service (if it exists)?

        :param can_select_trial_plan: The can_select_trial_plan of this ServiceBillingPlans.
        :type can_select_trial_plan: bool
        """

        self._can_select_trial_plan = can_select_trial_plan

    @property
    def current_billing_period(self):
        """Gets the current_billing_period of this ServiceBillingPlans.


        :return: The current_billing_period of this ServiceBillingPlans.
        :rtype: BillingAggregatedInformationGetByApp200ResponseBillingPlansBuildServiceCurrentBillingPeriod
        """
        return self._current_billing_period

    @current_billing_period.setter
    def current_billing_period(self, current_billing_period):
        """Sets the current_billing_period of this ServiceBillingPlans.


        :param current_billing_period: The current_billing_period of this ServiceBillingPlans.
        :type current_billing_period: BillingAggregatedInformationGetByApp200ResponseBillingPlansBuildServiceCurrentBillingPeriod
        """

        self._current_billing_period = current_billing_period

    @property
    def last_trial_plan_expiration_time(self):
        """Gets the last_trial_plan_expiration_time of this ServiceBillingPlans.

        Expiration time of the last selected trial plan. Will be null if trial plan was not used.

        :return: The last_trial_plan_expiration_time of this ServiceBillingPlans.
        :rtype: str
        """
        return self._last_trial_plan_expiration_time

    @last_trial_plan_expiration_time.setter
    def last_trial_plan_expiration_time(self, last_trial_plan_expiration_time):
        """Sets the last_trial_plan_expiration_time of this ServiceBillingPlans.

        Expiration time of the last selected trial plan. Will be null if trial plan was not used.

        :param last_trial_plan_expiration_time: The last_trial_plan_expiration_time of this ServiceBillingPlans.
        :type last_trial_plan_expiration_time: str
        """

        self._last_trial_plan_expiration_time = last_trial_plan_expiration_time
