from typing import List, Dict
from aiohttp import web

from openapi_server.models.computer_vision_image_create_response import ComputerVisionImageCreateResponse
from openapi_server.models.get_keywords_asset_id_parameter import GetKeywordsAssetIdParameter
from openapi_server.models.image_create_request import ImageCreateRequest
from openapi_server.models.image_create_response import ImageCreateResponse
from openapi_server.models.image_search_results import ImageSearchResults
from openapi_server.models.keyword_data_list import KeywordDataList
from openapi_server.models.language import Language
from openapi_server.models.video_search_results import VideoSearchResults
from openapi_server import util


async def get_keywords(request: web.Request, asset_id) -> web.Response:
    """List suggested keywords

    This endpoint returns a list of suggested keywords for a media item that you specify or upload.

    :param asset_id: The asset ID or upload ID to suggest keywords for
    :type asset_id: dict | bytes

    """
    asset_id = .from_dict(asset_id)
    return web.Response(status=200)


async def get_similar_images(request: web.Request, asset_id, license=None, safe=None, language=None, page=None, per_page=None, view=None) -> web.Response:
    """List similar images

    This endpoint returns images that are visually similar to an image that you specify or upload.

    :param asset_id: The asset ID or upload ID to find similar images for
    :type asset_id: str
    :param license: Show only images with the specified license
    :type license: List[str]
    :param safe: Enable or disable safe search
    :type safe: bool
    :param language: Language for the keywords and categories in the response
    :type language: dict | bytes
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param view: Amount of detail to render in the response
    :type view: str

    """
    language = .from_dict(language)
    return web.Response(status=200)


async def get_similar_videos(request: web.Request, asset_id, license=None, safe=None, language=None, page=None, per_page=None, view=None) -> web.Response:
    """List similar videos

    This endpoint returns videos that are visually similar to an image that you specify or upload.

    :param asset_id: The asset ID or upload ID to find similar videos for
    :type asset_id: str
    :param license: Show only videos with the specified license
    :type license: List[str]
    :param safe: Enable or disable safe search
    :type safe: bool
    :param language: Language for the keywords and categories in the response
    :type language: dict | bytes
    :param page: Page number
    :type page: int
    :param per_page: Number of results per page
    :type per_page: int
    :param view: Amount of detail to render in the response
    :type view: str

    """
    language = .from_dict(language)
    return web.Response(status=200)


async def upload_ephemeral_image(request: web.Request, body) -> web.Response:
    """Upload ephemeral images

    Deprecated; use &#x60;POST /v2/cv/images&#x60; instead. This endpoint uploads an image for reverse image search. The image must be in JPEG or PNG format. To get the search results, pass the ID that this endpoint returns to the &#x60;GET /v2/images/{id}/similar&#x60; endpoint.

    :param body: The image data in JPEG or PNG format
    :type body: dict | bytes

    """
    body = ImageCreateRequest.from_dict(body)
    return web.Response(status=200)


async def upload_image(request: web.Request, body) -> web.Response:
    """Upload images

    This endpoint uploads an image for reverse image or video search. Images must be in JPEG or PNG format. To get the search results, pass the upload ID that this endpoint returns to the GET /v2/cv/similar/images or GET /v2/cv/similar/videos endpoints. Contact us for access to this endpoint.

    :param body: A Base 64 encoded jpeg or png; images can be no larger than 10mb and can be no larger than 10,000 pixels in width or height
    :type body: dict | bytes

    """
    body = ImageCreateRequest.from_dict(body)
    return web.Response(status=200)
