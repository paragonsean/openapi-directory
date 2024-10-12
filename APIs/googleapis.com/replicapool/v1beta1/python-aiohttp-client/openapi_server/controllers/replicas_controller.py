from typing import List, Dict
from aiohttp import web

from openapi_server.models.replica import Replica
from openapi_server.models.replicas_delete_request import ReplicasDeleteRequest
from openapi_server.models.replicas_list_response import ReplicasListResponse
from openapi_server import util


async def replicapool_replicas_delete(request: web.Request, project_name, zone, pool_name, replica_name, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, body=None) -> web.Response:
    """replicapool_replicas_delete

    Deletes a replica from the pool.

    :param project_name: The project ID for this request.
    :type project_name: str
    :param zone: The zone where the replica lives.
    :type zone: str
    :param pool_name: The replica pool name for this request.
    :type pool_name: str
    :param replica_name: The name of the replica for this request.
    :type replica_name: str
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
    body = ReplicasDeleteRequest.from_dict(body)
    return web.Response(status=200)


async def replicapool_replicas_get(request: web.Request, project_name, zone, pool_name, replica_name, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """replicapool_replicas_get

    Gets information about a specific replica.

    :param project_name: The project ID for this request.
    :type project_name: str
    :param zone: The zone where the replica lives.
    :type zone: str
    :param pool_name: The replica pool name for this request.
    :type pool_name: str
    :param replica_name: The name of the replica for this request.
    :type replica_name: str
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


async def replicapool_replicas_list(request: web.Request, project_name, zone, pool_name, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, max_results=None, page_token=None) -> web.Response:
    """replicapool_replicas_list

    Lists all replicas in a pool.

    :param project_name: The project ID for this request.
    :type project_name: str
    :param zone: The zone where the replica pool lives.
    :type zone: str
    :param pool_name: The replica pool name for this request.
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
    :param max_results: Maximum count of results to be returned. Acceptable values are 0 to 100, inclusive. (Default: 50)
    :type max_results: int
    :param page_token: Set this to the nextPageToken value returned by a previous list request to obtain the next page of results from the previous list request.
    :type page_token: str

    """
    return web.Response(status=200)


async def replicapool_replicas_restart(request: web.Request, project_name, zone, pool_name, replica_name, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """replicapool_replicas_restart

    Restarts a replica in a pool.

    :param project_name: The project ID for this request.
    :type project_name: str
    :param zone: The zone where the replica lives.
    :type zone: str
    :param pool_name: The replica pool name for this request.
    :type pool_name: str
    :param replica_name: The name of the replica for this request.
    :type replica_name: str
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
