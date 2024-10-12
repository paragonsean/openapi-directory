from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def sales_creditmemo_management_v1_notify_post(request: web.Request, id) -> web.Response:
    """creditmemo/{id}/emails

    Emails a user a specified credit memo.

    :param id: The credit memo ID.
    :type id: int

    """
    return web.Response(status=200)
