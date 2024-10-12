from typing import List, Dict
from aiohttp import web

from openapi_server.models.anchore_image_tag_summary import AnchoreImageTagSummary
from openapi_server.models.api_error_response import ApiErrorResponse
from openapi_server import util


async def list_imagetags(request: web.Request, image_status=None, x_anchore_account=None) -> web.Response:
    """List all visible image digests and tags

    List all image tags visible to the user

    :param image_status: Filter images in one or more states such as active, deleting. Defaults to active images only if unspecified
    :type image_status: List[str]
    :param x_anchore_account: An account name to change the resource scope of the request to that account, if permissions allow (admin only)
    :type x_anchore_account: str

    """
    return web.Response(status=200)
