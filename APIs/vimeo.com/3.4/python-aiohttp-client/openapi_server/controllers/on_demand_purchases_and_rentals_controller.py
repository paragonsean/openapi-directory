from typing import List, Dict
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.on_demand_page import OnDemandPage
from openapi_server import util


async def check_if_vod_was_purchased(request: web.Request, user_id) -> web.Response:
    """Check if a user has made a purchase or rental from an On Demand page

    

    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def check_if_vod_was_purchased_alt1(request: web.Request, ondemand_id) -> web.Response:
    """Check if a user has made a purchase or rental from an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 

    """
    return web.Response(status=200)


async def get_vod_purchases(request: web.Request, direction=None, filter=None, page=None, per_page=None, sort=None) -> web.Response:
    """Get all the On Demand purchases and rentals that a user has made

    

    :param direction: The sort direction of the results.
    :type direction: str
    :param filter: The type of On Demand videos to show.  Option descriptions:  * &#x60;important&#x60; - Will show all pages which are about to expire. 
    :type filter: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)
