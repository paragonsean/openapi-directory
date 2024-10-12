from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tax_data_tax_rate_interface import TaxDataTaxRateInterface
from openapi_server import util


async def tax_tax_rate_repository_v1_delete_by_id_delete(request: web.Request, rate_id) -> web.Response:
    """taxRates/{rateId}

    Delete tax rate

    :param rate_id: 
    :type rate_id: int

    """
    return web.Response(status=200)


async def tax_tax_rate_repository_v1_get_get(request: web.Request, rate_id) -> web.Response:
    """taxRates/{rateId}

    Get tax rate

    :param rate_id: 
    :type rate_id: int

    """
    return web.Response(status=200)
