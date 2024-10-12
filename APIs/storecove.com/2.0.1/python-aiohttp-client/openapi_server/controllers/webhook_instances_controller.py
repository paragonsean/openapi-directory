from typing import List, Dict
from aiohttp import web

from openapi_server.models.webhook_instance import WebhookInstance
from openapi_server import util


async def delete_webhook_instance(request: web.Request, guid) -> web.Response:
    """DELETE a WebhookInstance

    DELETE a specific WebhookInstance

    :param guid: WebhookInstance guid
    :type guid: str
    :type guid: str

    """
    return web.Response(status=200)


async def get_webhook_instances(request: web.Request, ) -> web.Response:
    """GET a WebhookInstance

    GET a WebhookInstance from the queue. After processing it successfully, DELETE it and GET the next one. When a 204 is received, the queue is empty and the polling process can sleep for a while.


    """
    return web.Response(status=200)
