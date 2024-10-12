from typing import List, Dict
from aiohttp import web

from openapi_server.models.crm_response import CRMResponse
from openapi_server.models.error import Error
from openapi_server import util


async def crm_check(request: web.Request, vin, sale_date, api_key=None) -> web.Response:
    """CRM check of a particular vin

    Check whether particular vin has had a listing after stipulated date or not

    :param vin: The VIN to identify the car. Must be a valid 17 char VIN
    :type vin: str
    :param sale_date: sale date to check whether after this listing has appeared or not. Must be 8 character long, with YYYYMMDD format
    :type sale_date: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str

    """
    return web.Response(status=200)
