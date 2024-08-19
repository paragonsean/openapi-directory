from typing import List, Dict
from aiohttp import web

from openapi_server.models.accounts_list400_response import AccountsList400Response
from openapi_server.models.accounts_list401_response import AccountsList401Response
from openapi_server.models.accounts_list403_response import AccountsList403Response
from openapi_server.models.accounts_read404_response import AccountsRead404Response
from openapi_server.models.metro_area_network import MetroAreaNetwork
from openapi_server import util


async def metro_area_networks_list(request: web.Request, id=None, name=None, metro_area=None, service_provider=None) -> web.Response:
    """metro_area_networks_list

    List all MetroAreaNetworks

    :param id: Filter by id
    :type id: List[str]
    :param name: Filter by name
    :type name: str
    :param metro_area: Filter by metro_area
    :type metro_area: str
    :param service_provider: Filter by service_provider
    :type service_provider: str

    """
    return web.Response(status=200)


async def metro_area_networks_read(request: web.Request, id) -> web.Response:
    """metro_area_networks_read

    Retrieve a MetroAreaNetwork

    :param id: Get by id
    :type id: str

    """
    return web.Response(status=200)
