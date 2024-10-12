# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server.models.environment_model_haljson_links import EnvironmentModelHaljsonLinks
from openapi_server.models.rollout_percentage_item_model import RolloutPercentageItemModel
from openapi_server.models.rollout_rule_model import RolloutRuleModel
from openapi_server.models.setting_value_model_haljson_embedded import SettingValueModelHaljsonEmbedded
from openapi_server import util


class SettingValueModelHaljson(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, embedded: SettingValueModelHaljsonEmbedded=None, links: EnvironmentModelHaljsonLinks=None, last_updater_user_email: str=None, last_updater_user_full_name: str=None, read_only: bool=None, rollout_percentage_items: List[RolloutPercentageItemModel]=None, rollout_rules: List[RolloutRuleModel]=None, updated_at: datetime=None, value: object=None):
        """SettingValueModelHaljson - a model defined in OpenAPI

        :param embedded: The embedded of this SettingValueModelHaljson.
        :param links: The links of this SettingValueModelHaljson.
        :param last_updater_user_email: The last_updater_user_email of this SettingValueModelHaljson.
        :param last_updater_user_full_name: The last_updater_user_full_name of this SettingValueModelHaljson.
        :param read_only: The read_only of this SettingValueModelHaljson.
        :param rollout_percentage_items: The rollout_percentage_items of this SettingValueModelHaljson.
        :param rollout_rules: The rollout_rules of this SettingValueModelHaljson.
        :param updated_at: The updated_at of this SettingValueModelHaljson.
        :param value: The value of this SettingValueModelHaljson.
        """
        self.openapi_types = {
            'embedded': SettingValueModelHaljsonEmbedded,
            'links': EnvironmentModelHaljsonLinks,
            'last_updater_user_email': str,
            'last_updater_user_full_name': str,
            'read_only': bool,
            'rollout_percentage_items': List[RolloutPercentageItemModel],
            'rollout_rules': List[RolloutRuleModel],
            'updated_at': datetime,
            'value': object
        }

        self.attribute_map = {
            'embedded': '_embedded',
            'links': '_links',
            'last_updater_user_email': 'lastUpdaterUserEmail',
            'last_updater_user_full_name': 'lastUpdaterUserFullName',
            'read_only': 'readOnly',
            'rollout_percentage_items': 'rolloutPercentageItems',
            'rollout_rules': 'rolloutRules',
            'updated_at': 'updatedAt',
            'value': 'value'
        }

        self._embedded = embedded
        self._links = links
        self._last_updater_user_email = last_updater_user_email
        self._last_updater_user_full_name = last_updater_user_full_name
        self._read_only = read_only
        self._rollout_percentage_items = rollout_percentage_items
        self._rollout_rules = rollout_rules
        self._updated_at = updated_at
        self._value = value

    @classmethod
    def from_dict(cls, dikt: dict) -> 'SettingValueModelHaljson':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The SettingValueModel-haljson of this SettingValueModelHaljson.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def embedded(self):
        """Gets the embedded of this SettingValueModelHaljson.


        :return: The embedded of this SettingValueModelHaljson.
        :rtype: SettingValueModelHaljsonEmbedded
        """
        return self._embedded

    @embedded.setter
    def embedded(self, embedded):
        """Sets the embedded of this SettingValueModelHaljson.


        :param embedded: The embedded of this SettingValueModelHaljson.
        :type embedded: SettingValueModelHaljsonEmbedded
        """

        self._embedded = embedded

    @property
    def links(self):
        """Gets the links of this SettingValueModelHaljson.


        :return: The links of this SettingValueModelHaljson.
        :rtype: EnvironmentModelHaljsonLinks
        """
        return self._links

    @links.setter
    def links(self, links):
        """Sets the links of this SettingValueModelHaljson.


        :param links: The links of this SettingValueModelHaljson.
        :type links: EnvironmentModelHaljsonLinks
        """

        self._links = links

    @property
    def last_updater_user_email(self):
        """Gets the last_updater_user_email of this SettingValueModelHaljson.


        :return: The last_updater_user_email of this SettingValueModelHaljson.
        :rtype: str
        """
        return self._last_updater_user_email

    @last_updater_user_email.setter
    def last_updater_user_email(self, last_updater_user_email):
        """Sets the last_updater_user_email of this SettingValueModelHaljson.


        :param last_updater_user_email: The last_updater_user_email of this SettingValueModelHaljson.
        :type last_updater_user_email: str
        """

        self._last_updater_user_email = last_updater_user_email

    @property
    def last_updater_user_full_name(self):
        """Gets the last_updater_user_full_name of this SettingValueModelHaljson.


        :return: The last_updater_user_full_name of this SettingValueModelHaljson.
        :rtype: str
        """
        return self._last_updater_user_full_name

    @last_updater_user_full_name.setter
    def last_updater_user_full_name(self, last_updater_user_full_name):
        """Sets the last_updater_user_full_name of this SettingValueModelHaljson.


        :param last_updater_user_full_name: The last_updater_user_full_name of this SettingValueModelHaljson.
        :type last_updater_user_full_name: str
        """

        self._last_updater_user_full_name = last_updater_user_full_name

    @property
    def read_only(self):
        """Gets the read_only of this SettingValueModelHaljson.


        :return: The read_only of this SettingValueModelHaljson.
        :rtype: bool
        """
        return self._read_only

    @read_only.setter
    def read_only(self, read_only):
        """Sets the read_only of this SettingValueModelHaljson.


        :param read_only: The read_only of this SettingValueModelHaljson.
        :type read_only: bool
        """

        self._read_only = read_only

    @property
    def rollout_percentage_items(self):
        """Gets the rollout_percentage_items of this SettingValueModelHaljson.

        The percentage rule collection.

        :return: The rollout_percentage_items of this SettingValueModelHaljson.
        :rtype: List[RolloutPercentageItemModel]
        """
        return self._rollout_percentage_items

    @rollout_percentage_items.setter
    def rollout_percentage_items(self, rollout_percentage_items):
        """Sets the rollout_percentage_items of this SettingValueModelHaljson.

        The percentage rule collection.

        :param rollout_percentage_items: The rollout_percentage_items of this SettingValueModelHaljson.
        :type rollout_percentage_items: List[RolloutPercentageItemModel]
        """

        self._rollout_percentage_items = rollout_percentage_items

    @property
    def rollout_rules(self):
        """Gets the rollout_rules of this SettingValueModelHaljson.

        The targeting rule collection.

        :return: The rollout_rules of this SettingValueModelHaljson.
        :rtype: List[RolloutRuleModel]
        """
        return self._rollout_rules

    @rollout_rules.setter
    def rollout_rules(self, rollout_rules):
        """Sets the rollout_rules of this SettingValueModelHaljson.

        The targeting rule collection.

        :param rollout_rules: The rollout_rules of this SettingValueModelHaljson.
        :type rollout_rules: List[RolloutRuleModel]
        """

        self._rollout_rules = rollout_rules

    @property
    def updated_at(self):
        """Gets the updated_at of this SettingValueModelHaljson.


        :return: The updated_at of this SettingValueModelHaljson.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this SettingValueModelHaljson.


        :param updated_at: The updated_at of this SettingValueModelHaljson.
        :type updated_at: datetime
        """

        self._updated_at = updated_at

    @property
    def value(self):
        """Gets the value of this SettingValueModelHaljson.

        The value to serve. It must respect the setting type.

        :return: The value of this SettingValueModelHaljson.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this SettingValueModelHaljson.

        The value to serve. It must respect the setting type.

        :param value: The value of this SettingValueModelHaljson.
        :type value: object
        """

        self._value = value
