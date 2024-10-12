from typing import List, Dict
from aiohttp import web

from openapi_server.models.directory_data_country_information_interface import DirectoryDataCountryInformationInterface
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def directory_country_information_acquirer_v1_get_country_info_get(request: web.Request, country_id) -> web.Response:
    """directory/countries/{countryId}

    Get country and region information for the store.

    :param country_id: 
    :type country_id: str

    """
    return web.Response(status=200)
