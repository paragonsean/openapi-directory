from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.products_product_id_variants_get200_response import ProductsProductIdVariantsGet200Response
from openapi_server import util


async def products_product_id_variants_get(request: web.Request, product_id) -> web.Response:
    """Get a product&#39;s variants

    

    :param product_id: 
    :type product_id: str
    :type product_id: str

    """
    return web.Response(status=200)


async def products_product_id_variants_post(request: web.Request, product_id, ratio, variant_id, variant_type, name=None) -> web.Response:
    """Add a new variant to a product

    

    :param product_id: 
    :type product_id: str
    :type product_id: str
    :param ratio: 
    :type ratio: 
    :param variant_id: 
    :type variant_id: str
    :type variant_id: str
    :param variant_type: 
    :type variant_type: str
    :param name: Filters by name
    :type name: str

    """
    return web.Response(status=200)


async def products_product_id_variants_variant_type_variant_id_delete(request: web.Request, product_id, variant_type, variant_id) -> web.Response:
    """Delete a product variant

    

    :param product_id: 
    :type product_id: str
    :type product_id: str
    :param variant_type: 
    :type variant_type: str
    :param variant_id: 
    :type variant_id: str
    :type variant_id: str

    """
    return web.Response(status=200)
