from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.historical_listing import HistoricalListing
from openapi_server import util


async def get_car_history(request: web.Request, vin, api_key=None, fields=None, page=None, include_duplicates=None, sort_order=None) -> web.Response:
    """Get a cars online listing history

    The history API returns online listing history for a car identified by its VIN. History listings are sorted in the descending order of the listing date / last seen date

    :param vin: The VIN to identify the car. Must be a valid 17 char VIN
    :type vin: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param fields: List of fields to fetch, in case the default fields list in the response is to be trimmed down
    :type fields: str
    :param page: Page number to fetch the results for the given criteria. Default is 1.
    :type page: 
    :param include_duplicates: Flag to indicate whether to include duplicate historical records as well in the response
    :type include_duplicates: bool
    :param sort_order: Sort order - asc or desc. Default sort order is asc
    :type sort_order: str

    """
    return web.Response(status=200)


async def history_car_uk_vrm_get(request: web.Request, vrm, api_key=None, page=None, include_duplicates=None, sort_order=None) -> web.Response:
    """Get a cars online listing history

    The history API returns online listing history for a car identified by its VRM. History listings are sorted in the descending order of the listing date / last seen date

    :param vrm: The VRM to identify the car.
    :type vrm: str
    :param api_key: The API Authentication Key. Mandatory with all API calls.
    :type api_key: str
    :param page: Page number to fetch the results for the given criteria. Default is 1.
    :type page: 
    :param include_duplicates: Flag to indicate whether to include duplicate historical records as well in the response
    :type include_duplicates: bool
    :param sort_order: Sort order - asc or desc. Default sort order is asc
    :type sort_order: str

    """
    return web.Response(status=200)
