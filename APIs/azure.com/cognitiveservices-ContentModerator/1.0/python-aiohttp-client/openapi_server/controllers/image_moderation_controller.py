from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.evaluate import Evaluate
from openapi_server.models.found_faces import FoundFaces
from openapi_server.models.match_response import MatchResponse
from openapi_server.models.ocr import OCR
from openapi_server import util


async def image_moderation_evaluate(request: web.Request, cache_image=None) -> web.Response:
    """image_moderation_evaluate

    Returns probabilities of the image containing racy or adult content.

    :param cache_image: Whether to retain the submitted image for future use; defaults to false if omitted.
    :type cache_image: bool

    """
    return web.Response(status=200)


async def image_moderation_find_faces(request: web.Request, cache_image=None) -> web.Response:
    """image_moderation_find_faces

    Returns the list of faces found.

    :param cache_image: Whether to retain the submitted image for future use; defaults to false if omitted.
    :type cache_image: bool

    """
    return web.Response(status=200)


async def image_moderation_match(request: web.Request, list_id=None, cache_image=None) -> web.Response:
    """image_moderation_match

    Fuzzily match an image against one of your custom Image Lists. You can create and manage your custom image lists using &lt;a href&#x3D;\&quot;/docs/services/578ff44d2703741568569ab9/operations/578ff7b12703741568569abe\&quot;&gt;this&lt;/a&gt; API.     Returns ID and tags of matching image.&lt;br/&gt;  &lt;br/&gt;  Note: Refresh Index must be run on the corresponding Image List before additions and removals are reflected in the response.

    :param list_id: The list Id.
    :type list_id: str
    :param cache_image: Whether to retain the submitted image for future use; defaults to false if omitted.
    :type cache_image: bool

    """
    return web.Response(status=200)


async def image_moderation_ocr(request: web.Request, language, cache_image=None, enhanced=None) -> web.Response:
    """image_moderation_ocr

    Returns any text found in the image for the language specified. If no language is specified in input then the detection defaults to English.

    :param language: Language of the terms.
    :type language: str
    :param cache_image: Whether to retain the submitted image for future use; defaults to false if omitted.
    :type cache_image: bool
    :param enhanced: When set to True, the image goes through additional processing to come with additional candidates.  image/tiff is not supported when enhanced is set to true  Note: This impacts the response time.
    :type enhanced: bool

    """
    return web.Response(status=200)
