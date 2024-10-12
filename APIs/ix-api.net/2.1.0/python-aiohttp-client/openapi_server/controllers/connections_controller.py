from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.connection import Connection
from openapi_server import util


async def connections_list(request: web.Request, id=None, state=None, state__is_not=None, mode=None, mode__is_not=None, name=None, metro_area_network=None, pop=None, facility=None, external_ref=None) -> web.Response:
    """connections_list

    List all &#x60;connection&#x60;s.

    :param id: Filter by id
    :type id: List[str]
    :param state: Filter by state
    :type state: str
    :param state__is_not: Filter by state__is_not
    :type state__is_not: str
    :param mode: Filter by mode
    :type mode: str
    :param mode__is_not: Filter by mode__is_not
    :type mode__is_not: str
    :param name: Filter by name
    :type name: str
    :param metro_area_network: Filter by metro_area_network
    :type metro_area_network: str
    :param pop: Filter by pop
    :type pop: str
    :param facility: Filter by facility
    :type facility: str
    :param external_ref: Filter by external_ref
    :type external_ref: str

    """
    return web.Response(status=200)


async def connections_read(request: web.Request, id) -> web.Response:
    """connections_read

    Read a &#x60;connection&#x60;.

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)
