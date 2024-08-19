from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.queue import Queue
from openapi_server.models.queue_response import QueueResponse
from openapi_server import util


async def apps_app_id_queues_get(request: web.Request, app_id) -> web.Response:
    """Lists queues

    Lists the queues associated with the specified application ID.

    :param app_id: The application ID.
    :type app_id: str

    """
    return web.Response(status=200)


async def apps_app_id_queues_post(request: web.Request, app_id, body=None) -> web.Response:
    """Creates a queue

    Creates a queue for the application specified by application ID. The properties for the queue to be created are specified in the request body.

    :param app_id: The application ID.
    :type app_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = Queue.from_dict(body)
    return web.Response(status=200)


async def apps_app_id_queues_queue_id_delete(request: web.Request, app_id, queue_id) -> web.Response:
    """Deletes a queue

    Delete the queue with the specified queue name, from the application with the specified application ID.

    :param app_id: The application ID.
    :type app_id: str
    :param queue_id: The queue ID.
    :type queue_id: str

    """
    return web.Response(status=200)
