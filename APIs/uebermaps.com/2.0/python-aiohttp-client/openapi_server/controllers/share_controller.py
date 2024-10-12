from typing import List, Dict
from aiohttp import web

from openapi_server.models.map_with_auth_token import MapWithAuthToken
from openapi_server import util


async def share_map_id_get(request: web.Request, id) -> web.Response:
    """Get secret access token to share map

    Get secret access token of an uebermap with access set to &#39;Secret link&#39;. Pass the &#39;token&#39; on every request you make to access this uebermap and its resources. F.e. token&#x3D;1-x_gqu7eLBe3uKoAGAGXy

    :param id: Id of map
    :type id: int

    """
    return web.Response(status=200)
