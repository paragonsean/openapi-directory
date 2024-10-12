from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.point_of_presence import PointOfPresence
from openapi_server import util


async def pops_list(request: web.Request, id=None, facility=None, metro_area_network=None, capability_media_type=None, capability_speed=None, capability_speed__lt=None, capability_speed__lte=None, capability_speed__gt=None, capability_speed__gte=None) -> web.Response:
    """pops_list

    List all PoPs

    :param id: Filter by id
    :type id: List[str]
    :param facility: Filter by facility
    :type facility: str
    :param metro_area_network: Filter by metro_area_network
    :type metro_area_network: str
    :param capability_media_type: Filter by capability_media_type
    :type capability_media_type: str
    :param capability_speed: Filter by capability_speed
    :type capability_speed: int
    :param capability_speed__lt: Filter by capability_speed__lt
    :type capability_speed__lt: int
    :param capability_speed__lte: Filter by capability_speed__lte
    :type capability_speed__lte: int
    :param capability_speed__gt: Filter by capability_speed__gt
    :type capability_speed__gt: int
    :param capability_speed__gte: Filter by capability_speed__gte
    :type capability_speed__gte: int

    """
    return web.Response(status=200)


async def pops_read(request: web.Request, id) -> web.Response:
    """pops_read

    Get a single point of presence

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)
