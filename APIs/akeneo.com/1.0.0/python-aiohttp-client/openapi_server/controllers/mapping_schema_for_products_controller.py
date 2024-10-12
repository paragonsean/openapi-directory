from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_app_catalogs_mapping_schema_product200_response import GetAppCatalogsMappingSchemaProduct200Response
from openapi_server.models.post_token400_response import PostToken400Response
from openapi_server import util


async def delete_app_catalogs_mapping_schema_product(request: web.Request, id) -> web.Response:
    """Delete the product mapping schema related to a catalog

    This endpoint allows you to delete the product mapping schema related to a catalog

    :param id: Catalog ID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def get_app_catalogs_mapping_schema_product(request: web.Request, id) -> web.Response:
    """Get the product mapping schema related to a catalog

    This endpoint allows you to retrieve the product mapping schema related to a catalog

    :param id: Catalog ID
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def put_app_catalogs_mapping_schema_product(request: web.Request, id, body=None) -> web.Response:
    """Create or update the product mapping schema related to a catalog

    This endpoint allows you to create or update the product mapping schema related to a catalog

    :param id: Catalog ID
    :type id: str
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GetAppCatalogsMappingSchemaProduct200Response.from_dict(body)
    return web.Response(status=200)
