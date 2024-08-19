from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.port import Port
from openapi_server import util


async def ports_list(request: web.Request, id=None, state=None, state__is_not=None, media_type=None, pop=None, name=None, external_ref=None, device=None, speed=None, connection=None) -> web.Response:
    """ports_list

    List all ports.

    :param id: Filter by id
    :type id: List[str]
    :param state: Filter by state
    :type state: str
    :param state__is_not: Filter by state__is_not
    :type state__is_not: str
    :param media_type: Filter by media_type
    :type media_type: str
    :param pop: Filter by pop
    :type pop: str
    :param name: Filter by name
    :type name: str
    :param external_ref: Filter by external_ref
    :type external_ref: str
    :param device: Filter by device
    :type device: str
    :param speed: Filter by speed
    :type speed: str
    :param connection: Filter by connection
    :type connection: str

    """
    return web.Response(status=200)


async def ports_read(request: web.Request, id) -> web.Response:
    """ports_read

    Retrieve a port.

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)
