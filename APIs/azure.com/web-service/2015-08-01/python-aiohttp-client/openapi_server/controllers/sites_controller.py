from typing import List, Dict
from aiohttp import web

from openapi_server.models.backup_item import BackupItem
from openapi_server.models.backup_item_collection import BackupItemCollection
from openapi_server.models.backup_request import BackupRequest
from openapi_server.models.connection_string_dictionary import ConnectionStringDictionary
from openapi_server.models.csm_publishing_profile_options import CsmPublishingProfileOptions
from openapi_server.models.csm_site_recovery_entity import CsmSiteRecoveryEntity
from openapi_server.models.csm_slot_entity import CsmSlotEntity
from openapi_server.models.csm_usage_quota_collection import CsmUsageQuotaCollection
from openapi_server.models.deleted_site_collection import DeletedSiteCollection
from openapi_server.models.deployment import Deployment
from openapi_server.models.deployment_collection import DeploymentCollection
from openapi_server.models.host_name_binding import HostNameBinding
from openapi_server.models.host_name_binding_collection import HostNameBindingCollection
from openapi_server.models.metric_definition_collection import MetricDefinitionCollection
from openapi_server.models.network_features import NetworkFeatures
from openapi_server.models.premier_add_on_request import PremierAddOnRequest
from openapi_server.models.relay_service_connection_entity import RelayServiceConnectionEntity
from openapi_server.models.resource_metric_collection import ResourceMetricCollection
from openapi_server.models.restore_request import RestoreRequest
from openapi_server.models.restore_response import RestoreResponse
from openapi_server.models.site import Site
from openapi_server.models.site_auth_settings import SiteAuthSettings
from openapi_server.models.site_cloneability import SiteCloneability
from openapi_server.models.site_collection import SiteCollection
from openapi_server.models.site_config import SiteConfig
from openapi_server.models.site_instance_collection import SiteInstanceCollection
from openapi_server.models.site_logs_config import SiteLogsConfig
from openapi_server.models.site_source_control import SiteSourceControl
from openapi_server.models.slot_config_names_resource import SlotConfigNamesResource
from openapi_server.models.slot_difference_collection import SlotDifferenceCollection
from openapi_server.models.string_dictionary import StringDictionary
from openapi_server.models.user import User
from openapi_server.models.vnet_gateway import VnetGateway
from openapi_server.models.vnet_info import VnetInfo
from openapi_server import util


async def sites_add_site_premier_add_on(request: web.Request, resource_group_name, name, premier_add_on_name, subscription_id, api_version, premier_add_on) -> web.Response:
    """sites_add_site_premier_add_on

    

    :param resource_group_name: 
    :type resource_group_name: str
    :param name: 
    :type name: str
    :param premier_add_on_name: 
    :type premier_add_on_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param premier_add_on: 
    :type premier_add_on: dict | bytes

    """
    premier_add_on = PremierAddOnRequest.from_dict(premier_add_on)
    return web.Response(status=200)


async def sites_add_site_premier_add_on_slot(request: web.Request, resource_group_name, name, premier_add_on_name, slot, subscription_id, api_version, premier_add_on) -> web.Response:
    """sites_add_site_premier_add_on_slot

    

    :param resource_group_name: 
    :type resource_group_name: str
    :param name: 
    :type name: str
    :param premier_add_on_name: 
    :type premier_add_on_name: str
    :param slot: 
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param premier_add_on: 
    :type premier_add_on: dict | bytes

    """
    premier_add_on = PremierAddOnRequest.from_dict(premier_add_on)
    return web.Response(status=200)


async def sites_apply_slot_config_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, slot_swap_entity) -> web.Response:
    """Applies the configuration settings from the target slot onto the current slot

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of the source slot. Settings from the target slot will be applied onto this slot
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param slot_swap_entity: Request body that contains the target slot name. Settings from that slot will be applied on the source slot
    :type slot_swap_entity: dict | bytes

    """
    slot_swap_entity = CsmSlotEntity.from_dict(slot_swap_entity)
    return web.Response(status=200)


async def sites_apply_slot_config_to_production(request: web.Request, resource_group_name, name, subscription_id, api_version, slot_swap_entity) -> web.Response:
    """Applies the configuration settings from the target slot onto the current slot

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param slot_swap_entity: Request body that contains the target slot name. Settings from that slot will be applied on the source slot
    :type slot_swap_entity: dict | bytes

    """
    slot_swap_entity = CsmSlotEntity.from_dict(slot_swap_entity)
    return web.Response(status=200)


async def sites_backup_site(request: web.Request, resource_group_name, name, subscription_id, api_version, request) -> web.Response:
    """Creates web app backup

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: Information on backup request
    :type request: dict | bytes

    """
    request = BackupRequest.from_dict(request)
    return web.Response(status=200)


async def sites_backup_site_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, request) -> web.Response:
    """Creates web app backup

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: Information on backup request
    :type request: dict | bytes

    """
    request = BackupRequest.from_dict(request)
    return web.Response(status=200)


async def sites_create_deployment(request: web.Request, resource_group_name, name, id, subscription_id, api_version, deployment) -> web.Response:
    """Create a deployment

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param id: Id of the deployment
    :type id: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param deployment: Details of deployment
    :type deployment: dict | bytes

    """
    deployment = Deployment.from_dict(deployment)
    return web.Response(status=200)


async def sites_create_deployment_slot(request: web.Request, resource_group_name, name, id, slot, subscription_id, api_version, deployment) -> web.Response:
    """Create a deployment

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param id: Id of the deployment
    :type id: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param deployment: Details of deployment
    :type deployment: dict | bytes

    """
    deployment = Deployment.from_dict(deployment)
    return web.Response(status=200)


async def sites_create_instance_deployment(request: web.Request, resource_group_name, name, id, instance_id, subscription_id, api_version, deployment) -> web.Response:
    """Create a deployment

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param id: Id of the deployment
    :type id: str
    :param instance_id: Id of web app instance
    :type instance_id: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param deployment: Details of deployment
    :type deployment: dict | bytes

    """
    deployment = Deployment.from_dict(deployment)
    return web.Response(status=200)


async def sites_create_instance_deployment_slot(request: web.Request, resource_group_name, name, id, slot, instance_id, subscription_id, api_version, deployment) -> web.Response:
    """Create a deployment

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param id: Id of the deployment
    :type id: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param instance_id: Id of web app instance
    :type instance_id: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param deployment: Details of deployment
    :type deployment: dict | bytes

    """
    deployment = Deployment.from_dict(deployment)
    return web.Response(status=200)


async def sites_create_or_update_site(request: web.Request, resource_group_name, name, subscription_id, api_version, site_envelope, skip_dns_registration=None, skip_custom_domain_verification=None, force_dns_registration=None, ttl_in_seconds=None) -> web.Response:
    """Creates a new web app or modifies an existing web app.

    

    :param resource_group_name: Name of the resource group
    :type resource_group_name: str
    :param name: Name of the web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_envelope: Details of web app if it exists already
    :type site_envelope: dict | bytes
    :param skip_dns_registration: If true web app hostname is not registered with DNS on creation. This parameter is              only used for app creation
    :type skip_dns_registration: str
    :param skip_custom_domain_verification: If true, custom (non *.azurewebsites.net) domains associated with web app are not verified.
    :type skip_custom_domain_verification: str
    :param force_dns_registration: If true, web app hostname is force registered with DNS
    :type force_dns_registration: str
    :param ttl_in_seconds: Time to live in seconds for web app&#39;s default domain name
    :type ttl_in_seconds: str

    """
    site_envelope = Site.from_dict(site_envelope)
    return web.Response(status=200)


async def sites_create_or_update_site_config(request: web.Request, resource_group_name, name, subscription_id, api_version, site_config) -> web.Response:
    """Update the configuration of web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_config: Request body that contains the configuration setting for the web app
    :type site_config: dict | bytes

    """
    site_config = SiteConfig.from_dict(site_config)
    return web.Response(status=200)


async def sites_create_or_update_site_config_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, site_config) -> web.Response:
    """Update the configuration of web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_config: Request body that contains the configuration setting for the web app
    :type site_config: dict | bytes

    """
    site_config = SiteConfig.from_dict(site_config)
    return web.Response(status=200)


async def sites_create_or_update_site_host_name_binding(request: web.Request, resource_group_name, name, host_name, subscription_id, api_version, host_name_binding) -> web.Response:
    """Creates a web app hostname binding

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param host_name: Name of host
    :type host_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param host_name_binding: Host name binding information
    :type host_name_binding: dict | bytes

    """
    host_name_binding = HostNameBinding.from_dict(host_name_binding)
    return web.Response(status=200)


async def sites_create_or_update_site_host_name_binding_slot(request: web.Request, resource_group_name, name, host_name, slot, subscription_id, api_version, host_name_binding) -> web.Response:
    """Creates a web app hostname binding

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param host_name: Name of host
    :type host_name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param host_name_binding: Host name binding information
    :type host_name_binding: dict | bytes

    """
    host_name_binding = HostNameBinding.from_dict(host_name_binding)
    return web.Response(status=200)


async def sites_create_or_update_site_relay_service_connection(request: web.Request, resource_group_name, name, entity_name, subscription_id, api_version, connection_envelope) -> web.Response:
    """Creates a new association to a BizTalk Hybrid Connection, or updates an existing one.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param entity_name: The name by which the Hybrid Connection is identified
    :type entity_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The details of the Hybrid Connection
    :type connection_envelope: dict | bytes

    """
    connection_envelope = RelayServiceConnectionEntity.from_dict(connection_envelope)
    return web.Response(status=200)


async def sites_create_or_update_site_relay_service_connection_slot(request: web.Request, resource_group_name, name, entity_name, slot, subscription_id, api_version, connection_envelope) -> web.Response:
    """Creates a new association to a BizTalk Hybrid Connection, or updates an existing one.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param entity_name: The name by which the Hybrid Connection is identified
    :type entity_name: str
    :param slot: The name of the slot for the web app.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The details of the Hybrid Connection
    :type connection_envelope: dict | bytes

    """
    connection_envelope = RelayServiceConnectionEntity.from_dict(connection_envelope)
    return web.Response(status=200)


async def sites_create_or_update_site_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, site_envelope, skip_dns_registration=None, skip_custom_domain_verification=None, force_dns_registration=None, ttl_in_seconds=None) -> web.Response:
    """Creates a new web app or modifies an existing web app.

    

    :param resource_group_name: Name of the resource group
    :type resource_group_name: str
    :param name: Name of the web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_envelope: Details of web app if it exists already
    :type site_envelope: dict | bytes
    :param skip_dns_registration: If true web app hostname is not registered with DNS on creation. This parameter is              only used for app creation
    :type skip_dns_registration: str
    :param skip_custom_domain_verification: If true, custom (non *.azurewebsites.net) domains associated with web app are not verified.
    :type skip_custom_domain_verification: str
    :param force_dns_registration: If true, web app hostname is force registered with DNS
    :type force_dns_registration: str
    :param ttl_in_seconds: Time to live in seconds for web app&#39;s default domain name
    :type ttl_in_seconds: str

    """
    site_envelope = Site.from_dict(site_envelope)
    return web.Response(status=200)


async def sites_create_or_update_site_source_control(request: web.Request, resource_group_name, name, subscription_id, api_version, site_source_control) -> web.Response:
    """Update the source control configuration of web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_source_control: Request body that contains the source control parameters
    :type site_source_control: dict | bytes

    """
    site_source_control = SiteSourceControl.from_dict(site_source_control)
    return web.Response(status=200)


async def sites_create_or_update_site_source_control_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, site_source_control) -> web.Response:
    """Update the source control configuration of web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_source_control: Request body that contains the source control parameters
    :type site_source_control: dict | bytes

    """
    site_source_control = SiteSourceControl.from_dict(site_source_control)
    return web.Response(status=200)


async def sites_create_or_update_site_vnet_connection(request: web.Request, resource_group_name, name, vnet_name, subscription_id, api_version, connection_envelope) -> web.Response:
    """Adds a Virtual Network Connection or updates it&#39;s properties.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param vnet_name: The name of the Virtual Network
    :type vnet_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The properties of this Virtual Network Connection
    :type connection_envelope: dict | bytes

    """
    connection_envelope = VnetInfo.from_dict(connection_envelope)
    return web.Response(status=200)


async def sites_create_or_update_site_vnet_connection_gateway(request: web.Request, resource_group_name, name, vnet_name, gateway_name, subscription_id, api_version, connection_envelope) -> web.Response:
    """Updates the Virtual Network Gateway.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param vnet_name: The name of the Virtual Network
    :type vnet_name: str
    :param gateway_name: The name of the gateway. The only gateway that exists presently is \&quot;primary\&quot;
    :type gateway_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The properties to update this gateway with.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = VnetGateway.from_dict(connection_envelope)
    return web.Response(status=200)


async def sites_create_or_update_site_vnet_connection_gateway_slot(request: web.Request, resource_group_name, name, vnet_name, gateway_name, slot, subscription_id, api_version, connection_envelope) -> web.Response:
    """Updates the Virtual Network Gateway.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param vnet_name: The name of the Virtual Network
    :type vnet_name: str
    :param gateway_name: The name of the gateway. The only gateway that exists presently is \&quot;primary\&quot;
    :type gateway_name: str
    :param slot: The name of the slot for this web app.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The properties to update this gateway with.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = VnetGateway.from_dict(connection_envelope)
    return web.Response(status=200)


async def sites_create_or_update_site_vnet_connection_slot(request: web.Request, resource_group_name, name, vnet_name, slot, subscription_id, api_version, connection_envelope) -> web.Response:
    """Adds a Virtual Network Connection or updates it&#39;s properties.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param vnet_name: The name of the Virtual Network
    :type vnet_name: str
    :param slot: The name of the slot for this web app.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The properties of this Virtual Network Connection
    :type connection_envelope: dict | bytes

    """
    connection_envelope = VnetInfo.from_dict(connection_envelope)
    return web.Response(status=200)


async def sites_delete_backup(request: web.Request, resource_group_name, name, backup_id, subscription_id, api_version) -> web.Response:
    """Deletes a backup from Azure Storage

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param backup_id: Id of backup
    :type backup_id: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_delete_backup_slot(request: web.Request, resource_group_name, name, backup_id, slot, subscription_id, api_version) -> web.Response:
    """Deletes a backup from Azure Storage

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param backup_id: Id of backup
    :type backup_id: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_delete_deployment(request: web.Request, resource_group_name, name, id, subscription_id, api_version) -> web.Response:
    """Delete the deployment

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param id: Id of the deployment
    :type id: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_delete_deployment_slot(request: web.Request, resource_group_name, name, id, slot, subscription_id, api_version) -> web.Response:
    """Delete the deployment

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param id: Id of the deployment
    :type id: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_delete_instance_deployment(request: web.Request, resource_group_name, name, id, instance_id, subscription_id, api_version) -> web.Response:
    """Delete the deployment

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param id: Id of the deployment
    :type id: str
    :param instance_id: Id of web app instance
    :type instance_id: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_delete_instance_deployment_slot(request: web.Request, resource_group_name, name, id, slot, instance_id, subscription_id, api_version) -> web.Response:
    """Delete the deployment

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param id: Id of the deployment
    :type id: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param instance_id: Id of web app instance
    :type instance_id: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_delete_site(request: web.Request, resource_group_name, name, subscription_id, api_version, delete_metrics=None, delete_empty_server_farm=None, skip_dns_registration=None, delete_all_slots=None) -> web.Response:
    """Deletes a web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param delete_metrics: If true, web app metrics are also deleted
    :type delete_metrics: str
    :param delete_empty_server_farm: If true and App Service Plan is empty after web app deletion, App Service Plan is also deleted
    :type delete_empty_server_farm: str
    :param skip_dns_registration: If true, DNS registration is skipped
    :type skip_dns_registration: str
    :param delete_all_slots: If true, all slots associated with web app are also deleted
    :type delete_all_slots: str

    """
    return web.Response(status=200)


async def sites_delete_site_host_name_binding(request: web.Request, resource_group_name, name, host_name, subscription_id, api_version) -> web.Response:
    """Deletes a host name binding

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param host_name: Name of host
    :type host_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_delete_site_host_name_binding_slot(request: web.Request, resource_group_name, name, slot, host_name, subscription_id, api_version) -> web.Response:
    """Deletes a host name binding

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param host_name: Name of host
    :type host_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_delete_site_premier_add_on(request: web.Request, resource_group_name, name, premier_add_on_name, subscription_id, api_version) -> web.Response:
    """sites_delete_site_premier_add_on

    

    :param resource_group_name: 
    :type resource_group_name: str
    :param name: 
    :type name: str
    :param premier_add_on_name: 
    :type premier_add_on_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_delete_site_premier_add_on_slot(request: web.Request, resource_group_name, name, premier_add_on_name, slot, subscription_id, api_version) -> web.Response:
    """sites_delete_site_premier_add_on_slot

    

    :param resource_group_name: 
    :type resource_group_name: str
    :param name: 
    :type name: str
    :param premier_add_on_name: 
    :type premier_add_on_name: str
    :param slot: 
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_delete_site_relay_service_connection(request: web.Request, resource_group_name, name, entity_name, subscription_id, api_version) -> web.Response:
    """Removes the association to a BizTalk Hybrid Connection, identified by its entity name.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param entity_name: The name by which the Hybrid Connection is identified
    :type entity_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_delete_site_relay_service_connection_slot(request: web.Request, resource_group_name, name, entity_name, slot, subscription_id, api_version) -> web.Response:
    """Removes the association to a BizTalk Hybrid Connection, identified by its entity name.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param entity_name: The name by which the Hybrid Connection is identified
    :type entity_name: str
    :param slot: The name of the slot for the web app.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_delete_site_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, delete_metrics=None, delete_empty_server_farm=None, skip_dns_registration=None, delete_all_slots=None) -> web.Response:
    """Deletes a web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param delete_metrics: If true, web app metrics are also deleted
    :type delete_metrics: str
    :param delete_empty_server_farm: If true and App Service Plan is empty after web app deletion, App Service Plan is also deleted
    :type delete_empty_server_farm: str
    :param skip_dns_registration: If true, DNS registration is skipped
    :type skip_dns_registration: str
    :param delete_all_slots: If true, all slots associated with web app are also deleted
    :type delete_all_slots: str

    """
    return web.Response(status=200)


async def sites_delete_site_source_control(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Delete source control configuration of web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_delete_site_source_control_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Delete source control configuration of web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_delete_site_vnet_connection(request: web.Request, resource_group_name, name, vnet_name, subscription_id, api_version) -> web.Response:
    """Removes the specified Virtual Network Connection association from this web app.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param vnet_name: The name of the Virtual Network
    :type vnet_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_delete_site_vnet_connection_slot(request: web.Request, resource_group_name, name, vnet_name, slot, subscription_id, api_version) -> web.Response:
    """Removes the specified Virtual Network Connection association from this web app.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param vnet_name: The name of the Virtual Network
    :type vnet_name: str
    :param slot: The name of the slot for this web app.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_discover_site_restore(request: web.Request, resource_group_name, name, subscription_id, api_version, request) -> web.Response:
    """Discovers existing web app backups that can be restored

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: Information on restore request
    :type request: dict | bytes

    """
    request = RestoreRequest.from_dict(request)
    return web.Response(status=200)


async def sites_discover_site_restore_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, request) -> web.Response:
    """Discovers existing web app backups that can be restored

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: Information on restore request
    :type request: dict | bytes

    """
    request = RestoreRequest.from_dict(request)
    return web.Response(status=200)


async def sites_generate_new_site_publishing_password(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Generates new random app publishing password

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_generate_new_site_publishing_password_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Generates new random app publishing password

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_deleted_sites(request: web.Request, resource_group_name, subscription_id, api_version, properties_to_include=None, include_site_types=None) -> web.Response:
    """Gets deleted web apps in subscription

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param properties_to_include: Additional web app properties included in the response
    :type properties_to_include: str
    :param include_site_types: Types of apps included in the response
    :type include_site_types: str

    """
    return web.Response(status=200)


async def sites_get_deployment(request: web.Request, resource_group_name, name, id, subscription_id, api_version) -> web.Response:
    """Get the deployment

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param id: Id of the deployment
    :type id: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_deployment_slot(request: web.Request, resource_group_name, name, id, slot, subscription_id, api_version) -> web.Response:
    """Get the deployment

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param id: Id of the deployment
    :type id: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_deployments(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """List deployments

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_deployments_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """List deployments

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_instance_deployment(request: web.Request, resource_group_name, name, id, instance_id, subscription_id, api_version) -> web.Response:
    """Get the deployment

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param id: Id of the deployment
    :type id: str
    :param instance_id: Id of web app instance
    :type instance_id: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_instance_deployment_slot(request: web.Request, resource_group_name, name, id, slot, instance_id, subscription_id, api_version) -> web.Response:
    """Get the deployment

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param id: Id of the deployment
    :type id: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param instance_id: Id of web app instance
    :type instance_id: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_instance_deployments(request: web.Request, resource_group_name, name, instance_id, subscription_id, api_version) -> web.Response:
    """List deployments

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param instance_id: Id of web app instance
    :type instance_id: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_instance_deployments_slot(request: web.Request, resource_group_name, name, slot, instance_id, subscription_id, api_version) -> web.Response:
    """List deployments

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param instance_id: Id of web app instance
    :type instance_id: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site(request: web.Request, resource_group_name, name, subscription_id, api_version, properties_to_include=None) -> web.Response:
    """Get details of a web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param properties_to_include: Additional web app properties included in the response
    :type properties_to_include: str

    """
    return web.Response(status=200)


async def sites_get_site_backup_configuration(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the backup configuration for a web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_backup_configuration_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the backup configuration for a web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_backup_status(request: web.Request, resource_group_name, name, backup_id, subscription_id, api_version) -> web.Response:
    """Gets status of a web app backup that may be in progress.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param backup_id: Id of backup
    :type backup_id: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_backup_status_secrets(request: web.Request, resource_group_name, name, backup_id, subscription_id, api_version, request) -> web.Response:
    """Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param backup_id: Id of backup
    :type backup_id: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: Information on backup request
    :type request: dict | bytes

    """
    request = BackupRequest.from_dict(request)
    return web.Response(status=200)


async def sites_get_site_backup_status_secrets_slot(request: web.Request, resource_group_name, name, backup_id, slot, subscription_id, api_version, request) -> web.Response:
    """Gets status of a web app backup that may be in progress, including secrets associated with the backup, such as the Azure Storage SAS URL. Also can be used to update the SAS URL for the backup if a new URL is passed in the request body.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param backup_id: Id of backup
    :type backup_id: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: Information on backup request
    :type request: dict | bytes

    """
    request = BackupRequest.from_dict(request)
    return web.Response(status=200)


async def sites_get_site_backup_status_slot(request: web.Request, resource_group_name, name, backup_id, slot, subscription_id, api_version) -> web.Response:
    """Gets status of a web app backup that may be in progress.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param backup_id: Id of backup
    :type backup_id: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_config(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the configuration of the web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_config_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the configuration of the web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_host_name_binding(request: web.Request, resource_group_name, name, host_name, subscription_id, api_version) -> web.Response:
    """Get web app binding for a hostname

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param host_name: Name of host
    :type host_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_host_name_binding_slot(request: web.Request, resource_group_name, name, slot, host_name, subscription_id, api_version) -> web.Response:
    """Get web app binding for a hostname

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param host_name: Name of host
    :type host_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_host_name_bindings(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get web app hostname bindings

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_host_name_bindings_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Get web app hostname bindings

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_instance_identifiers(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets all instance of a web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_instance_identifiers_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets all instance of a web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_logs_config(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the web app logs configuration

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_logs_config_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the web app logs configuration

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_metric_definitions(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets metric definitions for web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_metric_definitions_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets metric definitions for web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_metrics(request: web.Request, resource_group_name, name, subscription_id, api_version, details=None, filter=None) -> web.Response:
    """Gets metrics for web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param details: If true, metric details are included in response
    :type details: bool
    :param filter: Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;.
    :type filter: str

    """
    return web.Response(status=200)


async def sites_get_site_metrics_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, details=None, filter=None) -> web.Response:
    """Gets metrics for web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param details: If true, metric details are included in response
    :type details: bool
    :param filter: Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;.
    :type filter: str

    """
    return web.Response(status=200)


async def sites_get_site_network_features(request: web.Request, resource_group_name, name, view, subscription_id, api_version) -> web.Response:
    """Retrieves a view of all network features in use on this web app.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param view: The type of view. This can either be \&quot;summary\&quot; or \&quot;detailed\&quot;.
    :type view: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_network_features_slot(request: web.Request, resource_group_name, name, view, slot, subscription_id, api_version) -> web.Response:
    """Retrieves a view of all network features in use on this web app.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param view: The type of view. This can either be \&quot;summary\&quot; or \&quot;detailed\&quot;.
    :type view: str
    :param slot: The name of the slot for this web app.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_operation(request: web.Request, resource_group_name, name, operation_id, subscription_id, api_version) -> web.Response:
    """Gets the operation for a web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param operation_id: Id of an operation
    :type operation_id: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_operation_slot(request: web.Request, resource_group_name, name, operation_id, slot, subscription_id, api_version) -> web.Response:
    """Gets the operation for a web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param operation_id: Id of an operation
    :type operation_id: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_premier_add_on(request: web.Request, resource_group_name, name, premier_add_on_name, subscription_id, api_version) -> web.Response:
    """sites_get_site_premier_add_on

    

    :param resource_group_name: 
    :type resource_group_name: str
    :param name: 
    :type name: str
    :param premier_add_on_name: 
    :type premier_add_on_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_premier_add_on_slot(request: web.Request, resource_group_name, name, premier_add_on_name, slot, subscription_id, api_version) -> web.Response:
    """sites_get_site_premier_add_on_slot

    

    :param resource_group_name: 
    :type resource_group_name: str
    :param name: 
    :type name: str
    :param premier_add_on_name: 
    :type premier_add_on_name: str
    :param slot: 
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_relay_service_connection(request: web.Request, resource_group_name, name, entity_name, subscription_id, api_version) -> web.Response:
    """Retrieves a BizTalk Hybrid Connection identified by its entity name.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param entity_name: The name by which the Hybrid Connection is identified
    :type entity_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_relay_service_connection_slot(request: web.Request, resource_group_name, name, entity_name, slot, subscription_id, api_version) -> web.Response:
    """Retrieves a BizTalk Hybrid Connection identified by its entity name.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param entity_name: The name by which the Hybrid Connection is identified
    :type entity_name: str
    :param slot: The name of the slot for the web app.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, properties_to_include=None) -> web.Response:
    """Get details of a web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param properties_to_include: Additional web app properties included in the response
    :type properties_to_include: str

    """
    return web.Response(status=200)


async def sites_get_site_slots(request: web.Request, resource_group_name, name, subscription_id, api_version, properties_to_include=None) -> web.Response:
    """Gets all the slots for a web apps

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param properties_to_include: List of app properties to include in the response
    :type properties_to_include: str

    """
    return web.Response(status=200)


async def sites_get_site_snapshots(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Returns all Snapshots to the user.

    

    :param resource_group_name: Webspace
    :type resource_group_name: str
    :param name: Website Name
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_snapshots_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Returns all Snapshots to the user.

    

    :param resource_group_name: Webspace
    :type resource_group_name: str
    :param name: Website Name
    :type name: str
    :param slot: Website Slot
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_source_control(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get the source control configuration of web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_source_control_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Get the source control configuration of web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_usages(request: web.Request, resource_group_name, name, subscription_id, api_version, filter=None) -> web.Response:
    """Gets the quota usage numbers for web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param filter: Return only usages specified in the filter. Filter is specified by using OData syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;.
    :type filter: str

    """
    return web.Response(status=200)


async def sites_get_site_usages_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, filter=None) -> web.Response:
    """Gets the quota usage numbers for web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param filter: Return only usages specified in the filter. Filter is specified by using OData syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;.
    :type filter: str

    """
    return web.Response(status=200)


async def sites_get_site_vnet_connection(request: web.Request, resource_group_name, name, vnet_name, subscription_id, api_version) -> web.Response:
    """Retrieves a specific Virtual Network Connection associated with this web app.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param vnet_name: The name of the Virtual Network
    :type vnet_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_vnet_connection_slot(request: web.Request, resource_group_name, name, vnet_name, slot, subscription_id, api_version) -> web.Response:
    """Retrieves a specific Virtual Network Connection associated with this web app.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param vnet_name: The name of the Virtual Network
    :type vnet_name: str
    :param slot: The name of the slot for this web app.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_vnet_connections(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Retrieves a list of all Virtual Network Connections associated with this web app.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_vnet_connections_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Retrieves a list of all Virtual Network Connections associated with this web app.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param slot: The name of the slot for this web app.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_vnet_gateway(request: web.Request, resource_group_name, name, vnet_name, gateway_name, subscription_id, api_version) -> web.Response:
    """Retrieves a Virtual Network connection gateway associated with this web app and virtual network.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param vnet_name: The name of the Virtual Network
    :type vnet_name: str
    :param gateway_name: The name of the gateway. The only gateway that exists presently is \&quot;primary\&quot;
    :type gateway_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_site_vnet_gateway_slot(request: web.Request, resource_group_name, name, vnet_name, gateway_name, slot, subscription_id, api_version) -> web.Response:
    """Retrieves a Virtual Network connection gateway associated with this web app and virtual network.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param vnet_name: The name of the Virtual Network
    :type vnet_name: str
    :param gateway_name: The name of the gateway. The only gateway that exists presently is \&quot;primary\&quot;
    :type gateway_name: str
    :param slot: The name of the slot for this web app.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_sites(request: web.Request, resource_group_name, subscription_id, api_version, properties_to_include=None, include_site_types=None, include_slots=None) -> web.Response:
    """Gets the web apps for a subscription in the specified resource group

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param properties_to_include: Additional web app properties included in the response
    :type properties_to_include: str
    :param include_site_types: Types of apps included in the response
    :type include_site_types: str
    :param include_slots: Whether or not to include deployments slots in results
    :type include_slots: bool

    """
    return web.Response(status=200)


async def sites_get_slot_config_names(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the names of application settings and connection string that remain with the slot during swap operation

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_get_slots_differences_from_production(request: web.Request, resource_group_name, name, subscription_id, api_version, slot_swap_entity) -> web.Response:
    """Get the difference in configuration settings between two web app slots

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param slot_swap_entity: Request body that contains the target slot name
    :type slot_swap_entity: dict | bytes

    """
    slot_swap_entity = CsmSlotEntity.from_dict(slot_swap_entity)
    return web.Response(status=200)


async def sites_get_slots_differences_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, slot_swap_entity) -> web.Response:
    """Get the difference in configuration settings between two web app slots

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of the source slot
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param slot_swap_entity: Request body that contains the target slot name
    :type slot_swap_entity: dict | bytes

    """
    slot_swap_entity = CsmSlotEntity.from_dict(slot_swap_entity)
    return web.Response(status=200)


async def sites_is_site_cloneable(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Creates a new web app or modifies an existing web app.

    

    :param resource_group_name: Name of the resource group
    :type resource_group_name: str
    :param name: Name of the web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_is_site_cloneable_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Creates a new web app or modifies an existing web app.

    

    :param resource_group_name: Name of the resource group
    :type resource_group_name: str
    :param name: Name of the web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_list_site_app_settings(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the application settings of web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_list_site_app_settings_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the application settings of web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_list_site_auth_settings(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the Authentication / Authorization settings associated with web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_list_site_auth_settings_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the Authentication / Authorization settings associated with web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_list_site_backups(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Lists all available backups for web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_list_site_backups_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Lists all available backups for web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_list_site_connection_strings(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the connection strings associated with web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_list_site_connection_strings_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the connection strings associated with web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_list_site_metadata(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the web app meta data.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_list_site_metadata_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the web app meta data.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_list_site_premier_add_ons(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """sites_list_site_premier_add_ons

    

    :param resource_group_name: 
    :type resource_group_name: str
    :param name: 
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_list_site_premier_add_ons_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """sites_list_site_premier_add_ons_slot

    

    :param resource_group_name: 
    :type resource_group_name: str
    :param name: 
    :type name: str
    :param slot: 
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_list_site_publishing_credentials(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets the web app publishing credentials

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_list_site_publishing_credentials_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Gets the web app publishing credentials

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_list_site_publishing_profile_xml(request: web.Request, resource_group_name, name, subscription_id, api_version, options) -> web.Response:
    """Gets the publishing profile for web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param options: Specifies options for publishing profile. Pass CsmPublishingProfileOptions.Format&#x3D;FileZilla3 for FileZilla FTP format.
    :type options: dict | bytes

    """
    options = CsmPublishingProfileOptions.from_dict(options)
    return web.Response(status=200)


async def sites_list_site_publishing_profile_xml_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, options) -> web.Response:
    """Gets the publishing profile for web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param options: Specifies options for publishing profile. Pass CsmPublishingProfileOptions.Format&#x3D;FileZilla3 for FileZilla FTP format.
    :type options: dict | bytes

    """
    options = CsmPublishingProfileOptions.from_dict(options)
    return web.Response(status=200)


async def sites_list_site_relay_service_connections(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Retrieves all BizTalk Hybrid Connections associated with this web app.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_list_site_relay_service_connections_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Retrieves all BizTalk Hybrid Connections associated with this web app.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param slot: The name of the slot for the web app.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_recover_site(request: web.Request, resource_group_name, name, subscription_id, api_version, recovery_entity) -> web.Response:
    """Recovers a deleted web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param recovery_entity: Snapshot data used for web app recovery. Snapshot information can be obtained by calling GetDeletedSites or GetSiteSnapshots API.
    :type recovery_entity: dict | bytes

    """
    recovery_entity = CsmSiteRecoveryEntity.from_dict(recovery_entity)
    return web.Response(status=200)


async def sites_recover_site_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, recovery_entity) -> web.Response:
    """Recovers a deleted web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param recovery_entity: Snapshot data used for web app recovery. Snapshot information can be obtained by calling GetDeletedSites or GetSiteSnapshots API.
    :type recovery_entity: dict | bytes

    """
    recovery_entity = CsmSiteRecoveryEntity.from_dict(recovery_entity)
    return web.Response(status=200)


async def sites_reset_production_slot_config(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Resets the configuration settings of the current slot if they were previously modified by calling ApplySlotConfig API

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_reset_slot_config_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Resets the configuration settings of the current slot if they were previously modified by calling ApplySlotConfig API

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_restart_site(request: web.Request, resource_group_name, name, subscription_id, api_version, soft_restart=None, synchronous=None) -> web.Response:
    """Restarts web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param soft_restart: Soft restart applies the configuration settings and restarts the app if necessary. Hard restart always restarts and reprovisions the app
    :type soft_restart: bool
    :param synchronous: If true then the API will block until the app has been restarted
    :type synchronous: bool

    """
    return web.Response(status=200)


async def sites_restart_site_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, soft_restart=None, synchronous=None) -> web.Response:
    """Restarts web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param soft_restart: Soft restart applies the configuration settings and restarts the app if necessary. Hard restart always restarts and reprovisions the app
    :type soft_restart: bool
    :param synchronous: If true then the API will block until the app has been restarted
    :type synchronous: bool

    """
    return web.Response(status=200)


async def sites_restore_site(request: web.Request, resource_group_name, name, backup_id, subscription_id, api_version, request) -> web.Response:
    """Restores a web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param backup_id: Id of backup to restore
    :type backup_id: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: Information on restore request
    :type request: dict | bytes

    """
    request = RestoreRequest.from_dict(request)
    return web.Response(status=200)


async def sites_restore_site_slot(request: web.Request, resource_group_name, name, backup_id, slot, subscription_id, api_version, request) -> web.Response:
    """Restores a web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param backup_id: Id of backup to restore
    :type backup_id: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: Information on restore request
    :type request: dict | bytes

    """
    request = RestoreRequest.from_dict(request)
    return web.Response(status=200)


async def sites_start_site(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Starts web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_start_site_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Starts web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_stop_site(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Stops web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_stop_site_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """Stops web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_swap_slot_with_production(request: web.Request, resource_group_name, name, subscription_id, api_version, slot_swap_entity) -> web.Response:
    """Swaps web app slots

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param slot_swap_entity: Request body that contains the target slot name
    :type slot_swap_entity: dict | bytes

    """
    slot_swap_entity = CsmSlotEntity.from_dict(slot_swap_entity)
    return web.Response(status=200)


async def sites_swap_slots_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, slot_swap_entity) -> web.Response:
    """Swaps web app slots

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of source slot for the swap
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param slot_swap_entity: Request body that contains the target slot name
    :type slot_swap_entity: dict | bytes

    """
    slot_swap_entity = CsmSlotEntity.from_dict(slot_swap_entity)
    return web.Response(status=200)


async def sites_sync_site_repository(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """sites_sync_site_repository

    

    :param resource_group_name: 
    :type resource_group_name: str
    :param name: 
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_sync_site_repository_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version) -> web.Response:
    """sites_sync_site_repository_slot

    

    :param resource_group_name: 
    :type resource_group_name: str
    :param name: 
    :type name: str
    :param slot: 
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def sites_update_site_app_settings(request: web.Request, resource_group_name, name, subscription_id, api_version, app_settings) -> web.Response:
    """Updates the application settings of web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param app_settings: Application settings of web app
    :type app_settings: dict | bytes

    """
    app_settings = StringDictionary.from_dict(app_settings)
    return web.Response(status=200)


async def sites_update_site_app_settings_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, app_settings) -> web.Response:
    """Updates the application settings of web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param app_settings: Application settings of web app
    :type app_settings: dict | bytes

    """
    app_settings = StringDictionary.from_dict(app_settings)
    return web.Response(status=200)


async def sites_update_site_auth_settings(request: web.Request, resource_group_name, name, subscription_id, api_version, site_auth_settings) -> web.Response:
    """Updates the Authentication / Authorization settings associated with web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_auth_settings: Auth settings associated with web app
    :type site_auth_settings: dict | bytes

    """
    site_auth_settings = SiteAuthSettings.from_dict(site_auth_settings)
    return web.Response(status=200)


async def sites_update_site_auth_settings_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, site_auth_settings) -> web.Response:
    """Updates the Authentication / Authorization settings associated with web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_auth_settings: Auth settings associated with web app
    :type site_auth_settings: dict | bytes

    """
    site_auth_settings = SiteAuthSettings.from_dict(site_auth_settings)
    return web.Response(status=200)


async def sites_update_site_backup_configuration(request: web.Request, resource_group_name, name, subscription_id, api_version, request) -> web.Response:
    """Updates backup configuration of web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: Information on backup request
    :type request: dict | bytes

    """
    request = BackupRequest.from_dict(request)
    return web.Response(status=200)


async def sites_update_site_backup_configuration_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, request) -> web.Response:
    """Updates backup configuration of web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param request: Information on backup request
    :type request: dict | bytes

    """
    request = BackupRequest.from_dict(request)
    return web.Response(status=200)


async def sites_update_site_config(request: web.Request, resource_group_name, name, subscription_id, api_version, site_config) -> web.Response:
    """Update the configuration of web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_config: Request body that contains the configuration setting for the web app
    :type site_config: dict | bytes

    """
    site_config = SiteConfig.from_dict(site_config)
    return web.Response(status=200)


async def sites_update_site_config_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, site_config) -> web.Response:
    """Update the configuration of web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_config: Request body that contains the configuration setting for the web app
    :type site_config: dict | bytes

    """
    site_config = SiteConfig.from_dict(site_config)
    return web.Response(status=200)


async def sites_update_site_connection_strings(request: web.Request, resource_group_name, name, subscription_id, api_version, connection_strings) -> web.Response:
    """Updates the connection strings associated with web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_strings: Connection strings associated with web app
    :type connection_strings: dict | bytes

    """
    connection_strings = ConnectionStringDictionary.from_dict(connection_strings)
    return web.Response(status=200)


async def sites_update_site_connection_strings_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, connection_strings) -> web.Response:
    """Updates the connection strings associated with web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_strings: Connection strings associated with web app
    :type connection_strings: dict | bytes

    """
    connection_strings = ConnectionStringDictionary.from_dict(connection_strings)
    return web.Response(status=200)


async def sites_update_site_logs_config(request: web.Request, resource_group_name, name, subscription_id, api_version, site_logs_config) -> web.Response:
    """Updates the meta data for web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_logs_config: Site logs configuration
    :type site_logs_config: dict | bytes

    """
    site_logs_config = SiteLogsConfig.from_dict(site_logs_config)
    return web.Response(status=200)


async def sites_update_site_logs_config_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, site_logs_config) -> web.Response:
    """Updates the meta data for web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_logs_config: Site logs configuration
    :type site_logs_config: dict | bytes

    """
    site_logs_config = SiteLogsConfig.from_dict(site_logs_config)
    return web.Response(status=200)


async def sites_update_site_metadata(request: web.Request, resource_group_name, name, subscription_id, api_version, metadata) -> web.Response:
    """Updates the meta data for web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param metadata: Meta data of web app
    :type metadata: dict | bytes

    """
    metadata = StringDictionary.from_dict(metadata)
    return web.Response(status=200)


async def sites_update_site_metadata_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, metadata) -> web.Response:
    """Updates the meta data for web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param metadata: Meta data of web app
    :type metadata: dict | bytes

    """
    metadata = StringDictionary.from_dict(metadata)
    return web.Response(status=200)


async def sites_update_site_relay_service_connection(request: web.Request, resource_group_name, name, entity_name, subscription_id, api_version, connection_envelope) -> web.Response:
    """Creates a new association to a BizTalk Hybrid Connection, or updates an existing one.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param entity_name: The name by which the Hybrid Connection is identified
    :type entity_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The details of the Hybrid Connection
    :type connection_envelope: dict | bytes

    """
    connection_envelope = RelayServiceConnectionEntity.from_dict(connection_envelope)
    return web.Response(status=200)


async def sites_update_site_relay_service_connection_slot(request: web.Request, resource_group_name, name, entity_name, slot, subscription_id, api_version, connection_envelope) -> web.Response:
    """Creates a new association to a BizTalk Hybrid Connection, or updates an existing one.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param entity_name: The name by which the Hybrid Connection is identified
    :type entity_name: str
    :param slot: The name of the slot for the web app.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The details of the Hybrid Connection
    :type connection_envelope: dict | bytes

    """
    connection_envelope = RelayServiceConnectionEntity.from_dict(connection_envelope)
    return web.Response(status=200)


async def sites_update_site_source_control(request: web.Request, resource_group_name, name, subscription_id, api_version, site_source_control) -> web.Response:
    """Update the source control configuration of web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_source_control: Request body that contains the source control parameters
    :type site_source_control: dict | bytes

    """
    site_source_control = SiteSourceControl.from_dict(site_source_control)
    return web.Response(status=200)


async def sites_update_site_source_control_slot(request: web.Request, resource_group_name, name, slot, subscription_id, api_version, site_source_control) -> web.Response:
    """Update the source control configuration of web app

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param slot: Name of web app slot. If not specified then will default to production slot.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param site_source_control: Request body that contains the source control parameters
    :type site_source_control: dict | bytes

    """
    site_source_control = SiteSourceControl.from_dict(site_source_control)
    return web.Response(status=200)


async def sites_update_site_vnet_connection(request: web.Request, resource_group_name, name, vnet_name, subscription_id, api_version, connection_envelope) -> web.Response:
    """Adds a Virtual Network Connection or updates it&#39;s properties.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param vnet_name: The name of the Virtual Network
    :type vnet_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The properties of this Virtual Network Connection
    :type connection_envelope: dict | bytes

    """
    connection_envelope = VnetInfo.from_dict(connection_envelope)
    return web.Response(status=200)


async def sites_update_site_vnet_connection_gateway(request: web.Request, resource_group_name, name, vnet_name, gateway_name, subscription_id, api_version, connection_envelope) -> web.Response:
    """Updates the Virtual Network Gateway.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param vnet_name: The name of the Virtual Network
    :type vnet_name: str
    :param gateway_name: The name of the gateway. The only gateway that exists presently is \&quot;primary\&quot;
    :type gateway_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The properties to update this gateway with.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = VnetGateway.from_dict(connection_envelope)
    return web.Response(status=200)


async def sites_update_site_vnet_connection_gateway_slot(request: web.Request, resource_group_name, name, vnet_name, gateway_name, slot, subscription_id, api_version, connection_envelope) -> web.Response:
    """Updates the Virtual Network Gateway.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param vnet_name: The name of the Virtual Network
    :type vnet_name: str
    :param gateway_name: The name of the gateway. The only gateway that exists presently is \&quot;primary\&quot;
    :type gateway_name: str
    :param slot: The name of the slot for this web app.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The properties to update this gateway with.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = VnetGateway.from_dict(connection_envelope)
    return web.Response(status=200)


async def sites_update_site_vnet_connection_slot(request: web.Request, resource_group_name, name, vnet_name, slot, subscription_id, api_version, connection_envelope) -> web.Response:
    """Adds a Virtual Network Connection or updates it&#39;s properties.

    

    :param resource_group_name: The resource group name
    :type resource_group_name: str
    :param name: The name of the web app
    :type name: str
    :param vnet_name: The name of the Virtual Network
    :type vnet_name: str
    :param slot: The name of the slot for this web app.
    :type slot: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The properties of this Virtual Network Connection
    :type connection_envelope: dict | bytes

    """
    connection_envelope = VnetInfo.from_dict(connection_envelope)
    return web.Response(status=200)


async def sites_update_slot_config_names(request: web.Request, resource_group_name, name, subscription_id, api_version, slot_config_names) -> web.Response:
    """Updates the names of application settings and connection string that remain with the slot during swap operation

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of web app
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param slot_config_names: Request body containing the names of application settings and connection strings
    :type slot_config_names: dict | bytes

    """
    slot_config_names = SlotConfigNamesResource.from_dict(slot_config_names)
    return web.Response(status=200)
