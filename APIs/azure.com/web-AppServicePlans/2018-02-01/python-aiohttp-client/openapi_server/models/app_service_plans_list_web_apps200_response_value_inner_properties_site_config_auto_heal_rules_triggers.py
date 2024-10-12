# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_auto_heal_rules_triggers_requests import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_auto_heal_rules_triggers_slow_requests import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersSlowRequests
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_auto_heal_rules_triggers_status_codes_inner import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner
from openapi_server import util


class AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, private_bytes_in_kb: int=None, requests: AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests=None, slow_requests: AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersSlowRequests=None, status_codes: List[AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner]=None):
        """AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers - a model defined in OpenAPI

        :param private_bytes_in_kb: The private_bytes_in_kb of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.
        :param requests: The requests of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.
        :param slow_requests: The slow_requests of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.
        :param status_codes: The status_codes of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.
        """
        self.openapi_types = {
            'private_bytes_in_kb': int,
            'requests': AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests,
            'slow_requests': AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersSlowRequests,
            'status_codes': List[AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner]
        }

        self.attribute_map = {
            'private_bytes_in_kb': 'privateBytesInKB',
            'requests': 'requests',
            'slow_requests': 'slowRequests',
            'status_codes': 'statusCodes'
        }

        self._private_bytes_in_kb = private_bytes_in_kb
        self._requests = requests
        self._slow_requests = slow_requests
        self._status_codes = status_codes

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AppServicePlans_ListWebApps_200_response_value_inner_properties_siteConfig_autoHealRules_triggers of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def private_bytes_in_kb(self):
        """Gets the private_bytes_in_kb of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.

        A rule based on private bytes.

        :return: The private_bytes_in_kb of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.
        :rtype: int
        """
        return self._private_bytes_in_kb

    @private_bytes_in_kb.setter
    def private_bytes_in_kb(self, private_bytes_in_kb):
        """Sets the private_bytes_in_kb of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.

        A rule based on private bytes.

        :param private_bytes_in_kb: The private_bytes_in_kb of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.
        :type private_bytes_in_kb: int
        """

        self._private_bytes_in_kb = private_bytes_in_kb

    @property
    def requests(self):
        """Gets the requests of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.


        :return: The requests of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.
        :rtype: AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests
        """
        return self._requests

    @requests.setter
    def requests(self, requests):
        """Sets the requests of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.


        :param requests: The requests of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.
        :type requests: AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests
        """

        self._requests = requests

    @property
    def slow_requests(self):
        """Gets the slow_requests of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.


        :return: The slow_requests of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.
        :rtype: AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersSlowRequests
        """
        return self._slow_requests

    @slow_requests.setter
    def slow_requests(self, slow_requests):
        """Sets the slow_requests of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.


        :param slow_requests: The slow_requests of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.
        :type slow_requests: AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersSlowRequests
        """

        self._slow_requests = slow_requests

    @property
    def status_codes(self):
        """Gets the status_codes of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.

        A rule based on status codes.

        :return: The status_codes of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.
        :rtype: List[AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner]
        """
        return self._status_codes

    @status_codes.setter
    def status_codes(self, status_codes):
        """Sets the status_codes of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.

        A rule based on status codes.

        :param status_codes: The status_codes of this AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers.
        :type status_codes: List[AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner]
        """

        self._status_codes = status_codes
