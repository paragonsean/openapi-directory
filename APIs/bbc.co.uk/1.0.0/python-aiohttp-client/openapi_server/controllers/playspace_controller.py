from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.playspace_container import PlayspaceContainer
from openapi_server import util


async def get_container(request: web.Request, authorization, x_api_key, id) -> web.Response:
    """Playspace Container by ID

    Playspace Container by ID 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param id: Playspace Container ID
    :type id: str

    """
    return web.Response(status=200)


async def suggest_container(request: web.Request, authorization, x_api_key, previous_pid, previous_container=None) -> web.Response:
    """Suggested Playspace Container

    Suggested Playspace Container 

    :param authorization: Bearer OAUTH_TOKEN
    :type authorization: str
    :param x_api_key: API_KEY
    :type x_api_key: str
    :param previous_pid: Clip or Episode PID of the previous or first content item in the Playspace stream.
    :type previous_pid: str
    :param previous_container: Container ID of the previous container in the Playspace stream.
    :type previous_container: str

    """
    return web.Response(status=200)
