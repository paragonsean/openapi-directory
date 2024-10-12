# coding: utf-8

# import models into model package
from openapi_server.models.app_service_plan_patch_resource import AppServicePlanPatchResource
from openapi_server.models.app_service_plans_create_or_update_vnet_route_request import AppServicePlansCreateOrUpdateVnetRouteRequest
from openapi_server.models.app_service_plans_get200_response import AppServicePlansGet200Response
from openapi_server.models.app_service_plans_get_hybrid_connection200_response import AppServicePlansGetHybridConnection200Response
from openapi_server.models.app_service_plans_get_hybrid_connection200_response_properties import AppServicePlansGetHybridConnection200ResponseProperties
from openapi_server.models.app_service_plans_get_vnet_from_server_farm200_response import AppServicePlansGetVnetFromServerFarm200Response
from openapi_server.models.app_service_plans_get_vnet_gateway200_response import AppServicePlansGetVnetGateway200Response
from openapi_server.models.app_service_plans_get_vnet_gateway200_response_properties import AppServicePlansGetVnetGateway200ResponseProperties
from openapi_server.models.app_service_plans_list200_response import AppServicePlansList200Response
from openapi_server.models.app_service_plans_list200_response_value_inner import AppServicePlansList200ResponseValueInner
from openapi_server.models.app_service_plans_list200_response_value_inner_properties import AppServicePlansList200ResponseValueInnerProperties
from openapi_server.models.app_service_plans_list200_response_value_inner_properties_hosting_environment_profile import AppServicePlansList200ResponseValueInnerPropertiesHostingEnvironmentProfile
from openapi_server.models.app_service_plans_list200_response_value_inner_sku import AppServicePlansList200ResponseValueInnerSku
from openapi_server.models.app_service_plans_list200_response_value_inner_sku_capabilities_inner import AppServicePlansList200ResponseValueInnerSkuCapabilitiesInner
from openapi_server.models.app_service_plans_list200_response_value_inner_sku_sku_capacity import AppServicePlansList200ResponseValueInnerSkuSkuCapacity
from openapi_server.models.app_service_plans_list_default_response import AppServicePlansListDefaultResponse
from openapi_server.models.app_service_plans_list_default_response_error import AppServicePlansListDefaultResponseError
from openapi_server.models.app_service_plans_list_default_response_error_details_inner import AppServicePlansListDefaultResponseErrorDetailsInner
from openapi_server.models.app_service_plans_list_hybrid_connection_keys200_response import AppServicePlansListHybridConnectionKeys200Response
from openapi_server.models.app_service_plans_list_hybrid_connection_keys200_response_properties import AppServicePlansListHybridConnectionKeys200ResponseProperties
from openapi_server.models.app_service_plans_list_metric_defintions200_response import AppServicePlansListMetricDefintions200Response
from openapi_server.models.app_service_plans_list_metric_defintions200_response_value_inner import AppServicePlansListMetricDefintions200ResponseValueInner
from openapi_server.models.app_service_plans_list_metric_defintions200_response_value_inner_properties import AppServicePlansListMetricDefintions200ResponseValueInnerProperties
from openapi_server.models.app_service_plans_list_metric_defintions200_response_value_inner_properties_metric_availabilities_inner import AppServicePlansListMetricDefintions200ResponseValueInnerPropertiesMetricAvailabilitiesInner
from openapi_server.models.app_service_plans_list_metrics200_response import AppServicePlansListMetrics200Response
from openapi_server.models.app_service_plans_list_metrics200_response_value_inner import AppServicePlansListMetrics200ResponseValueInner
from openapi_server.models.app_service_plans_list_metrics200_response_value_inner_metric_values_inner import AppServicePlansListMetrics200ResponseValueInnerMetricValuesInner
from openapi_server.models.app_service_plans_list_metrics200_response_value_inner_metric_values_inner_properties_inner import AppServicePlansListMetrics200ResponseValueInnerMetricValuesInnerPropertiesInner
from openapi_server.models.app_service_plans_list_metrics200_response_value_inner_name import AppServicePlansListMetrics200ResponseValueInnerName
from openapi_server.models.app_service_plans_list_usages200_response import AppServicePlansListUsages200Response
from openapi_server.models.app_service_plans_list_usages200_response_value_inner import AppServicePlansListUsages200ResponseValueInner
from openapi_server.models.app_service_plans_list_usages200_response_value_inner_name import AppServicePlansListUsages200ResponseValueInnerName
from openapi_server.models.app_service_plans_list_vnets200_response_inner import AppServicePlansListVnets200ResponseInner
from openapi_server.models.app_service_plans_list_vnets200_response_inner_properties import AppServicePlansListVnets200ResponseInnerProperties
from openapi_server.models.app_service_plans_list_vnets200_response_inner_properties_routes_inner import AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner
from openapi_server.models.app_service_plans_list_vnets200_response_inner_properties_routes_inner_properties import AppServicePlansListVnets200ResponseInnerPropertiesRoutesInnerProperties
from openapi_server.models.app_service_plans_list_web_apps200_response import AppServicePlansListWebApps200Response
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner import AppServicePlansListWebApps200ResponseValueInner
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_identity import AppServicePlansListWebApps200ResponseValueInnerIdentity
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_identity_user_assigned_identities_value import AppServicePlansListWebApps200ResponseValueInnerIdentityUserAssignedIdentitiesValue
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties import AppServicePlansListWebApps200ResponseValueInnerProperties
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_cloning_info import AppServicePlansListWebApps200ResponseValueInnerPropertiesCloningInfo
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_geo_distributions_inner import AppServicePlansListWebApps200ResponseValueInnerPropertiesGeoDistributionsInner
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_host_name_ssl_states_inner import AppServicePlansListWebApps200ResponseValueInnerPropertiesHostNameSslStatesInner
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfig
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_api_definition import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigApiDefinition
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_app_settings_inner import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAppSettingsInner
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_auto_heal_rules import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRules
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_auto_heal_rules_actions import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActions
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_auto_heal_rules_actions_custom_action import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesActionsCustomAction
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_auto_heal_rules_triggers import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggers
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_auto_heal_rules_triggers_requests import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersRequests
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_auto_heal_rules_triggers_slow_requests import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersSlowRequests
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_auto_heal_rules_triggers_status_codes_inner import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAutoHealRulesTriggersStatusCodesInner
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_azure_storage_accounts_value import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigAzureStorageAccountsValue
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_connection_strings_inner import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigConnectionStringsInner
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_cors import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigCors
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_experiments import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperiments
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_experiments_ramp_up_rules_inner import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigExperimentsRampUpRulesInner
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_handler_mappings_inner import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigHandlerMappingsInner
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_ip_security_restrictions_inner import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigIpSecurityRestrictionsInner
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_limits import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigLimits
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_machine_key import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigMachineKey
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_push import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPush
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_push_properties import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigPushProperties
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_virtual_applications_inner import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInner
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_site_config_virtual_applications_inner_virtual_directories_inner import AppServicePlansListWebApps200ResponseValueInnerPropertiesSiteConfigVirtualApplicationsInnerVirtualDirectoriesInner
from openapi_server.models.app_service_plans_list_web_apps200_response_value_inner_properties_slot_swap_status import AppServicePlansListWebApps200ResponseValueInnerPropertiesSlotSwapStatus
from openapi_server.models.hybrid_connection_collection import HybridConnectionCollection
from openapi_server.models.hybrid_connection_collection_value_inner import HybridConnectionCollectionValueInner
from openapi_server.models.hybrid_connection_limits import HybridConnectionLimits
from openapi_server.models.resource_collection import ResourceCollection
