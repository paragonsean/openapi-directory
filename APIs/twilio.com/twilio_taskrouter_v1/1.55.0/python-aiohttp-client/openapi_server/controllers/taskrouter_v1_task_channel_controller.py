from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_task_channel_response import ListTaskChannelResponse
from openapi_server.models.taskrouter_v1_workspace_task_channel import TaskrouterV1WorkspaceTaskChannel
from openapi_server import util


async def create_task_channel(request: web.Request, workspace_sid, friendly_name, unique_name, channel_optimized_routing=None) -> web.Response:
    """create_task_channel

    

    :param workspace_sid: The SID of the Workspace that the new Task Channel belongs to.
    :type workspace_sid: str
    :param friendly_name: A descriptive string that you create to describe the Task Channel. It can be up to 64 characters long.
    :type friendly_name: str
    :param unique_name: An application-defined string that uniquely identifies the Task Channel, such as &#x60;voice&#x60; or &#x60;sms&#x60;.
    :type unique_name: str
    :param channel_optimized_routing: Whether the Task Channel should prioritize Workers that have been idle. If &#x60;true&#x60;, Workers that have been idle the longest are prioritized.
    :type channel_optimized_routing: bool

    """
    return web.Response(status=200)


async def delete_task_channel(request: web.Request, workspace_sid, sid) -> web.Response:
    """delete_task_channel

    

    :param workspace_sid: The SID of the Workspace with the Task Channel to delete.
    :type workspace_sid: str
    :param sid: The SID of the Task Channel resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_task_channel(request: web.Request, workspace_sid, sid) -> web.Response:
    """fetch_task_channel

    

    :param workspace_sid: The SID of the Workspace with the Task Channel to fetch.
    :type workspace_sid: str
    :param sid: The SID of the Task Channel resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_task_channel(request: web.Request, workspace_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_task_channel

    

    :param workspace_sid: The SID of the Workspace with the Task Channel to read.
    :type workspace_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_task_channel(request: web.Request, workspace_sid, sid, channel_optimized_routing=None, friendly_name=None) -> web.Response:
    """update_task_channel

    

    :param workspace_sid: The SID of the Workspace with the Task Channel to update.
    :type workspace_sid: str
    :param sid: The SID of the Task Channel resource to update.
    :type sid: str
    :param channel_optimized_routing: Whether the TaskChannel should prioritize Workers that have been idle. If &#x60;true&#x60;, Workers that have been idle the longest are prioritized.
    :type channel_optimized_routing: bool
    :param friendly_name: A descriptive string that you create to describe the Task Channel. It can be up to 64 characters long.
    :type friendly_name: str

    """
    return web.Response(status=200)
