from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_response_similarity import APIResponseSimilarity
from openapi_server.models.src_searchly_api_v1_controllers_similarity_by_content_request import SrcSearchlyApiV1ControllersSimilarityByContentRequest
from openapi_server import util


async def src_searchly_api_v1_controllers_similarity_by_content(request: web.Request, body) -> web.Response:
    """API endpoint to search similarity using content

    Endpoint for an end-user client to search similarity by content.  If you want to run the /similarity/by_content operation, you can do so via an HTTP POST command to the following URL:  &#x60;&#x60;&#x60; https://searchly.asuarez.dev/api/v1/similarity/by_content &#x60;&#x60;&#x60; 

    :param body: Body wrapper for the request.
    :type body: dict | bytes

    """
    body = SrcSearchlyApiV1ControllersSimilarityByContentRequest.from_dict(body)
    return web.Response(status=200)


async def src_searchly_api_v1_controllers_similarity_by_song(request: web.Request, song_id) -> web.Response:
    """API endpoint to search similarity using a song identifier

    Endpoint for an end-user client to search similarity by song identifier.  If you want to run the /similarity/by_song operation, you can do so via an HTTP GET command to the following URL:  &#x60;&#x60;&#x60; https://searchly.asuarez.dev/api/v1/similarity/by_song &#x60;&#x60;&#x60; 

    :param song_id: Song identifier.
    :type song_id: int

    """
    return web.Response(status=200)
