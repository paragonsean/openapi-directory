from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.operations import Operations
from openapi_server import util


async def fetch_operations(request: web.Request, resource_owner_id=None) -> web.Response:
    """Retrieve the operations accessible to a a given user.

    Retrieve the **operations** accessible to the authenticated user. Filter the results by resource owner if the &#x60;resourceOwnerId&#x60; query parameter is specified.

    :param resource_owner_id: Optional comma-separated list of resource owner unique identifiers by which to filter results.
    :type resource_owner_id: str

    """
    return web.Response(status=200)
