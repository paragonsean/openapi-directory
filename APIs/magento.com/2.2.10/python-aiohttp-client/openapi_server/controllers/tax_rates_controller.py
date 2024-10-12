from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.tax_data_tax_rate_interface import TaxDataTaxRateInterface
from openapi_server.models.tax_tax_rate_repository_v1_save_put_request import TaxTaxRateRepositoryV1SavePutRequest
from openapi_server import util


async def tax_tax_rate_repository_v1_save_post(request: web.Request, body=None) -> web.Response:
    """taxRates

    Create or update tax rate

    :param body: 
    :type body: dict | bytes

    """
    body = TaxTaxRateRepositoryV1SavePutRequest.from_dict(body)
    return web.Response(status=200)


async def tax_tax_rate_repository_v1_save_put(request: web.Request, body=None) -> web.Response:
    """taxRates

    Create or update tax rate

    :param body: 
    :type body: dict | bytes

    """
    body = TaxTaxRateRepositoryV1SavePutRequest.from_dict(body)
    return web.Response(status=200)
