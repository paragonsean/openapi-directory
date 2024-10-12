from typing import List, Dict
from aiohttp import web

from openapi_server.models.tag_resource_list_by_service200_response import TagResourceListByService200Response
from openapi_server.models.tag_resource_list_by_service_default_response import TagResourceListByServiceDefaultResponse
from openapi_server import util


async def tag_resource_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None) -> web.Response:
    """tag_resource_list_by_service

    Lists a collection of resources associated with tags.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: | Field       | Supported operators    | Supported functions               | |-------------|------------------------|-----------------------------------|   |aid | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |name | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |displayName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |apiName | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |apiRevision | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |path | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |description | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |serviceUrl | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |method | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |urlTemplate | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |terms | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith| |state | eq |    | |isCurrent | eq |    | 
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int

    """
    return web.Response(status=200)
