from typing import List, Dict
from aiohttp import web

from openapi_server.models.json_artist import JsonArtist
from openapi_server import util


async def resource10_artist_mbid_get_artist_get(request: web.Request, mbid) -> web.Response:
    """.

    &lt;p&gt; Returns an artist for a given Musicbrainz MBID &lt;/p&gt;

    :param mbid: a Musicbrainz MBID, e.g. 0bfba3d3-6a04-4779-bb0a-df07df5b0558
    :type mbid: str

    """
    return web.Response(status=200)
