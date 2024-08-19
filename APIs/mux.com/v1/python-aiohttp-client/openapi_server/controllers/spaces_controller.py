from typing import List, Dict
from aiohttp import web

from openapi_server.models.broadcast_response import BroadcastResponse
from openapi_server.models.create_broadcast_request import CreateBroadcastRequest
from openapi_server.models.create_space_request import CreateSpaceRequest
from openapi_server.models.list_spaces_response import ListSpacesResponse
from openapi_server.models.space_response import SpaceResponse
from openapi_server.models.start_space_broadcast_response import StartSpaceBroadcastResponse
from openapi_server.models.stop_space_broadcast_response import StopSpaceBroadcastResponse
from openapi_server import util


async def create_space(request: web.Request, body) -> web.Response:
    """Create a space

    Create a new space. Spaces are used to build [real-time video applications.](https://mux.com/real-time-video)

    :param body: 
    :type body: dict | bytes

    """
    body = CreateSpaceRequest.from_dict(body)
    return web.Response(status=200)


async def create_space_broadcast(request: web.Request, space_id, body) -> web.Response:
    """Create a space broadcast

    Creates a new broadcast. Broadcasts are used to create composited versions of your space, which can be broadcast to live streams. **Note:** By default only a single broadcast destination can be specified. Contact Mux support if you need more.

    :param space_id: The space ID.
    :type space_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateBroadcastRequest.from_dict(body)
    return web.Response(status=200)


async def delete_space(request: web.Request, space_id) -> web.Response:
    """Delete a space

    Deletes a space. Spaces can only be deleted when &#x60;idle&#x60;.

    :param space_id: The space ID.
    :type space_id: str

    """
    return web.Response(status=200)


async def delete_space_broadcast(request: web.Request, space_id, broadcast_id) -> web.Response:
    """Delete a space broadcast

    Deletes a single broadcast of a specific space. Broadcasts can only be deleted when &#x60;idle&#x60;.

    :param space_id: The space ID.
    :type space_id: str
    :param broadcast_id: The broadcast ID.
    :type broadcast_id: str

    """
    return web.Response(status=200)


async def get_space(request: web.Request, space_id) -> web.Response:
    """Retrieve a space

    Retrieves the details of a space that has previously been created. Supply the unique space ID that was returned from your create space request, and Mux will return the information about the corresponding space. The same information is returned when creating a space.

    :param space_id: The space ID.
    :type space_id: str

    """
    return web.Response(status=200)


async def get_space_broadcast(request: web.Request, space_id, broadcast_id) -> web.Response:
    """Retrieve space broadcast

    Retrieves the details of a broadcast of a specific space.

    :param space_id: The space ID.
    :type space_id: str
    :param broadcast_id: The broadcast ID.
    :type broadcast_id: str

    """
    return web.Response(status=200)


async def list_spaces(request: web.Request, limit=None, page=None) -> web.Response:
    """List spaces

    List all spaces in the current enviroment.

    :param limit: Number of items to include in the response
    :type limit: int
    :param page: Offset by this many pages, of the size of &#x60;limit&#x60;
    :type page: int

    """
    return web.Response(status=200)


async def start_space_broadcast(request: web.Request, space_id, broadcast_id) -> web.Response:
    """Start a space broadcast

    Starts broadcasting a space to the associated destination. Broadcasts can only be started when the space is &#x60;active&#x60; (when there are participants connected).

    :param space_id: The space ID.
    :type space_id: str
    :param broadcast_id: The broadcast ID.
    :type broadcast_id: str

    """
    return web.Response(status=200)


async def stop_space_broadcast(request: web.Request, space_id, broadcast_id) -> web.Response:
    """Stop a space broadcast

    Stops broadcasting a space, causing the destination live stream to become idle. This API also automatically calls &#x60;complete&#x60; on the destination live stream. Broadcasts are also automatically stopped when a space becomes idle.

    :param space_id: The space ID.
    :type space_id: str
    :param broadcast_id: The broadcast ID.
    :type broadcast_id: str

    """
    return web.Response(status=200)
