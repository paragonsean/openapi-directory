from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server.models.invited_user_info import InvitedUserInfo
from openapi_server.models.user_info import UserInfo
from openapi_server.models.user_invitation_info import UserInvitationInfo
from openapi_server.models.user_invitation_result import UserInvitationResult
from openapi_server.models.user_membership import UserMembership
from openapi_server.models.users_invitation import UsersInvitation
from openapi_server import util


async def teams_team_id_memberships_get(request: web.Request, team_id) -> web.Response:
    """Get all invites of a team.

    

    :param team_id: Team ID of team you want to request.
    :type team_id: str

    """
    return web.Response(status=200)


async def teams_team_id_memberships_post(request: web.Request, team_id, body=None) -> web.Response:
    """Invite users to a team

    

    :param team_id: Id of team the user should be invited to.
    :type team_id: str
    :param body: Information about user to invite and inviter id.
    :type body: dict | bytes

    """
    body = UsersInvitation.from_dict(body)
    return web.Response(status=200)


async def teams_team_id_memberships_resend_invite_mail_post(request: web.Request, team_id, body=None) -> web.Response:
    """Sends invite email again if an invite exists

    

    :param team_id: Team ID of team with invited user.
    :type team_id: str
    :param body: Information which user should be invited again.
    :type body: dict | bytes

    """
    body = UserInvitationInfo.from_dict(body)
    return web.Response(status=200)


async def teams_team_id_memberships_user_id_delete(request: web.Request, team_id, user_id, requester_user_id=None) -> web.Response:
    """Removes a user or invitation from a team, and may delete the user if he is not in any team.

    

    :param team_id: ID of the team the user should be deleted from
    :type team_id: str
    :param user_id: ID of the user that should be deleted
    :type user_id: str
    :param requester_user_id: User ID of user which will remove the other user.
    :type requester_user_id: str

    """
    return web.Response(status=200)


async def teams_team_id_memberships_user_id_put(request: web.Request, team_id, user_id, requester_user_id=None, body=None) -> web.Response:
    """Update user&#39;s team membership.

    Updates the user&#39;s team membership. You can move the user to another team within the subscription  and/or change the user&#39;s role.

    :param team_id: Team the user you want to update belongs to at the moment.
    :type team_id: str
    :param user_id: User ID of user you want to update.
    :type user_id: str
    :param requester_user_id: User ID of user which you want to change role with. This must be provided when using an api key. This user must have role administrator (for setting administrator role) or team administrator (for setting  rights.
    :type requester_user_id: str
    :param body: Information about role id and target team id.
    :type body: dict | bytes

    """
    body = UserMembership.from_dict(body)
    return web.Response(status=200)
