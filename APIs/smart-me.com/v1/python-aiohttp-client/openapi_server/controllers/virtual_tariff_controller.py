from typing import List, Dict
from aiohttp import web

from openapi_server.models.virtual_tariffs_of_folder import VirtualTariffsOfFolder
from openapi_server import util


async def api_virtual_tariff_id_get(request: web.Request, id) -> web.Response:
    """Gets all virtual tariffs of a folder

    Gets all virtual tariffs of a folder

    :param id: The ID of the Folder
    :type id: str

    """
    return web.Response(status=200)


async def virtual_tariff_get(request: web.Request, ) -> web.Response:
    """Gets all Virtual Tariffs of a user

    Gets all Virtual Tariffs of a user


    """
    return web.Response(status=200)
