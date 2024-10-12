from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_models_api_error import APIModelsApiError
from openapi_server.models.update_system_models_checkin_result import UpdateSystemModelsCheckinResult
from openapi_server import util


async def update_system_get_cached_files(request: web.Request, client_id, expired) -> web.Response:
    """Get a list of Cached Files installed on the client Machine.

    No Documentation Found.

    :param client_id: The ClientID of the Client
    :type client_id: str
    :param expired: Only Expired Files (true|false)
    :type expired: bool

    """
    return web.Response(status=200)


async def update_system_get_checkin(request: web.Request, client_id, preview, run_all_inventories=None) -> web.Response:
    """Checks the Client ID into the Update System.

    No Documentation Found.

    :param client_id: The Client ID to check-in.  If this is a new client ID it will be added to Clients.
    :type client_id: str
    :param preview: Get Pkgs w\\o updating Datetimes(true|false)
    :type preview: bool
    :param run_all_inventories: Force return inventories. Defaults to false.
    :type run_all_inventories: bool

    """
    return web.Response(status=200)
