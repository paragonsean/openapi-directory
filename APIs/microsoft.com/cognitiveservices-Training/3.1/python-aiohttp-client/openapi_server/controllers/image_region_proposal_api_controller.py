from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_vision_error import CustomVisionError
from openapi_server.models.image_region_proposal import ImageRegionProposal
from openapi_server import util


async def get_image_region_proposals(request: web.Request, project_id, image_id, training_key) -> web.Response:
    """Get region proposals for an image. Returns empty array if no proposals are found.

    This API will get region proposals for an image along with confidences for the region. It returns an empty array if no proposals are found.

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param image_id: The image id.
    :type image_id: str
    :type image_id: str
    :param training_key: API key.
    :type training_key: str

    """
    return web.Response(status=200)
