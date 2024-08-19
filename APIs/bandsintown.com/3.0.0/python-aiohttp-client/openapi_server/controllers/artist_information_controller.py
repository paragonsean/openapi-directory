from typing import List, Dict
from aiohttp import web

from openapi_server.models.artist_data import ArtistData
from openapi_server import util


async def artist(request: web.Request, artistname, app_id) -> web.Response:
    """Get artist information

    Get artist information 

    :param artistname: The name of the artist. If it contains one of the special characters below, please be sure to replace it by the corresponding code: for / use %252F, for ? use %253F, for * use %252A, and for \&quot; use %27C
    :type artistname: str
    :param app_id: The application ID assigned to you by Bandsintown
    :type app_id: str

    """
    return web.Response(status=200)
