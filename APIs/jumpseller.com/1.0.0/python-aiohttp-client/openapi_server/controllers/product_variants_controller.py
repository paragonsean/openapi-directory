from typing import List, Dict
from aiohttp import web

from openapi_server.models.count import Count
from openapi_server.models.not_found import NotFound
from openapi_server.models.variant import Variant
from openapi_server.models.variant_edit import VariantEdit
from openapi_server import util


async def products_id_variants_count_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Count all Product Variants.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: ID of the Product
    :type id: int

    """
    return web.Response(status=200)


async def products_id_variants_json_get(request: web.Request, login, authtoken, id) -> web.Response:
    """Retrieve all Product Variants.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: ID of the Product
    :type id: int

    """
    return web.Response(status=200)


async def products_id_variants_json_post(request: web.Request, login, authtoken, id, body) -> web.Response:
    """Create a new Product Variant.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int
    :param body: Product Variant parameters.
    :type body: dict | bytes

    """
    body = VariantEdit.from_dict(body)
    return web.Response(status=200)


async def products_id_variants_variant_id_json_get(request: web.Request, login, authtoken, id, variant_id) -> web.Response:
    """Retrieve a single Product Variant.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int
    :param variant_id: Id of the Product Variant
    :type variant_id: int

    """
    return web.Response(status=200)


async def products_id_variants_variant_id_json_put(request: web.Request, login, authtoken, id, variant_id, body) -> web.Response:
    """Modify an existing Product Variant.

    

    :param login: API OAuth login.
    :type login: str
    :param authtoken: API OAuth token.
    :type authtoken: str
    :param id: Id of the Product
    :type id: int
    :param variant_id: Id of the Product Variant
    :type variant_id: int
    :param body: Product Variant parameters to change
    :type body: dict | bytes

    """
    body = VariantEdit.from_dict(body)
    return web.Response(status=200)
