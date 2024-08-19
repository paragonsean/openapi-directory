from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.role import Role
from openapi_server import util


async def roles_list(request: web.Request, id=None, name=None, contact=None) -> web.Response:
    """roles_list

    List all roles available.

    :param id: Filter by id
    :type id: List[str]
    :param name: Filter by name
    :type name: str
    :param contact: Filter by contact
    :type contact: str

    """
    return web.Response(status=200)


async def roles_read(request: web.Request, id, id2=None, name=None) -> web.Response:
    """roles_read

    Get a single &#x60;Role&#x60;.

    :param id: Get by id
    :type id: str
    :param id2: Filter by id
    :type id2: List[str]
    :param name: Filter by name
    :type name: str

    """
    return web.Response(status=200)
