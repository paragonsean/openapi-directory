from typing import List, Dict
from aiohttp import web

from openapi_server.models.async_request_status import AsyncRequestStatus
from openapi_server import util


async def create_managed_volume_generate_script_job(request: web.Request, id) -> web.Response:
    """Generate and download unified view script

    Start an asynchronous job to generate and download a script to unify export paths across channels in managed volume export.

    :param id: ID of snapshot export.
    :type id: str

    """
    return web.Response(status=200)
