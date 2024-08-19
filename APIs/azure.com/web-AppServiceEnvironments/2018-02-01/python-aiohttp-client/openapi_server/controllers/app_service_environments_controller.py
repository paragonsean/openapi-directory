from typing import List, Dict
from aiohttp import web

from openapi_server.models.address_response import AddressResponse
from openapi_server.models.app_service_environment_collection import AppServiceEnvironmentCollection
from openapi_server.models.app_service_environment_patch_resource import AppServiceEnvironmentPatchResource
from openapi_server.models.app_service_environment_resource import AppServiceEnvironmentResource
from openapi_server.models.app_service_environments_change_vnet200_response import AppServiceEnvironmentsChangeVnet200Response
from openapi_server.models.app_service_environments_change_vnet_request import AppServiceEnvironmentsChangeVnetRequest
from openapi_server.models.app_service_environments_list_app_service_plans200_response import AppServiceEnvironmentsListAppServicePlans200Response
from openapi_server.models.app_service_environments_list_default_response import AppServiceEnvironmentsListDefaultResponse
from openapi_server.models.app_service_environments_list_metrics200_response import AppServiceEnvironmentsListMetrics200Response
from openapi_server.models.app_service_environments_list_multi_role_pool_instance_metric_definitions200_response import AppServiceEnvironmentsListMultiRolePoolInstanceMetricDefinitions200Response
from openapi_server.models.app_service_environments_list_operations200_response_inner import AppServiceEnvironmentsListOperations200ResponseInner
from openapi_server.models.app_service_environments_list_usages200_response import AppServiceEnvironmentsListUsages200Response
from openapi_server.models.hosting_environment_diagnostics import HostingEnvironmentDiagnostics
from openapi_server.models.inbound_environment_endpoint_collection import InboundEnvironmentEndpointCollection
from openapi_server.models.metric_definition import MetricDefinition
from openapi_server.models.outbound_environment_endpoint_collection import OutboundEnvironmentEndpointCollection
from openapi_server.models.sku_info_collection import SkuInfoCollection
from openapi_server.models.stamp_capacity_collection import StampCapacityCollection
from openapi_server.models.usage_collection import UsageCollection
from openapi_server.models.worker_pool_collection import WorkerPoolCollection
from openapi_server.models.worker_pool_resource import WorkerPoolResource
from openapi_server import util


async def app_service_environments_change_vnet(request: web.Request, resource_group_name, name, subscription_id, api_version, vnet_info) -> web.Response:
    """Move an App Service Environment to a different VNET.

    Move an App Service Environment to a different VNET.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param vnet_info: Details for the new virtual network.
    :type vnet_info: dict | bytes

    """
    vnet_info = AppServiceEnvironmentsChangeVnetRequest.from_dict(vnet_info)
    return web.Response(status=200)


async def app_service_environments_create_or_update(request: web.Request, resource_group_name, name, subscription_id, api_version, hosting_environment_envelope) -> web.Response:
    """Create or update an App Service Environment.

    Create or update an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param hosting_environment_envelope: Configuration details of the App Service Environment.
    :type hosting_environment_envelope: dict | bytes

    """
    hosting_environment_envelope = AppServiceEnvironmentResource.from_dict(hosting_environment_envelope)
    return web.Response(status=200)


async def app_service_environments_create_or_update_multi_role_pool(request: web.Request, resource_group_name, name, subscription_id, api_version, multi_role_pool_envelope) -> web.Response:
    """Create or update a multi-role pool.

    Create or update a multi-role pool.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param multi_role_pool_envelope: Properties of the multi-role pool.
    :type multi_role_pool_envelope: dict | bytes

    """
    multi_role_pool_envelope = WorkerPoolResource.from_dict(multi_role_pool_envelope)
    return web.Response(status=200)


async def app_service_environments_create_or_update_worker_pool(request: web.Request, resource_group_name, name, worker_pool_name, subscription_id, api_version, worker_pool_envelope) -> web.Response:
    """Create or update a worker pool.

    Create or update a worker pool.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param worker_pool_name: Name of the worker pool.
    :type worker_pool_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param worker_pool_envelope: Properties of the worker pool.
    :type worker_pool_envelope: dict | bytes

    """
    worker_pool_envelope = WorkerPoolResource.from_dict(worker_pool_envelope)
    return web.Response(status=200)


async def app_service_environments_delete(request: web.Request, resource_group_name, name, subscription_id, api_version, force_delete=None) -> web.Response:
    """Delete an App Service Environment.

    Delete an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param force_delete: Specify &lt;code&gt;true&lt;/code&gt; to force the deletion even if the App Service Environment contains resources. The default is &lt;code&gt;false&lt;/code&gt;.
    :type force_delete: bool

    """
    return web.Response(status=200)


async def app_service_environments_get(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get the properties of an App Service Environment.

    Get the properties of an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_get_diagnostics_item(request: web.Request, resource_group_name, name, diagnostics_name, subscription_id, api_version) -> web.Response:
    """Get a diagnostics item for an App Service Environment.

    Get a diagnostics item for an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param diagnostics_name: Name of the diagnostics item.
    :type diagnostics_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_get_inbound_network_dependencies_endpoints(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get the network endpoints of all inbound dependencies of an App Service Environment.

    Get the network endpoints of all inbound dependencies of an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_get_multi_role_pool(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get properties of a multi-role pool.

    Get properties of a multi-role pool.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_get_outbound_network_dependencies_endpoints(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get the network endpoints of all outbound dependencies of an App Service Environment.

    Get the network endpoints of all outbound dependencies of an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_get_worker_pool(request: web.Request, resource_group_name, name, worker_pool_name, subscription_id, api_version) -> web.Response:
    """Get properties of a worker pool.

    Get properties of a worker pool.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param worker_pool_name: Name of the worker pool.
    :type worker_pool_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_list(request: web.Request, subscription_id, api_version) -> web.Response:
    """Get all App Service Environments for a subscription.

    Get all App Service Environments for a subscription.

    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_list_app_service_plans(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get all App Service plans in an App Service Environment.

    Get all App Service plans in an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_list_by_resource_group(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """Get all App Service Environments in a resource group.

    Get all App Service Environments in a resource group.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_list_capacities(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get the used, available, and total worker capacity an App Service Environment.

    Get the used, available, and total worker capacity an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_list_diagnostics(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get diagnostic information for an App Service Environment.

    Get diagnostic information for an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_list_metric_definitions(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get global metric definitions of an App Service Environment.

    Get global metric definitions of an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_list_metrics(request: web.Request, resource_group_name, name, subscription_id, api_version, details=None, filter=None) -> web.Response:
    """Get global metrics of an App Service Environment.

    Get global metrics of an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
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


async def app_service_environments_list_multi_role_metric_definitions(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get metric definitions for a multi-role pool of an App Service Environment.

    Get metric definitions for a multi-role pool of an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_list_multi_role_metrics(request: web.Request, resource_group_name, name, subscription_id, api_version, start_time=None, end_time=None, time_grain=None, details=None, filter=None) -> web.Response:
    """Get metrics for a multi-role pool of an App Service Environment.

    Get metrics for a multi-role pool of an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param start_time: Beginning time of the metrics query.
    :type start_time: str
    :param end_time: End time of the metrics query.
    :type end_time: str
    :param time_grain: Time granularity of the metrics query.
    :type time_grain: str
    :param details: Specify &lt;code&gt;true&lt;/code&gt; to include instance details. The default is &lt;code&gt;false&lt;/code&gt;.
    :type details: bool
    :param filter: Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;.
    :type filter: str

    """
    return web.Response(status=200)


async def app_service_environments_list_multi_role_pool_instance_metric_definitions(request: web.Request, resource_group_name, name, instance, subscription_id, api_version) -> web.Response:
    """Get metric definitions for a specific instance of a multi-role pool of an App Service Environment.

    Get metric definitions for a specific instance of a multi-role pool of an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param instance: Name of the instance in the multi-role pool.
    :type instance: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_list_multi_role_pool_instance_metrics(request: web.Request, resource_group_name, name, instance, subscription_id, api_version, details=None) -> web.Response:
    """Get metrics for a specific instance of a multi-role pool of an App Service Environment.

    Get metrics for a specific instance of a multi-role pool of an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param instance: Name of the instance in the multi-role pool.
    :type instance: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param details: Specify &lt;code&gt;true&lt;/code&gt; to include instance details. The default is &lt;code&gt;false&lt;/code&gt;.
    :type details: bool

    """
    return web.Response(status=200)


async def app_service_environments_list_multi_role_pool_skus(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get available SKUs for scaling a multi-role pool.

    Get available SKUs for scaling a multi-role pool.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_list_multi_role_pools(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get all multi-role pools.

    Get all multi-role pools.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_list_multi_role_usages(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get usage metrics for a multi-role pool of an App Service Environment.

    Get usage metrics for a multi-role pool of an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_list_operations(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """List all currently running operations on the App Service Environment.

    List all currently running operations on the App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_list_usages(request: web.Request, resource_group_name, name, subscription_id, api_version, filter=None) -> web.Response:
    """Get global usage metrics of an App Service Environment.

    Get global usage metrics of an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param filter: Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq 2014-01-01T00:00:00Z and endTime eq 2014-12-31T23:59:59Z and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;.
    :type filter: str

    """
    return web.Response(status=200)


async def app_service_environments_list_vips(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get IP addresses assigned to an App Service Environment.

    Get IP addresses assigned to an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_list_web_apps(request: web.Request, resource_group_name, name, subscription_id, api_version, properties_to_include=None) -> web.Response:
    """Get all apps in an App Service Environment.

    Get all apps in an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param properties_to_include: Comma separated list of app properties to include.
    :type properties_to_include: str

    """
    return web.Response(status=200)


async def app_service_environments_list_web_worker_metric_definitions(request: web.Request, resource_group_name, name, worker_pool_name, subscription_id, api_version) -> web.Response:
    """Get metric definitions for a worker pool of an App Service Environment.

    Get metric definitions for a worker pool of an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param worker_pool_name: Name of the worker pool.
    :type worker_pool_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_list_web_worker_metrics(request: web.Request, resource_group_name, name, worker_pool_name, subscription_id, api_version, details=None, filter=None) -> web.Response:
    """Get metrics for a worker pool of a AppServiceEnvironment (App Service Environment).

    Get metrics for a worker pool of a AppServiceEnvironment (App Service Environment).

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param worker_pool_name: Name of worker pool
    :type worker_pool_name: str
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


async def app_service_environments_list_web_worker_usages(request: web.Request, resource_group_name, name, worker_pool_name, subscription_id, api_version) -> web.Response:
    """Get usage metrics for a worker pool of an App Service Environment.

    Get usage metrics for a worker pool of an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param worker_pool_name: Name of the worker pool.
    :type worker_pool_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_list_worker_pool_instance_metric_definitions(request: web.Request, resource_group_name, name, worker_pool_name, instance, subscription_id, api_version) -> web.Response:
    """Get metric definitions for a specific instance of a worker pool of an App Service Environment.

    Get metric definitions for a specific instance of a worker pool of an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param worker_pool_name: Name of the worker pool.
    :type worker_pool_name: str
    :param instance: Name of the instance in the worker pool.
    :type instance: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_list_worker_pool_instance_metrics(request: web.Request, resource_group_name, name, worker_pool_name, instance, subscription_id, api_version, details=None, filter=None) -> web.Response:
    """Get metrics for a specific instance of a worker pool of an App Service Environment.

    Get metrics for a specific instance of a worker pool of an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param worker_pool_name: Name of the worker pool.
    :type worker_pool_name: str
    :param instance: Name of the instance in the worker pool.
    :type instance: str
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


async def app_service_environments_list_worker_pool_skus(request: web.Request, resource_group_name, name, worker_pool_name, subscription_id, api_version) -> web.Response:
    """Get available SKUs for scaling a worker pool.

    Get available SKUs for scaling a worker pool.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param worker_pool_name: Name of the worker pool.
    :type worker_pool_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_list_worker_pools(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get all worker pools of an App Service Environment.

    Get all worker pools of an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_reboot(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Reboot all machines in an App Service Environment.

    Reboot all machines in an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_resume(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Resume an App Service Environment.

    Resume an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_suspend(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Suspend an App Service Environment.

    Suspend an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def app_service_environments_update(request: web.Request, resource_group_name, name, subscription_id, api_version, hosting_environment_envelope) -> web.Response:
    """Create or update an App Service Environment.

    Create or update an App Service Environment.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param hosting_environment_envelope: Configuration details of the App Service Environment.
    :type hosting_environment_envelope: dict | bytes

    """
    hosting_environment_envelope = AppServiceEnvironmentPatchResource.from_dict(hosting_environment_envelope)
    return web.Response(status=200)


async def app_service_environments_update_multi_role_pool(request: web.Request, resource_group_name, name, subscription_id, api_version, multi_role_pool_envelope) -> web.Response:
    """Create or update a multi-role pool.

    Create or update a multi-role pool.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param multi_role_pool_envelope: Properties of the multi-role pool.
    :type multi_role_pool_envelope: dict | bytes

    """
    multi_role_pool_envelope = WorkerPoolResource.from_dict(multi_role_pool_envelope)
    return web.Response(status=200)


async def app_service_environments_update_worker_pool(request: web.Request, resource_group_name, name, worker_pool_name, subscription_id, api_version, worker_pool_envelope) -> web.Response:
    """Create or update a worker pool.

    Create or update a worker pool.

    :param resource_group_name: Name of the resource group to which the resource belongs.
    :type resource_group_name: str
    :param name: Name of the App Service Environment.
    :type name: str
    :param worker_pool_name: Name of the worker pool.
    :type worker_pool_name: str
    :param subscription_id: Your Azure subscription ID. This is a GUID-formatted string (e.g. 00000000-0000-0000-0000-000000000000).
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param worker_pool_envelope: Properties of the worker pool.
    :type worker_pool_envelope: dict | bytes

    """
    worker_pool_envelope = WorkerPoolResource.from_dict(worker_pool_envelope)
    return web.Response(status=200)
