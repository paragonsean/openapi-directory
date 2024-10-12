from typing import List, Dict
from aiohttp import web

from openapi_server.models.custom_vision_error import CustomVisionError
from openapi_server.models.suggested_tag_and_region import SuggestedTagAndRegion
from openapi_server import util


async def suggest_tags_and_regions(request: web.Request, project_id, iteration_id, image_ids) -> web.Response:
    """Suggest tags and regions for an array/batch of untagged images. Returns empty array if no tags are found.

    This API will get suggested tags and regions for an array/batch of untagged images along with confidences for the tags. It returns an empty array if no tags are found.  There is a limit of 64 images in the batch.

    :param project_id: The project id.
    :type project_id: str
    :type project_id: str
    :param iteration_id: IterationId to use for tag and region suggestion.
    :type iteration_id: str
    :type iteration_id: str
    :param image_ids: Array of image ids tag suggestion are needed for. Use GetUntaggedImages API to get imageIds.
    :type image_ids: List[str]

    """
    return web.Response(status=200)
