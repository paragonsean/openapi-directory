from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.full_product_update_request import FullProductUpdateRequest
from openapi_server.models.product_count_response import ProductCountResponse
from openapi_server.models.product_create_request import ProductCreateRequest
from openapi_server.models.product_response import ProductResponse
from openapi_server.models.variant_options_response import VariantOptionsResponse
from openapi_server import util


async def count_all_products(request: web.Request, organization_uuid) -> web.Response:
    """Retrieve the count of existing products

    

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str

    """
    return web.Response(status=200)


async def create_product(request: web.Request, organization_uuid, body, return_entity=None) -> web.Response:
    """Create a new product

    

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str
    :param body: 
    :type body: dict | bytes
    :param return_entity: 
    :type return_entity: bool

    """
    body = ProductCreateRequest.from_dict(body)
    return web.Response(status=200)


async def delete_product(request: web.Request, organization_uuid, product_uuid) -> web.Response:
    """Delete a single product

    

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str
    :param product_uuid: 
    :type product_uuid: str
    :type product_uuid: str

    """
    return web.Response(status=200)


async def delete_products(request: web.Request, organization_uuid, uuid) -> web.Response:
    """Delete a list of products

    

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str
    :param uuid: List of product UUIDs to be deleted
    :type uuid: List[str]

    """
    return web.Response(status=200)


async def get_all_options(request: web.Request, organization_uuid) -> web.Response:
    """Retrieve an aggregate of active Options in the library

    

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str

    """
    return web.Response(status=200)


async def get_all_products_in_pos(request: web.Request, organization_uuid) -> web.Response:
    """Retrieve all products visible in POS

    

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str

    """
    return web.Response(status=200)


async def get_all_products_v2(request: web.Request, organization_uuid, sort=None) -> web.Response:
    """Retrieve all products visible in POS – v2

    

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str
    :param sort: If true, sorts response by created date
    :type sort: bool

    """
    return web.Response(status=200)


async def get_product(request: web.Request, organization_uuid, product_uuid, if_none_match=None) -> web.Response:
    """Retrieve a single product

    Get the full product with the provided UUID. The method supports conditional GET through providing a HttpHeaders.IF_NONE_MATCH header. If the conditional prerequisite is fullfilled, the full product is returned, otherwise a 304 not modified will be returned with an empty body.

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str
    :param product_uuid: 
    :type product_uuid: str
    :type product_uuid: str
    :param if_none_match: 
    :type if_none_match: str

    """
    return web.Response(status=200)


async def update_product(request: web.Request, organization_uuid, product_uuid, body, if_match=None) -> web.Response:
    """Update a single product

    Updates a product entity using JSON merge patch (https://tools.ietf.org/html/rfc7386). This means that only included fields will be changed: null values removes the field on the target entity, and other values updates the field. Conditional updates are supported through the HttpHeaders.IF_MATCH header. If the conditional prerequisite is fullfilled, the product is updated: otherwise a 412 (precondition failed) will be returned with an empty body.

    :param organization_uuid: 
    :type organization_uuid: str
    :type organization_uuid: str
    :param product_uuid: 
    :type product_uuid: str
    :type product_uuid: str
    :param body: 
    :type body: dict | bytes
    :param if_match: 
    :type if_match: str

    """
    body = FullProductUpdateRequest.from_dict(body)
    return web.Response(status=200)
