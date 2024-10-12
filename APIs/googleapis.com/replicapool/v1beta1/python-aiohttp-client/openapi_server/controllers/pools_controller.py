from typing import List, Dict
from aiohttp import web

from openapi_server.models.pool import Pool
from openapi_server.models.pools_delete_request import PoolsDeleteRequest
from openapi_server.models.pools_list_response import PoolsListResponse
from openapi_server.models.template import Template
from openapi_server import util


async def replicapool_pools_delete(request: web.Request, project_name, zone, pool_name, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """replicapool_pools_delete

    Deletes a replica pool.

    :param project_name: The project ID for this replica pool.
    :type project_name: str
    :param zone: The zone for this replica pool.
    :type zone: str
    :param pool_name: The name of the replica pool for this request.
    :type pool_name: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = PoolsDeleteRequest.from_dict(body)
    return web.Response(status=200)


async def replicapool_pools_get(request: web.Request, project_name, zone, pool_name, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """replicapool_pools_get

    Gets information about a single replica pool.

    :param project_name: The project ID for this replica pool.
    :type project_name: str
    :param zone: The zone for this replica pool.
    :type zone: str
    :param pool_name: The name of the replica pool for this request.
    :type pool_name: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def replicapool_pools_insert(request: web.Request, project_name, zone, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """replicapool_pools_insert

    Inserts a new replica pool.

    :param project_name: The project ID for this replica pool.
    :type project_name: str
    :param zone: The zone for this replica pool.
    :type zone: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = Pool.from_dict(body)
    return web.Response(status=200)


async def replicapool_pools_list(request: web.Request, project_name, zone, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, max_results=None, page_token=None) -> web.Response:
    """replicapool_pools_list

    List all replica pools.

    :param project_name: The project ID for this request.
    :type project_name: str
    :param zone: The zone for this replica pool.
    :type zone: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param max_results: Maximum count of results to be returned. Acceptable values are 0 to 100, inclusive. (Default: 50)
    :type max_results: int
    :param page_token: Set this to the nextPageToken value returned by a previous list request to obtain the next page of results from the previous list request.
    :type page_token: str

    """
    return web.Response(status=200)


async def replicapool_pools_resize(request: web.Request, project_name, zone, pool_name, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, num_replicas=None) -> web.Response:
    """replicapool_pools_resize

    Resize a pool. This is an asynchronous operation, and multiple overlapping resize requests can be made. Replica Pools will use the information from the last resize request.

    :param project_name: The project ID for this replica pool.
    :type project_name: str
    :param zone: The zone for this replica pool.
    :type zone: str
    :param pool_name: The name of the replica pool for this request.
    :type pool_name: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param num_replicas: The desired number of replicas to resize to. If this number is larger than the existing number of replicas, new replicas will be added. If the number is smaller, then existing replicas will be deleted.
    :type num_replicas: int

    """
    return web.Response(status=200)


async def replicapool_pools_updatetemplate(request: web.Request, project_name, zone, pool_name, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """replicapool_pools_updatetemplate

    Update the template used by the pool.

    :param project_name: The project ID for this replica pool.
    :type project_name: str
    :param zone: The zone for this replica pool.
    :type zone: str
    :param pool_name: The name of the replica pool for this request.
    :type pool_name: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param body: 
    :type body: dict | bytes

    """
    body = Template.from_dict(body)
    return web.Response(status=200)
