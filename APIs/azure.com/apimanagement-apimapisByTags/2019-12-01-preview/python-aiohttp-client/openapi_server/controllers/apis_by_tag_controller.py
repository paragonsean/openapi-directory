from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_list_by_tags200_response import ApiListByTags200Response
from openapi_server.models.api_list_by_tags_default_response import ApiListByTagsDefaultResponse
from openapi_server import util


async def api_list_by_tags(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None, include_not_tagged_apis=None) -> web.Response:
    """api_list_by_tags

    Lists a collection of apis associated with tags.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   |name | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |displayName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |apiRevision | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |path | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |serviceUrl | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |isCurrent | eq |    | 
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int
    :param include_not_tagged_apis: Include not tagged APIs.
    :type include_not_tagged_apis: bool

    """
    return web.Response(status=200)
