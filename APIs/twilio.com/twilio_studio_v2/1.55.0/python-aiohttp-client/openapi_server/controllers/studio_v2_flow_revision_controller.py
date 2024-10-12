from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_flow_revision_response import ListFlowRevisionResponse
from openapi_server.models.studio_v2_flow_flow_revision import StudioV2FlowFlowRevision
from openapi_server import util


async def fetch_flow_revision(request: web.Request, sid, revision) -> web.Response:
    """fetch_flow_revision

    Retrieve a specific Flow revision.

    :param sid: The SID of the Flow resource to fetch.
    :type sid: str
    :param revision: Specific Revision number or can be &#x60;LatestPublished&#x60; and &#x60;LatestRevision&#x60;.
    :type revision: str

    """
    return web.Response(status=200)


async def list_flow_revision(request: web.Request, sid, page_size=None, page=None, page_token=None) -> web.Response:
    """list_flow_revision

    Retrieve a list of all Flows revisions.

    :param sid: The SID of the Flow resource to fetch.
    :type sid: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)
