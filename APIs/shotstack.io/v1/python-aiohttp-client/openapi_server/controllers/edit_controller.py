from typing import List, Dict
from aiohttp import web

from openapi_server.models.edit import Edit
from openapi_server.models.queued_response import QueuedResponse
from openapi_server.models.render_response import RenderResponse
from openapi_server import util


async def get_render(request: web.Request, id) -> web.Response:
    """Get Render Status

    Get the rendering status, temporary asset url and details of a render by ID.  **base URL:** https://api.shotstack.io/{version}

    :param id: The id of the timeline render task in UUID format
    :type id: str

    """
    return web.Response(status=200)


async def post_render(request: web.Request, body) -> web.Response:
    """Render Asset

    Queue and render the contents of a timeline as a video, image or audio file.

    :param body: The video, image or audio edit specified using JSON.  **base URL:** https://api.shotstack.io/{version}
    :type body: dict | bytes

    """
    body = Edit.from_dict(body)
    return web.Response(status=200)
