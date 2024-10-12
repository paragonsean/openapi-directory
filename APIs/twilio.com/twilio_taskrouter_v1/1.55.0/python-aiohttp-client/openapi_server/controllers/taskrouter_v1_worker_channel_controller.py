from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_worker_channel_response import ListWorkerChannelResponse
from openapi_server.models.taskrouter_v1_workspace_worker_worker_channel import TaskrouterV1WorkspaceWorkerWorkerChannel
from openapi_server import util


async def fetch_worker_channel(request: web.Request, workspace_sid, worker_sid, sid) -> web.Response:
    """fetch_worker_channel

    

    :param workspace_sid: The SID of the Workspace with the WorkerChannel to fetch.
    :type workspace_sid: str
    :param worker_sid: The SID of the Worker with the WorkerChannel to fetch.
    :type worker_sid: str
    :param sid: The SID of the WorkerChannel to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_worker_channel(request: web.Request, workspace_sid, worker_sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_worker_channel

    

    :param workspace_sid: The SID of the Workspace with the WorkerChannels to read.
    :type workspace_sid: str
    :param worker_sid: The SID of the Worker with the WorkerChannels to read.
    :type worker_sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_worker_channel(request: web.Request, workspace_sid, worker_sid, sid, available=None, capacity=None) -> web.Response:
    """update_worker_channel

    

    :param workspace_sid: The SID of the Workspace with the WorkerChannel to update.
    :type workspace_sid: str
    :param worker_sid: The SID of the Worker with the WorkerChannel to update.
    :type worker_sid: str
    :param sid: The SID of the WorkerChannel to update.
    :type sid: str
    :param available: Whether the WorkerChannel is available. Set to &#x60;false&#x60; to prevent the Worker from receiving any new Tasks of this TaskChannel type.
    :type available: bool
    :param capacity: The total number of Tasks that the Worker should handle for the TaskChannel type. TaskRouter creates reservations for Tasks of this TaskChannel type up to the specified capacity. If the capacity is 0, no new reservations will be created.
    :type capacity: int

    """
    return web.Response(status=200)
