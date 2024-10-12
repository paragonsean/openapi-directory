from typing import List, Dict
from aiohttp import web

from openapi_server.models.export_completed_response import ExportCompletedResponse
from openapi_server.models.export_in_progress_response import ExportInProgressResponse
from openapi_server import util


async def status_completed(request: web.Request, content_type, accept) -> web.Response:
    """Export order report with status &#39;Completed&#39;

    Retrieves a list of all order reports that are &#x60;completed&#x60;, by &#x60;accountName&#x60;. Be aware that the scope of the export log is per user.     &gt; This endpoint is for VTEX internal use, and it is not meant to be used by clients.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)


async def status_in_progress(request: web.Request, content_type, accept) -> web.Response:
    """Export order report with status &#39;In Progress&#39;

    Retrieves a list of all order reports that are &#x60;in progress&#x60;, by &#x60;accountName&#x60;. Be aware that the scope of the export log is per user.     &gt; This endpoint is for VTEX internal use, and it is not meant to be used by clients.

    :param content_type: Type of the content being sent.
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str

    """
    return web.Response(status=200)
