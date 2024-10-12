from typing import List, Dict
from aiohttp import web

from openapi_server.models.image_by_name_info import ImageByNameInfo
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def get_general_image(request: web.Request, name, type) -> web.Response:
    """Get General Image.

    

    :param name: The name of the image.
    :type name: str
    :param type: Image Type (primary, backdrop, logo, etc).
    :type type: str

    """
    return web.Response(status=200)


async def get_general_images(request: web.Request, ) -> web.Response:
    """Get all general images.

    


    """
    return web.Response(status=200)


async def get_media_info_image(request: web.Request, theme, name) -> web.Response:
    """Get media info image.

    

    :param theme: The theme to get the image from.
    :type theme: str
    :param name: The name of the image.
    :type name: str

    """
    return web.Response(status=200)


async def get_media_info_images(request: web.Request, ) -> web.Response:
    """Get all media info images.

    


    """
    return web.Response(status=200)


async def get_rating_image(request: web.Request, theme, name) -> web.Response:
    """Get rating image.

    

    :param theme: The theme to get the image from.
    :type theme: str
    :param name: The name of the image.
    :type name: str

    """
    return web.Response(status=200)


async def get_rating_images(request: web.Request, ) -> web.Response:
    """Get all general images.

    


    """
    return web.Response(status=200)
