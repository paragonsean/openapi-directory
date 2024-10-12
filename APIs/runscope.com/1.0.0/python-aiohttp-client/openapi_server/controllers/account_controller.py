from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.account_get200_response import AccountGet200Response
from openapi_server.models.agent import Agent
from openapi_server.models.error import Error
from openapi_server.models.teams_team_id_integrations_get200_response import TeamsTeamIdIntegrationsGet200Response
from openapi_server import util


async def account_get(request: web.Request, ) -> web.Response:
    """Account Resource

    Information about the authorized account.


    """
    return web.Response(status=200)


async def teams_team_id_agents_get(request: web.Request, team_id) -> web.Response:
    """Team agents list

    List currently connected agents associated with a given team.

    :param team_id: Unique identifier for team
    :type team_id: str

    """
    return web.Response(status=200)


async def teams_team_id_integrations_get(request: web.Request, team_id) -> web.Response:
    """Team integrations list

    Returns a list of integrations configured for the team.

    :param team_id: Unique identifier for team
    :type team_id: str

    """
    return web.Response(status=200)


async def teams_team_id_people_get(request: web.Request, team_id) -> web.Response:
    """Teams Resource

    List people and integrations associated with a given team.

    :param team_id: Unique identifier for team
    :type team_id: str

    """
    return web.Response(status=200)
