from typing import List, Dict
from aiohttp import web

from openapi_server.models.nitro import Nitro
from openapi_server import util


async def get_raw_ancestors(request: web.Request, pid) -> web.Response:
    """Get raw ancestors

    Get raw ancestors

    :param pid: 
    :type pid: str

    """
    return web.Response(status=200)


async def get_raw_brand(request: web.Request, pid) -> web.Response:
    """Get raw brand

    Get raw brand

    :param pid: 
    :type pid: str

    """
    return web.Response(status=200)


async def get_raw_brand_franchises(request: web.Request, pid) -> web.Response:
    """Get raw brand franchise

    Get raw brand franchises

    :param pid: 
    :type pid: str

    """
    return web.Response(status=200)


async def get_raw_episode(request: web.Request, pid) -> web.Response:
    """Get raw episode

    Get raw episode

    :param pid: 
    :type pid: str

    """
    return web.Response(status=200)


async def get_raw_formats(request: web.Request, pid) -> web.Response:
    """Get raw formats

    Get raw formats

    :param pid: 
    :type pid: str

    """
    return web.Response(status=200)


async def get_raw_genre_groups(request: web.Request, pid) -> web.Response:
    """Get raw genre groups

    Get raw genre groups

    :param pid: 
    :type pid: str

    """
    return web.Response(status=200)


async def get_raw_image(request: web.Request, pid) -> web.Response:
    """Get raw image

    Get raw image

    :param pid: 
    :type pid: str

    """
    return web.Response(status=200)


async def get_raw_masterbrand(request: web.Request, mbid) -> web.Response:
    """Get raw masterbrand

    Get raw masterbrand

    :param mbid: 
    :type mbid: str

    """
    return web.Response(status=200)


async def get_raw_promotion(request: web.Request, pid) -> web.Response:
    """Get raw promotion

    Get raw promotion

    :param pid: 
    :type pid: str

    """
    return web.Response(status=200)
