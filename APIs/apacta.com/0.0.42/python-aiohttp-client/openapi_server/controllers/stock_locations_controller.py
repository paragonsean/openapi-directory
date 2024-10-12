from typing import List, Dict
from aiohttp import web

from openapi_server.models.clocking_records_clocking_record_id_put200_response import ClockingRecordsClockingRecordIdPut200Response
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.stock_locations_get200_response import StockLocationsGet200Response
from openapi_server.models.stock_locations_location_id_get200_response import StockLocationsLocationIdGet200Response
from openapi_server.models.stock_locations_post_request import StockLocationsPostRequest
from openapi_server import util


async def stock_locations_get(request: web.Request, name=None) -> web.Response:
    """List stock_locations

    

    :param name: Used to filter on the &#x60;name&#x60; of the stock_locations
    :type name: str

    """
    return web.Response(status=200)


async def stock_locations_location_id_delete(request: web.Request, location_id) -> web.Response:
    """Delete location

    

    :param location_id: 
    :type location_id: str

    """
    return web.Response(status=200)


async def stock_locations_location_id_get(request: web.Request, location_id) -> web.Response:
    """View single location

    

    :param location_id: 
    :type location_id: str

    """
    return web.Response(status=200)


async def stock_locations_location_id_put(request: web.Request, location_id) -> web.Response:
    """Edit location

    

    :param location_id: 
    :type location_id: str

    """
    return web.Response(status=200)


async def stock_locations_post(request: web.Request, body=None) -> web.Response:
    """Add new stock_locations

    

    :param body: 
    :type body: dict | bytes

    """
    body = StockLocationsPostRequest.from_dict(body)
    return web.Response(status=200)
