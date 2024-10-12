from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_group_request_body import CreateGroupRequestBody
from openapi_server.models.group_admin_request_body import GroupAdminRequestBody
from openapi_server.models.group_invite_response import GroupInviteResponse
from openapi_server.models.group_response import GroupResponse
from openapi_server.models.groups_response import GroupsResponse
from openapi_server.models.remove_group_participant_request_body import RemoveGroupParticipantRequestBody
from openapi_server.models.update_group_info_request_body import UpdateGroupInfoRequestBody
from openapi_server import util


async def create_group(request: web.Request, body) -> web.Response:
    """Create-Group

    

    :param body: 
    :type body: dict | bytes

    """
    body = CreateGroupRequestBody.from_dict(body)
    return web.Response(status=200)


async def delete_group_icon(request: web.Request, group_id, file) -> web.Response:
    """Delete-Group-Icon

    

    :param group_id: 
    :type group_id: str
    :param file: 
    :type file: str

    """
    return web.Response(status=200)


async def delete_group_invite(request: web.Request, group_id) -> web.Response:
    """Delete-Group-Invite

    

    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def demote_group_admin(request: web.Request, group_id, body) -> web.Response:
    """Demote-Group-Admin

    

    :param group_id: 
    :type group_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GroupAdminRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_all_groups(request: web.Request, ) -> web.Response:
    """Get-All-Groups

    


    """
    return web.Response(status=200)


async def get_group_icon_binary(request: web.Request, group_id) -> web.Response:
    """Get-Group-Icon-Binary

    

    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def get_group_info(request: web.Request, group_id) -> web.Response:
    """Get-Group-Info

    

    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def get_group_invite(request: web.Request, group_id) -> web.Response:
    """Get-Group-Invite

    

    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def leave_group(request: web.Request, group_id) -> web.Response:
    """Leave-Group

    

    :param group_id: 
    :type group_id: str

    """
    return web.Response(status=200)


async def promote_to_group_admin(request: web.Request, group_id, body) -> web.Response:
    """Promote-To-Group-Admin

    

    :param group_id: 
    :type group_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = GroupAdminRequestBody.from_dict(body)
    return web.Response(status=200)


async def remove_group_participant(request: web.Request, group_id, body) -> web.Response:
    """Remove-Group-Participant

    

    :param group_id: 
    :type group_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = RemoveGroupParticipantRequestBody.from_dict(body)
    return web.Response(status=200)


async def set_group_icon(request: web.Request, group_id, file) -> web.Response:
    """Set-Group-Icon

    

    :param group_id: 
    :type group_id: str
    :param file: 
    :type file: str

    """
    return web.Response(status=200)


async def update_group_info(request: web.Request, group_id, body) -> web.Response:
    """Update-Group-Info

    

    :param group_id: 
    :type group_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateGroupInfoRequestBody.from_dict(body)
    return web.Response(status=200)
