from typing import List, Dict
from aiohttp import web

from openapi_server.models.artists_image_search_field_values import ArtistsImageSearchFieldValues
from openapi_server.models.artists_video_search_field_values import ArtistsVideoSearchFieldValues
from openapi_server import util


async def v3_artists_images_get(request: web.Request, accept_language=None, artist_name=None, fields=None, page=None, page_size=None) -> web.Response:
    """Search for images by a photographer

    

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param artist_name: Name of artist for desired images
    :type artist_name: str
    :param fields: Comma separated list of fields. Allows restricting which fields are returned. If no fields are selected, the summary_set of fields are returned.
    :type fields: list | bytes
    :param page: Identifies page to return. Default page is 1.
    :type page: int
    :param page_size: Specifies page size. Default page_size is 10, maximum page_size is 100.
    :type page_size: int

    """
    fields = [ArtistsImageSearchFieldValues.from_dict(d) for d in fields]
    return web.Response(status=200)


async def v3_artists_videos_get(request: web.Request, accept_language=None, artist_name=None, fields=None, page=None, page_size=None) -> web.Response:
    """Search for videos by a photographer

    

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param artist_name: Name of artist for desired images
    :type artist_name: str
    :param fields: Comma separated list of fields. Allows restricting which fields are returned. If no fields are selected, the summary_set of fields are returned.
    :type fields: list | bytes
    :param page: Identifies page to return. Default page is 1.
    :type page: int
    :param page_size: Specifies page size. Default page_size is 10, maximum page_size is 100.
    :type page_size: int

    """
    fields = [ArtistsVideoSearchFieldValues.from_dict(d) for d in fields]
    return web.Response(status=200)
