from typing import List, Dict
from aiohttp import web

from openapi_server.models.directory_data_country_information_interface import DirectoryDataCountryInformationInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def directory_country_information_acquirer_v1_get_countries_info_get(request: web.Request, ) -> web.Response:
    """directory/countries

    Get all countries and regions information for the store.


    """
    return web.Response(status=200)
