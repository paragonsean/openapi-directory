from typing import List, Dict
from aiohttp import web

from openapi_server.models.profile_image import ProfileImage
from openapi_server import util


async def get_profile_image(request: web.Request, username) -> web.Response:
    """A Users or organizations profile image

    This endpoint allows the client to retrieve a user or organization profile image information by its         corresponding username.

    :param username: The parameter is the username of the user or the username of the organization.
    :type username: str

    """
    return web.Response(status=200)
