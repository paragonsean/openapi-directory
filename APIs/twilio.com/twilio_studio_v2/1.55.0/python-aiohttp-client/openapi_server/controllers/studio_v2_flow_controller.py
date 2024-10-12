from typing import List, Dict
from aiohttp import web

from openapi_server.models.flow_enum_status import FlowEnumStatus
from openapi_server.models.list_flow_response import ListFlowResponse
from openapi_server.models.studio_v2_flow import StudioV2Flow
from openapi_server import util


async def create_flow(request: web.Request, definition, friendly_name, status, commit_message=None) -> web.Response:
    """create_flow

    Create a Flow.

    :param definition: JSON representation of flow definition.
    :type definition: dict | bytes
    :param friendly_name: The string that you assigned to describe the Flow.
    :type friendly_name: str
    :param status: 
    :type status: str
    :param commit_message: Description of change made in the revision.
    :type commit_message: str

    """
    definition = object.from_dict(definition)
    return web.Response(status=200)


async def delete_flow(request: web.Request, sid) -> web.Response:
    """delete_flow

    Delete a specific Flow.

    :param sid: The SID of the Flow resource to delete.
    :type sid: str

    """
    return web.Response(status=200)


async def fetch_flow(request: web.Request, sid) -> web.Response:
    """fetch_flow

    Retrieve a specific Flow.

    :param sid: The SID of the Flow resource to fetch.
    :type sid: str

    """
    return web.Response(status=200)


async def list_flow(request: web.Request, page_size=None, page=None, page_token=None) -> web.Response:
    """list_flow

    Retrieve a list of all Flows.

    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_flow(request: web.Request, sid, status, commit_message=None, definition=None, friendly_name=None) -> web.Response:
    """update_flow

    Update a Flow.

    :param sid: The SID of the Flow resource to fetch.
    :type sid: str
    :param status: 
    :type status: str
    :param commit_message: Description of change made in the revision.
    :type commit_message: str
    :param definition: JSON representation of flow definition.
    :type definition: dict | bytes
    :param friendly_name: The string that you assigned to describe the Flow.
    :type friendly_name: str

    """
    definition = object.from_dict(definition)
    return web.Response(status=200)
