from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.search_response import SearchResponse
from openapi_server import util


async def get_recall_history(request: web.Request, vin, api_key=None, page=None) -> web.Response:
    """Recall info by vin

    Get a particular recall information for a vin

    :param vin: The VIN to identify the car. Must be a valid 17 char VIN
    :type vin: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param page: Page number to fetch the results for the given criteria. Default is 1.
    :type page: 

    """
    return web.Response(status=200)
