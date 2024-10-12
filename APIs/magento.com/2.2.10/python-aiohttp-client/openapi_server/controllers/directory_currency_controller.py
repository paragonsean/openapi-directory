from typing import List, Dict
from aiohttp import web

from openapi_server.models.directory_data_currency_information_interface import DirectoryDataCurrencyInformationInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def directory_currency_information_acquirer_v1_get_currency_info_get(request: web.Request, ) -> web.Response:
    """directory/currency

    Get currency information for the store.


    """
    return web.Response(status=200)
