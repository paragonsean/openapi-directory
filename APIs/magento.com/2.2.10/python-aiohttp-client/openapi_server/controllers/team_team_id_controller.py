from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_data_team_interface import CompanyDataTeamInterface
from openapi_server.models.company_team_repository_v1_create_post_request import CompanyTeamRepositoryV1CreatePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def company_team_repository_v1_delete_by_id_delete(request: web.Request, team_id) -> web.Response:
    """team/{teamId}

    Delete a team from the company structure.

    :param team_id: 
    :type team_id: int

    """
    return web.Response(status=200)


async def company_team_repository_v1_get_get(request: web.Request, team_id) -> web.Response:
    """team/{teamId}

    Returns data for a team in the company, by entity id.

    :param team_id: 
    :type team_id: int

    """
    return web.Response(status=200)


async def company_team_repository_v1_save_put(request: web.Request, team_id, body=None) -> web.Response:
    """team/{teamId}

    Update a team in the company structure.

    :param team_id: 
    :type team_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CompanyTeamRepositoryV1CreatePostRequest.from_dict(body)
    return web.Response(status=200)
