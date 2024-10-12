# coding: utf-8

from datetime import date, datetime

from typing import List, Dict, Type

from openapi_server.models.base_model import Model
from openapi_server import util


class AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, app_settings_overrides: Dict[str, str]=None, clone_custom_host_names: bool=None, clone_source_control: bool=None, configure_load_balancing: bool=None, correlation_id: str=None, hosting_environment: str=None, overwrite: bool=None, source_web_app_id: str=None, source_web_app_location: str=None, traffic_manager_profile_id: str=None, traffic_manager_profile_name: str=None):
        """AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo - a model defined in OpenAPI

        :param app_settings_overrides: The app_settings_overrides of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :param clone_custom_host_names: The clone_custom_host_names of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :param clone_source_control: The clone_source_control of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :param configure_load_balancing: The configure_load_balancing of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :param correlation_id: The correlation_id of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :param hosting_environment: The hosting_environment of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :param overwrite: The overwrite of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :param source_web_app_id: The source_web_app_id of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :param source_web_app_location: The source_web_app_location of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :param traffic_manager_profile_id: The traffic_manager_profile_id of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :param traffic_manager_profile_name: The traffic_manager_profile_name of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        """
        self.openapi_types = {
            'app_settings_overrides': Dict[str, str],
            'clone_custom_host_names': bool,
            'clone_source_control': bool,
            'configure_load_balancing': bool,
            'correlation_id': str,
            'hosting_environment': str,
            'overwrite': bool,
            'source_web_app_id': str,
            'source_web_app_location': str,
            'traffic_manager_profile_id': str,
            'traffic_manager_profile_name': str
        }

        self.attribute_map = {
            'app_settings_overrides': 'appSettingsOverrides',
            'clone_custom_host_names': 'cloneCustomHostNames',
            'clone_source_control': 'cloneSourceControl',
            'configure_load_balancing': 'configureLoadBalancing',
            'correlation_id': 'correlationId',
            'hosting_environment': 'hostingEnvironment',
            'overwrite': 'overwrite',
            'source_web_app_id': 'sourceWebAppId',
            'source_web_app_location': 'sourceWebAppLocation',
            'traffic_manager_profile_id': 'trafficManagerProfileId',
            'traffic_manager_profile_name': 'trafficManagerProfileName'
        }

        self._app_settings_overrides = app_settings_overrides
        self._clone_custom_host_names = clone_custom_host_names
        self._clone_source_control = clone_source_control
        self._configure_load_balancing = configure_load_balancing
        self._correlation_id = correlation_id
        self._hosting_environment = hosting_environment
        self._overwrite = overwrite
        self._source_web_app_id = source_web_app_id
        self._source_web_app_location = source_web_app_location
        self._traffic_manager_profile_id = traffic_manager_profile_id
        self._traffic_manager_profile_name = traffic_manager_profile_name

    @classmethod
    def from_dict(cls, dikt: dict) -> 'AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo':
        """Returns the dict as a model

        :param dikt: A dict.
        :return: The AppServicePlans_ListWebApps_200_response_value_inner_properties_cloningInfo of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        """
        return util.deserialize_model(dikt, cls)

    @property
    def app_settings_overrides(self):
        """Gets the app_settings_overrides of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        Application setting overrides for cloned app. If specified, these settings override the settings cloned  from source app. Otherwise, application settings from source app are retained.

        :return: The app_settings_overrides of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :rtype: Dict[str, str]
        """
        return self._app_settings_overrides

    @app_settings_overrides.setter
    def app_settings_overrides(self, app_settings_overrides):
        """Sets the app_settings_overrides of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        Application setting overrides for cloned app. If specified, these settings override the settings cloned  from source app. Otherwise, application settings from source app are retained.

        :param app_settings_overrides: The app_settings_overrides of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :type app_settings_overrides: Dict[str, str]
        """

        self._app_settings_overrides = app_settings_overrides

    @property
    def clone_custom_host_names(self):
        """Gets the clone_custom_host_names of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        <code>true</code> to clone custom hostnames from source app; otherwise, <code>false</code>.

        :return: The clone_custom_host_names of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :rtype: bool
        """
        return self._clone_custom_host_names

    @clone_custom_host_names.setter
    def clone_custom_host_names(self, clone_custom_host_names):
        """Sets the clone_custom_host_names of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        <code>true</code> to clone custom hostnames from source app; otherwise, <code>false</code>.

        :param clone_custom_host_names: The clone_custom_host_names of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :type clone_custom_host_names: bool
        """

        self._clone_custom_host_names = clone_custom_host_names

    @property
    def clone_source_control(self):
        """Gets the clone_source_control of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        <code>true</code> to clone source control from source app; otherwise, <code>false</code>.

        :return: The clone_source_control of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :rtype: bool
        """
        return self._clone_source_control

    @clone_source_control.setter
    def clone_source_control(self, clone_source_control):
        """Sets the clone_source_control of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        <code>true</code> to clone source control from source app; otherwise, <code>false</code>.

        :param clone_source_control: The clone_source_control of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :type clone_source_control: bool
        """

        self._clone_source_control = clone_source_control

    @property
    def configure_load_balancing(self):
        """Gets the configure_load_balancing of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        <code>true</code> to configure load balancing for source and destination app.

        :return: The configure_load_balancing of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :rtype: bool
        """
        return self._configure_load_balancing

    @configure_load_balancing.setter
    def configure_load_balancing(self, configure_load_balancing):
        """Sets the configure_load_balancing of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        <code>true</code> to configure load balancing for source and destination app.

        :param configure_load_balancing: The configure_load_balancing of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :type configure_load_balancing: bool
        """

        self._configure_load_balancing = configure_load_balancing

    @property
    def correlation_id(self):
        """Gets the correlation_id of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        Correlation ID of cloning operation. This ID ties multiple cloning operations together to use the same snapshot.

        :return: The correlation_id of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :rtype: str
        """
        return self._correlation_id

    @correlation_id.setter
    def correlation_id(self, correlation_id):
        """Sets the correlation_id of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        Correlation ID of cloning operation. This ID ties multiple cloning operations together to use the same snapshot.

        :param correlation_id: The correlation_id of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :type correlation_id: str
        """

        self._correlation_id = correlation_id

    @property
    def hosting_environment(self):
        """Gets the hosting_environment of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        App Service Environment.

        :return: The hosting_environment of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :rtype: str
        """
        return self._hosting_environment

    @hosting_environment.setter
    def hosting_environment(self, hosting_environment):
        """Sets the hosting_environment of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        App Service Environment.

        :param hosting_environment: The hosting_environment of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :type hosting_environment: str
        """

        self._hosting_environment = hosting_environment

    @property
    def overwrite(self):
        """Gets the overwrite of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        <code>true</code> to overwrite destination app; otherwise, <code>false</code>.

        :return: The overwrite of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :rtype: bool
        """
        return self._overwrite

    @overwrite.setter
    def overwrite(self, overwrite):
        """Sets the overwrite of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        <code>true</code> to overwrite destination app; otherwise, <code>false</code>.

        :param overwrite: The overwrite of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :type overwrite: bool
        """

        self._overwrite = overwrite

    @property
    def source_web_app_id(self):
        """Gets the source_web_app_id of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        ARM resource ID of the source app. App resource ID is of the form  /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName} for production slots and  /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slotName} for other slots.

        :return: The source_web_app_id of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :rtype: str
        """
        return self._source_web_app_id

    @source_web_app_id.setter
    def source_web_app_id(self, source_web_app_id):
        """Sets the source_web_app_id of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        ARM resource ID of the source app. App resource ID is of the form  /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName} for production slots and  /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Web/sites/{siteName}/slots/{slotName} for other slots.

        :param source_web_app_id: The source_web_app_id of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :type source_web_app_id: str
        """
        if source_web_app_id is None:
            raise ValueError("Invalid value for `source_web_app_id`, must not be `None`")

        self._source_web_app_id = source_web_app_id

    @property
    def source_web_app_location(self):
        """Gets the source_web_app_location of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        Location of source app ex: West US or North Europe

        :return: The source_web_app_location of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :rtype: str
        """
        return self._source_web_app_location

    @source_web_app_location.setter
    def source_web_app_location(self, source_web_app_location):
        """Sets the source_web_app_location of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        Location of source app ex: West US or North Europe

        :param source_web_app_location: The source_web_app_location of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :type source_web_app_location: str
        """

        self._source_web_app_location = source_web_app_location

    @property
    def traffic_manager_profile_id(self):
        """Gets the traffic_manager_profile_id of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        ARM resource ID of the Traffic Manager profile to use, if it exists. Traffic Manager resource ID is of the form  /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficManagerProfiles/{profileName}.

        :return: The traffic_manager_profile_id of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :rtype: str
        """
        return self._traffic_manager_profile_id

    @traffic_manager_profile_id.setter
    def traffic_manager_profile_id(self, traffic_manager_profile_id):
        """Sets the traffic_manager_profile_id of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        ARM resource ID of the Traffic Manager profile to use, if it exists. Traffic Manager resource ID is of the form  /subscriptions/{subId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Network/trafficManagerProfiles/{profileName}.

        :param traffic_manager_profile_id: The traffic_manager_profile_id of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :type traffic_manager_profile_id: str
        """

        self._traffic_manager_profile_id = traffic_manager_profile_id

    @property
    def traffic_manager_profile_name(self):
        """Gets the traffic_manager_profile_name of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        Name of Traffic Manager profile to create. This is only needed if Traffic Manager profile does not already exist.

        :return: The traffic_manager_profile_name of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :rtype: str
        """
        return self._traffic_manager_profile_name

    @traffic_manager_profile_name.setter
    def traffic_manager_profile_name(self, traffic_manager_profile_name):
        """Sets the traffic_manager_profile_name of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.

        Name of Traffic Manager profile to create. This is only needed if Traffic Manager profile does not already exist.

        :param traffic_manager_profile_name: The traffic_manager_profile_name of this AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo.
        :type traffic_manager_profile_name: str
        """

        self._traffic_manager_profile_name = traffic_manager_profile_name
