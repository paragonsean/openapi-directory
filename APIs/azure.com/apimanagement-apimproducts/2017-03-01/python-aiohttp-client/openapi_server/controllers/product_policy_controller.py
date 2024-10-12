from typing import List, Dict
from aiohttp import web

from openapi_server.models.product_list_default_response import ProductListDefaultResponse
from openapi_server.models.product_policy_list_by_product200_response import ProductPolicyListByProduct200Response
from openapi_server.models.product_policy_list_by_product200_response_value_inner import ProductPolicyListByProduct200ResponseValueInner
from openapi_server import util


async def product_policy_create_or_update(request: web.Request, product_id, policy_id, api_version, parameters) -> web.Response:
    """product_policy_create_or_update

    Creates or updates policy configuration for the Product.

    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param policy_id: The identifier of the Policy.
    :type policy_id: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param parameters: The policy contents to apply.
    :type parameters: dict | bytes

    """
    parameters = ProductPolicyListByProduct200ResponseValueInner.from_dict(parameters)
    return web.Response(status=200)


async def product_policy_delete(request: web.Request, product_id, policy_id, if_match, api_version) -> web.Response:
    """product_policy_delete

    Deletes the policy configuration at the Product.

    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param policy_id: The identifier of the Policy.
    :type policy_id: str
    :param if_match: The entity state (Etag) version of the product policy to update. A value of \&quot;*\&quot; can be used for If-Match to unconditionally apply the operation.
    :type if_match: str
    :param api_version: Version of the API to be used with the client request.
    :type api_version: str

    """
    return web.Response(status=200)


async def product_policy_get(request: web.Request, api_version, product_id, policy_id) -> web.Response:
    """product_policy_get

    Get the policy configuration at the Product level.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str
    :param policy_id: The identifier of the Policy.
    :type policy_id: str

    """
    return web.Response(status=200)


async def product_policy_list_by_product(request: web.Request, api_version, product_id) -> web.Response:
    """product_policy_list_by_product

    Get the policy configuration at the Product level.

    :param api_version: Version of the API to be used with the client request.
    :type api_version: str
    :param product_id: Product identifier. Must be unique in the current API Management service instance.
    :type product_id: str

    """
    return web.Response(status=200)
