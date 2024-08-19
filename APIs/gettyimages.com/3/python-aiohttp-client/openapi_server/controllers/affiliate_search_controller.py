from typing import List, Dict
from aiohttp import web

from openapi_server.models.affiliate_image_search_response import AffiliateImageSearchResponse
from openapi_server.models.affiliate_search_style import AffiliateSearchStyle
from openapi_server.models.affiliate_video_search_response import AffiliateVideoSearchResponse
from openapi_server import util


async def v3_affiliates_search_images_get(request: web.Request, accept_language=None, phrase=None, style=None) -> web.Response:
    """

    

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param phrase: Search images using a search phrase.
    :type phrase: str
    :param style: Filter based on graphical style of the image.
    :type style: dict | bytes

    """
    style = .from_dict(style)
    return web.Response(status=200)


async def v3_affiliates_search_videos_get(request: web.Request, accept_language=None, phrase=None) -> web.Response:
    """v3_affiliates_search_videos_get

    

    :param accept_language: Provide a header to specify the language of result values. Supported values: cs (iStock only), de, en-GB, en-US, es, fi (iStock only), fr, hu (iStock only), id (iStock only), it, ja, ko (creative assets only), nl, pl (creative assets only), pt-BR, pt-PT, ro (iStock only), ru (creative assets only), sv, th (iStock only), tr, uk (iStock only), vi (iStock only), zh-HK (creative assets only).
    :type accept_language: str
    :param phrase: 
    :type phrase: str

    """
    return web.Response(status=200)
