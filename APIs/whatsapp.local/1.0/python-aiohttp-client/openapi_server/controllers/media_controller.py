from typing import List, Dict
from aiohttp import web

from openapi_server.models.upload_media_response import UploadMediaResponse
from openapi_server import util


async def delete_media(request: web.Request, media_id) -> web.Response:
    """Delete-Media

    

    :param media_id: 
    :type media_id: str

    """
    return web.Response(status=200)


async def download_media(request: web.Request, media_id) -> web.Response:
    """Download-Media

    

    :param media_id: 
    :type media_id: str

    """
    return web.Response(status=200)


async def upload_media(request: web.Request, body) -> web.Response:
    """Upload-Media

    

    :param body: 
    :type body: str

    """
    return web.Response(status=200)
