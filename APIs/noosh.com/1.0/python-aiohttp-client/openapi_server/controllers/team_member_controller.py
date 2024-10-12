from typing import List, Dict
from aiohttp import web

from openapi_server.models.contact_user_vo import ContactUserVO
from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.team_member_base_inf_vo import TeamMemberBaseInfVO
from openapi_server.models.team_member_list_vo import TeamMemberListVO
from openapi_server.models.team_member_po import TeamMemberPO
from openapi_server.models.v1x1_invited_team_member_results_vo import V1x1InvitedTeamMemberResultsVO
from openapi_server import util


async def delete_team_member_of_project(request: web.Request, workgroup_id, project_id, teammember_id) -> web.Response:
    """Delete a team member for the specific project.

    Delete a team member for the specific project.

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param teammember_id: 
    :type teammember_id: str

    """
    return web.Response(status=200)


async def get_team_member_list_of_client_project(request: web.Request, workgroup_id, project_id) -> web.Response:
    """List team member of client project side.

    List team member of client project side.

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def get_team_member_list_of_project(request: web.Request, workgroup_id, project_id) -> web.Response:
    """List team member of project.

    List team member of project.

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str

    """
    return web.Response(status=200)


async def post_team_member_of_project(request: web.Request, workgroup_id, project_id, body=None) -> web.Response:
    """Invite a team member or all the members of team template for the specific project.

    Invite a team member or all the members of team template for the specific project.

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TeamMemberPO.from_dict(body)
    return web.Response(status=200)


async def v1_workgroups_workgroup_id_projects_project_id_teammembers_post(request: web.Request, workgroup_id, project_id, body=None) -> web.Response:
    """Deprecated, please use 1.1 Version

    Deprecated, please use 1.1 Version

    :param workgroup_id: 
    :type workgroup_id: str
    :param project_id: 
    :type project_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = ContactUserVO.from_dict(body)
    return web.Response(status=200)
