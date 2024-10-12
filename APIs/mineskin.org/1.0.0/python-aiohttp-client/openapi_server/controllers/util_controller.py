from typing import List, Dict
from aiohttp import web

from openapi_server.models.user_validation import UserValidation
from openapi_server import util


async def validate_name_name_get(request: web.Request, name, user_agent) -> web.Response:
    """validate_name_name_get

    

    :param name: 
    :type name: str
    :param user_agent: Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
    :type user_agent: str

    """
    return web.Response(status=200)


async def validate_uuid_uuid_get(request: web.Request, uuid, user_agent) -> web.Response:
    """validate_uuid_uuid_get

    

    :param uuid: 
    :type uuid: str
    :param user_agent: Custom User-Agent for your application, see [user-agent.dev](https://user-agent.dev/) for implementation examples
    :type user_agent: str

    """
    return web.Response(status=200)
