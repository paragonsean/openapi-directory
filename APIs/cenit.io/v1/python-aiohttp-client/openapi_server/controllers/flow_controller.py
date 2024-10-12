from typing import List, Dict
from aiohttp import web

from openapi_server.models.flow import Flow
from openapi_server import util


async def setup_flow_get(request: web.Request, ) -> web.Response:
    """Returns a list of flows

    Returns a list of flows you&#39;ve previously created. The flows are returned in sorted order, with the most recent flow appearing first.


    """
    return web.Response(status=200)


async def setup_flow_id_delete(request: web.Request, id) -> web.Response:
    """Delete a flow.

    Deletes the specified flow.

    :param id: Flow ID
    :type id: str

    """
    return web.Response(status=200)


async def setup_flow_id_get(request: web.Request, id) -> web.Response:
    """Retrieve an existing flow

    Retrieves the details of an existing flow. You need only supply the unique flow identifier that was returned upon flow creation.

    :param id: Flow ID
    :type id: str

    """
    return web.Response(status=200)


async def setup_flow_post(request: web.Request, ) -> web.Response:
    """Create or update a flow

    Creates or updates the specified flow. Any parameters not provided will be left unchanged.


    """
    return web.Response(status=200)
