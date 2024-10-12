from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_item import BackupItem
from openapi_server.models.backup_item_collection import BackupItemCollection
from openapi_server.models.backup_request import BackupRequest
from openapi_server.models.connection_string_dictionary import ConnectionStringDictionary
from openapi_server.models.continuous_web_job import ContinuousWebJob
from openapi_server.models.continuous_web_job_collection import ContinuousWebJobCollection
from openapi_server.models.csm_publishing_profile_options import CsmPublishingProfileOptions
from openapi_server.models.csm_slot_entity import CsmSlotEntity
from openapi_server.models.custom_hostname_analysis_result import CustomHostnameAnalysisResult
from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_collection import DeploymentCollection
from openapi_server.models.function_envelope import FunctionEnvelope
from openapi_server.models.function_envelope_collection import FunctionEnvelopeCollection
from openapi_server.models.function_secrets import FunctionSecrets
from openapi_server.models.host_name_binding import HostNameBinding
from openapi_server.models.host_name_binding_collection import HostNameBindingCollection
from openapi_server.models.ms_deploy import MSDeploy
from openapi_server.models.ms_deploy_log import MSDeployLog
from openapi_server.models.ms_deploy_status import MSDeployStatus
from openapi_server.models.migrate_my_sql_request import MigrateMySqlRequest
from openapi_server.models.migrate_my_sql_status import MigrateMySqlStatus
from openapi_server.models.network_features import NetworkFeatures
from openapi_server.models.perf_mon_counter_collection import PerfMonCounterCollection
from openapi_server.models.premier_add_on import PremierAddOn
from openapi_server.models.process_info import ProcessInfo
from openapi_server.models.process_info_collection import ProcessInfoCollection
from openapi_server.models.process_module_info import ProcessModuleInfo
from openapi_server.models.process_module_info_collection import ProcessModuleInfoCollection
from openapi_server.models.process_thread_info import ProcessThreadInfo
from openapi_server.models.process_thread_info_collection import ProcessThreadInfoCollection
from openapi_server.models.public_certificate import PublicCertificate
from openapi_server.models.public_certificate_collection import PublicCertificateCollection
from openapi_server.models.relay_service_connection_entity import RelayServiceConnectionEntity
from openapi_server.models.restore_request import RestoreRequest
from openapi_server.models.restore_response import RestoreResponse
from openapi_server.models.site_auth_settings import SiteAuthSettings
from openapi_server.models.site_cloneability import SiteCloneability
from openapi_server.models.site_config_resource import SiteConfigResource
from openapi_server.models.site_config_resource_collection import SiteConfigResourceCollection
from openapi_server.models.site_configuration_snapshot_info_collection import SiteConfigurationSnapshotInfoCollection
from openapi_server.models.site_extension_info import SiteExtensionInfo
from openapi_server.models.site_extension_info_collection import SiteExtensionInfoCollection
from openapi_server.models.site_logs_config import SiteLogsConfig
from openapi_server.models.site_patch_resource import SitePatchResource
from openapi_server.models.site_php_error_log_flag import SitePhpErrorLogFlag
from openapi_server.models.site_source_control import SiteSourceControl
from openapi_server.models.slot_config_names_resource import SlotConfigNamesResource
from openapi_server.models.slot_difference_collection import SlotDifferenceCollection
from openapi_server.models.snapshot_collection import SnapshotCollection
from openapi_server.models.storage_migration_options import StorageMigrationOptions
from openapi_server.models.storage_migration_response import StorageMigrationResponse
from openapi_server.models.string_dictionary import StringDictionary
from openapi_server.models.triggered_job_history import TriggeredJobHistory
from openapi_server.models.triggered_job_history_collection import TriggeredJobHistoryCollection
from openapi_server.models.triggered_web_job import TriggeredWebJob
from openapi_server.models.triggered_web_job_collection import TriggeredWebJobCollection
from openapi_server.models.web_app_instance_collection import WebAppInstanceCollection
from openapi_server.models.web_apps_get200_response import WebAppsGet200Response
from openapi_server.models.web_apps_get_domain_ownership_identifier200_response import WebAppsGetDomainOwnershipIdentifier200Response
from openapi_server.models.web_apps_get_hybrid_connection200_response import WebAppsGetHybridConnection200Response
from openapi_server.models.web_apps_get_vnet_connection_gateway_slot200_response import WebAppsGetVnetConnectionGatewaySlot200Response
from openapi_server.models.web_apps_get_vnet_connection_slot200_response import WebAppsGetVnetConnectionSlot200Response
from openapi_server.models.web_apps_list200_response import WebAppsList200Response
from openapi_server.models.web_apps_list_domain_ownership_identifiers200_response import WebAppsListDomainOwnershipIdentifiers200Response
from openapi_server.models.web_apps_list_hybrid_connection_keys200_response import WebAppsListHybridConnectionKeys200Response
from openapi_server.models.web_apps_list_metric_definitions200_response import WebAppsListMetricDefinitions200Response
from openapi_server.models.web_apps_list_metrics200_response import WebAppsListMetrics200Response
from openapi_server.models.web_apps_list_publishing_credentials200_response import WebAppsListPublishingCredentials200Response
from openapi_server.models.web_apps_list_usages_slot200_response import WebAppsListUsagesSlot200Response
from openapi_server.models.web_apps_list_vnet_connections_slot200_response_inner import WebAppsListVnetConnectionsSlot200ResponseInner
from openapi_server.models.web_apps_migrate_my_sql200_response import WebAppsMigrateMySql200Response
from openapi_server.models.web_apps_recover_request import WebAppsRecoverRequest
from openapi_server.models.web_apps_update_site_push_settings_request import WebAppsUpdateSitePushSettingsRequest
from openapi_server.models.web_job import WebJob
from openapi_server.models.web_job_collection import WebJobCollection
from openapi_server import util


async def web_apps_add_premier_add_on(request: web.Request, resource_group_name, name, premier_add_on_name, subscription_id, api_version, premier_add_on) -> web.Response:
    """Updates a named add-on of an app.

    Updates a named add-on of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param premier_add_on_name: Add-on name.
    :type premier_add_on_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param premier_add_on: A JSON representation of the edited premier add-on.
    :type premier_add_on: dict | bytes

    """
    premier_add_on = PremierAddOn.from_dict(premier_add_on)
    return web.Response(status=200)


async def web_apps_add_premier_add_on_slot(request: web.Request, resource_group_name, name, premier_add_on_name, slot, subscription_id, api_version, premier_add_on) -> web.Response:
    """Updates a named add-on of an app.

    Updates a named add-on of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param premier_add_on_name: Add-on name.
    :type premier_add_on_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will update the named add-on for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param premier_add_on: A JSON representation of the edited premier add-on.
    :type premier_add_on: dict | bytes

    """
    premier_add_on = PremierAddOn.from_dict(premier_add_on)
    return web.Response(status=200)


async def web_apps_analyze_custom_hostname(request: web.Request, resource_group_name, name, subscription_id, api_version, host_name=None) -> web.Response:
    """Analyze a custom hostname.

    Analyze a custom hostname.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param host_name: Custom hostname.
    :type host_name: str

    """
    return web.Response(status=200)


async def web_apps_analyze_custom_hostname_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, host_name=None) -> web.Response:
    """Analyze a custom hostname.

    Analyze a custom hostname.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param host_name: Custom hostname.
    :type host_name: str

    """
    return web.Response(status=200)


async def web_apps_apply_slot_config_to_production(request: web.Request, resource_group_name, name, subscription_id, api_version, slot_swap_entity) -> web.Response:
    """Applies the configuration settings from the target slot onto the current slot.

    Applies the configuration settings from the target slot onto the current slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param slot_swap_entity: JSON object that contains the target slot name. See example.
    :type slot_swap_entity: dict | bytes

    """
    slot_swap_entity = CsmSlotEntity.from_dict(slot_swap_entity)
    return web.Response(status=200)


async def web_apps_apply_slot_configuration_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, slot_swap_entity) -> web.Response:
    """Applies the configuration settings from the target slot onto the current slot.

    Applies the configuration settings from the target slot onto the current slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the source slot. If a slot is not specified, the production slot is used as the source slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param slot_swap_entity: JSON object that contains the target slot name. See example.
    :type slot_swap_entity: dict | bytes

    """
    slot_swap_entity = CsmSlotEntity.from_dict(slot_swap_entity)
    return web.Response(status=200)


async def web_apps_backup(request: web.Request, resource_group_name, name, subscription_id, api_version, request) -> web.Response:
    """Creates a backup of an app.

    Creates a backup of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: Backup configuration. You can use the JSON response from the POST action as input here.
    :type request: dict | bytes

    """
    request = BackupRequest.from_dict(request)
    return web.Response(status=200)


async def web_apps_backup_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, request) -> web.Response:
    """Creates a backup of an app.

    Creates a backup of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will create a backup for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: Backup configuration. You can use the JSON response from the POST action as input here.
    :type request: dict | bytes

    """
    request = BackupRequest.from_dict(request)
    return web.Response(status=200)


async def web_apps_create_deployment(request: web.Request, resource_group_name, name, id, subscription_id, api_version, deployment) -> web.Response:
    """Create a deployment for an app, or a deployment slot.

    Create a deployment for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param id: ID of an existing deployment.
    :type id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param deployment: Deployment details.
    :type deployment: dict | bytes

    """
    deployment = Deployment.from_dict(deployment)
    return web.Response(status=200)


async def web_apps_create_deployment_slot(request: web.Request, resource_group_name, name, id, slot, subscription_id, api_version, deployment) -> web.Response:
    """Create a deployment for an app, or a deployment slot.

    Create a deployment for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param id: ID of an existing deployment.
    :type id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API creates a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param deployment: Deployment details.
    :type deployment: dict | bytes

    """
    deployment = Deployment.from_dict(deployment)
    return web.Response(status=200)


async def web_apps_create_function(request: web.Request, resource_group_name, name, function_name, subscription_id, api_version, function_envelope) -> web.Response:
    """Create function for web site, or a deployment slot.

    Create function for web site, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param function_name: Function name.
    :type function_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param function_envelope: Function details.
    :type function_envelope: dict | bytes

    """
    function_envelope = FunctionEnvelope.from_dict(function_envelope)
    return web.Response(status=200)


async def web_apps_create_instance_function_slot(request: web.Request, resource_group_name, name, function_name, slot, subscription_id, api_version, function_envelope) -> web.Response:
    """Create function for web site, or a deployment slot.

    Create function for web site, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param function_name: Function name.
    :type function_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param function_envelope: Function details.
    :type function_envelope: dict | bytes

    """
    function_envelope = FunctionEnvelope.from_dict(function_envelope)
    return web.Response(status=200)


async def web_apps_create_instance_ms_deploy_operation(request: web.Request, resource_group_name, name, instance_id, subscription_id, api_version, ms_deploy) -> web.Response:
    """Invoke the MSDeploy web app extension.

    Invoke the MSDeploy web app extension.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param instance_id: ID of web app instance.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param ms_deploy: Details of MSDeploy operation
    :type ms_deploy: dict | bytes

    """
    ms_deploy = MSDeploy.from_dict(ms_deploy)
    return web.Response(status=200)


async def web_apps_create_instance_ms_deploy_operation_slot(request: web.Request, resource_group_name, name, slot, instance_id, subscription_id, api_version, ms_deploy) -> web.Response:
    """Invoke the MSDeploy web app extension.

    Invoke the MSDeploy web app extension.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param instance_id: ID of web app instance.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param ms_deploy: Details of MSDeploy operation
    :type ms_deploy: dict | bytes

    """
    ms_deploy = MSDeploy.from_dict(ms_deploy)
    return web.Response(status=200)


async def web_apps_create_ms_deploy_operation(request: web.Request, resource_group_name, name, subscription_id, api_version, ms_deploy) -> web.Response:
    """Invoke the MSDeploy web app extension.

    Invoke the MSDeploy web app extension.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param ms_deploy: Details of MSDeploy operation
    :type ms_deploy: dict | bytes

    """
    ms_deploy = MSDeploy.from_dict(ms_deploy)
    return web.Response(status=200)


async def web_apps_create_ms_deploy_operation_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, ms_deploy) -> web.Response:
    """Invoke the MSDeploy web app extension.

    Invoke the MSDeploy web app extension.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param ms_deploy: Details of MSDeploy operation
    :type ms_deploy: dict | bytes

    """
    ms_deploy = MSDeploy.from_dict(ms_deploy)
    return web.Response(status=200)


async def web_apps_create_or_update(request: web.Request, resource_group_name, name, subscription_id, api_version, site_envelope) -> web.Response:
    """Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

    Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Unique name of the app to create or update. To create or update a deployment slot, use the {slot} parameter.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_envelope: A JSON representation of the app properties. See example.
    :type site_envelope: dict | bytes

    """
    site_envelope = WebAppsGet200Response.from_dict(site_envelope)
    return web.Response(status=200)


async def web_apps_create_or_update_configuration(request: web.Request, resource_group_name, name, subscription_id, api_version, site_config) -> web.Response:
    """Updates the configuration of an app.

    Updates the configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_config: JSON representation of a SiteConfig object. See example.
    :type site_config: dict | bytes

    """
    site_config = SiteConfigResource.from_dict(site_config)
    return web.Response(status=200)


async def web_apps_create_or_update_configuration_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, site_config) -> web.Response:
    """Updates the configuration of an app.

    Updates the configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will update configuration for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_config: JSON representation of a SiteConfig object. See example.
    :type site_config: dict | bytes

    """
    site_config = SiteConfigResource.from_dict(site_config)
    return web.Response(status=200)


async def web_apps_create_or_update_domain_ownership_identifier(request: web.Request, resource_group_name, name, domain_ownership_identifier_name, subscription_id, api_version, domain_ownership_identifier) -> web.Response:
    """Creates a domain ownership identifier for web app, or updates an existing ownership identifier.

    Creates a domain ownership identifier for web app, or updates an existing ownership identifier.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param domain_ownership_identifier_name: Name of domain ownership identifier.
    :type domain_ownership_identifier_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param domain_ownership_identifier: A JSON representation of the domain ownership properties.
    :type domain_ownership_identifier: dict | bytes

    """
    domain_ownership_identifier = WebAppsGetDomainOwnershipIdentifier200Response.from_dict(domain_ownership_identifier)
    return web.Response(status=200)


async def web_apps_create_or_update_domain_ownership_identifier_slot(request: web.Request, resource_group_name, name, domain_ownership_identifier_name, slot, subscription_id, api_version, domain_ownership_identifier) -> web.Response:
    """Creates a domain ownership identifier for web app, or updates an existing ownership identifier.

    Creates a domain ownership identifier for web app, or updates an existing ownership identifier.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param domain_ownership_identifier_name: Name of domain ownership identifier.
    :type domain_ownership_identifier_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param domain_ownership_identifier: A JSON representation of the domain ownership properties.
    :type domain_ownership_identifier: dict | bytes

    """
    domain_ownership_identifier = WebAppsGetDomainOwnershipIdentifier200Response.from_dict(domain_ownership_identifier)
    return web.Response(status=200)


async def web_apps_create_or_update_host_name_binding(request: web.Request, resource_group_name, name, host_name, subscription_id, api_version, host_name_binding) -> web.Response:
    """Creates a hostname binding for an app.

    Creates a hostname binding for an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param host_name: Hostname in the hostname binding.
    :type host_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param host_name_binding: Binding details. This is the JSON representation of a HostNameBinding object.
    :type host_name_binding: dict | bytes

    """
    host_name_binding = HostNameBinding.from_dict(host_name_binding)
    return web.Response(status=200)


async def web_apps_create_or_update_host_name_binding_slot(request: web.Request, resource_group_name, name, host_name, slot, subscription_id, api_version, host_name_binding) -> web.Response:
    """Creates a hostname binding for an app.

    Creates a hostname binding for an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param host_name: Hostname in the hostname binding.
    :type host_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will create a binding for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param host_name_binding: Binding details. This is the JSON representation of a HostNameBinding object.
    :type host_name_binding: dict | bytes

    """
    host_name_binding = HostNameBinding.from_dict(host_name_binding)
    return web.Response(status=200)


async def web_apps_create_or_update_hybrid_connection(request: web.Request, resource_group_name, name, namespace_name, relay_name, subscription_id, api_version, connection_envelope) -> web.Response:
    """Creates a new Hybrid Connection using a Service Bus relay.

    Creates a new Hybrid Connection using a Service Bus relay.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: The name of the web app.
    :type name: str
    :param namespace_name: The namespace for this hybrid connection.
    :type namespace_name: str
    :param relay_name: The relay name for this hybrid connection.
    :type relay_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The details of the hybrid connection.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = WebAppsGetHybridConnection200Response.from_dict(connection_envelope)
    return web.Response(status=200)


async def web_apps_create_or_update_hybrid_connection_slot(request: web.Request, resource_group_name, name, namespace_name, relay_name, slot, subscription_id, api_version, connection_envelope) -> web.Response:
    """Creates a new Hybrid Connection using a Service Bus relay.

    Creates a new Hybrid Connection using a Service Bus relay.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: The name of the web app.
    :type name: str
    :param namespace_name: The namespace for this hybrid connection.
    :type namespace_name: str
    :param relay_name: The relay name for this hybrid connection.
    :type relay_name: str
    :param slot: The name of the slot for the web app.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The details of the hybrid connection.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = WebAppsGetHybridConnection200Response.from_dict(connection_envelope)
    return web.Response(status=200)


async def web_apps_create_or_update_public_certificate(request: web.Request, resource_group_name, name, public_certificate_name, subscription_id, api_version, public_certificate) -> web.Response:
    """Creates a hostname binding for an app.

    Creates a hostname binding for an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param public_certificate_name: Public certificate name.
    :type public_certificate_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param public_certificate: Public certificate details. This is the JSON representation of a PublicCertificate object.
    :type public_certificate: dict | bytes

    """
    public_certificate = PublicCertificate.from_dict(public_certificate)
    return web.Response(status=200)


async def web_apps_create_or_update_public_certificate_slot(request: web.Request, resource_group_name, name, public_certificate_name, slot, subscription_id, api_version, public_certificate) -> web.Response:
    """Creates a hostname binding for an app.

    Creates a hostname binding for an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param public_certificate_name: Public certificate name.
    :type public_certificate_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will create a binding for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param public_certificate: Public certificate details. This is the JSON representation of a PublicCertificate object.
    :type public_certificate: dict | bytes

    """
    public_certificate = PublicCertificate.from_dict(public_certificate)
    return web.Response(status=200)


async def web_apps_create_or_update_relay_service_connection(request: web.Request, resource_group_name, name, entity_name, subscription_id, api_version, connection_envelope) -> web.Response:
    """Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).

    Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param entity_name: Name of the hybrid connection configuration.
    :type entity_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: Details of the hybrid connection configuration.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = RelayServiceConnectionEntity.from_dict(connection_envelope)
    return web.Response(status=200)


async def web_apps_create_or_update_relay_service_connection_slot(request: web.Request, resource_group_name, name, entity_name, slot, subscription_id, api_version, connection_envelope) -> web.Response:
    """Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).

    Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param entity_name: Name of the hybrid connection configuration.
    :type entity_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will create or update a hybrid connection for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: Details of the hybrid connection configuration.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = RelayServiceConnectionEntity.from_dict(connection_envelope)
    return web.Response(status=200)


async def web_apps_create_or_update_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, site_envelope, skip_dns_registration=None, skip_custom_domain_verification=None, force_dns_registration=None, ttl_in_seconds=None) -> web.Response:
    """Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

    Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Unique name of the app to create or update. To create or update a deployment slot, use the {slot} parameter.
    :type name: str
    :param slot: Name of the deployment slot to create or update. By default, this API attempts to create or modify the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_envelope: A JSON representation of the app properties. See example.
    :type site_envelope: dict | bytes
    :param skip_dns_registration: If true web app hostname is not registered with DNS on creation. This parameter is  only used for app creation.
    :type skip_dns_registration: bool
    :param skip_custom_domain_verification: If true, custom (non *.azurewebsites.net) domains associated with web app are not verified.
    :type skip_custom_domain_verification: bool
    :param force_dns_registration: If true, web app hostname is force registered with DNS.
    :type force_dns_registration: bool
    :param ttl_in_seconds: Time to live in seconds for web app&#39;s default domain name.
    :type ttl_in_seconds: str

    """
    site_envelope = WebAppsGet200Response.from_dict(site_envelope)
    return web.Response(status=200)


async def web_apps_create_or_update_source_control(request: web.Request, resource_group_name, name, subscription_id, api_version, site_source_control) -> web.Response:
    """Updates the source control configuration of an app.

    Updates the source control configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_source_control: JSON representation of a SiteSourceControl object. See example.
    :type site_source_control: dict | bytes

    """
    site_source_control = SiteSourceControl.from_dict(site_source_control)
    return web.Response(status=200)


async def web_apps_create_or_update_source_control_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, site_source_control) -> web.Response:
    """Updates the source control configuration of an app.

    Updates the source control configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will update the source control configuration for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_source_control: JSON representation of a SiteSourceControl object. See example.
    :type site_source_control: dict | bytes

    """
    site_source_control = SiteSourceControl.from_dict(site_source_control)
    return web.Response(status=200)


async def web_apps_create_or_update_vnet_connection(request: web.Request, resource_group_name, name, vnet_name, subscription_id, api_version, connection_envelope) -> web.Response:
    """Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).

    Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param vnet_name: Name of an existing Virtual Network.
    :type vnet_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: Properties of the Virtual Network connection. See example.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = WebAppsGetVnetConnectionSlot200Response.from_dict(connection_envelope)
    return web.Response(status=200)


async def web_apps_create_or_update_vnet_connection_gateway(request: web.Request, resource_group_name, name, vnet_name, gateway_name, subscription_id, api_version, connection_envelope) -> web.Response:
    """Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).

    Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param vnet_name: Name of the Virtual Network.
    :type vnet_name: str
    :param gateway_name: Name of the gateway. Currently, the only supported string is \&quot;primary\&quot;.
    :type gateway_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The properties to update this gateway with.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = WebAppsGetVnetConnectionGatewaySlot200Response.from_dict(connection_envelope)
    return web.Response(status=200)


async def web_apps_create_or_update_vnet_connection_gateway_slot(request: web.Request, resource_group_name, name, vnet_name, gateway_name, slot, subscription_id, api_version, connection_envelope) -> web.Response:
    """Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).

    Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param vnet_name: Name of the Virtual Network.
    :type vnet_name: str
    :param gateway_name: Name of the gateway. Currently, the only supported string is \&quot;primary\&quot;.
    :type gateway_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will add or update a gateway for the production slot&#39;s Virtual Network.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The properties to update this gateway with.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = WebAppsGetVnetConnectionGatewaySlot200Response.from_dict(connection_envelope)
    return web.Response(status=200)


async def web_apps_create_or_update_vnet_connection_slot(request: web.Request, resource_group_name, name, vnet_name, slot, subscription_id, api_version, connection_envelope) -> web.Response:
    """Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).

    Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param vnet_name: Name of an existing Virtual Network.
    :type vnet_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will add or update connections for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: Properties of the Virtual Network connection. See example.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = WebAppsGetVnetConnectionSlot200Response.from_dict(connection_envelope)
    return web.Response(status=200)


async def web_apps_delete(request: web.Request, resource_group_name, name, subscription_id, api_version, delete_metrics=None, delete_empty_server_farm=None) -> web.Response:
    """Deletes a web, mobile, or API app, or one of the deployment slots.

    Deletes a web, mobile, or API app, or one of the deployment slots.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app to delete.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param delete_metrics: If true, web app metrics are also deleted.
    :type delete_metrics: bool
    :param delete_empty_server_farm: Specify false if you want to keep empty App Service plan. By default, empty App Service plan is deleted.
    :type delete_empty_server_farm: bool

    """
    return web.Response(status=200)


async def web_apps_delete_backup(request: web.Request, resource_group_name, name, backup_id, subscription_id, api_version) -> web.Response:
    """Deletes a backup of an app by its ID.

    Deletes a backup of an app by its ID.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param backup_id: ID of the backup.
    :type backup_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_backup_configuration(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Deletes the backup configuration of an app.

    Deletes the backup configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_backup_configuration_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Deletes the backup configuration of an app.

    Deletes the backup configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will delete the backup configuration for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_backup_slot(request: web.Request, resource_group_name, name, backup_id, slot, subscription_id, api_version) -> web.Response:
    """Deletes a backup of an app by its ID.

    Deletes a backup of an app by its ID.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param backup_id: ID of the backup.
    :type backup_id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will delete a backup of the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_continuous_web_job(request: web.Request, resource_group_name, name, web_job_name, subscription_id, api_version) -> web.Response:
    """Delete a continuous web job by its ID for an app, or a deployment slot.

    Delete a continuous web job by its ID for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param web_job_name: Name of Web Job.
    :type web_job_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_continuous_web_job_slot(request: web.Request, resource_group_name, name, web_job_name, slot, subscription_id, api_version) -> web.Response:
    """Delete a continuous web job by its ID for an app, or a deployment slot.

    Delete a continuous web job by its ID for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param web_job_name: Name of Web Job.
    :type web_job_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_deployment(request: web.Request, resource_group_name, name, id, subscription_id, api_version) -> web.Response:
    """Delete a deployment by its ID for an app, or a deployment slot.

    Delete a deployment by its ID for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param id: Deployment ID.
    :type id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_deployment_slot(request: web.Request, resource_group_name, name, id, slot, subscription_id, api_version) -> web.Response:
    """Delete a deployment by its ID for an app, or a deployment slot.

    Delete a deployment by its ID for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param id: Deployment ID.
    :type id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_domain_ownership_identifier(request: web.Request, resource_group_name, name, domain_ownership_identifier_name, subscription_id, api_version) -> web.Response:
    """Deletes a domain ownership identifier for a web app.

    Deletes a domain ownership identifier for a web app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param domain_ownership_identifier_name: Name of domain ownership identifier.
    :type domain_ownership_identifier_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_domain_ownership_identifier_slot(request: web.Request, resource_group_name, name, domain_ownership_identifier_name, slot, subscription_id, api_version) -> web.Response:
    """Deletes a domain ownership identifier for a web app.

    Deletes a domain ownership identifier for a web app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param domain_ownership_identifier_name: Name of domain ownership identifier.
    :type domain_ownership_identifier_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_function(request: web.Request, resource_group_name, name, function_name, subscription_id, api_version) -> web.Response:
    """Delete a function for web site, or a deployment slot.

    Delete a function for web site, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param function_name: Function name.
    :type function_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_host_name_binding(request: web.Request, resource_group_name, name, host_name, subscription_id, api_version) -> web.Response:
    """Deletes a hostname binding for an app.

    Deletes a hostname binding for an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param host_name: Hostname in the hostname binding.
    :type host_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_host_name_binding_slot(request: web.Request, resource_group_name, name, slot, host_name, subscription_id, api_version) -> web.Response:
    """Deletes a hostname binding for an app.

    Deletes a hostname binding for an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot.
    :type slot: str
    :param host_name: Hostname in the hostname binding.
    :type host_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_hybrid_connection(request: web.Request, resource_group_name, name, namespace_name, relay_name, subscription_id, api_version) -> web.Response:
    """Removes a Hybrid Connection from this site.

    Removes a Hybrid Connection from this site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: The name of the web app.
    :type name: str
    :param namespace_name: The namespace for this hybrid connection.
    :type namespace_name: str
    :param relay_name: The relay name for this hybrid connection.
    :type relay_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_hybrid_connection_slot(request: web.Request, resource_group_name, name, namespace_name, relay_name, slot, subscription_id, api_version) -> web.Response:
    """Removes a Hybrid Connection from this site.

    Removes a Hybrid Connection from this site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: The name of the web app.
    :type name: str
    :param namespace_name: The namespace for this hybrid connection.
    :type namespace_name: str
    :param relay_name: The relay name for this hybrid connection.
    :type relay_name: str
    :param slot: The name of the slot for the web app.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_instance_function_slot(request: web.Request, resource_group_name, name, function_name, slot, subscription_id, api_version) -> web.Response:
    """Delete a function for web site, or a deployment slot.

    Delete a function for web site, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param function_name: Function name.
    :type function_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_instance_process(request: web.Request, resource_group_name, name, process_id, instance_id, subscription_id, api_version) -> web.Response:
    """Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.

    Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param instance_id: ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_instance_process_slot(request: web.Request, resource_group_name, name, process_id, slot, instance_id, subscription_id, api_version) -> web.Response:
    """Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.

    Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
    :type slot: str
    :param instance_id: ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_premier_add_on(request: web.Request, resource_group_name, name, premier_add_on_name, subscription_id, api_version) -> web.Response:
    """Delete a premier add-on from an app.

    Delete a premier add-on from an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param premier_add_on_name: Add-on name.
    :type premier_add_on_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_premier_add_on_slot(request: web.Request, resource_group_name, name, premier_add_on_name, slot, subscription_id, api_version) -> web.Response:
    """Delete a premier add-on from an app.

    Delete a premier add-on from an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param premier_add_on_name: Add-on name.
    :type premier_add_on_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will delete the named add-on for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_process(request: web.Request, resource_group_name, name, process_id, subscription_id, api_version) -> web.Response:
    """Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.

    Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_process_slot(request: web.Request, resource_group_name, name, process_id, slot, subscription_id, api_version) -> web.Response:
    """Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.

    Terminate a process by its ID for a web site, or a deployment slot, or specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_public_certificate(request: web.Request, resource_group_name, name, public_certificate_name, subscription_id, api_version) -> web.Response:
    """Deletes a hostname binding for an app.

    Deletes a hostname binding for an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param public_certificate_name: Public certificate name.
    :type public_certificate_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_public_certificate_slot(request: web.Request, resource_group_name, name, slot, public_certificate_name, subscription_id, api_version) -> web.Response:
    """Deletes a hostname binding for an app.

    Deletes a hostname binding for an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot.
    :type slot: str
    :param public_certificate_name: Public certificate name.
    :type public_certificate_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_relay_service_connection(request: web.Request, resource_group_name, name, entity_name, subscription_id, api_version) -> web.Response:
    """Deletes a relay service connection by its name.

    Deletes a relay service connection by its name.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param entity_name: Name of the hybrid connection configuration.
    :type entity_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_relay_service_connection_slot(request: web.Request, resource_group_name, name, entity_name, slot, subscription_id, api_version) -> web.Response:
    """Deletes a relay service connection by its name.

    Deletes a relay service connection by its name.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param entity_name: Name of the hybrid connection configuration.
    :type entity_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will delete a hybrid connection for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_site_extension(request: web.Request, resource_group_name, name, site_extension_id, subscription_id, api_version) -> web.Response:
    """Remove a site extension from a web site, or a deployment slot.

    Remove a site extension from a web site, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param site_extension_id: Site extension name.
    :type site_extension_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_site_extension_slot(request: web.Request, resource_group_name, name, site_extension_id, slot, subscription_id, api_version) -> web.Response:
    """Remove a site extension from a web site, or a deployment slot.

    Remove a site extension from a web site, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param site_extension_id: Site extension name.
    :type site_extension_id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, delete_metrics=None, delete_empty_server_farm=None, skip_dns_registration=None) -> web.Response:
    """Deletes a web, mobile, or API app, or one of the deployment slots.

    Deletes a web, mobile, or API app, or one of the deployment slots.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app to delete.
    :type name: str
    :param slot: Name of the deployment slot to delete. By default, the API deletes the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param delete_metrics: If true, web app metrics are also deleted.
    :type delete_metrics: bool
    :param delete_empty_server_farm: Specify true if the App Service plan will be empty after app deletion and you want to delete the empty App Service plan. By default, the empty App Service plan is not deleted.
    :type delete_empty_server_farm: bool
    :param skip_dns_registration: If true, DNS registration is skipped.
    :type skip_dns_registration: bool

    """
    return web.Response(status=200)


async def web_apps_delete_source_control(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Deletes the source control configuration of an app.

    Deletes the source control configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_source_control_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Deletes the source control configuration of an app.

    Deletes the source control configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will delete the source control configuration for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_triggered_web_job(request: web.Request, resource_group_name, name, web_job_name, subscription_id, api_version) -> web.Response:
    """Delete a triggered web job by its ID for an app, or a deployment slot.

    Delete a triggered web job by its ID for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param web_job_name: Name of Web Job.
    :type web_job_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_triggered_web_job_slot(request: web.Request, resource_group_name, name, web_job_name, slot, subscription_id, api_version) -> web.Response:
    """Delete a triggered web job by its ID for an app, or a deployment slot.

    Delete a triggered web job by its ID for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param web_job_name: Name of Web Job.
    :type web_job_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_vnet_connection(request: web.Request, resource_group_name, name, vnet_name, subscription_id, api_version) -> web.Response:
    """Deletes a connection from an app (or deployment slot to a named virtual network.

    Deletes a connection from an app (or deployment slot to a named virtual network.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param vnet_name: Name of the virtual network.
    :type vnet_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_delete_vnet_connection_slot(request: web.Request, resource_group_name, name, vnet_name, slot, subscription_id, api_version) -> web.Response:
    """Deletes a connection from an app (or deployment slot to a named virtual network.

    Deletes a connection from an app (or deployment slot to a named virtual network.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param vnet_name: Name of the virtual network.
    :type vnet_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will delete the connection for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_discover_restore(request: web.Request, resource_group_name, name, subscription_id, api_version, request) -> web.Response:
    """Discovers an existing app backup that can be restored from a blob in Azure storage.

    Discovers an existing app backup that can be restored from a blob in Azure storage.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: A RestoreRequest object that includes Azure storage URL and blog name for discovery of backup.
    :type request: dict | bytes

    """
    request = RestoreRequest.from_dict(request)
    return web.Response(status=200)


async def web_apps_discover_restore_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, request) -> web.Response:
    """Discovers an existing app backup that can be restored from a blob in Azure storage.

    Discovers an existing app backup that can be restored from a blob in Azure storage.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will perform discovery for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: A RestoreRequest object that includes Azure storage URL and blog name for discovery of backup.
    :type request: dict | bytes

    """
    request = RestoreRequest.from_dict(request)
    return web.Response(status=200)


async def web_apps_generate_new_site_publishing_password(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Generates a new publishing password for an app (or deployment slot, if specified).

    Generates a new publishing password for an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_generate_new_site_publishing_password_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Generates a new publishing password for an app (or deployment slot, if specified).

    Generates a new publishing password for an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API generate a new publishing password for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the details of a web, mobile, or API app.

    Gets the details of a web, mobile, or API app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_auth_settings(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the Authentication/Authorization settings of an app.

    Gets the Authentication/Authorization settings of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_auth_settings_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the Authentication/Authorization settings of an app.

    Gets the Authentication/Authorization settings of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get the settings for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_backup_configuration(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the backup configuration of an app.

    Gets the backup configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_backup_configuration_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the backup configuration of an app.

    Gets the backup configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get the backup configuration for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_backup_status(request: web.Request, resource_group_name, name, backup_id, subscription_id, api_version) -> web.Response:
    """Gets a backup of an app by its ID.

    Gets a backup of an app by its ID.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param backup_id: ID of the backup.
    :type backup_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_backup_status_slot(request: web.Request, resource_group_name, name, backup_id, slot, subscription_id, api_version) -> web.Response:
    """Gets a backup of an app by its ID.

    Gets a backup of an app by its ID.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param backup_id: ID of the backup.
    :type backup_id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get a backup of the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_configuration(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc.

    Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_configuration_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc.

    Gets the configuration of an app, such as platform version and bitness, default documents, virtual applications, Always On, etc.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will return configuration for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_configuration_snapshot(request: web.Request, resource_group_name, name, snapshot_id, subscription_id, api_version) -> web.Response:
    """Gets a snapshot of the configuration of an app at a previous point in time.

    Gets a snapshot of the configuration of an app at a previous point in time.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param snapshot_id: The ID of the snapshot to read.
    :type snapshot_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_configuration_snapshot_slot(request: web.Request, resource_group_name, name, snapshot_id, slot, subscription_id, api_version) -> web.Response:
    """Gets a snapshot of the configuration of an app at a previous point in time.

    Gets a snapshot of the configuration of an app at a previous point in time.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param snapshot_id: The ID of the snapshot to read.
    :type snapshot_id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will return configuration for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_continuous_web_job(request: web.Request, resource_group_name, name, web_job_name, subscription_id, api_version) -> web.Response:
    """Gets a continuous web job by its ID for an app, or a deployment slot.

    Gets a continuous web job by its ID for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param web_job_name: Name of Web Job.
    :type web_job_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_continuous_web_job_slot(request: web.Request, resource_group_name, name, web_job_name, slot, subscription_id, api_version) -> web.Response:
    """Gets a continuous web job by its ID for an app, or a deployment slot.

    Gets a continuous web job by its ID for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param web_job_name: Name of Web Job.
    :type web_job_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_deployment(request: web.Request, resource_group_name, name, id, subscription_id, api_version) -> web.Response:
    """Get a deployment by its ID for an app, or a deployment slot.

    Get a deployment by its ID for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param id: Deployment ID.
    :type id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_deployment_slot(request: web.Request, resource_group_name, name, id, slot, subscription_id, api_version) -> web.Response:
    """Get a deployment by its ID for an app, or a deployment slot.

    Get a deployment by its ID for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param id: Deployment ID.
    :type id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API gets a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_diagnostic_logs_configuration(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the logging configuration of an app.

    Gets the logging configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_diagnostic_logs_configuration_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the logging configuration of an app.

    Gets the logging configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get the logging configuration for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_domain_ownership_identifier(request: web.Request, resource_group_name, name, domain_ownership_identifier_name, subscription_id, api_version) -> web.Response:
    """Get domain ownership identifier for web app.

    Get domain ownership identifier for web app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param domain_ownership_identifier_name: Name of domain ownership identifier.
    :type domain_ownership_identifier_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_domain_ownership_identifier_slot(request: web.Request, resource_group_name, name, domain_ownership_identifier_name, slot, subscription_id, api_version) -> web.Response:
    """Get domain ownership identifier for web app.

    Get domain ownership identifier for web app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param domain_ownership_identifier_name: Name of domain ownership identifier.
    :type domain_ownership_identifier_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_function(request: web.Request, resource_group_name, name, function_name, subscription_id, api_version) -> web.Response:
    """Get function information by its ID for web site, or a deployment slot.

    Get function information by its ID for web site, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param function_name: Function name.
    :type function_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_functions_admin_token(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Fetch a short lived token that can be exchanged for a master key.

    Fetch a short lived token that can be exchanged for a master key.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_functions_admin_token_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Fetch a short lived token that can be exchanged for a master key.

    Fetch a short lived token that can be exchanged for a master key.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_host_name_binding(request: web.Request, resource_group_name, name, host_name, subscription_id, api_version) -> web.Response:
    """Get the named hostname binding for an app (or deployment slot, if specified).

    Get the named hostname binding for an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param host_name: Hostname in the hostname binding.
    :type host_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_host_name_binding_slot(request: web.Request, resource_group_name, name, slot, host_name, subscription_id, api_version) -> web.Response:
    """Get the named hostname binding for an app (or deployment slot, if specified).

    Get the named hostname binding for an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API the named binding for the production slot.
    :type slot: str
    :param host_name: Hostname in the hostname binding.
    :type host_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_hybrid_connection(request: web.Request, resource_group_name, name, namespace_name, relay_name, subscription_id, api_version) -> web.Response:
    """Retrieves a specific Service Bus Hybrid Connection used by this Web App.

    Retrieves a specific Service Bus Hybrid Connection used by this Web App.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: The name of the web app.
    :type name: str
    :param namespace_name: The namespace for this hybrid connection.
    :type namespace_name: str
    :param relay_name: The relay name for this hybrid connection.
    :type relay_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_hybrid_connection_slot(request: web.Request, resource_group_name, name, namespace_name, relay_name, slot, subscription_id, api_version) -> web.Response:
    """Retrieves a specific Service Bus Hybrid Connection used by this Web App.

    Retrieves a specific Service Bus Hybrid Connection used by this Web App.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: The name of the web app.
    :type name: str
    :param namespace_name: The namespace for this hybrid connection.
    :type namespace_name: str
    :param relay_name: The relay name for this hybrid connection.
    :type relay_name: str
    :param slot: The name of the slot for the web app.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_instance_function_slot(request: web.Request, resource_group_name, name, function_name, slot, subscription_id, api_version) -> web.Response:
    """Get function information by its ID for web site, or a deployment slot.

    Get function information by its ID for web site, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param function_name: Function name.
    :type function_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_instance_ms_deploy_log(request: web.Request, resource_group_name, name, instance_id, subscription_id, api_version) -> web.Response:
    """Get the MSDeploy Log for the last MSDeploy operation.

    Get the MSDeploy Log for the last MSDeploy operation.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param instance_id: ID of web app instance.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_instance_ms_deploy_log_slot(request: web.Request, resource_group_name, name, slot, instance_id, subscription_id, api_version) -> web.Response:
    """Get the MSDeploy Log for the last MSDeploy operation.

    Get the MSDeploy Log for the last MSDeploy operation.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param instance_id: ID of web app instance.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_instance_ms_deploy_status(request: web.Request, resource_group_name, name, instance_id, subscription_id, api_version) -> web.Response:
    """Get the status of the last MSDeploy operation.

    Get the status of the last MSDeploy operation.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param instance_id: ID of web app instance.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_instance_ms_deploy_status_slot(request: web.Request, resource_group_name, name, slot, instance_id, subscription_id, api_version) -> web.Response:
    """Get the status of the last MSDeploy operation.

    Get the status of the last MSDeploy operation.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param instance_id: ID of web app instance.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_instance_process(request: web.Request, resource_group_name, name, process_id, instance_id, subscription_id, api_version) -> web.Response:
    """Get process information by its ID for a specific scaled-out instance in a web site.

    Get process information by its ID for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param instance_id: ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_instance_process_dump(request: web.Request, resource_group_name, name, process_id, instance_id, subscription_id, api_version) -> web.Response:
    """Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.

    Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param instance_id: ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_instance_process_dump_slot(request: web.Request, resource_group_name, name, process_id, slot, instance_id, subscription_id, api_version) -> web.Response:
    """Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.

    Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
    :type slot: str
    :param instance_id: ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_instance_process_module(request: web.Request, resource_group_name, name, process_id, base_address, instance_id, subscription_id, api_version) -> web.Response:
    """Get process information by its ID for a specific scaled-out instance in a web site.

    Get process information by its ID for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param base_address: Module base address.
    :type base_address: str
    :param instance_id: ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_instance_process_module_slot(request: web.Request, resource_group_name, name, process_id, base_address, slot, instance_id, subscription_id, api_version) -> web.Response:
    """Get process information by its ID for a specific scaled-out instance in a web site.

    Get process information by its ID for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param base_address: Module base address.
    :type base_address: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
    :type slot: str
    :param instance_id: ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_instance_process_slot(request: web.Request, resource_group_name, name, process_id, slot, instance_id, subscription_id, api_version) -> web.Response:
    """Get process information by its ID for a specific scaled-out instance in a web site.

    Get process information by its ID for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
    :type slot: str
    :param instance_id: ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_instance_process_thread(request: web.Request, resource_group_name, name, process_id, thread_id, instance_id, subscription_id, api_version) -> web.Response:
    """Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.

    Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param thread_id: TID.
    :type thread_id: str
    :param instance_id: ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_instance_process_thread_slot(request: web.Request, resource_group_name, name, process_id, thread_id, slot, instance_id, subscription_id, api_version) -> web.Response:
    """Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.

    Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param thread_id: TID.
    :type thread_id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
    :type slot: str
    :param instance_id: ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_migrate_my_sql_status(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled

    Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_migrate_my_sql_status_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled

    Returns the status of MySql in app migration, if one is active, and whether or not MySql in app is enabled

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param slot: Name of the deployment slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_ms_deploy_log(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get the MSDeploy Log for the last MSDeploy operation.

    Get the MSDeploy Log for the last MSDeploy operation.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_ms_deploy_log_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Get the MSDeploy Log for the last MSDeploy operation.

    Get the MSDeploy Log for the last MSDeploy operation.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_ms_deploy_status(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get the status of the last MSDeploy operation.

    Get the status of the last MSDeploy operation.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_ms_deploy_status_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Get the status of the last MSDeploy operation.

    Get the status of the last MSDeploy operation.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_premier_add_on(request: web.Request, resource_group_name, name, premier_add_on_name, subscription_id, api_version) -> web.Response:
    """Gets a named add-on of an app.

    Gets a named add-on of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param premier_add_on_name: Add-on name.
    :type premier_add_on_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_premier_add_on_slot(request: web.Request, resource_group_name, name, premier_add_on_name, slot, subscription_id, api_version) -> web.Response:
    """Gets a named add-on of an app.

    Gets a named add-on of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param premier_add_on_name: Add-on name.
    :type premier_add_on_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get the named add-on for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_process(request: web.Request, resource_group_name, name, process_id, subscription_id, api_version) -> web.Response:
    """Get process information by its ID for a specific scaled-out instance in a web site.

    Get process information by its ID for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_process_dump(request: web.Request, resource_group_name, name, process_id, subscription_id, api_version) -> web.Response:
    """Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.

    Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_process_dump_slot(request: web.Request, resource_group_name, name, process_id, slot, subscription_id, api_version) -> web.Response:
    """Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.

    Get a memory dump of a process by its ID for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_process_module(request: web.Request, resource_group_name, name, process_id, base_address, subscription_id, api_version) -> web.Response:
    """Get process information by its ID for a specific scaled-out instance in a web site.

    Get process information by its ID for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param base_address: Module base address.
    :type base_address: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_process_module_slot(request: web.Request, resource_group_name, name, process_id, base_address, slot, subscription_id, api_version) -> web.Response:
    """Get process information by its ID for a specific scaled-out instance in a web site.

    Get process information by its ID for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param base_address: Module base address.
    :type base_address: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_process_slot(request: web.Request, resource_group_name, name, process_id, slot, subscription_id, api_version) -> web.Response:
    """Get process information by its ID for a specific scaled-out instance in a web site.

    Get process information by its ID for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_process_thread(request: web.Request, resource_group_name, name, process_id, thread_id, subscription_id, api_version) -> web.Response:
    """Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.

    Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param thread_id: TID.
    :type thread_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_process_thread_slot(request: web.Request, resource_group_name, name, process_id, thread_id, slot, subscription_id, api_version) -> web.Response:
    """Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.

    Get thread information by Thread ID for a specific process, in a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param thread_id: TID.
    :type thread_id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_public_certificate(request: web.Request, resource_group_name, name, public_certificate_name, subscription_id, api_version) -> web.Response:
    """Get the named public certificate for an app (or deployment slot, if specified).

    Get the named public certificate for an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param public_certificate_name: Public certificate name.
    :type public_certificate_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_public_certificate_slot(request: web.Request, resource_group_name, name, slot, public_certificate_name, subscription_id, api_version) -> web.Response:
    """Get the named public certificate for an app (or deployment slot, if specified).

    Get the named public certificate for an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API the named binding for the production slot.
    :type slot: str
    :param public_certificate_name: Public certificate name.
    :type public_certificate_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_relay_service_connection(request: web.Request, resource_group_name, name, entity_name, subscription_id, api_version) -> web.Response:
    """Gets a hybrid connection configuration by its name.

    Gets a hybrid connection configuration by its name.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param entity_name: Name of the hybrid connection.
    :type entity_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_relay_service_connection_slot(request: web.Request, resource_group_name, name, entity_name, slot, subscription_id, api_version) -> web.Response:
    """Gets a hybrid connection configuration by its name.

    Gets a hybrid connection configuration by its name.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param entity_name: Name of the hybrid connection.
    :type entity_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get a hybrid connection for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_site_extension(request: web.Request, resource_group_name, name, site_extension_id, subscription_id, api_version) -> web.Response:
    """Get site extension information by its ID for a web site, or a deployment slot.

    Get site extension information by its ID for a web site, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param site_extension_id: Site extension name.
    :type site_extension_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_site_extension_slot(request: web.Request, resource_group_name, name, site_extension_id, slot, subscription_id, api_version) -> web.Response:
    """Get site extension information by its ID for a web site, or a deployment slot.

    Get site extension information by its ID for a web site, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param site_extension_id: Site extension name.
    :type site_extension_id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_site_php_error_log_flag(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets web app&#39;s event logs.

    Gets web app&#39;s event logs.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_site_php_error_log_flag_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets web app&#39;s event logs.

    Gets web app&#39;s event logs.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the details of a web, mobile, or API app.

    Gets the details of a web, mobile, or API app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. By default, this API returns the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_source_control(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the source control configuration of an app.

    Gets the source control configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_source_control_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the source control configuration of an app.

    Gets the source control configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get the source control configuration for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_triggered_web_job(request: web.Request, resource_group_name, name, web_job_name, subscription_id, api_version) -> web.Response:
    """Gets a triggered web job by its ID for an app, or a deployment slot.

    Gets a triggered web job by its ID for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param web_job_name: Name of Web Job.
    :type web_job_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_triggered_web_job_history(request: web.Request, resource_group_name, name, web_job_name, id, subscription_id, api_version) -> web.Response:
    """Gets a triggered web job&#39;s history by its ID for an app, , or a deployment slot.

    Gets a triggered web job&#39;s history by its ID for an app, , or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param web_job_name: Name of Web Job.
    :type web_job_name: str
    :param id: History ID.
    :type id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_triggered_web_job_history_slot(request: web.Request, resource_group_name, name, web_job_name, id, slot, subscription_id, api_version) -> web.Response:
    """Gets a triggered web job&#39;s history by its ID for an app, , or a deployment slot.

    Gets a triggered web job&#39;s history by its ID for an app, , or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param web_job_name: Name of Web Job.
    :type web_job_name: str
    :param id: History ID.
    :type id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_triggered_web_job_slot(request: web.Request, resource_group_name, name, web_job_name, slot, subscription_id, api_version) -> web.Response:
    """Gets a triggered web job by its ID for an app, or a deployment slot.

    Gets a triggered web job by its ID for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param web_job_name: Name of Web Job.
    :type web_job_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_vnet_connection(request: web.Request, resource_group_name, name, vnet_name, subscription_id, api_version) -> web.Response:
    """Gets a virtual network the app (or deployment slot) is connected to by name.

    Gets a virtual network the app (or deployment slot) is connected to by name.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param vnet_name: Name of the virtual network.
    :type vnet_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_vnet_connection_gateway(request: web.Request, resource_group_name, name, vnet_name, gateway_name, subscription_id, api_version) -> web.Response:
    """Gets an app&#39;s Virtual Network gateway.

    Gets an app&#39;s Virtual Network gateway.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param vnet_name: Name of the Virtual Network.
    :type vnet_name: str
    :param gateway_name: Name of the gateway. Currently, the only supported string is \&quot;primary\&quot;.
    :type gateway_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_vnet_connection_gateway_slot(request: web.Request, resource_group_name, name, vnet_name, gateway_name, slot, subscription_id, api_version) -> web.Response:
    """Gets an app&#39;s Virtual Network gateway.

    Gets an app&#39;s Virtual Network gateway.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param vnet_name: Name of the Virtual Network.
    :type vnet_name: str
    :param gateway_name: Name of the gateway. Currently, the only supported string is \&quot;primary\&quot;.
    :type gateway_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get a gateway for the production slot&#39;s Virtual Network.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_vnet_connection_slot(request: web.Request, resource_group_name, name, vnet_name, slot, subscription_id, api_version) -> web.Response:
    """Gets a virtual network the app (or deployment slot) is connected to by name.

    Gets a virtual network the app (or deployment slot) is connected to by name.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param vnet_name: Name of the virtual network.
    :type vnet_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get the named virtual network for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_web_job(request: web.Request, resource_group_name, name, web_job_name, subscription_id, api_version) -> web.Response:
    """Get webjob information for an app, or a deployment slot.

    Get webjob information for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param web_job_name: Name of the web job.
    :type web_job_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_web_job_slot(request: web.Request, resource_group_name, name, web_job_name, slot, subscription_id, api_version) -> web.Response:
    """Get webjob information for an app, or a deployment slot.

    Get webjob information for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param web_job_name: Name of the web job.
    :type web_job_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_web_site_container_logs(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the last lines of docker logs for the given site

    Gets the last lines of docker logs for the given site

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_web_site_container_logs_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the last lines of docker logs for the given site

    Gets the last lines of docker logs for the given site

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_web_site_container_logs_zip(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the ZIP archived docker log files for the given site

    Gets the ZIP archived docker log files for the given site

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_get_web_site_container_logs_zip_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the ZIP archived docker log files for the given site

    Gets the ZIP archived docker log files for the given site

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_install_site_extension(request: web.Request, resource_group_name, name, site_extension_id, subscription_id, api_version) -> web.Response:
    """Install site extension on a web site, or a deployment slot.

    Install site extension on a web site, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param site_extension_id: Site extension name.
    :type site_extension_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_install_site_extension_slot(request: web.Request, resource_group_name, name, site_extension_id, slot, subscription_id, api_version) -> web.Response:
    """Install site extension on a web site, or a deployment slot.

    Install site extension on a web site, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param site_extension_id: Site extension name.
    :type site_extension_id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_is_cloneable(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Shows whether an app can be cloned to another resource group or subscription.

    Shows whether an app can be cloned to another resource group or subscription.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_is_cloneable_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Shows whether an app can be cloned to another resource group or subscription.

    Shows whether an app can be cloned to another resource group or subscription.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. By default, this API returns information on the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """Get all apps for a subscription.

    Get all apps for a subscription.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_application_settings(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the application settings of an app.

    Gets the application settings of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_application_settings_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the application settings of an app.

    Gets the application settings of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get the application settings for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_backup_status_secrets(request: web.Request, resource_group_name, name, backup_id, subscription_id, api_version, request) -> web.Response:
    """Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.

    Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param backup_id: ID of backup.
    :type backup_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: Information on backup request.
    :type request: dict | bytes

    """
    request = BackupRequest.from_dict(request)
    return web.Response(status=200)


async def web_apps_list_backup_status_secrets_slot(request: web.Request, resource_group_name, name, backup_id, slot, subscription_id, api_version, request) -> web.Response:
    """Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.

    Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param backup_id: ID of backup.
    :type backup_id: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: Information on backup request.
    :type request: dict | bytes

    """
    request = BackupRequest.from_dict(request)
    return web.Response(status=200)


async def web_apps_list_backups(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets existing backups of an app.

    Gets existing backups of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_backups_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets existing backups of an app.

    Gets existing backups of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get backups of the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version, include_slots=None) -> web.Response:
    """Gets all web, mobile, and API apps in the specified resource group.

    Gets all web, mobile, and API apps in the specified resource group.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param include_slots: Specify &lt;strong&gt;true&lt;/strong&gt; to include deployment slots in results. The default is false, which only gives you the production slot of all apps.
    :type include_slots: bool

    """
    return web.Response(status=200)


async def web_apps_list_configuration_snapshot_info(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot.

    Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_configuration_snapshot_info_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot.

    Gets a list of web app configuration snapshots identifiers. Each element of the list contains a timestamp and the ID of the snapshot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will return configuration for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_configurations(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """List the configurations of an app

    List the configurations of an app

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_configurations_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """List the configurations of an app

    List the configurations of an app

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will return configuration for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_connection_strings(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the connection strings of an app.

    Gets the connection strings of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_connection_strings_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the connection strings of an app.

    Gets the connection strings of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get the connection settings for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_continuous_web_jobs(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """List continuous web jobs for an app, or a deployment slot.

    List continuous web jobs for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_continuous_web_jobs_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """List continuous web jobs for an app, or a deployment slot.

    List continuous web jobs for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_deployment_log(request: web.Request, resource_group_name, name, id, subscription_id, api_version) -> web.Response:
    """List deployment log for specific deployment for an app, or a deployment slot.

    List deployment log for specific deployment for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param id: The ID of a specific deployment. This is the value of the name property in the JSON response from \&quot;GET /api/sites/{siteName}/deployments\&quot;.
    :type id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_deployment_log_slot(request: web.Request, resource_group_name, name, id, slot, subscription_id, api_version) -> web.Response:
    """List deployment log for specific deployment for an app, or a deployment slot.

    List deployment log for specific deployment for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param id: The ID of a specific deployment. This is the value of the name property in the JSON response from \&quot;GET /api/sites/{siteName}/deployments\&quot;.
    :type id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_deployments(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """List deployments for an app, or a deployment slot.

    List deployments for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_deployments_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """List deployments for an app, or a deployment slot.

    List deployments for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_domain_ownership_identifiers(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Lists ownership identifiers for domain associated with web app.

    Lists ownership identifiers for domain associated with web app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_domain_ownership_identifiers_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Lists ownership identifiers for domain associated with web app.

    Lists ownership identifiers for domain associated with web app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_function_secrets(request: web.Request, resource_group_name, name, function_name, subscription_id, api_version) -> web.Response:
    """Get function secrets for a function in a web site, or a deployment slot.

    Get function secrets for a function in a web site, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param function_name: Function name.
    :type function_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_function_secrets_slot(request: web.Request, resource_group_name, name, function_name, slot, subscription_id, api_version) -> web.Response:
    """Get function secrets for a function in a web site, or a deployment slot.

    Get function secrets for a function in a web site, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param function_name: Function name.
    :type function_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_functions(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """List the functions for a web site, or a deployment slot.

    List the functions for a web site, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_host_name_bindings(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get hostname bindings for an app or a deployment slot.

    Get hostname bindings for an app or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_host_name_bindings_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Get hostname bindings for an app or a deployment slot.

    Get hostname bindings for an app or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API gets hostname bindings for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_hybrid_connection_keys(request: web.Request, resource_group_name, name, namespace_name, relay_name, subscription_id, api_version) -> web.Response:
    """Gets the send key name and value for a Hybrid Connection.

    Gets the send key name and value for a Hybrid Connection.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: The name of the web app.
    :type name: str
    :param namespace_name: The namespace for this hybrid connection.
    :type namespace_name: str
    :param relay_name: The relay name for this hybrid connection.
    :type relay_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_hybrid_connection_keys_slot(request: web.Request, resource_group_name, name, namespace_name, relay_name, slot, subscription_id, api_version) -> web.Response:
    """Gets the send key name and value for a Hybrid Connection.

    Gets the send key name and value for a Hybrid Connection.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: The name of the web app.
    :type name: str
    :param namespace_name: The namespace for this hybrid connection.
    :type namespace_name: str
    :param relay_name: The relay name for this hybrid connection.
    :type relay_name: str
    :param slot: The name of the slot for the web app.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_hybrid_connections(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Retrieves all Service Bus Hybrid Connections used by this Web App.

    Retrieves all Service Bus Hybrid Connections used by this Web App.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: The name of the web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_hybrid_connections_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Retrieves all Service Bus Hybrid Connections used by this Web App.

    Retrieves all Service Bus Hybrid Connections used by this Web App.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: The name of the web app.
    :type name: str
    :param slot: The name of the slot for the web app.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_instance_functions_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """List the functions for a web site, or a deployment slot.

    List the functions for a web site, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_instance_identifiers(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets all scale-out instances of an app.

    Gets all scale-out instances of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_instance_identifiers_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets all scale-out instances of an app.

    Gets all scale-out instances of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API gets the production slot instances.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_instance_process_modules(request: web.Request, resource_group_name, name, process_id, instance_id, subscription_id, api_version) -> web.Response:
    """List module information for a process by its ID for a specific scaled-out instance in a web site.

    List module information for a process by its ID for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param instance_id: ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_instance_process_modules_slot(request: web.Request, resource_group_name, name, process_id, slot, instance_id, subscription_id, api_version) -> web.Response:
    """List module information for a process by its ID for a specific scaled-out instance in a web site.

    List module information for a process by its ID for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
    :type slot: str
    :param instance_id: ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_instance_process_threads(request: web.Request, resource_group_name, name, process_id, instance_id, subscription_id, api_version) -> web.Response:
    """List the threads in a process by its ID for a specific scaled-out instance in a web site.

    List the threads in a process by its ID for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param instance_id: ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_instance_process_threads_slot(request: web.Request, resource_group_name, name, process_id, slot, instance_id, subscription_id, api_version) -> web.Response:
    """List the threads in a process by its ID for a specific scaled-out instance in a web site.

    List the threads in a process by its ID for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
    :type slot: str
    :param instance_id: ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_instance_processes(request: web.Request, resource_group_name, name, instance_id, subscription_id, api_version) -> web.Response:
    """Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.

    Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param instance_id: ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_instance_processes_slot(request: web.Request, resource_group_name, name, slot, instance_id, subscription_id, api_version) -> web.Response:
    """Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.

    Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
    :type slot: str
    :param instance_id: ID of a specific scaled-out instance. This is the value of the name property in the JSON response from \&quot;GET api/sites/{siteName}/instances\&quot;.
    :type instance_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_metadata(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the metadata of an app.

    Gets the metadata of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_metadata_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the metadata of an app.

    Gets the metadata of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get the metadata for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_metric_definitions(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets all metric definitions of an app (or deployment slot, if specified).

    Gets all metric definitions of an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_metric_definitions_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets all metric definitions of an app (or deployment slot, if specified).

    Gets all metric definitions of an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get metric definitions of the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_metrics(request: web.Request, resource_group_name, name, subscription_id, api_version, details=None, filter=None) -> web.Response:
    """Gets performance metrics of an app (or deployment slot, if specified).

    Gets performance metrics of an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param details: Specify \&quot;true\&quot; to include metric details in the response. It is \&quot;false\&quot; by default.
    :type details: bool
    :param filter: Return only metrics specified in the filter (using OData syntax). For example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;.
    :type filter: str

    """
    return web.Response(status=200)


async def web_apps_list_metrics_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, details=None, filter=None) -> web.Response:
    """Gets performance metrics of an app (or deployment slot, if specified).

    Gets performance metrics of an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get metrics of the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param details: Specify \&quot;true\&quot; to include metric details in the response. It is \&quot;false\&quot; by default.
    :type details: bool
    :param filter: Return only metrics specified in the filter (using OData syntax). For example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;.
    :type filter: str

    """
    return web.Response(status=200)


async def web_apps_list_network_features(request: web.Request, resource_group_name, name, view, subscription_id, api_version) -> web.Response:
    """Gets all network features used by the app (or deployment slot, if specified).

    Gets all network features used by the app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param view: The type of view. This can either be \&quot;summary\&quot; or \&quot;detailed\&quot;.
    :type view: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_network_features_slot(request: web.Request, resource_group_name, name, view, slot, subscription_id, api_version) -> web.Response:
    """Gets all network features used by the app (or deployment slot, if specified).

    Gets all network features used by the app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param view: The type of view. This can either be \&quot;summary\&quot; or \&quot;detailed\&quot;.
    :type view: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get network features for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_perf_mon_counters(request: web.Request, resource_group_name, name, subscription_id, api_version, filter=None) -> web.Response:
    """Gets perfmon counters for web app.

    Gets perfmon counters for web app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param filter: Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;.
    :type filter: str

    """
    return web.Response(status=200)


async def web_apps_list_perf_mon_counters_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, filter=None) -> web.Response:
    """Gets perfmon counters for web app.

    Gets perfmon counters for web app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param filter: Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;.
    :type filter: str

    """
    return web.Response(status=200)


async def web_apps_list_premier_add_ons(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the premier add-ons of an app.

    Gets the premier add-ons of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_premier_add_ons_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the premier add-ons of an app.

    Gets the premier add-ons of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get the premier add-ons for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_process_modules(request: web.Request, resource_group_name, name, process_id, subscription_id, api_version) -> web.Response:
    """List module information for a process by its ID for a specific scaled-out instance in a web site.

    List module information for a process by its ID for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_process_modules_slot(request: web.Request, resource_group_name, name, process_id, slot, subscription_id, api_version) -> web.Response:
    """List module information for a process by its ID for a specific scaled-out instance in a web site.

    List module information for a process by its ID for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_process_threads(request: web.Request, resource_group_name, name, process_id, subscription_id, api_version) -> web.Response:
    """List the threads in a process by its ID for a specific scaled-out instance in a web site.

    List the threads in a process by its ID for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_process_threads_slot(request: web.Request, resource_group_name, name, process_id, slot, subscription_id, api_version) -> web.Response:
    """List the threads in a process by its ID for a specific scaled-out instance in a web site.

    List the threads in a process by its ID for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param process_id: PID.
    :type process_id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_processes(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.

    Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_processes_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.

    Get list of processes for a web site, or a deployment slot, or for a specific scaled-out instance in a web site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_public_certificates(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get public certificates for an app or a deployment slot.

    Get public certificates for an app or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_public_certificates_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Get public certificates for an app or a deployment slot.

    Get public certificates for an app or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API gets hostname bindings for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_publishing_credentials(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the Git/FTP publishing credentials of an app.

    Gets the Git/FTP publishing credentials of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_publishing_credentials_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the Git/FTP publishing credentials of an app.

    Gets the Git/FTP publishing credentials of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get the publishing credentials for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_publishing_profile_xml_with_secrets(request: web.Request, resource_group_name, name, subscription_id, api_version, publishing_profile_options) -> web.Response:
    """Gets the publishing profile for an app (or deployment slot, if specified).

    Gets the publishing profile for an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param publishing_profile_options: Specifies publishingProfileOptions for publishing profile. For example, use {\&quot;format\&quot;: \&quot;FileZilla3\&quot;} to get a FileZilla publishing profile.
    :type publishing_profile_options: dict | bytes

    """
    publishing_profile_options = CsmPublishingProfileOptions.from_dict(publishing_profile_options)
    return web.Response(status=200)


async def web_apps_list_publishing_profile_xml_with_secrets_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, publishing_profile_options) -> web.Response:
    """Gets the publishing profile for an app (or deployment slot, if specified).

    Gets the publishing profile for an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get the publishing profile for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param publishing_profile_options: Specifies publishingProfileOptions for publishing profile. For example, use {\&quot;format\&quot;: \&quot;FileZilla3\&quot;} to get a FileZilla publishing profile.
    :type publishing_profile_options: dict | bytes

    """
    publishing_profile_options = CsmPublishingProfileOptions.from_dict(publishing_profile_options)
    return web.Response(status=200)


async def web_apps_list_relay_service_connections(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets hybrid connections configured for an app (or deployment slot, if specified).

    Gets hybrid connections configured for an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_relay_service_connections_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets hybrid connections configured for an app (or deployment slot, if specified).

    Gets hybrid connections configured for an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get hybrid connections for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_site_extensions(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get list of site extensions for a web site, or a deployment slot.

    Get list of site extensions for a web site, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_site_extensions_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Get list of site extensions for a web site, or a deployment slot.

    Get list of site extensions for a web site, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_site_push_settings(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the Push settings associated with web app.

    Gets the Push settings associated with web app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_site_push_settings_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the Push settings associated with web app.

    Gets the Push settings associated with web app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_slot_configuration_names(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the names of app settings and connection strings that stick to the slot (not swapped).

    Gets the names of app settings and connection strings that stick to the slot (not swapped).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_slot_differences_from_production(request: web.Request, resource_group_name, name, subscription_id, api_version, slot_swap_entity) -> web.Response:
    """Get the difference in configuration settings between two web app slots.

    Get the difference in configuration settings between two web app slots.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param slot_swap_entity: JSON object that contains the target slot name. See example.
    :type slot_swap_entity: dict | bytes

    """
    slot_swap_entity = CsmSlotEntity.from_dict(slot_swap_entity)
    return web.Response(status=200)


async def web_apps_list_slot_differences_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, slot_swap_entity) -> web.Response:
    """Get the difference in configuration settings between two web app slots.

    Get the difference in configuration settings between two web app slots.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the source slot. If a slot is not specified, the production slot is used as the source slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param slot_swap_entity: JSON object that contains the target slot name. See example.
    :type slot_swap_entity: dict | bytes

    """
    slot_swap_entity = CsmSlotEntity.from_dict(slot_swap_entity)
    return web.Response(status=200)


async def web_apps_list_slots(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets an app&#39;s deployment slots.

    Gets an app&#39;s deployment slots.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_snapshots(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Returns all Snapshots to the user.

    Returns all Snapshots to the user.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Website Name.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_snapshots_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Returns all Snapshots to the user.

    Returns all Snapshots to the user.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Website Name.
    :type name: str
    :param slot: Website Slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_sync_function_triggers(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """This is to allow calling via powershell and ARM template.

    This is to allow calling via powershell and ARM template.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_sync_function_triggers_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """This is to allow calling via powershell and ARM template.

    This is to allow calling via powershell and ARM template.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will restore a backup of the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_triggered_web_job_history(request: web.Request, resource_group_name, name, web_job_name, subscription_id, api_version) -> web.Response:
    """List a triggered web job&#39;s history for an app, or a deployment slot.

    List a triggered web job&#39;s history for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param web_job_name: Name of Web Job.
    :type web_job_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_triggered_web_job_history_slot(request: web.Request, resource_group_name, name, web_job_name, slot, subscription_id, api_version) -> web.Response:
    """List a triggered web job&#39;s history for an app, or a deployment slot.

    List a triggered web job&#39;s history for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param web_job_name: Name of Web Job.
    :type web_job_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_triggered_web_jobs(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """List triggered web jobs for an app, or a deployment slot.

    List triggered web jobs for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_triggered_web_jobs_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """List triggered web jobs for an app, or a deployment slot.

    List triggered web jobs for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_usages(request: web.Request, resource_group_name, name, subscription_id, api_version, filter=None) -> web.Response:
    """Gets the quota usage information of an app (or deployment slot, if specified).

    Gets the quota usage information of an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param filter: Return only information specified in the filter (using OData syntax). For example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;.
    :type filter: str

    """
    return web.Response(status=200)


async def web_apps_list_usages_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, filter=None) -> web.Response:
    """Gets the quota usage information of an app (or deployment slot, if specified).

    Gets the quota usage information of an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get quota information of the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param filter: Return only information specified in the filter (using OData syntax). For example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;.
    :type filter: str

    """
    return web.Response(status=200)


async def web_apps_list_vnet_connections(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the virtual networks the app (or deployment slot) is connected to.

    Gets the virtual networks the app (or deployment slot) is connected to.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_vnet_connections_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the virtual networks the app (or deployment slot) is connected to.

    Gets the virtual networks the app (or deployment slot) is connected to.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will get virtual network connections for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_web_jobs(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """List webjobs for an app, or a deployment slot.

    List webjobs for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_list_web_jobs_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """List webjobs for an app, or a deployment slot.

    List webjobs for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API returns deployments for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_migrate_my_sql(request: web.Request, resource_group_name, name, subscription_id, api_version, migration_request_envelope) -> web.Response:
    """Migrates a local (in-app) MySql database to a remote MySql database.

    Migrates a local (in-app) MySql database to a remote MySql database.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param migration_request_envelope: MySql migration options.
    :type migration_request_envelope: dict | bytes

    """
    migration_request_envelope = MigrateMySqlRequest.from_dict(migration_request_envelope)
    return web.Response(status=200)


async def web_apps_migrate_storage(request: web.Request, subscription_name, resource_group_name, name, subscription_id, api_version, migration_options) -> web.Response:
    """Restores a web app.

    Restores a web app.

    :param subscription_name: Azure subscription.
    :type subscription_name: str
    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param migration_options: Migration migrationOptions.
    :type migration_options: dict | bytes

    """
    migration_options = StorageMigrationOptions.from_dict(migration_options)
    return web.Response(status=200)


async def web_apps_recover(request: web.Request, resource_group_name, name, subscription_id, api_version, recovery_entity) -> web.Response:
    """Recovers a web app to a previous snapshot.

    Recovers a web app to a previous snapshot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param recovery_entity: Snapshot data used for web app recovery. Snapshot information can be obtained by calling GetDeletedSites or GetSiteSnapshots API.
    :type recovery_entity: dict | bytes

    """
    recovery_entity = WebAppsRecoverRequest.from_dict(recovery_entity)
    return web.Response(status=200)


async def web_apps_recover_site_configuration_snapshot(request: web.Request, resource_group_name, name, snapshot_id, subscription_id, api_version) -> web.Response:
    """Reverts the configuration of an app to a previous snapshot.

    Reverts the configuration of an app to a previous snapshot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param snapshot_id: The ID of the snapshot to read.
    :type snapshot_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_recover_site_configuration_snapshot_slot(request: web.Request, resource_group_name, name, snapshot_id, slot, subscription_id, api_version) -> web.Response:
    """Reverts the configuration of an app to a previous snapshot.

    Reverts the configuration of an app to a previous snapshot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param snapshot_id: The ID of the snapshot to read.
    :type snapshot_id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will return configuration for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_recover_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, recovery_entity) -> web.Response:
    """Recovers a web app to a previous snapshot.

    Recovers a web app to a previous snapshot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param recovery_entity: Snapshot data used for web app recovery. Snapshot information can be obtained by calling GetDeletedSites or GetSiteSnapshots API.
    :type recovery_entity: dict | bytes

    """
    recovery_entity = WebAppsRecoverRequest.from_dict(recovery_entity)
    return web.Response(status=200)


async def web_apps_reset_production_slot_config(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Resets the configuration settings of the current slot if they were previously modified by calling the API with POST.

    Resets the configuration settings of the current slot if they were previously modified by calling the API with POST.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_reset_slot_configuration_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Resets the configuration settings of the current slot if they were previously modified by calling the API with POST.

    Resets the configuration settings of the current slot if they were previously modified by calling the API with POST.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API resets configuration settings for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_restart(request: web.Request, resource_group_name, name, subscription_id, api_version, soft_restart=None, synchronous=None) -> web.Response:
    """Restarts an app (or deployment slot, if specified).

    Restarts an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param soft_restart: Specify true to apply the configuration settings and restarts the app only if necessary. By default, the API always restarts and reprovisions the app.
    :type soft_restart: bool
    :param synchronous: Specify true to block until the app is restarted. By default, it is set to false, and the API responds immediately (asynchronous).
    :type synchronous: bool

    """
    return web.Response(status=200)


async def web_apps_restart_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, soft_restart=None, synchronous=None) -> web.Response:
    """Restarts an app (or deployment slot, if specified).

    Restarts an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will restart the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param soft_restart: Specify true to apply the configuration settings and restarts the app only if necessary. By default, the API always restarts and reprovisions the app.
    :type soft_restart: bool
    :param synchronous: Specify true to block until the app is restarted. By default, it is set to false, and the API responds immediately (asynchronous).
    :type synchronous: bool

    """
    return web.Response(status=200)


async def web_apps_restore(request: web.Request, resource_group_name, name, backup_id, subscription_id, api_version, request) -> web.Response:
    """Restores a specific backup to another app (or deployment slot, if specified).

    Restores a specific backup to another app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param backup_id: ID of the backup.
    :type backup_id: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: Information on restore request .
    :type request: dict | bytes

    """
    request = RestoreRequest.from_dict(request)
    return web.Response(status=200)


async def web_apps_restore_slot(request: web.Request, resource_group_name, name, backup_id, slot, subscription_id, api_version, request) -> web.Response:
    """Restores a specific backup to another app (or deployment slot, if specified).

    Restores a specific backup to another app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param backup_id: ID of the backup.
    :type backup_id: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will restore a backup of the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: Information on restore request .
    :type request: dict | bytes

    """
    request = RestoreRequest.from_dict(request)
    return web.Response(status=200)


async def web_apps_run_triggered_web_job(request: web.Request, resource_group_name, name, web_job_name, subscription_id, api_version) -> web.Response:
    """Run a triggered web job for an app, or a deployment slot.

    Run a triggered web job for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param web_job_name: Name of Web Job.
    :type web_job_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_run_triggered_web_job_slot(request: web.Request, resource_group_name, name, web_job_name, slot, subscription_id, api_version) -> web.Response:
    """Run a triggered web job for an app, or a deployment slot.

    Run a triggered web job for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param web_job_name: Name of Web Job.
    :type web_job_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_start(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Starts an app (or deployment slot, if specified).

    Starts an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_start_continuous_web_job(request: web.Request, resource_group_name, name, web_job_name, subscription_id, api_version) -> web.Response:
    """Start a continuous web job for an app, or a deployment slot.

    Start a continuous web job for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param web_job_name: Name of Web Job.
    :type web_job_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_start_continuous_web_job_slot(request: web.Request, resource_group_name, name, web_job_name, slot, subscription_id, api_version) -> web.Response:
    """Start a continuous web job for an app, or a deployment slot.

    Start a continuous web job for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param web_job_name: Name of Web Job.
    :type web_job_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_start_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Starts an app (or deployment slot, if specified).

    Starts an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will start the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_start_web_site_network_trace(request: web.Request, resource_group_name, name, subscription_id, api_version, duration_in_seconds=None, max_frame_length=None, sas_url=None) -> web.Response:
    """Start capturing network packets for the site.

    Start capturing network packets for the site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: The name of the web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param duration_in_seconds: The duration to keep capturing in seconds.
    :type duration_in_seconds: int
    :param max_frame_length: The maximum frame length in bytes (Optional).
    :type max_frame_length: int
    :param sas_url: The Blob URL to store capture file.
    :type sas_url: str

    """
    return web.Response(status=200)


async def web_apps_start_web_site_network_trace_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, duration_in_seconds=None, max_frame_length=None, sas_url=None) -> web.Response:
    """Start capturing network packets for the site.

    Start capturing network packets for the site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: The name of the web app.
    :type name: str
    :param slot: The name of the slot for this web app.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param duration_in_seconds: The duration to keep capturing in seconds.
    :type duration_in_seconds: int
    :param max_frame_length: The maximum frame length in bytes (Optional).
    :type max_frame_length: int
    :param sas_url: The Blob URL to store capture file.
    :type sas_url: str

    """
    return web.Response(status=200)


async def web_apps_stop(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Stops an app (or deployment slot, if specified).

    Stops an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_stop_continuous_web_job(request: web.Request, resource_group_name, name, web_job_name, subscription_id, api_version) -> web.Response:
    """Stop a continuous web job for an app, or a deployment slot.

    Stop a continuous web job for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param web_job_name: Name of Web Job.
    :type web_job_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_stop_continuous_web_job_slot(request: web.Request, resource_group_name, name, web_job_name, slot, subscription_id, api_version) -> web.Response:
    """Stop a continuous web job for an app, or a deployment slot.

    Stop a continuous web job for an app, or a deployment slot.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Site name.
    :type name: str
    :param web_job_name: Name of Web Job.
    :type web_job_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API deletes a deployment for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_stop_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Stops an app (or deployment slot, if specified).

    Stops an app (or deployment slot, if specified).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will stop the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_stop_web_site_network_trace(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Stop ongoing capturing network packets for the site.

    Stop ongoing capturing network packets for the site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: The name of the web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_stop_web_site_network_trace_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Stop ongoing capturing network packets for the site.

    Stop ongoing capturing network packets for the site.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: The name of the web app.
    :type name: str
    :param slot: The name of the slot for this web app.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_swap_slot_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, slot_swap_entity) -> web.Response:
    """Swaps two deployment slots of an app.

    Swaps two deployment slots of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the source slot. If a slot is not specified, the production slot is used as the source slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param slot_swap_entity: JSON object that contains the target slot name. See example.
    :type slot_swap_entity: dict | bytes

    """
    slot_swap_entity = CsmSlotEntity.from_dict(slot_swap_entity)
    return web.Response(status=200)


async def web_apps_swap_slot_with_production(request: web.Request, resource_group_name, name, subscription_id, api_version, slot_swap_entity) -> web.Response:
    """Swaps two deployment slots of an app.

    Swaps two deployment slots of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param slot_swap_entity: JSON object that contains the target slot name. See example.
    :type slot_swap_entity: dict | bytes

    """
    slot_swap_entity = CsmSlotEntity.from_dict(slot_swap_entity)
    return web.Response(status=200)


async def web_apps_sync_function_triggers(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Syncs function trigger metadata to the scale controller

    Syncs function trigger metadata to the scale controller

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_sync_function_triggers_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Syncs function trigger metadata to the scale controller

    Syncs function trigger metadata to the scale controller

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will restore a backup of the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_sync_repository(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Sync web app repository.

    Sync web app repository.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_sync_repository_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Sync web app repository.

    Sync web app repository.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def web_apps_update(request: web.Request, resource_group_name, name, subscription_id, api_version, site_envelope) -> web.Response:
    """Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

    Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Unique name of the app to create or update. To create or update a deployment slot, use the {slot} parameter.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_envelope: A JSON representation of the app properties. See example.
    :type site_envelope: dict | bytes

    """
    site_envelope = SitePatchResource.from_dict(site_envelope)
    return web.Response(status=200)


async def web_apps_update_application_settings(request: web.Request, resource_group_name, name, subscription_id, api_version, app_settings) -> web.Response:
    """Replaces the application settings of an app.

    Replaces the application settings of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param app_settings: Application settings of the app.
    :type app_settings: dict | bytes

    """
    app_settings = StringDictionary.from_dict(app_settings)
    return web.Response(status=200)


async def web_apps_update_application_settings_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, app_settings) -> web.Response:
    """Replaces the application settings of an app.

    Replaces the application settings of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will update the application settings for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param app_settings: Application settings of the app.
    :type app_settings: dict | bytes

    """
    app_settings = StringDictionary.from_dict(app_settings)
    return web.Response(status=200)


async def web_apps_update_auth_settings(request: web.Request, resource_group_name, name, subscription_id, api_version, site_auth_settings) -> web.Response:
    """Updates the Authentication / Authorization settings associated with web app.

    Updates the Authentication / Authorization settings associated with web app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_auth_settings: Auth settings associated with web app.
    :type site_auth_settings: dict | bytes

    """
    site_auth_settings = SiteAuthSettings.from_dict(site_auth_settings)
    return web.Response(status=200)


async def web_apps_update_auth_settings_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, site_auth_settings) -> web.Response:
    """Updates the Authentication / Authorization settings associated with web app.

    Updates the Authentication / Authorization settings associated with web app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_auth_settings: Auth settings associated with web app.
    :type site_auth_settings: dict | bytes

    """
    site_auth_settings = SiteAuthSettings.from_dict(site_auth_settings)
    return web.Response(status=200)


async def web_apps_update_backup_configuration(request: web.Request, resource_group_name, name, subscription_id, api_version, request) -> web.Response:
    """Updates the backup configuration of an app.

    Updates the backup configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: Edited backup configuration.
    :type request: dict | bytes

    """
    request = BackupRequest.from_dict(request)
    return web.Response(status=200)


async def web_apps_update_backup_configuration_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, request) -> web.Response:
    """Updates the backup configuration of an app.

    Updates the backup configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will update the backup configuration for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: Edited backup configuration.
    :type request: dict | bytes

    """
    request = BackupRequest.from_dict(request)
    return web.Response(status=200)


async def web_apps_update_configuration(request: web.Request, resource_group_name, name, subscription_id, api_version, site_config) -> web.Response:
    """Updates the configuration of an app.

    Updates the configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_config: JSON representation of a SiteConfig object. See example.
    :type site_config: dict | bytes

    """
    site_config = SiteConfigResource.from_dict(site_config)
    return web.Response(status=200)


async def web_apps_update_configuration_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, site_config) -> web.Response:
    """Updates the configuration of an app.

    Updates the configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will update configuration for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_config: JSON representation of a SiteConfig object. See example.
    :type site_config: dict | bytes

    """
    site_config = SiteConfigResource.from_dict(site_config)
    return web.Response(status=200)


async def web_apps_update_connection_strings(request: web.Request, resource_group_name, name, subscription_id, api_version, connection_strings) -> web.Response:
    """Replaces the connection strings of an app.

    Replaces the connection strings of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_strings: Connection strings of the app or deployment slot. See example.
    :type connection_strings: dict | bytes

    """
    connection_strings = ConnectionStringDictionary.from_dict(connection_strings)
    return web.Response(status=200)


async def web_apps_update_connection_strings_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, connection_strings) -> web.Response:
    """Replaces the connection strings of an app.

    Replaces the connection strings of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will update the connection settings for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_strings: Connection strings of the app or deployment slot. See example.
    :type connection_strings: dict | bytes

    """
    connection_strings = ConnectionStringDictionary.from_dict(connection_strings)
    return web.Response(status=200)


async def web_apps_update_diagnostic_logs_config(request: web.Request, resource_group_name, name, subscription_id, api_version, site_logs_config) -> web.Response:
    """Updates the logging configuration of an app.

    Updates the logging configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_logs_config: A SiteLogsConfig JSON object that contains the logging configuration to change in the \&quot;properties\&quot; property.
    :type site_logs_config: dict | bytes

    """
    site_logs_config = SiteLogsConfig.from_dict(site_logs_config)
    return web.Response(status=200)


async def web_apps_update_diagnostic_logs_config_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, site_logs_config) -> web.Response:
    """Updates the logging configuration of an app.

    Updates the logging configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will update the logging configuration for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_logs_config: A SiteLogsConfig JSON object that contains the logging configuration to change in the \&quot;properties\&quot; property.
    :type site_logs_config: dict | bytes

    """
    site_logs_config = SiteLogsConfig.from_dict(site_logs_config)
    return web.Response(status=200)


async def web_apps_update_domain_ownership_identifier(request: web.Request, resource_group_name, name, domain_ownership_identifier_name, subscription_id, api_version, domain_ownership_identifier) -> web.Response:
    """Creates a domain ownership identifier for web app, or updates an existing ownership identifier.

    Creates a domain ownership identifier for web app, or updates an existing ownership identifier.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param domain_ownership_identifier_name: Name of domain ownership identifier.
    :type domain_ownership_identifier_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param domain_ownership_identifier: A JSON representation of the domain ownership properties.
    :type domain_ownership_identifier: dict | bytes

    """
    domain_ownership_identifier = WebAppsGetDomainOwnershipIdentifier200Response.from_dict(domain_ownership_identifier)
    return web.Response(status=200)


async def web_apps_update_domain_ownership_identifier_slot(request: web.Request, resource_group_name, name, domain_ownership_identifier_name, slot, subscription_id, api_version, domain_ownership_identifier) -> web.Response:
    """Creates a domain ownership identifier for web app, or updates an existing ownership identifier.

    Creates a domain ownership identifier for web app, or updates an existing ownership identifier.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param domain_ownership_identifier_name: Name of domain ownership identifier.
    :type domain_ownership_identifier_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will delete the binding for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param domain_ownership_identifier: A JSON representation of the domain ownership properties.
    :type domain_ownership_identifier: dict | bytes

    """
    domain_ownership_identifier = WebAppsGetDomainOwnershipIdentifier200Response.from_dict(domain_ownership_identifier)
    return web.Response(status=200)


async def web_apps_update_hybrid_connection(request: web.Request, resource_group_name, name, namespace_name, relay_name, subscription_id, api_version, connection_envelope) -> web.Response:
    """Creates a new Hybrid Connection using a Service Bus relay.

    Creates a new Hybrid Connection using a Service Bus relay.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: The name of the web app.
    :type name: str
    :param namespace_name: The namespace for this hybrid connection.
    :type namespace_name: str
    :param relay_name: The relay name for this hybrid connection.
    :type relay_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The details of the hybrid connection.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = WebAppsGetHybridConnection200Response.from_dict(connection_envelope)
    return web.Response(status=200)


async def web_apps_update_hybrid_connection_slot(request: web.Request, resource_group_name, name, namespace_name, relay_name, slot, subscription_id, api_version, connection_envelope) -> web.Response:
    """Creates a new Hybrid Connection using a Service Bus relay.

    Creates a new Hybrid Connection using a Service Bus relay.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: The name of the web app.
    :type name: str
    :param namespace_name: The namespace for this hybrid connection.
    :type namespace_name: str
    :param relay_name: The relay name for this hybrid connection.
    :type relay_name: str
    :param slot: The name of the slot for the web app.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The details of the hybrid connection.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = WebAppsGetHybridConnection200Response.from_dict(connection_envelope)
    return web.Response(status=200)


async def web_apps_update_metadata(request: web.Request, resource_group_name, name, subscription_id, api_version, metadata) -> web.Response:
    """Replaces the metadata of an app.

    Replaces the metadata of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param metadata: Edited metadata of the app or deployment slot. See example.
    :type metadata: dict | bytes

    """
    metadata = StringDictionary.from_dict(metadata)
    return web.Response(status=200)


async def web_apps_update_metadata_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, metadata) -> web.Response:
    """Replaces the metadata of an app.

    Replaces the metadata of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will update the metadata for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param metadata: Edited metadata of the app or deployment slot. See example.
    :type metadata: dict | bytes

    """
    metadata = StringDictionary.from_dict(metadata)
    return web.Response(status=200)


async def web_apps_update_relay_service_connection(request: web.Request, resource_group_name, name, entity_name, subscription_id, api_version, connection_envelope) -> web.Response:
    """Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).

    Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param entity_name: Name of the hybrid connection configuration.
    :type entity_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: Details of the hybrid connection configuration.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = RelayServiceConnectionEntity.from_dict(connection_envelope)
    return web.Response(status=200)


async def web_apps_update_relay_service_connection_slot(request: web.Request, resource_group_name, name, entity_name, slot, subscription_id, api_version, connection_envelope) -> web.Response:
    """Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).

    Creates a new hybrid connection configuration (PUT), or updates an existing one (PATCH).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param entity_name: Name of the hybrid connection configuration.
    :type entity_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will create or update a hybrid connection for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: Details of the hybrid connection configuration.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = RelayServiceConnectionEntity.from_dict(connection_envelope)
    return web.Response(status=200)


async def web_apps_update_site_push_settings(request: web.Request, resource_group_name, name, subscription_id, api_version, push_settings) -> web.Response:
    """Updates the Push settings associated with web app.

    Updates the Push settings associated with web app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param push_settings: Push settings associated with web app.
    :type push_settings: dict | bytes

    """
    push_settings = WebAppsUpdateSitePushSettingsRequest.from_dict(push_settings)
    return web.Response(status=200)


async def web_apps_update_site_push_settings_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, push_settings) -> web.Response:
    """Updates the Push settings associated with web app.

    Updates the Push settings associated with web app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of web app.
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param push_settings: Push settings associated with web app.
    :type push_settings: dict | bytes

    """
    push_settings = WebAppsUpdateSitePushSettingsRequest.from_dict(push_settings)
    return web.Response(status=200)


async def web_apps_update_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, site_envelope, skip_dns_registration=None, skip_custom_domain_verification=None, force_dns_registration=None, ttl_in_seconds=None) -> web.Response:
    """Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

    Creates a new web, mobile, or API app in an existing resource group, or updates an existing app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Unique name of the app to create or update. To create or update a deployment slot, use the {slot} parameter.
    :type name: str
    :param slot: Name of the deployment slot to create or update. By default, this API attempts to create or modify the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_envelope: A JSON representation of the app properties. See example.
    :type site_envelope: dict | bytes
    :param skip_dns_registration: If true web app hostname is not registered with DNS on creation. This parameter is  only used for app creation.
    :type skip_dns_registration: bool
    :param skip_custom_domain_verification: If true, custom (non *.azurewebsites.net) domains associated with web app are not verified.
    :type skip_custom_domain_verification: bool
    :param force_dns_registration: If true, web app hostname is force registered with DNS.
    :type force_dns_registration: bool
    :param ttl_in_seconds: Time to live in seconds for web app&#39;s default domain name.
    :type ttl_in_seconds: str

    """
    site_envelope = SitePatchResource.from_dict(site_envelope)
    return web.Response(status=200)


async def web_apps_update_slot_configuration_names(request: web.Request, resource_group_name, name, subscription_id, api_version, slot_config_names) -> web.Response:
    """Updates the names of application settings and connection string that remain with the slot during swap operation.

    Updates the names of application settings and connection string that remain with the slot during swap operation.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param slot_config_names: Names of application settings and connection strings. See example.
    :type slot_config_names: dict | bytes

    """
    slot_config_names = SlotConfigNamesResource.from_dict(slot_config_names)
    return web.Response(status=200)


async def web_apps_update_source_control(request: web.Request, resource_group_name, name, subscription_id, api_version, site_source_control) -> web.Response:
    """Updates the source control configuration of an app.

    Updates the source control configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_source_control: JSON representation of a SiteSourceControl object. See example.
    :type site_source_control: dict | bytes

    """
    site_source_control = SiteSourceControl.from_dict(site_source_control)
    return web.Response(status=200)


async def web_apps_update_source_control_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, site_source_control) -> web.Response:
    """Updates the source control configuration of an app.

    Updates the source control configuration of an app.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will update the source control configuration for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_source_control: JSON representation of a SiteSourceControl object. See example.
    :type site_source_control: dict | bytes

    """
    site_source_control = SiteSourceControl.from_dict(site_source_control)
    return web.Response(status=200)


async def web_apps_update_vnet_connection(request: web.Request, resource_group_name, name, vnet_name, subscription_id, api_version, connection_envelope) -> web.Response:
    """Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).

    Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param vnet_name: Name of an existing Virtual Network.
    :type vnet_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: Properties of the Virtual Network connection. See example.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = WebAppsGetVnetConnectionSlot200Response.from_dict(connection_envelope)
    return web.Response(status=200)


async def web_apps_update_vnet_connection_gateway(request: web.Request, resource_group_name, name, vnet_name, gateway_name, subscription_id, api_version, connection_envelope) -> web.Response:
    """Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).

    Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param vnet_name: Name of the Virtual Network.
    :type vnet_name: str
    :param gateway_name: Name of the gateway. Currently, the only supported string is \&quot;primary\&quot;.
    :type gateway_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The properties to update this gateway with.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = WebAppsGetVnetConnectionGatewaySlot200Response.from_dict(connection_envelope)
    return web.Response(status=200)


async def web_apps_update_vnet_connection_gateway_slot(request: web.Request, resource_group_name, name, vnet_name, gateway_name, slot, subscription_id, api_version, connection_envelope) -> web.Response:
    """Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).

    Adds a gateway to a connected Virtual Network (PUT) or updates it (PATCH).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param vnet_name: Name of the Virtual Network.
    :type vnet_name: str
    :param gateway_name: Name of the gateway. Currently, the only supported string is \&quot;primary\&quot;.
    :type gateway_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will add or update a gateway for the production slot&#39;s Virtual Network.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The properties to update this gateway with.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = WebAppsGetVnetConnectionGatewaySlot200Response.from_dict(connection_envelope)
    return web.Response(status=200)


async def web_apps_update_vnet_connection_slot(request: web.Request, resource_group_name, name, vnet_name, slot, subscription_id, api_version, connection_envelope) -> web.Response:
    """Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).

    Adds a Virtual Network connection to an app or slot (PUT) or updates the connection properties (PATCH).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the app.
    :type name: str
    :param vnet_name: Name of an existing Virtual Network.
    :type vnet_name: str
    :param slot: Name of the deployment slot. If a slot is not specified, the API will add or update connections for the production slot.
    :type slot: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: Properties of the Virtual Network connection. See example.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = WebAppsGetVnetConnectionSlot200Response.from_dict(connection_envelope)
    return web.Response(status=200)
