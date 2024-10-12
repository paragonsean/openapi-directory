from typing import List, Dict
from aiohttp import web

from openapi_server.models.contentpro_search_get200_response import ContentproSearchGet200Response
from openapi_server.models.contentpro_similar_text_post_request import ContentproSimilarTextPostRequest
from openapi_server import util


async def contentpro_similar_text_post(request: web.Request, body) -> web.Response:
    """The /contentpro-similar-text endpoint accepts and arbitrary piece of text and returns similar articles and blogs written by companies.

    

    :param body: We&#39;ll provide information about related companies and articles based on the text you provide.
    :type body: dict | bytes

    """
    body = ContentproSimilarTextPostRequest.from_dict(body)
    return web.Response(status=200)
