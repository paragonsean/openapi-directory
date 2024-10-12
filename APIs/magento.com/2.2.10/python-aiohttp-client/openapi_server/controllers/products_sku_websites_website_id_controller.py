from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def catalog_product_website_link_repository_v1_delete_by_id_delete(request: web.Request, sku, website_id) -> web.Response:
    """products/{sku}/websites/{websiteId}

    Remove the website assignment from the product by product sku

    :param sku: 
    :type sku: str
    :param website_id: 
    :type website_id: int

    """
    return web.Response(status=200)
