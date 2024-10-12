from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.experience_response import ExperienceResponse
from openapi_server import util


async def get_experience_homepage(request: web.Request, x_api_key) -> web.Response:
    """Homepage Experience

    Homepage Experience 

    :param x_api_key: API_KEY
    :type x_api_key: str

    """
    return web.Response(status=200)
