from typing import List, Dict
from aiohttp import web

from openapi_server.models.flex_v1_channel import FlexV1Channel
from openapi_server.models.list_channel_response import ListChannelResponse
from openapi_server import util


async def create_channel(request: web.Request, chat_friendly_name, chat_user_friendly_name, flex_flow_sid, identity, chat_unique_name=None, long_lived=None, pre_engagement_data=None, target=None, task_attributes=None, task_sid=None) -> web.Response:
    """create_channel

    

    :param chat_friendly_name: The chat channel&#39;s friendly name.
    :type chat_friendly_name: str
    :param chat_user_friendly_name: The chat participant&#39;s friendly name.
    :type chat_user_friendly_name: str
    :param flex_flow_sid: The SID of the Flex Flow.
    :type flex_flow_sid: str
    :param identity: The &#x60;identity&#x60; value that uniquely identifies the new resource&#39;s chat User.
    :type identity: str
    :param chat_unique_name: The chat channel&#39;s unique name.
    :type chat_unique_name: str
    :param long_lived: Whether to create the channel as long-lived.
    :type long_lived: bool
    :param pre_engagement_data: The pre-engagement data.
    :type pre_engagement_data: str
    :param target: The Target Contact Identity, for example the phone number of an SMS.
    :type target: str
    :param task_attributes: The Task attributes to be added for the TaskRouter Task.
    :type task_attributes: str
    :param task_sid: The SID of the TaskRouter Task. Only valid when integration type is &#x60;task&#x60;. &#x60;null&#x60; for integration types &#x60;studio&#x60; &amp; &#x60;external&#x60;
    :type task_sid: str

    """
    return web.Response(status=200)


async def delete_channel(request: web.Request, sid) -> web.Response:
    """delete_channel

    

    :param sid: The SID of the Flex chat channel resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_channel(request: web.Request, sid) -> web.Response:
    """fetch_channel

    

    :param sid: The SID of the Flex chat channel resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_channel(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_channel

    

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
