from typing import List, Dict
from aiohttp import web

from openapi_server.models.app_service_plan_patch_resource import AppServicePlanPatchResource
from openapi_server.models.app_service_plans_create_or_update_vnet_route_request import AppServicePlansCreateOrUpdateVnetRouteRequest
from openapi_server.models.app_service_plans_get200_response import AppServicePlansGet200Response
from openapi_server.models.app_service_plans_get_hybrid_connection200_response import AppServicePlansGetHybridConnection200Response
from openapi_server.models.app_service_plans_get_vnet_from_server_farm200_response import AppServicePlansGetVnetFromServerFarm200Response
from openapi_server.models.app_service_plans_get_vnet_gateway200_response import AppServicePlansGetVnetGateway200Response
from openapi_server.models.app_service_plans_list200_response import AppServicePlansList200Response
from openapi_server.models.app_service_plans_list200_response_value_inner_sku_capabilities_inner import AppServicePlansList200ResponseValueInnerSkuCapabilitiesInner
from openapi_server.models.app_service_plans_list_default_response import AppServicePlansListDefaultResponse
from openapi_server.models.app_service_plans_list_hybrid_connection_keys200_response import AppServicePlansListHybridConnectionKeys200Response
from openapi_server.models.app_service_plans_list_metric_defintions200_response import AppServicePlansListMetricDefintions200Response
from openapi_server.models.app_service_plans_list_metrics200_response import AppServicePlansListMetrics200Response
from openapi_server.models.app_service_plans_list_usages200_response import AppServicePlansListUsages200Response
from openapi_server.models.app_service_plans_list_vnets200_response_inner import AppServicePlansListVnets200ResponseInner
from openapi_server.models.app_service_plans_list_vnets200_response_inner_properties_routes_inner import AppServicePlansListVnets200ResponseInnerPropertiesRoutesInner
from openapi_server.models.app_service_plans_list_web_apps200_response import AppServicePlansListWebApps200Response
from openapi_server.models.hybrid_connection_collection import HybridConnectionCollection
from openapi_server.models.hybrid_connection_limits import HybridConnectionLimits
from openapi_server.models.resource_collection import ResourceCollection
from openapi_server import util


async def app_service_plans_create_or_update(request: web.Request, resource_group_name, name, subscription_id, api_version, app_service_plan) -> web.Response:
    """Creates or updates an App Service Plan.

    Creates or updates an App Service Plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param app_service_plan: Details of the App Service plan.
    :type app_service_plan: dict | bytes

    """
    app_service_plan = AppServicePlansGet200Response.from_dict(app_service_plan)
    return web.Response(status=200)


async def app_service_plans_create_or_update_vnet_route(request: web.Request, resource_group_name, name, vnet_name, route_name, subscription_id, api_version, route) -> web.Response:
    """Create or update a Virtual Network route in an App Service plan.

    Create or update a Virtual Network route in an App Service plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param vnet_name: Name of the Virtual Network.
    :type vnet_name: str
    :param route_name: Name of the Virtual Network route.
    :type route_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param route: Definition of the Virtual Network route.
    :type route: dict | bytes

    """
    route = AppServicePlansCreateOrUpdateVnetRouteRequest.from_dict(route)
    return web.Response(status=200)


async def app_service_plans_delete(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Delete an App Service plan.

    Delete an App Service plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_plans_delete_hybrid_connection(request: web.Request, resource_group_name, name, namespace_name, relay_name, subscription_id, api_version) -> web.Response:
    """Delete a Hybrid Connection in use in an App Service plan.

    Delete a Hybrid Connection in use in an App Service plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param namespace_name: Name of the Service Bus namespace.
    :type namespace_name: str
    :param relay_name: Name of the Service Bus relay.
    :type relay_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_plans_delete_vnet_route(request: web.Request, resource_group_name, name, vnet_name, route_name, subscription_id, api_version) -> web.Response:
    """Delete a Virtual Network route in an App Service plan.

    Delete a Virtual Network route in an App Service plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param vnet_name: Name of the Virtual Network.
    :type vnet_name: str
    :param route_name: Name of the Virtual Network route.
    :type route_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_plans_get(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get an App Service plan.

    Get an App Service plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_plans_get_hybrid_connection(request: web.Request, resource_group_name, name, namespace_name, relay_name, subscription_id, api_version) -> web.Response:
    """Retrieve a Hybrid Connection in use in an App Service plan.

    Retrieve a Hybrid Connection in use in an App Service plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param namespace_name: Name of the Service Bus namespace.
    :type namespace_name: str
    :param relay_name: Name of the Service Bus relay.
    :type relay_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_plans_get_hybrid_connection_plan_limit(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get the maximum number of Hybrid Connections allowed in an App Service plan.

    Get the maximum number of Hybrid Connections allowed in an App Service plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_plans_get_route_for_vnet(request: web.Request, resource_group_name, name, vnet_name, route_name, subscription_id, api_version) -> web.Response:
    """Get a Virtual Network route in an App Service plan.

    Get a Virtual Network route in an App Service plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param vnet_name: Name of the Virtual Network.
    :type vnet_name: str
    :param route_name: Name of the Virtual Network route.
    :type route_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_plans_get_server_farm_skus(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Gets all selectable SKUs for a given App Service Plan

    Gets all selectable SKUs for a given App Service Plan

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of App Service Plan
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_plans_get_vnet_from_server_farm(request: web.Request, resource_group_name, name, vnet_name, subscription_id, api_version) -> web.Response:
    """Get a Virtual Network associated with an App Service plan.

    Get a Virtual Network associated with an App Service plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param vnet_name: Name of the Virtual Network.
    :type vnet_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_plans_get_vnet_gateway(request: web.Request, resource_group_name, name, vnet_name, gateway_name, subscription_id, api_version) -> web.Response:
    """Get a Virtual Network gateway.

    Get a Virtual Network gateway.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param vnet_name: Name of the Virtual Network.
    :type vnet_name: str
    :param gateway_name: Name of the gateway. Only the &#39;primary&#39; gateway is supported.
    :type gateway_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_plans_list(request: web.Request, subscription_id, api_version, detailed=None) -> web.Response:
    """Get all App Service plans for a subscription.

    Get all App Service plans for a subscription.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param detailed: Specify &lt;code&gt;true&lt;/code&gt; to return all App Service plan properties. The default is &lt;code&gt;false&lt;/code&gt;, which returns a subset of the properties.  Retrieval of all properties may increase the API latency.
    :type detailed: bool

    """
    return web.Response(status=200)


async def app_service_plans_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """Get all App Service plans in a resource group.

    Get all App Service plans in a resource group.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_plans_list_capabilities(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """List all capabilities of an App Service plan.

    List all capabilities of an App Service plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_plans_list_hybrid_connection_keys(request: web.Request, resource_group_name, name, namespace_name, relay_name, subscription_id, api_version) -> web.Response:
    """Get the send key name and value of a Hybrid Connection.

    Get the send key name and value of a Hybrid Connection.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param namespace_name: The name of the Service Bus namespace.
    :type namespace_name: str
    :param relay_name: The name of the Service Bus relay.
    :type relay_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_plans_list_hybrid_connections(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Retrieve all Hybrid Connections in use in an App Service plan.

    Retrieve all Hybrid Connections in use in an App Service plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_plans_list_metric_defintions(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get metrics that can be queried for an App Service plan, and their definitions.

    Get metrics that can be queried for an App Service plan, and their definitions.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_plans_list_metrics(request: web.Request, resource_group_name, name, subscription_id, api_version, details=None, filter=None) -> web.Response:
    """Get metrics for an App Service plan.

    Get metrics for an App Service plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param details: Specify &lt;code&gt;true&lt;/code&gt; to include instance details. The default is &lt;code&gt;false&lt;/code&gt;.
    :type details: bool
    :param filter: Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;.
    :type filter: str

    """
    return web.Response(status=200)


async def app_service_plans_list_routes_for_vnet(request: web.Request, resource_group_name, name, vnet_name, subscription_id, api_version) -> web.Response:
    """Get all routes that are associated with a Virtual Network in an App Service plan.

    Get all routes that are associated with a Virtual Network in an App Service plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param vnet_name: Name of the Virtual Network.
    :type vnet_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_plans_list_usages(request: web.Request, resource_group_name, name, subscription_id, api_version, filter=None) -> web.Response:
    """Gets server farm usage information

    Gets server farm usage information

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of App Service Plan
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param filter: Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;).
    :type filter: str

    """
    return web.Response(status=200)


async def app_service_plans_list_vnets(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get all Virtual Networks associated with an App Service plan.

    Get all Virtual Networks associated with an App Service plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_plans_list_web_apps(request: web.Request, resource_group_name, name, subscription_id, api_version, skip_token=None, filter=None, top=None) -> web.Response:
    """Get all apps associated with an App Service plan.

    Get all apps associated with an App Service plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param skip_token: Skip to a web app in the list of webapps associated with app service plan. If specified, the resulting list will contain web apps starting from (including) the skipToken. Otherwise, the resulting list contains web apps from the start of the list
    :type skip_token: str
    :param filter: Supported filter: $filter&#x3D;state eq running. Returns only web apps that are currently running
    :type filter: str
    :param top: List page size. If specified, results are paged.
    :type top: str

    """
    return web.Response(status=200)


async def app_service_plans_list_web_apps_by_hybrid_connection(request: web.Request, resource_group_name, name, namespace_name, relay_name, subscription_id, api_version) -> web.Response:
    """Get all apps that use a Hybrid Connection in an App Service Plan.

    Get all apps that use a Hybrid Connection in an App Service Plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param namespace_name: Name of the Hybrid Connection namespace.
    :type namespace_name: str
    :param relay_name: Name of the Hybrid Connection relay.
    :type relay_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_plans_reboot_worker(request: web.Request, resource_group_name, name, worker_name, subscription_id, api_version) -> web.Response:
    """Reboot a worker machine in an App Service plan.

    Reboot a worker machine in an App Service plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param worker_name: Name of worker machine, which typically starts with RD.
    :type worker_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_plans_restart_web_apps(request: web.Request, resource_group_name, name, subscription_id, api_version, soft_restart=None) -> web.Response:
    """Restart all apps in an App Service plan.

    Restart all apps in an App Service plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param soft_restart: Specify &lt;code&gt;true&lt;/code&gt; to perform a soft restart, applies the configuration settings and restarts the apps if necessary. The default is &lt;code&gt;false&lt;/code&gt;, which always restarts and reprovisions the apps
    :type soft_restart: bool

    """
    return web.Response(status=200)


async def app_service_plans_update(request: web.Request, resource_group_name, name, subscription_id, api_version, app_service_plan) -> web.Response:
    """Creates or updates an App Service Plan.

    Creates or updates an App Service Plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param app_service_plan: Details of the App Service plan.
    :type app_service_plan: dict | bytes

    """
    app_service_plan = AppServicePlanPatchResource.from_dict(app_service_plan)
    return web.Response(status=200)


async def app_service_plans_update_vnet_gateway(request: web.Request, resource_group_name, name, vnet_name, gateway_name, subscription_id, api_version, connection_envelope) -> web.Response:
    """Update a Virtual Network gateway.

    Update a Virtual Network gateway.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param vnet_name: Name of the Virtual Network.
    :type vnet_name: str
    :param gateway_name: Name of the gateway. Only the &#39;primary&#39; gateway is supported.
    :type gateway_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param connection_envelope: Definition of the gateway.
    :type connection_envelope: dict | bytes

    """
    connection_envelope = AppServicePlansGetVnetGateway200Response.from_dict(connection_envelope)
    return web.Response(status=200)


async def app_service_plans_update_vnet_route(request: web.Request, resource_group_name, name, vnet_name, route_name, subscription_id, api_version, route) -> web.Response:
    """Create or update a Virtual Network route in an App Service plan.

    Create or update a Virtual Network route in an App Service plan.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service plan.
    :type name: str
    :param vnet_name: Name of the Virtual Network.
    :type vnet_name: str
    :param route_name: Name of the Virtual Network route.
    :type route_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param route: Definition of the Virtual Network route.
    :type route: dict | bytes

    """
    route = AppServicePlansCreateOrUpdateVnetRouteRequest.from_dict(route)
    return web.Response(status=200)
