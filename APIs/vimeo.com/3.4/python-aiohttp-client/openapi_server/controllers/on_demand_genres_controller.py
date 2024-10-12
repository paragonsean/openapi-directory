from typing import List, Dict
from aiohttp import web

from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.on_demand_genre import OnDemandGenre
from openapi_server.models.on_demand_page import OnDemandPage
from openapi_server import util


async def add_vod_genre(request: web.Request, genre_id, ondemand_id) -> web.Response:
    """Add a genre to an On Demand page

    

    :param genre_id: The ID of the genre.
    :type genre_id: str
    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 

    """
    return web.Response(status=200)


async def delete_vod_genre(request: web.Request, genre_id, ondemand_id) -> web.Response:
    """Remove a genre from an On Demand page

    

    :param genre_id: The ID of the genre.
    :type genre_id: str
    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 

    """
    return web.Response(status=200)


async def get_genre_vod(request: web.Request, genre_id, ondemand_id) -> web.Response:
    """Get a specific On Demand page in a genre

    Check whether a genre contains an On Demand page.

    :param genre_id: The ID of the genre.
    :type genre_id: str
    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 

    """
    return web.Response(status=200)


async def get_genre_vods(request: web.Request, genre_id, direction=None, filter=None, page=None, per_page=None, query=None, sort=None) -> web.Response:
    """Get all the On Demand pages in a genre

    

    :param genre_id: The ID of the genre.
    :type genre_id: str
    :param direction: The sort direction of the results.
    :type direction: str
    :param filter: The attribute by which to filter the results.
    :type filter: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param query: The search query to use to filter the results.
    :type query: str
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def get_vod_genre(request: web.Request, genre_id) -> web.Response:
    """Get a specific On Demand genre

    

    :param genre_id: The ID of the genre.
    :type genre_id: str

    """
    return web.Response(status=200)


async def get_vod_genre_by_ondemand_id(request: web.Request, genre_id, ondemand_id) -> web.Response:
    """Check whether an On Demand page belongs to a genre

    

    :param genre_id: The ID of the genre.
    :type genre_id: str
    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 

    """
    return web.Response(status=200)


async def get_vod_genres(request: web.Request, ) -> web.Response:
    """Get all On Demand genres

    


    """
    return web.Response(status=200)


async def get_vod_genres_by_ondemand_id(request: web.Request, ondemand_id) -> web.Response:
    """Get all the genres of an On Demand page

    

    :param ondemand_id: The ID of the On Demand.
    :type ondemand_id: 

    """
    return web.Response(status=200)
