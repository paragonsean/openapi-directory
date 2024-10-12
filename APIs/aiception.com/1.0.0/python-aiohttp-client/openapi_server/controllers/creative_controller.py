from typing import List, Dict
from aiohttp import web

from openapi_server.models.artistic_image_post_request import ArtisticImagePostRequest
from openapi_server.models.task import Task
from openapi_server import util


async def artistic_image_post(request: web.Request, body) -> web.Response:
    """Create an artistic image [ image_url, style_url -&gt; id ]

    Given an image content and a style image create a new stylized image of the content.

    :param body: The content image and the style image
    :type body: dict | bytes

    """
    body = ArtisticImagePostRequest.from_dict(body)
    return web.Response(status=200)


async def artistic_image_task_id_get(request: web.Request, task_id) -> web.Response:
    """Gets a artistic image by task id [ id -&gt; artistic image task ]

    The artistic_image will have the urls of the stylized images.

    :param task_id: An internal id for the task
    :type task_id: str

    """
    return web.Response(status=200)
