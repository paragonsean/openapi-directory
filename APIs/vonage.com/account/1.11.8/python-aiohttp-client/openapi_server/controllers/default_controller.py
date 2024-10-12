from typing import List, Dict
from aiohttp import web

from openapi_server.models.account_hal_response import AccountHalResponse
from openapi_server.models.location_hal_response import LocationHalResponse
from openapi_server.models.locations_hal_response import LocationsHalResponse
from openapi_server import util


async def account_ctrl_get_account_services_by_account_id(request: web.Request, account_id) -> web.Response:
    """Get account data by ID

    

    :param account_id: The Vonage Business Cloud account ID
    :type account_id: 

    """
    return web.Response(status=200)


async def account_ctrl_get_location_by_id(request: web.Request, account_id, location_id) -> web.Response:
    """Get location data by account ID and location ID

    

    :param account_id: The Vonage Business Cloud account ID
    :type account_id: 
    :param location_id: The Vonage Business Cloud location ID
    :type location_id: 

    """
    return web.Response(status=200)


async def account_ctrl_get_locations_by_account_id(request: web.Request, account_id) -> web.Response:
    """Get account locations data by account ID

    

    :param account_id: The Vonage Business Cloud account ID
    :type account_id: 

    """
    return web.Response(status=200)
