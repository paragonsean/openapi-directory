from typing import List, Dict
from aiohttp import web

from openapi_server.models.address_response import AddressResponse
from openapi_server.models.csm_usage_quota_collection import CsmUsageQuotaCollection
from openapi_server.models.hosting_environment import HostingEnvironment
from openapi_server.models.hosting_environment_collection import HostingEnvironmentCollection
from openapi_server.models.hosting_environment_diagnostics import HostingEnvironmentDiagnostics
from openapi_server.models.metric_definition import MetricDefinition
from openapi_server.models.metric_definition_collection import MetricDefinitionCollection
from openapi_server.models.resource_metric_collection import ResourceMetricCollection
from openapi_server.models.server_farm_collection import ServerFarmCollection
from openapi_server.models.site_collection import SiteCollection
from openapi_server.models.sku_info_collection import SkuInfoCollection
from openapi_server.models.stamp_capacity_collection import StampCapacityCollection
from openapi_server.models.usage_collection import UsageCollection
from openapi_server.models.worker_pool import WorkerPool
from openapi_server.models.worker_pool_collection import WorkerPoolCollection
from openapi_server import util


async def hosting_environments_create_or_update_hosting_environment(request: web.Request, resource_group_name, name, subscription_id, api_version, hosting_environment_envelope) -> web.Response:
    """Create or update a hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param hosting_environment_envelope: Properties of hostingEnvironment (App Service Environment)
    :type hosting_environment_envelope: dict | bytes

    """
    hosting_environment_envelope = HostingEnvironment.from_dict(hosting_environment_envelope)
    return web.Response(status=200)


async def hosting_environments_create_or_update_multi_role_pool(request: web.Request, resource_group_name, name, subscription_id, api_version, multi_role_pool_envelope) -> web.Response:
    """Create or update a multiRole pool.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param multi_role_pool_envelope: Properties of multiRole pool
    :type multi_role_pool_envelope: dict | bytes

    """
    multi_role_pool_envelope = WorkerPool.from_dict(multi_role_pool_envelope)
    return web.Response(status=200)


async def hosting_environments_create_or_update_worker_pool(request: web.Request, resource_group_name, name, worker_pool_name, subscription_id, api_version, worker_pool_envelope) -> web.Response:
    """Create or update a worker pool.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param worker_pool_name: Name of worker pool
    :type worker_pool_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param worker_pool_envelope: Properties of worker pool
    :type worker_pool_envelope: dict | bytes

    """
    worker_pool_envelope = WorkerPool.from_dict(worker_pool_envelope)
    return web.Response(status=200)


async def hosting_environments_delete_hosting_environment(request: web.Request, resource_group_name, name, subscription_id, api_version, force_delete=None) -> web.Response:
    """Delete a hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param force_delete: Delete even if the hostingEnvironment (App Service Environment) contains resources
    :type force_delete: bool

    """
    return web.Response(status=200)


async def hosting_environments_get_hosting_environment(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get properties of hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_hosting_environment_capacities(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get used, available, and total worker capacity for hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_hosting_environment_diagnostics(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get diagnostic information for hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_hosting_environment_diagnostics_item(request: web.Request, resource_group_name, name, diagnostics_name, subscription_id, api_version) -> web.Response:
    """Get diagnostic information for hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param diagnostics_name: Name of the diagnostics
    :type diagnostics_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_hosting_environment_metric_definitions(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get global metric definitions of hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_hosting_environment_metrics(request: web.Request, resource_group_name, name, subscription_id, api_version, details=None, filter=None) -> web.Response:
    """Get global metrics of hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param details: Include instance details
    :type details: bool
    :param filter: Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;.
    :type filter: str

    """
    return web.Response(status=200)


async def hosting_environments_get_hosting_environment_multi_role_metric_definitions(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get metric definitions for a multiRole pool of a hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_hosting_environment_multi_role_metrics(request: web.Request, resource_group_name, name, subscription_id, api_version, start_time=None, end_time=None, time_grain=None, details=None, filter=None) -> web.Response:
    """Get metrics for a multiRole pool of a hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param start_time: Beginning time of metrics query
    :type start_time: str
    :param end_time: End time of metrics query
    :type end_time: str
    :param time_grain: Time granularity of metrics query
    :type time_grain: str
    :param details: Include instance details
    :type details: bool
    :param filter: Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;.
    :type filter: str

    """
    return web.Response(status=200)


async def hosting_environments_get_hosting_environment_multi_role_usages(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get usages for a multiRole pool of a hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_hosting_environment_operation(request: web.Request, resource_group_name, name, operation_id, subscription_id, api_version) -> web.Response:
    """Get status of an operation on a hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param operation_id: operation identifier GUID
    :type operation_id: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_hosting_environment_operations(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """List all currently running operations on the hostingEnvironment (App Service Environment)

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_hosting_environment_server_farms(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get all serverfarms (App Service Plans) on the hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_hosting_environment_sites(request: web.Request, resource_group_name, name, subscription_id, api_version, properties_to_include=None) -> web.Response:
    """Get all sites on the hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param properties_to_include: Comma separated list of site properties to include
    :type properties_to_include: str

    """
    return web.Response(status=200)


async def hosting_environments_get_hosting_environment_usages(request: web.Request, resource_group_name, name, subscription_id, api_version, filter=None) -> web.Response:
    """Get global usages of hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param filter: Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;.
    :type filter: str

    """
    return web.Response(status=200)


async def hosting_environments_get_hosting_environment_vips(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get IP addresses assigned to the hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_hosting_environment_web_hosting_plans(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get all serverfarms (App Service Plans) on the hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_hosting_environment_web_worker_metric_definitions(request: web.Request, resource_group_name, name, worker_pool_name, subscription_id, api_version) -> web.Response:
    """Get metric definitions for a worker pool of a hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param worker_pool_name: Name of worker pool
    :type worker_pool_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_hosting_environment_web_worker_metrics(request: web.Request, resource_group_name, name, worker_pool_name, subscription_id, api_version, details=None, filter=None) -> web.Response:
    """Get metrics for a worker pool of a hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param worker_pool_name: Name of worker pool
    :type worker_pool_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param details: Include instance details
    :type details: bool
    :param filter: Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;.
    :type filter: str

    """
    return web.Response(status=200)


async def hosting_environments_get_hosting_environment_web_worker_usages(request: web.Request, resource_group_name, name, worker_pool_name, subscription_id, api_version) -> web.Response:
    """Get usages for a worker pool of a hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param worker_pool_name: Name of worker pool
    :type worker_pool_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_hosting_environments(request: web.Request, resource_group_name, subscription_id, api_version) -> web.Response:
    """Get all hostingEnvironments (App Service Environments) in a resource group.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_multi_role_pool(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get properties of a multiRole pool.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_multi_role_pool_instance_metric_definitions(request: web.Request, resource_group_name, name, instance, subscription_id, api_version) -> web.Response:
    """Get metric definitions for a specific instance of a multiRole pool of a hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param instance: Name of instance in the multiRole pool&amp;gt;
    :type instance: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_multi_role_pool_instance_metrics(request: web.Request, resource_group_name, name, instance, subscription_id, api_version, details=None) -> web.Response:
    """Get metrics for a specific instance of a multiRole pool of a hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param instance: Name of instance in the multiRole pool
    :type instance: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param details: Include instance details
    :type details: bool

    """
    return web.Response(status=200)


async def hosting_environments_get_multi_role_pool_skus(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get available skus for scaling a multiRole pool.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_multi_role_pools(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get all multi role pools

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_worker_pool(request: web.Request, resource_group_name, name, worker_pool_name, subscription_id, api_version) -> web.Response:
    """Get properties of a worker pool.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param worker_pool_name: Name of worker pool
    :type worker_pool_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_worker_pool_instance_metric_definitions(request: web.Request, resource_group_name, name, worker_pool_name, instance, subscription_id, api_version) -> web.Response:
    """Get metric definitions for a specific instance of a worker pool of a hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param worker_pool_name: Name of worker pool
    :type worker_pool_name: str
    :param instance: Name of instance in the worker pool
    :type instance: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_worker_pool_instance_metrics(request: web.Request, resource_group_name, name, worker_pool_name, instance, subscription_id, api_version, details=None, filter=None) -> web.Response:
    """Get metrics for a specific instance of a worker pool of a hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param worker_pool_name: Name of worker pool
    :type worker_pool_name: str
    :param instance: Name of instance in the worker pool
    :type instance: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str
    :param details: Include instance details
    :type details: bool
    :param filter: Return only usages/metrics specified in the filter. Filter conforms to odata syntax. Example: $filter&#x3D;(name.value eq &#39;Metric1&#39; or name.value eq &#39;Metric2&#39;) and startTime eq &#39;2014-01-01T00:00:00Z&#39; and endTime eq &#39;2014-12-31T23:59:59Z&#39; and timeGrain eq duration&#39;[Hour|Minute|Day]&#39;.
    :type filter: str

    """
    return web.Response(status=200)


async def hosting_environments_get_worker_pool_skus(request: web.Request, resource_group_name, name, worker_pool_name, subscription_id, api_version) -> web.Response:
    """Get available skus for scaling a worker pool.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param worker_pool_name: Name of worker pool
    :type worker_pool_name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_get_worker_pools(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Get all worker pools

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_reboot_hosting_environment(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Reboots all machines in a hostingEnvironment (App Service Environment).

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_resume_hosting_environment(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Resumes the hostingEnvironment.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)


async def hosting_environments_suspend_hosting_environment(request: web.Request, resource_group_name, name, subscription_id, api_version) -> web.Response:
    """Suspends the hostingEnvironment.

    

    :param resource_group_name: Name of resource group
    :type resource_group_name: str
    :param name: Name of hostingEnvironment (App Service Environment)
    :type name: str
    :param subscription_id: Subscription Id
    :type subscription_id: str
    :param api_version: API Version
    :type api_version: str

    """
    return web.Response(status=200)
