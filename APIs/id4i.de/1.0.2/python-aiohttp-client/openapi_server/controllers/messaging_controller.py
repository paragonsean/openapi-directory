from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.queue_presentation import QueuePresentation
from openapi_server.models.queue_update_request import QueueUpdateRequest
from openapi_server.models.send_custom_message import SendCustomMessage
from openapi_server import util


async def enqueue_custom_message(request: web.Request, organization_id, body) -> web.Response:
    """Enqueue a custom message

    Enqueue a custom organisation message with custom data.

    :param organization_id: The organisation namespace
    :type organization_id: str
    :param body: request
    :type body: dict | bytes

    """
    body = SendCustomMessage.from_dict(body)
    return web.Response(status=200)


async def get_default_queue(request: web.Request, organization_id) -> web.Response:
    """get_default_queue

    

    :param organization_id: organizationId
    :type organization_id: str

    """
    return web.Response(status=200)


async def patch_default_queue(request: web.Request, organization_id, body) -> web.Response:
    """patch_default_queue

    

    :param organization_id: organizationId
    :type organization_id: str
    :param body: request
    :type body: dict | bytes

    """
    body = QueueUpdateRequest.from_dict(body)
    return web.Response(status=200)
