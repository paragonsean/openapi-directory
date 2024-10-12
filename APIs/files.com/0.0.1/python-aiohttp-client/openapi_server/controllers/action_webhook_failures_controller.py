from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def post_action_webhook_failures_id_retry(request: web.Request, id) -> web.Response:
    """retry Action Webhook Failure

    retry Action Webhook Failure

    :param id: Action Webhook Failure ID.
    :type id: int

    """
    return web.Response(status=200)
