from typing import List, Dict
from aiohttp import web

from openapi_server.models.not_found import NotFound
from openapi_server.models.server_size import ServerSize
from openapi_server.models.server_size_data import ServerSizeData
from openapi_server.models.server_size_error import ServerSizeError
from openapi_server import util


async def servers_options_resources_read(request: web.Request, size) -> web.Response:
    """Get a server size by id

    

    :param size: Server size unique identifier expressed as UUID or name.
    :type size: str

    """
    return web.Response(status=200)


async def servers_options_server_size_create(request: web.Request, serversize_data=None) -> web.Response:
    """Create a new server size item

    Only super users with on-premises version have acceess to this endpoint.

    :param serversize_data: 
    :type serversize_data: dict | bytes

    """
    serversize_data = ServerSizeData.from_dict(serversize_data)
    return web.Response(status=200)


async def servers_options_server_size_delete(request: web.Request, size) -> web.Response:
    """Delete a server size by id

    Only super users with on-premises version have acceess to this endpoint.

    :param size: Server size unique identifier expressed as UUID or name.
    :type size: str

    """
    return web.Response(status=200)


async def servers_options_server_size_replace(request: web.Request, size, serversize_data=None) -> web.Response:
    """Replace a server size by id

    Only super users with on-premises version have acceess to this endpoint.

    :param size: Server size unique identifier expressed as UUID or name.
    :type size: str
    :param serversize_data: 
    :type serversize_data: dict | bytes

    """
    serversize_data = ServerSizeData.from_dict(serversize_data)
    return web.Response(status=200)


async def servers_options_server_size_update(request: web.Request, size, serversize_data=None) -> web.Response:
    """Update a server size by id

    Only super users with on-premises version have acceess to this endpoint.

    :param size: Server size unique identifier expressed as UUID or name.
    :type size: str
    :param serversize_data: 
    :type serversize_data: dict | bytes

    """
    serversize_data = ServerSizeData.from_dict(serversize_data)
    return web.Response(status=200)


async def servers_options_sizes_list(request: web.Request, limit=None, offset=None, ordering=None) -> web.Response:
    """Retrieve available server sizes

    

    :param limit: Set limit when retrieving items.
    :type limit: str
    :param offset: Offset when retrieving items.
    :type offset: str
    :param ordering: Set order when retrieving items.
    :type ordering: str

    """
    return web.Response(status=200)
