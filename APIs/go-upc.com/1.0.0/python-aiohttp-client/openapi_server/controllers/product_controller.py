from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.get_product_info200_response import GetProductInfo200Response
from openapi_server import util


async def get_product_info(request: web.Request, code) -> web.Response:
    """Retrieve product info for a particular barcode number (UPC, EAN, or ISBN).

    

    :param code: 
    :type code: str

    """
    return web.Response(status=200)
