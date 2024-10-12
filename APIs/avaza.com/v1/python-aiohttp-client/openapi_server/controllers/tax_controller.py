from typing import List, Dict
from aiohttp import web

from openapi_server.models.tax_list import TaxList
from openapi_server import util


async def tax_get(request: web.Request, ) -> web.Response:
    """Get List of Taxes configured in the Avaza account.

    


    """
    return web.Response(status=200)
