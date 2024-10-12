from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_activity_response import ListActivityResponse
from openapi_server.models.taskrouter_v1_workspace_activity import TaskrouterV1WorkspaceActivity
from openapi_server import util


async def create_activity(request: web.Request, workspace_sid, friendly_name, available=None) -> web.Response:
    """create_activity

    

    :param workspace_sid: The SID of the Workspace that the new Activity belongs to.
    :type workspace_sid: str
    :param friendly_name: A descriptive string that you create to describe the Activity resource. It can be up to 64 characters long. These names are used to calculate and expose statistics about Workers, and provide visibility into the state of each Worker. Examples of friendly names include: &#x60;on-call&#x60;, &#x60;break&#x60;, and &#x60;email&#x60;.
    :type friendly_name: str
    :param available: Whether the Worker should be eligible to receive a Task when it occupies the Activity. A value of &#x60;true&#x60;, &#x60;1&#x60;, or &#x60;yes&#x60; specifies the Activity is available. All other values specify that it is not. The value cannot be changed after the Activity is created.
    :type available: bool

    """
    return web.Response(status=200)


async def delete_activity(request: web.Request, workspace_sid, sid) -> web.Response:
    """delete_activity

    

    :param workspace_sid: The SID of the Workspace with the Activity resources to delete.
    :type workspace_sid: str
    :param sid: The SID of the Activity resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_activity(request: web.Request, workspace_sid, sid) -> web.Response:
    """fetch_activity

    

    :param workspace_sid: The SID of the Workspace with the Activity resources to fetch.
    :type workspace_sid: str
    :param sid: The SID of the Activity resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_activity(request: web.Request, workspace_sid, friendly_name=None, available=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_activity

    

    :param workspace_sid: The SID of the Workspace with the Activity resources to read.
    :type workspace_sid: str
    :param friendly_name: The &#x60;friendly_name&#x60; of the Activity resources to read.
    :type friendly_name: str
    :param available: Whether return only Activity resources that are available or unavailable. A value of &#x60;true&#x60; returns only available activities. Values of &#39;1&#39; or &#x60;yes&#x60; also indicate &#x60;true&#x60;. All other values represent &#x60;false&#x60; and return activities that are unavailable.
    :type available: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_activity(request: web.Request, workspace_sid, sid, friendly_name=None) -> web.Response:
    """update_activity

    

    :param workspace_sid: The SID of the Workspace with the Activity resources to update.
    :type workspace_sid: str
    :param sid: The SID of the Activity resource to update.
    :type sid: str
    :param friendly_name: A descriptive string that you create to describe the Activity resource. It can be up to 64 characters long. These names are used to calculate and expose statistics about Workers, and provide visibility into the state of each Worker. Examples of friendly names include: &#x60;on-call&#x60;, &#x60;break&#x60;, and &#x60;email&#x60;.
    :type friendly_name: str

    """
    return web.Response(status=200)
