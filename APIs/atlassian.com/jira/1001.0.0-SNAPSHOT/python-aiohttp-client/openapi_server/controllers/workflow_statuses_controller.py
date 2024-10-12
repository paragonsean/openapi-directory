from typing import List, Dict
from aiohttp import web

from openapi_server.models.status_details import StatusDetails
from openapi_server import util


async def get_status(request: web.Request, id_or_name) -> web.Response:
    """Get status

    Returns a status. The status must be associated with an active workflow to be returned.  If a name is used on more than one status, only the status found first is returned. Therefore, identifying the status by its ID may be preferable.  This operation can be accessed anonymously.  [Permissions](#permissions) required: None.

    :param id_or_name: The ID or name of the status.
    :type id_or_name: str

    """
    return web.Response(status=200)


async def get_statuses(request: web.Request, ) -> web.Response:
    """Get all statuses

    Returns a list of all statuses associated with active workflows.  This operation can be accessed anonymously.  **[Permissions](#permissions) required:** None.


    """
    return web.Response(status=200)
