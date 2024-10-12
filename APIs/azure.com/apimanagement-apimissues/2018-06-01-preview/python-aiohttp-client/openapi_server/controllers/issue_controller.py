from typing import List, Dict
from aiohttp import web

from openapi_server.models.issue_get200_response import IssueGet200Response
from openapi_server.models.issue_list_by_service200_response import IssueListByService200Response
from openapi_server.models.issue_list_by_service_default_response import IssueListByServiceDefaultResponse
from openapi_server import util


async def issue_get(request: web.Request, resource_group_name, service_name, issue_id, api_version, subscription_id) -> web.Response:
    """issue_get

    Gets API Management issue details

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param issue_id: Issue identifier. Must be unique in the current API Management service instance.
    :type issue_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def issue_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """issue_list_by_service

    Lists a collection of issues in the specified service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   |name | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |apiId | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |title | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |authorName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |state | eq |    | 
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)
