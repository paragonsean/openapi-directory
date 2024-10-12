from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.resource_owner import ResourceOwner
from openapi_server import util


async def get_resource_owner(request: web.Request, resource_owner_id) -> web.Response:
    """Retrieve a resource owner by ID

    Retrieve a resource owner for the given &#x60;resourceOwnerId&#x60;.

    :param resource_owner_id: Unique identifier of the resource owner.
    :type resource_owner_id: str
    :type resource_owner_id: str

    """
    return web.Response(status=200)
