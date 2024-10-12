from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_vod_alt1_request import CreateVodAlt1Request
from openapi_server.models.edit_vod_request import EditVodRequest
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.on_demand_page import OnDemandPage
from openapi_server import util


async def create_vod(request: web.Request, user_id, body) -> web.Response:
    """Create an On Demand page

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = CreateVodAlt1Request.from_dict(body)
    return web.Response(status=200)


async def create_vod_alt1(request: web.Request, body) -> web.Response:
    """Create an On Demand page

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateVodAlt1Request.from_dict(body)
    return web.Response(status=200)


async def delete_vod_draft(request: web.Request, ondemand_id) -> web.Response:
    """Delete a draft of an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 

    """
    return web.Response(status=200)


async def edit_vod(request: web.Request, ondemand_id, body=None) -> web.Response:
    """Edit an On Demand page

    Enable preorders or publish the page.

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = EditVodRequest.from_dict(body)
    return web.Response(status=200)


async def get_user_vods(request: web.Request, user_id, direction=None, filter=None, page=None, per_page=None, sort=None) -> web.Response:
    """Get all the On Demand pages of a user

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param direction: The sort direction of the results.
    :type direction: str
    :param filter: The type of On Demand pages to return.
    :type filter: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def get_user_vods_alt1(request: web.Request, direction=None, filter=None, page=None, per_page=None, sort=None) -> web.Response:
    """Get all the On Demand pages of a user

    

    :param direction: The sort direction of the results.
    :type direction: str
    :param filter: The type of On Demand pages to return.
    :type filter: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def get_vod(request: web.Request, ondemand_id) -> web.Response:
    """Get a specific On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 

    """
    return web.Response(status=200)
