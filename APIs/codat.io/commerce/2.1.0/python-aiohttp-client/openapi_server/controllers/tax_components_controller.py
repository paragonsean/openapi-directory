from typing import List, Dict
from aiohttp import web

from openapi_server.models.tax_components import TaxComponents
from openapi_server import util


async def get_tax_components(request: web.Request, company_id, connection_id) -> web.Response:
    """List tax components

    This endpoint returns a lits of tax rates from the commerce platform, including tax rate names and values. This supports the mapping of tax rates from the commerce platform to the accounting platform.

    :param company_id: 
    :type company_id: str
    :type company_id: str
    :param connection_id: 
    :type connection_id: str
    :type connection_id: str

    """
    return web.Response(status=200)
