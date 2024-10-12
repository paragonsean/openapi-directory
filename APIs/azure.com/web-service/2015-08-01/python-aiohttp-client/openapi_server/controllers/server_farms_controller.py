from typing import List, Dict
from aiohttp import web

from openapi_server.models.metric_definition_collection import MetricDefinitionCollection
from openapi_server.models.resource_metric_collection import ResourceMetricCollection
from openapi_server.models.server_farm_collection import ServerFarmCollection
from openapi_server.models.server_farm_with_rich_sku import ServerFarmWithRichSku
from openapi_server.models.site_collection import SiteCollection
from openapi_server.models.vnet_gateway import VnetGateway
from openapi_server.models.vnet_info import VnetInfo
from openapi_server.models.vnet_route import VnetRoute
from openapi_server import util


async def server_farms_create_or_update_server_farm(request: web.Request, resource_group_name, name, subscription_id, api_version, server_farm_envelope, allow_pending_state=None) -> web.Response:
    """Creates or updates an App Service Plan

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of App Service Plan
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param server_farm_envelope: Details of App Service Plan
    :type server_farm_envelope: dict | bytes
    :param allow_pending_state: OBSOLETE: If true, allow pending state for App Service Plan
    :type allow_pending_state: bool

    """
    server_farm_envelope = ServerFarmWithRichSku.from_dict(server_farm_envelope)
    return web.Response(status=200)


async def server_farms_create_or_update_vnet_route(request: web.Request, resource_group_name, name, vnet_name, route_name, subscription_id, api_version, route) -> web.Response:
    """Creates a new route or updates an existing route for a vnet in an app service plan.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of App Service Plan
    :type name: str
    :param vnet_name: Name of virtual network
    :type vnet_name: str
    :param route_name: Name of the virtual network route
    :type route_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param route: The route object
    :type route: dict | bytes

    """
    route = VnetRoute.from_dict(route)
    return web.Response(status=200)


async def server_farms_delete_server_farm(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Deletes a App Service Plan

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of App Service Plan
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def server_farms_delete_vnet_route(request: web.Request, resource_group_name, name, vnet_name, route_name, subscription_id, api_version) -> web.Response:
    """Deletes an existing route for a vnet in an app service plan.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of App Service Plan
    :type name: str
    :param vnet_name: Name of virtual network
    :type vnet_name: str
    :param route_name: Name of the virtual network route
    :type route_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def server_farms_get_route_for_vnet(request: web.Request, resource_group_name, name, vnet_name, route_name, subscription_id, api_version) -> web.Response:
    """Gets a specific route associated with a vnet, in an app service plan

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of App Service Plan
    :type name: str
    :param vnet_name: Name of virtual network
    :type vnet_name: str
    :param route_name: Name of the virtual network route
    :type route_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def server_farms_get_routes_for_vnet(request: web.Request, resource_group_name, name, vnet_name, subscription_id, api_version) -> web.Response:
    """Gets a list of all routes associated with a vnet, in an app service plan

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of App Service Plan
    :type name: str
    :param vnet_name: Name of virtual network
    :type vnet_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def server_farms_get_server_farm(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets specified App Service Plan in a resource group

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of App Service Plan
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def server_farms_get_server_farm_metric_defintions(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """List of metrics that can be queried for an App Service Plan

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of App Service Plan
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def server_farms_get_server_farm_metrics(request: web.Request, resource_group_name, name, subscription_id, api_version, details=None, filter=None) -> web.Response:
    """Queries for App Service Plan metrics

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of App Service Plan
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param details: If true, metrics are broken down per App Service Plan instance
    :type details: bool
    :param filter: Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;.
    :type filter: str

    """
    return web.Response(status=200)


async def server_farms_get_server_farm_operation(request: web.Request, resource_group_name, name, operation_id, subscription_id, api_version) -> web.Response:
    """Gets a server farm operation

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of server farm
    :type name: str
    :param operation_id: Id of Server farm operation\&quot;&amp;gt;
    :type operation_id: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def server_farms_get_server_farm_sites(request: web.Request, resource_group_name, name, subscription_id, api_version, skip_token=None, filter=None, top=None) -> web.Response:
    """Gets list of Apps associated with an App Service Plan

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of App Service Plan
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param skip_token: Skip to of web apps in a list. If specified, the resulting list will contain web apps starting from (including) the skipToken. Else, the resulting list contains web apps from the start of the list
    :type skip_token: str
    :param filter: Supported filter: $filter&#x3D;state eq running. Returns only web apps that are currently running
    :type filter: str
    :param top: List page size. If specified, results are paged.
    :type top: str

    """
    return web.Response(status=200)


async def server_farms_get_server_farm_vnet_gateway(request: web.Request, resource_group_name, name, vnet_name, gateway_name, subscription_id, api_version) -> web.Response:
    """Gets the vnet gateway.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of the App Service Plan
    :type name: str
    :param vnet_name: Name of the virtual network
    :type vnet_name: str
    :param gateway_name: Name of the gateway. Only the &#39;primary&#39; gateway is supported.
    :type gateway_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def server_farms_get_server_farms(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """Gets collection of App Service Plans in a resource group for a given subscription.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def server_farms_get_vnet_from_server_farm(request: web.Request, resource_group_name, name, vnet_name, subscription_id, api_version) -> web.Response:
    """Gets a vnet associated with an App Service Plan

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of App Service Plan
    :type name: str
    :param vnet_name: Name of virtual network
    :type vnet_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def server_farms_get_vnets_for_server_farm(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets list of VNets associated with App Service Plan

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of App Service Plan
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def server_farms_reboot_worker_for_server_farm(request: web.Request, resource_group_name, name, worker_name, subscription_id, api_version) -> web.Response:
    """Submit a reboot request for a worker machine in the specified server farm

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of server farm
    :type name: str
    :param worker_name: Name of worker machine, typically starts with RD
    :type worker_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def server_farms_restart_sites_for_server_farm(request: web.Request, resource_group_name, name, subscription_id, api_version, soft_restart=None) -> web.Response:
    """Restarts web apps in a specified App Service Plan

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of App Service Plan
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param soft_restart: Soft restart applies the configuration settings and restarts the apps if necessary. Hard restart always restarts and reprovisions the apps
    :type soft_restart: bool

    """
    return web.Response(status=200)


async def server_farms_update_server_farm_vnet_gateway(request: web.Request, resource_group_name, name, vnet_name, gateway_name, subscription_id, api_version, connection_envelope) -> web.Response:
    """Updates the vnet gateway

    

    :param resource_group_name: The resource group
    :type resource_group_name: str
    :param name: The name of the App Service Plan
    :type name: str
    :param vnet_name: The name of the virtual network
    :type vnet_name: str
    :param gateway_name: The name of the gateway. Only &#39;primary&#39; is supported.
    :type gateway_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: The gateway entity.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = VnetGateway.from_dict(connection_envelope)
    return web.Response(status=200)


async def server_farms_update_vnet_route(request: web.Request, resource_group_name, name, vnet_name, route_name, subscription_id, api_version, route) -> web.Response:
    """Creates a new route or updates an existing route for a vnet in an app service plan.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of App Service Plan
    :type name: str
    :param vnet_name: Name of virtual network
    :type vnet_name: str
    :param route_name: Name of the virtual network route
    :type route_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param route: The route object
    :type route: dict | bytes

    """
    route = VnetRoute.from_dict(route)
    return web.Response(status=200)
