from typing import List, Dict
from aiohttp import web

from openapi_server.models.auto_scale_run import AutoScaleRun
from openapi_server.models.batch_error import BatchError
from openapi_server.models.cloud_pool import CloudPool
from openapi_server.models.cloud_pool_list_result import CloudPoolListResult
from openapi_server.models.pool_add_parameter import PoolAddParameter
from openapi_server.models.pool_enable_auto_scale_parameter import PoolEnableAutoScaleParameter
from openapi_server.models.pool_evaluate_auto_scale_parameter import PoolEvaluateAutoScaleParameter
from openapi_server.models.pool_list_pool_usage_metrics_result import PoolListPoolUsageMetricsResult
from openapi_server.models.pool_patch_parameter import PoolPatchParameter
from openapi_server.models.pool_resize_parameter import PoolResizeParameter
from openapi_server.models.pool_statistics import PoolStatistics
from openapi_server.models.pool_update_properties_parameter import PoolUpdatePropertiesParameter
from openapi_server.models.pool_upgrade_os_parameter import PoolUpgradeOSParameter
from openapi_server import util


async def pool_add(request: web.Request, api_version, pool, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Adds a pool to the specified account.

    When naming pools, avoid including sensitive information such as user names or secret project names. This information may appear in telemetry logs accessible to Microsoft Support engineers.

    :param api_version: Client API Version.
    :type api_version: str
    :param pool: The pool to be added.
    :type pool: dict | bytes
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    pool = PoolAddParameter.from_dict(pool)
    return web.Response(status=200)


async def pool_delete(request: web.Request, pool_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """Deletes a pool from the specified account.

    When you request that a pool be deleted, the following actions occur: the pool state is set to deleting; any ongoing resize operation on the pool are stopped; the Batch service starts resizing the pool to zero nodes; any tasks running on existing nodes are terminated and requeued (as if a resize pool operation had been requested with the default requeue option); finally, the pool is removed from the system. Because running tasks are requeued, the user can rerun these tasks by updating their job to target a different pool. The tasks can then run on the new pool. If you want to override the requeue behavior, then you should call resize pool explicitly to shrink the pool to zero size before deleting the pool. If you call an Update, Patch or Delete API on a pool in the deleting state, it will fail with HTTP status code 409 with error code PoolBeingDeleted.

    :param pool_id: The ID of the pool to delete.
    :type pool_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param if_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified.
    :type if_match: str
    :param if_none_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag.
    :type if_none_match: str
    :param if_modified_since: Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    :type if_modified_since: str
    :param if_unmodified_since: Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    :type if_unmodified_since: str

    """
    return web.Response(status=200)


async def pool_disable_auto_scale(request: web.Request, pool_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Disables automatic scaling for a pool.

    

    :param pool_id: The ID of the pool on which to disable automatic scaling.
    :type pool_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def pool_enable_auto_scale(request: web.Request, pool_id, api_version, pool_enable_auto_scale_parameter, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """Enables automatic scaling for a pool.

    You cannot enable automatic scaling on a pool if a resize operation is in progress on the pool. If automatic scaling of the pool is currently disabled, you must specify a valid autoscale formula as part of the request. If automatic scaling of the pool is already enabled, you may specify a new autoscale formula and/or a new evaluation interval. You cannot call this API for the same pool more than once every 30 seconds.

    :param pool_id: The ID of the pool on which to enable automatic scaling.
    :type pool_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param pool_enable_auto_scale_parameter: The parameters for the request.
    :type pool_enable_auto_scale_parameter: dict | bytes
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param if_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified.
    :type if_match: str
    :param if_none_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag.
    :type if_none_match: str
    :param if_modified_since: Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    :type if_modified_since: str
    :param if_unmodified_since: Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    :type if_unmodified_since: str

    """
    pool_enable_auto_scale_parameter = PoolEnableAutoScaleParameter.from_dict(pool_enable_auto_scale_parameter)
    return web.Response(status=200)


async def pool_evaluate_auto_scale(request: web.Request, pool_id, api_version, pool_evaluate_auto_scale_parameter, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Gets the result of evaluating an automatic scaling formula on the pool.

    This API is primarily for validating an autoscale formula, as it simply returns the result without applying the formula to the pool.

    :param pool_id: The ID of the pool on which to evaluate the automatic scaling formula.
    :type pool_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param pool_evaluate_auto_scale_parameter: The parameters for the request.
    :type pool_evaluate_auto_scale_parameter: dict | bytes
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    pool_evaluate_auto_scale_parameter = PoolEvaluateAutoScaleParameter.from_dict(pool_evaluate_auto_scale_parameter)
    return web.Response(status=200)


async def pool_exists(request: web.Request, pool_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """pool_exists

    Gets basic properties of a pool.

    :param pool_id: The ID of the pool to get.
    :type pool_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param if_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified.
    :type if_match: str
    :param if_none_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag.
    :type if_none_match: str
    :param if_modified_since: Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    :type if_modified_since: str
    :param if_unmodified_since: Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    :type if_unmodified_since: str

    """
    return web.Response(status=200)


async def pool_get(request: web.Request, pool_id, api_version, select=None, expand=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """pool_get

    Gets information about the specified pool.

    :param pool_id: The ID of the pool to get.
    :type pool_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param select: An OData $select clause.
    :type select: str
    :param expand: An OData $expand clause.
    :type expand: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param if_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified.
    :type if_match: str
    :param if_none_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag.
    :type if_none_match: str
    :param if_modified_since: Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    :type if_modified_since: str
    :param if_unmodified_since: Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    :type if_unmodified_since: str

    """
    return web.Response(status=200)


async def pool_get_all_pools_lifetime_statistics(request: web.Request, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Gets lifetime summary statistics for all of the pools in the specified account.

    Statistics are aggregated across all pools that have ever existed in the account, from account creation to the last update time of the statistics.

    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def pool_list(request: web.Request, api_version, filter=None, select=None, expand=None, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Lists all of the pools in the specified account.

    

    :param api_version: Client API Version.
    :type api_version: str
    :param filter: An OData $filter clause.
    :type filter: str
    :param select: An OData $select clause.
    :type select: str
    :param expand: An OData $expand clause.
    :type expand: str
    :param maxresults: The maximum number of items to return in the response. A maximum of 1000 pools can be returned.
    :type maxresults: int
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def pool_list_pool_usage_metrics(request: web.Request, api_version, starttime=None, endtime=None, filter=None, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Lists the usage metrics, aggregated by pool across individual time intervals, for the specified account.

    If you do not specify a $filter clause including a poolId, the response includes all pools that existed in the account in the time range of the returned aggregation intervals.

    :param api_version: Client API Version.
    :type api_version: str
    :param starttime: The earliest time from which to include metrics. This must be at least two and a half hours before the current time. If not specified this defaults to the start time of the last aggregation interval currently available.
    :type starttime: str
    :param endtime: The latest time from which to include metrics. This must be at least two hours before the current time. If not specified this defaults to the end time of the last aggregation interval currently available.
    :type endtime: str
    :param filter: An OData $filter clause. If this is not specified the response includes all pools that existed in the account in the time range of the returned aggregation intervals.
    :type filter: str
    :param maxresults: The maximum number of items to return in the response. A maximum of 1000 results will be returned.
    :type maxresults: int
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    starttime = util.deserialize_datetime(starttime)
    endtime = util.deserialize_datetime(endtime)
    return web.Response(status=200)


async def pool_patch(request: web.Request, pool_id, api_version, pool_patch_parameter, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """Updates the properties of the specified pool.

    This only replaces the pool properties specified in the request. For example, if the pool has a start task associated with it, and a request does not specify a start task element, then the pool keeps the existing start task.

    :param pool_id: The ID of the pool to update.
    :type pool_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param pool_patch_parameter: The parameters for the request.
    :type pool_patch_parameter: dict | bytes
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param if_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified.
    :type if_match: str
    :param if_none_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag.
    :type if_none_match: str
    :param if_modified_since: Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    :type if_modified_since: str
    :param if_unmodified_since: Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    :type if_unmodified_since: str

    """
    pool_patch_parameter = PoolPatchParameter.from_dict(pool_patch_parameter)
    return web.Response(status=200)


async def pool_resize(request: web.Request, pool_id, api_version, pool_resize_parameter, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """Changes the number of compute nodes that are assigned to a pool.

    You can only resize a pool when its allocation state is steady. If the pool is already resizing, the request fails with status code 409. When you resize a pool, the pool&#39;s allocation state changes from steady to resizing. You cannot resize pools which are configured for automatic scaling. If you try to do this, the Batch service returns an error 409. If you resize a pool downwards, the Batch service chooses which nodes to remove. To remove specific nodes, use the pool remove nodes API instead.

    :param pool_id: The ID of the pool to resize.
    :type pool_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param pool_resize_parameter: The parameters for the request.
    :type pool_resize_parameter: dict | bytes
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param if_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified.
    :type if_match: str
    :param if_none_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag.
    :type if_none_match: str
    :param if_modified_since: Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    :type if_modified_since: str
    :param if_unmodified_since: Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    :type if_unmodified_since: str

    """
    pool_resize_parameter = PoolResizeParameter.from_dict(pool_resize_parameter)
    return web.Response(status=200)


async def pool_stop_resize(request: web.Request, pool_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """Stops an ongoing resize operation on the pool.

    This does not restore the pool to its previous state before the resize operation: it only stops any further changes being made, and the pool maintains its current state. A resize operation need not be an explicit resize pool request; this API can also be used to halt the initial sizing of the pool when it is created.

    :param pool_id: The ID of the pool whose resizing you want to stop.
    :type pool_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param if_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified.
    :type if_match: str
    :param if_none_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag.
    :type if_none_match: str
    :param if_modified_since: Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    :type if_modified_since: str
    :param if_unmodified_since: Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    :type if_unmodified_since: str

    """
    return web.Response(status=200)


async def pool_update_properties(request: web.Request, pool_id, api_version, pool_update_properties_parameter, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Updates the properties of the specified pool.

    This fully replaces all the updatable properties of the pool. For example, if the pool has a start task associated with it and if start task is not specified with this request, then the Batch service will remove the existing start task.

    :param pool_id: The ID of the pool to update.
    :type pool_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param pool_update_properties_parameter: The parameters for the request.
    :type pool_update_properties_parameter: dict | bytes
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    pool_update_properties_parameter = PoolUpdatePropertiesParameter.from_dict(pool_update_properties_parameter)
    return web.Response(status=200)


async def pool_upgrade_os(request: web.Request, pool_id, api_version, pool_upgrade_os_parameter, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None, if_match=None, if_none_match=None, if_modified_since=None, if_unmodified_since=None) -> web.Response:
    """Upgrades the operating system of the specified pool.

    During an upgrade, the Batch service upgrades each compute node in the pool. When a compute node is chosen for upgrade, any tasks running on that node are removed from the node and returned to the queue to be rerun later (or on a different compute node). The node will be unavailable until the upgrade is complete. This operation results in temporarily reduced pool capacity as nodes are taken out of service to be upgraded. Although the Batch service tries to avoid upgrading all compute nodes at the same time, it does not guarantee to do this (particularly on small pools); therefore, the pool may be temporarily unavailable to run tasks. When this operation runs, the pool state changes to upgrading. When all compute nodes have finished upgrading, the pool state returns to active.

    :param pool_id: The ID of the pool to upgrade.
    :type pool_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param pool_upgrade_os_parameter: The parameters for the request.
    :type pool_upgrade_os_parameter: dict | bytes
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str
    :param if_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag is an exact match as specified.
    :type if_match: str
    :param if_none_match: An ETag is specified. Specify this header to perform the operation only if the resource&#39;s ETag does not match the specified ETag.
    :type if_none_match: str
    :param if_modified_since: Specify this header to perform the operation only if the resource has been modified since the specified date/time.
    :type if_modified_since: str
    :param if_unmodified_since: Specify this header to perform the operation only if the resource has not been modified since the specified date/time.
    :type if_unmodified_since: str

    """
    pool_upgrade_os_parameter = PoolUpgradeOSParameter.from_dict(pool_upgrade_os_parameter)
    return web.Response(status=200)
