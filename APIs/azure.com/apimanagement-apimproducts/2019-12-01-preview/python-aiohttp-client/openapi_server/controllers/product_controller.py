from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_get200_response import ProductGet200Response
from openapi_server.models.product_list_by_service200_response import ProductListByService200Response
from openapi_server.models.product_list_by_service_default_response import ProductListByServiceDefaultResponse
from openapi_server.models.product_update_request import ProductUpdateRequest
from openapi_server import util


async def product_create_or_update(request: web.Request, resource_group_name, service_name, product_id, api_version, subscription_id, parameters, if_match=None) -> web.Response:
    """product_create_or_update

    Creates or Updates a product.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Create or update parameters.
    :type parameters: dict | bytes
    :param if_match: ETag of the Entity. Not required when creating an entity, but required when updating an entity.
    :type if_match: str

    """
    parameters = ProductGet200Response.from_dict(parameters)
    return web.Response(status=200)


async def product_delete(request: web.Request, resource_group_name, service_name, product_id, if_match, api_version, subscription_id, delete_subscriptions=None) -> web.Response:
    """product_delete

    Delete product.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param delete_subscriptions: Delete existing subscriptions associated with the product or not.
    :type delete_subscriptions: bool

    """
    return web.Response(status=200)


async def product_get(request: web.Request, resource_group_name, service_name, product_id, api_version, subscription_id) -> web.Response:
    """product_get

    Gets the details of the product specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def product_get_entity_tag(request: web.Request, resource_group_name, service_name, product_id, api_version, subscription_id) -> web.Response:
    """product_get_entity_tag

    Gets the entity state (Etag) version of the product specified by its identifier.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str

    """
    return web.Response(status=200)


async def product_list_by_service(request: web.Request, resource_group_name, service_name, api_version, subscription_id, filter=None, top=None, skip=None, expand_groups=None, tags=None) -> web.Response:
    """product_list_by_service

    Lists a collection of products in the specified service instance.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param filter: |   Field     |     Usage     |     Supported operators     |     Supported functions     |&lt;/br&gt;|-------------|-------------|-------------|-------------|&lt;/br&gt;| name | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| displayName | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| description | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| terms | filter | ge, le, eq, ne, gt, lt | substringof, contains, startswith, endswith | &lt;/br&gt;| state | filter | eq |     | &lt;/br&gt;| groups | expand |     |     | &lt;/br&gt;
    :type filter: str
    :param top: Number of records to return.
    :type top: int
    :param skip: Number of records to skip.
    :type skip: int
    :param expand_groups: When set to true, the response contains an array of groups that have visibility to the product. The default is false.
    :type expand_groups: bool
    :param tags: Products which are part of a specific tag.
    :type tags: str

    """
    return web.Response(status=200)


async def product_update(request: web.Request, resource_group_name, service_name, product_id, if_match, api_version, subscription_id, parameters) -> web.Response:
    """product_update

    Update existing product details.

    :param resource_group_name: The name of the resource group.
    :type resource_group_name: str
    :param service_name: The name of the API Management service.
    :type service_name: str
    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param if_match: ETag of the Entity. ETag should match the current entity state from the header response of the GET request or it should be * for unconditional update.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param subscription_id: Subscription credentials which uniquely identify Microsoft Azure subscription. The subscription ID forms part of the URI for every service call.
    :type subscription_id: str
    :param parameters: Update parameters.
    :type parameters: dict | bytes

    """
    parameters = ProductUpdateRequest.from_dict(parameters)
    return web.Response(status=200)
