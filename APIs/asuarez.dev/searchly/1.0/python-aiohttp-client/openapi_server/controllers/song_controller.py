from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_response_song import APIResponseSong
from openapi_server import util


async def src_searchly_api_v1_controllers_song_search(request: web.Request, query) -> web.Response:
    """API endpoint to search songs from the database given a query

    Endpoint for an end-user client to search songs from the database given a String query.  If you want to run the /song/search operation, you can do so via an HTTP GET command to the following URL:  &#x60;&#x60;&#x60; https://searchly.asuarez.dev/api/v1/song/search &#x60;&#x60;&#x60; 

    :param query: Query.
    :type query: str

    """
    return web.Response(status=200)
