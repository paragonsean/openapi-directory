from typing import List, Dict
from aiohttp import web

from openapi_server.models.edit_vod_background_request import EditVodBackgroundRequest
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.picture import Picture
from openapi_server import util


async def create_vod_background(request: web.Request, ondemand_id) -> web.Response:
    """Add a background to an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 

    """
    return web.Response(status=200)


async def delete_vod_background(request: web.Request, background_id, ondemand_id) -> web.Response:
    """Remove a background from an On Demand page

    

    :param background_id: The ID of the background.
    :type background_id: 
    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 

    """
    return web.Response(status=200)


async def edit_vod_background(request: web.Request, background_id, ondemand_id, body=None) -> web.Response:
    """Edit a background of an On Demand page

    

    :param background_id: The ID of the background.
    :type background_id: 
    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = EditVodBackgroundRequest.from_dict(body)
    return web.Response(status=200)


async def get_vod_background(request: web.Request, background_id, ondemand_id) -> web.Response:
    """Get a specific background of an On Demand page

    

    :param background_id: The ID of the background.
    :type background_id: 
    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 

    """
    return web.Response(status=200)


async def get_vod_backgrounds(request: web.Request, ondemand_id, page=None, per_page=None) -> web.Response:
    """Get all the backgrounds of an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)
