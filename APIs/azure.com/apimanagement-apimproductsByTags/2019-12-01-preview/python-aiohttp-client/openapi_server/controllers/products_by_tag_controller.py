from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_list_by_tags200_response import ProductListByTags200Response
from openapi_server.models.product_list_by_tags_default_response import ProductListByTagsDefaultResponse
from openapi_server import util


async def product_list_by_tags(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None, include_not_tagged_products=None) -> web.Response:
    """product_list_by_tags

    Lists a collection of products associated with tags.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| name | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| displayName | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| description | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| terms | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| state | filter | eq | substringof, contains, startswith, endswith | &lt;/br&gt;
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int
    :param include_not_tagged_products: Include not tagged Products.
    :type include_not_tagged_products: bool

    """
    return web.Response(status=200)
