from typing import List, Dict
from aiohttp import web

from openapi_server.models.domain import Domain
from openapi_server.models.legacy_error import LegacyError
from openapi_server import util


async def add_video_privacy_domain(request: web.Request, domain, video_id) -> web.Response:
    """Permit a video to be embedded on a domain

    If domain privacy is enabled for this video, this method permits the video to be embedded on the specified domain.

    :param domain: The domain name.
    :type domain: str
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def delete_video_privacy_domain(request: web.Request, domain, video_id) -> web.Response:
    """Restrict a video from being embedded on a domain

    

    :param domain: The domain name.
    :type domain: str
    :param video_id: The ID of the video.
    :type video_id: 

    """
    return web.Response(status=200)


async def get_video_privacy_domains(request: web.Request, video_id, page=None, per_page=None) -> web.Response:
    """Get all the domains on which a video can be embedded

    

    :param video_id: The ID of the video.
    :type video_id: 
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 

    """
    return web.Response(status=200)
