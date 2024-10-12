from typing import List, Dict
from aiohttp import web

from openapi_server.models.automatic_invitations_list_vo import AutomaticInvitationsListVO
from openapi_server.models.http_status_vo import HTTPStatusVO
from openapi_server.models.profile_image_vo import ProfileImageVO
from openapi_server.models.team_template_expand_vo import TeamTemplateExpandVO
from openapi_server.models.team_template_list_vo import TeamTemplateListVO
from openapi_server import util


async def get_automatic_invitation_list(request: web.Request, workgroup_id) -> web.Response:
    """List current user&#39;s automatic invitations info 

    List current user&#39;s automatic invitations info 

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def get_team_template_detail(request: web.Request, workgroup_id, team_template_id) -> web.Response:
    """Get current user&#39;s team template detal info 

    Get current user&#39;s team template detal info 

    :param workgroup_id: 
    :type workgroup_id: str
    :param team_template_id: 
    :type team_template_id: str

    """
    return web.Response(status=200)


async def get_team_template_list(request: web.Request, workgroup_id) -> web.Response:
    """List current user&#39;s team templates info 

    List current user&#39;s team templates info 

    :param workgroup_id: 
    :type workgroup_id: str

    """
    return web.Response(status=200)


async def upload_profile_image(request: web.Request, workgroup_id, body=None) -> web.Response:
    """Upload Profile Image.  A multipart/form-data request with a name \&quot;file\&quot;

    Upload Profile Image.  A multipart/form-data request with a name \&quot;file\&quot;

    :param workgroup_id: 
    :type workgroup_id: str
    :param body: 
    :type body: str

    """
    return web.Response(status=200)
