from typing import List, Dict
from aiohttp import web

from openapi_server.models.company_team_repository_v1_create_post_request import CompanyTeamRepositoryV1CreatePostRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def company_team_repository_v1_create_post(request: web.Request, company_id, body=None) -> web.Response:
    """team/{companyId}

    Create a team in the company structure.

    :param company_id: 
    :type company_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = CompanyTeamRepositoryV1CreatePostRequest.from_dict(body)
    return web.Response(status=200)
