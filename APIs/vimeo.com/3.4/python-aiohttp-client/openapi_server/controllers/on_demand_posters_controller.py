from typing import List, Dict
from aiohttp import web

from openapi_server.models.edit_vod_poster_request import EditVodPosterRequest
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.picture import Picture
from openapi_server import util


async def add_vod_poster(request: web.Request, ondemand_id) -> web.Response:
    """Add a poster to an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 

    """
    return web.Response(status=200)


async def edit_vod_poster(request: web.Request, ondemand_id, poster_id, body=None) -> web.Response:
    """Edit a poster of an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 
    :param poster_id: The ID of the picture.
    :type poster_id: 
    :param body: 
    :type body: dict | bytes

    """
    body = EditVodPosterRequest.from_dict(body)
    return web.Response(status=200)


async def get_vod_poster(request: web.Request, ondemand_id, poster_id) -> web.Response:
    """Get a specific poster of an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 
    :param poster_id: The ID of the picture.
    :type poster_id: 

    """
    return web.Response(status=200)


async def get_vod_posters(request: web.Request, ondemand_id, page=None, per_page=None) -> web.Response:
    """Get all the posters of an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)
