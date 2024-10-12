from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_response import ApiResponse
from openapi_server.models.default_response_dtoof_gym_dto import DefaultResponseDTOOfGymDTO
from openapi_server import util


async def gym_get(request: web.Request, gym_id) -> web.Response:
    """Get gym details This will return all properties related to gym entity             

    

    :param gym_id: indentity number (primary key) for gym object
    :type gym_id: int

    """
    return web.Response(status=200)
