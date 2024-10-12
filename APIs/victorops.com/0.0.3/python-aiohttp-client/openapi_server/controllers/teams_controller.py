from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_team_member_payload import AddTeamMemberPayload
from openapi_server.models.add_team_payload import AddTeamPayload
from openapi_server.models.escalation_policy_list import EscalationPolicyList
from openapi_server.models.list_team_members_response import ListTeamMembersResponse
from openapi_server.models.remove_team_member_payload import RemoveTeamMemberPayload
from openapi_server.models.team_admins_response import TeamAdminsResponse
from openapi_server.models.team_detail import TeamDetail
from openapi_server import util


async def api_public_v1_team_get(request: web.Request, x_vo_api_id, x_vo_api_key) -> web.Response:
    """List teams

    Get a list of teams for your organization.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str

    """
    return web.Response(status=200)


async def api_public_v1_team_post(request: web.Request, x_vo_api_id, x_vo_api_key, body) -> web.Response:
    """Add a team

    Add a team to your organization.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param body: The team information
    :type body: dict | bytes

    """
    body = AddTeamPayload.from_dict(body)
    return web.Response(status=200)


async def api_public_v1_team_team_admins_get(request: web.Request, x_vo_api_id, x_vo_api_key, team) -> web.Response:
    """Retrieve a list of team admins for a team

    Get the team admins for the specified team.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param team: The VictorOps team
    :type team: str

    """
    return web.Response(status=200)


async def api_public_v1_team_team_delete(request: web.Request, x_vo_api_id, x_vo_api_key, team) -> web.Response:
    """Remove a team

    Remove a team from your organization.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param team: The VictorOps team to be deleted
    :type team: str

    """
    return web.Response(status=200)


async def api_public_v1_team_team_get(request: web.Request, x_vo_api_id, x_vo_api_key, team) -> web.Response:
    """Retrieve information for a team

    Get the information for the specified team.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param team: The VictorOps team to fetch
    :type team: str

    """
    return web.Response(status=200)


async def api_public_v1_team_team_members_get(request: web.Request, x_vo_api_id, x_vo_api_key, team) -> web.Response:
    """Retrieve a list of members for a team

    Get the members for the specified team.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param team: The VictorOps team to fetch
    :type team: str

    """
    return web.Response(status=200)


async def api_public_v1_team_team_members_post(request: web.Request, x_vo_api_id, x_vo_api_key, team, body) -> web.Response:
    """Add a team member

    Add a team member to your team.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param team: The VictorOps team to fetch
    :type team: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddTeamMemberPayload.from_dict(body)
    return web.Response(status=200)


async def api_public_v1_team_team_members_user_delete(request: web.Request, x_vo_api_id, x_vo_api_key, team, user, body) -> web.Response:
    """Remove a team member

    Remove a team from your organization.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param team: The VictorOps team to be deleted
    :type team: str
    :param user: The team member username
    :type user: str
    :param body: The user information
    :type body: dict | bytes

    """
    body = RemoveTeamMemberPayload.from_dict(body)
    return web.Response(status=200)


async def api_public_v1_team_team_policies_get_0(request: web.Request, x_vo_api_id, x_vo_api_key, team) -> web.Response:
    """Retrieve a list of escalation policies for a team

    Get the escalation policies for the specified team.  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param team: The VictorOps team to fetch
    :type team: str

    """
    return web.Response(status=200)


async def api_public_v1_team_team_put(request: web.Request, x_vo_api_id, x_vo_api_key, team, body) -> web.Response:
    """Update a team

    Update the designated team  This API may be called a maximum of 60 times per minute. 

    :param x_vo_api_id: Your API ID
    :type x_vo_api_id: str
    :param x_vo_api_key: Your API Key
    :type x_vo_api_key: str
    :param team: The VictorOps team to be updated
    :type team: str
    :param body: The team information
    :type body: dict | bytes

    """
    body = AddTeamPayload.from_dict(body)
    return web.Response(status=200)
