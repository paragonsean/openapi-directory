from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_queue_member import ApiV2010AccountQueueMember
from openapi_server.models.list_member_response import ListMemberResponse
from openapi_server import util


async def fetch_member(request: web.Request, account_sid, queue_sid, call_sid) -> web.Response:
    """fetch_member

    Fetch a specific member from the queue

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Member resource(s) to fetch.
    :type account_sid: str
    :param queue_sid: The SID of the Queue in which to find the members to fetch.
    :type queue_sid: str
    :param call_sid: The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource(s) to fetch.
    :type call_sid: str

    """
    return web.Response(status=200)


async def list_member(request: web.Request, account_sid, queue_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_member

    Retrieve the members of the queue

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Member resource(s) to read.
    :type account_sid: str
    :param queue_sid: The SID of the Queue in which to find the members
    :type queue_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_member(request: web.Request, account_sid, queue_sid, call_sid, url, method=None) -> web.Response:
    """update_member

    Dequeue a member from a queue and have the member&#39;s call begin executing the TwiML document at that URL

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the Member resource(s) to update.
    :type account_sid: str
    :param queue_sid: The SID of the Queue in which to find the members to update.
    :type queue_sid: str
    :param call_sid: The [Call](https://www.twilio.com/docs/voice/api/call-resource) SID of the resource(s) to update.
    :type call_sid: str
    :param url: The absolute URL of the Queue resource.
    :type url: str
    :param method: How to pass the update request data. Can be &#x60;GET&#x60; or &#x60;POST&#x60; and the default is &#x60;POST&#x60;. &#x60;POST&#x60; sends the data as encoded form data and &#x60;GET&#x60; sends the data as query parameters.
    :type method: str

    """
    return web.Response(status=200)
