from typing import List, Dict
from aiohttp import web

from openapi_server.models.exec_api import ExecAPI
from openapi_server.models.type import Type
from openapi_server import util


async def marketstat_get(request: web.Request, typeid, regionlimit=None, usesystem=None) -> web.Response:
    """XML Marketstat

    

    :param typeid: TypeID. Multiple TypeIDs can be specified in the following format (up to 200 TypeIDs per request): typeid&#x3D;34&amp;typeid&#x3D;35 or typeid&#x3D;34,35 
    :type typeid: List[int]
    :param regionlimit: Limit the statistics to a single region.
    :type regionlimit: int
    :param usesystem: Limit the statistics to a single solar system.
    :type usesystem: int

    """
    return web.Response(status=200)


async def marketstat_json_get(request: web.Request, typeid, regionlimit=None, usesystem=None) -> web.Response:
    """JSON Marketstat

    

    :param typeid: TypeID. Multiple TypeIDs can be specified in the following format (up to 200 TypeIDs per request): typeid&#x3D;34&amp;typeid&#x3D;35 or typeid&#x3D;34,35 
    :type typeid: List[int]
    :param regionlimit: Limit the statistics to a single region.
    :type regionlimit: int
    :param usesystem: Limit the statistics to a single region.
    :type usesystem: int

    """
    return web.Response(status=200)


async def marketstat_json_post(request: web.Request, typeid, regionlimit=None, usesystem=None) -> web.Response:
    """JSON Marketstat

    

    :param typeid: TypeID. Multiple TypeIDs can be specified in the following format (up to 200 TypeIDs per request): typeid&#x3D;34&amp;typeid&#x3D;35 or typeid&#x3D;34,35 
    :type typeid: List[int]
    :param regionlimit: Limit the statistics to a single region.
    :type regionlimit: int
    :param usesystem: Limit the statistics to a single region.
    :type usesystem: int

    """
    return web.Response(status=200)


async def marketstat_post(request: web.Request, typeid, regionlimit=None, usesystem=None) -> web.Response:
    """XML Marketstat

    

    :param typeid: TypeID. Multiple TypeIDs can be specified in the following format (up to 200 TypeIDs per request): typeid&#x3D;34&amp;typeid&#x3D;35 or typeid&#x3D;34,35 
    :type typeid: List[int]
    :param regionlimit: Limit the statistics to a single region.
    :type regionlimit: int
    :param usesystem: Limit the statistics to a single solar system.
    :type usesystem: int

    """
    return web.Response(status=200)
