from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_list_by_service_default_response import ApiListByServiceDefaultResponse
from openapi_server.models.issue_comment_collection import IssueCommentCollection
from openapi_server.models.issue_comment_contract import IssueCommentContract
from openapi_server import util


async def api_issue_comment_create_or_update(request: web.Request, resource_group_name, service_name, api_id, issue_id, comment_id, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """api_issue_comment_create_or_update

    Creates a new Comment for the Issue in an API or updates an existing one.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param issue_id: Issue identifier. Must be unique in the current API Management service instance.
    :type issue_id: str
    :param comment_id: Comment identifier within an Issue. Must be unique in the current Issue.
    :type comment_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Create parameters.
    :type parameters: dict | bytes
    :param if_match: ETag of the Issue Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str

    """
    parameters = IssueCommentContract.from_dict(parameters)
    return web.Response(status=200)


async def api_issue_comment_delete(request: web.Request, resource_group_name, service_name, api_id, issue_id, comment_id, if_match, api_version, subscription_id) -> web.Response:
    """api_issue_comment_delete

    Deletes the specified comment from an Issue.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param issue_id: Issue identifier. Must be unique in the current API Management service instance.
    :type issue_id: str
    :param comment_id: Comment identifier within an Issue. Must be unique in the current Issue.
    :type comment_id: str
    :param if_match: ETag of the Issue Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_issue_comment_get(request: web.Request, resource_group_name, service_name, api_id, issue_id, comment_id, api_version, subscription_id) -> web.Response:
    """api_issue_comment_get

    Gets the details of the issue Comment for an API specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param issue_id: Issue identifier. Must be unique in the current API Management service instance.
    :type issue_id: str
    :param comment_id: Comment identifier within an Issue. Must be unique in the current Issue.
    :type comment_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_issue_comment_get_entity_tag(request: web.Request, resource_group_name, service_name, api_id, issue_id, comment_id, api_version, subscription_id) -> web.Response:
    """api_issue_comment_get_entity_tag

    Gets the entity state (Etag) version of the issue Comment for an API specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param issue_id: Issue identifier. Must be unique in the current API Management service instance.
    :type issue_id: str
    :param comment_id: Comment identifier within an Issue. Must be unique in the current Issue.
    :type comment_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def api_issue_comment_list_by_service(request: web.Request, resource_group_name, service_name, api_id, api_version, issue_id, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """api_issue_comment_list_by_service

    Lists all comments for the Issue associated with the specified API.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_id: API identifier. Must be unique in the current API Management service instance.
    :type api_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param issue_id: Issue identifier. Must be unique in the current API Management service instance.
    :type issue_id: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------| | id          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith | | userId          | ge, le, eq, ne, gt, lt | substringof, startswith, endswith |
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)
