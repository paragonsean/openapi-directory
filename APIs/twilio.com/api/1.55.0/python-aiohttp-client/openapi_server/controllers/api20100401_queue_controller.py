from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_queue import ApiV2010AccountQueue
from openapi_server.models.list_queue_response import ListQueueResponse
from openapi_server import util


async def create_queue(request: web.Request, account_sid, friendly_name, max_size=None) -> web.Response:
    """create_queue

    Create a queue

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that will create the resource.
    :type account_sid: str
    :param friendly_name: A descriptive string that you created to describe this resource. It can be up to 64 characters long.
    :type friendly_name: str
    :param max_size: The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.
    :type max_size: int

    """
    return web.Response(status=200)


async def delete_queue(request: web.Request, account_sid, sid) -> web.Response:
    """delete_queue

    Remove an empty queue

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to delete.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Queue resource to delete
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_queue(request: web.Request, account_sid, sid) -> web.Response:
    """fetch_queue

    Fetch an instance of a queue identified by the QueueSid

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to fetch.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Queue resource to fetch
    :type sid: str

    """
    return web.Response(status=200)


async def list_queue(request: web.Request, account_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_queue

    Retrieve a list of queues belonging to the account used to make the request

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resources to read.
    :type account_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_queue(request: web.Request, account_sid, sid, friendly_name=None, max_size=None) -> web.Response:
    """update_queue

    Update the queue with the new parameters

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Queue resource to update.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the Queue resource to update
    :type sid: str
    :param friendly_name: A descriptive string that you created to describe this resource. It can be up to 64 characters long.
    :type friendly_name: str
    :param max_size: The maximum number of calls allowed to be in the queue. The default is 1000. The maximum is 5000.
    :type max_size: int

    """
    return web.Response(status=200)
