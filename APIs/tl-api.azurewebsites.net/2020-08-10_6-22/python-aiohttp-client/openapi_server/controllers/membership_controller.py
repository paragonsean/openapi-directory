from typing import List, Dict
from aiohttp import web

from openapi_server.models.member_dto import MemberDTO
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def membership_get(request: web.Request, ) -> web.Response:
    """Get all of the members details This will return all properties related to member entity             

    


    """
    return web.Response(status=200)


async def membership_post(request: web.Request, body) -> web.Response:
    """Add new Member             

    

    :param body: member object
    :type body: dict | bytes

    """
    body = MemberDTO.from_dict(body)
    return web.Response(status=200)
