from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_response import ApiResponse
from openapi_server import util


async def ack_message(request: web.Request, queue_name, queue_message_id) -> web.Response:
    """Acknowledge that Queue Message has been processed.

    

    :param queue_name: Name of Queue
    :type queue_name: str
    :param queue_message_id: ID of Queue Message to be acknowledged
    :type queue_message_id: str

    """
    return web.Response(status=200)


async def create_queue(request: web.Request, ) -> web.Response:
    """Create new queue.

    


    """
    return web.Response(status=200)


async def delete_queue(request: web.Request, queue_name, confirm=None) -> web.Response:
    """Delete Queue.

    

    :param queue_name: 
    :type queue_name: str
    :param confirm: 
    :type confirm: bool

    """
    return web.Response(status=200)


async def get_list_of_queues(request: web.Request, ) -> web.Response:
    """Get list of all Queues.

    


    """
    return web.Response(status=200)


async def get_message_data(request: web.Request, queue_name, queue_message_id) -> web.Response:
    """Get data associated with a Queue Message.

    

    :param queue_name: Name of Queue
    :type queue_name: str
    :param queue_message_id: ID of Queue Message for which data is to be returned
    :type queue_message_id: str

    """
    return web.Response(status=200)


async def get_next_messages(request: web.Request, queue_name, count=None) -> web.Response:
    """Get next Queue Messages from a Queue

    

    :param queue_name: Name of Queue
    :type queue_name: str
    :param count: Number of messages to get
    :type count: str

    """
    return web.Response(status=200)


async def get_queue_config(request: web.Request, queue_name) -> web.Response:
    """Get Queue config.

    

    :param queue_name: Name of Queue
    :type queue_name: str

    """
    return web.Response(status=200)


async def send_message_binary(request: web.Request, queue_name, content_type, body, regions=None, delay=None, expiration=None) -> web.Response:
    """Send Queue Message with a binary data (blob) payload.

    

    :param queue_name: Name of Queue
    :type queue_name: str
    :param content_type: Content type of the data to be sent with Queue Message
    :type content_type: str
    :param body: Data to be send with Queue Message
    :type body: List[str]
    :param regions: Regions to which message is to be sent
    :type regions: str
    :param delay: 
    :type delay: str
    :param expiration: 
    :type expiration: str

    """
    return web.Response(status=200)


async def update_queue_config(request: web.Request, queue_name) -> web.Response:
    """Update Queue configuration.

    

    :param queue_name: 
    :type queue_name: str

    """
    return web.Response(status=200)
