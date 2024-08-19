from typing import List, Dict
from aiohttp import web

from openapi_server.models.membership import Membership
from openapi_server.models.membership_list import MembershipList
from openapi_server.models.team import Team
from openapi_server.models.team_list import TeamList
from openapi_server.models.teams_create_membership_request import TeamsCreateMembershipRequest
from openapi_server.models.teams_create_request import TeamsCreateRequest
from openapi_server.models.teams_update_membership_roles_request import TeamsUpdateMembershipRolesRequest
from openapi_server.models.teams_update_membership_status_request import TeamsUpdateMembershipStatusRequest
from openapi_server.models.teams_update_request import TeamsUpdateRequest
from openapi_server import util


async def teams_create(request: web.Request, body=None) -> web.Response:
    """Create Team

    Create a new team. The user who creates the team will automatically be assigned as the owner of the team. The team owner can invite new members, who will be able add new owners and update or delete the team from your project.

    :param body: 
    :type body: dict | bytes

    """
    body = TeamsCreateRequest.from_dict(body)
    return web.Response(status=200)


async def teams_create_membership(request: web.Request, team_id, body=None) -> web.Response:
    """Create Team Membership

    Use this endpoint to invite a new member to join your team. If initiated from Client SDK, an email with a link to join the team will be sent to the new member&#39;s email address if the member doesn&#39;t exist in the project it will be created automatically. If initiated from server side SDKs, new member will automatically be added to the team.  Use the &#39;URL&#39; parameter to redirect the user from the invitation email back to your app. When the user is redirected, use the [Update Team Membership Status](/docs/client/teams#teamsUpdateMembershipStatus) endpoint to allow the user to accept the invitation to the team.  While calling from side SDKs the redirect url can be empty string.  Please note that in order to avoid a [Redirect Attacks](https://github.com/OWASP/CheatSheetSeries/blob/master/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.md) the only valid redirect URL&#39;s are the once from domains you have set when added your platforms in the console interface.

    :param team_id: Team unique ID.
    :type team_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsCreateMembershipRequest.from_dict(body)
    return web.Response(status=200)


async def teams_delete(request: web.Request, team_id) -> web.Response:
    """Delete Team

    Delete a team by its unique ID. Only team owners have write access for this resource.

    :param team_id: Team unique ID.
    :type team_id: str

    """
    return web.Response(status=200)


async def teams_delete_membership(request: web.Request, team_id, membership_id) -> web.Response:
    """Delete Team Membership

    This endpoint allows a user to leave a team or for a team owner to delete the membership of any other team member. You can also use this endpoint to delete a user membership even if it is not accepted.

    :param team_id: Team unique ID.
    :type team_id: str
    :param membership_id: Membership ID.
    :type membership_id: str

    """
    return web.Response(status=200)


async def teams_get(request: web.Request, team_id) -> web.Response:
    """Get Team

    Get a team by its unique ID. All team members have read access for this resource.

    :param team_id: Team unique ID.
    :type team_id: str

    """
    return web.Response(status=200)


async def teams_get_memberships(request: web.Request, team_id, search=None, limit=None, offset=None, order_type=None) -> web.Response:
    """Get Team Memberships

    Get a team members by the team unique ID. All team members have read access for this list of resources.

    :param team_id: Team unique ID.
    :type team_id: str
    :param search: Search term to filter your list results. Max length: 256 chars.
    :type search: str
    :param limit: Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
    :type limit: int
    :param offset: Results offset. The default value is 0. Use this param to manage pagination.
    :type offset: int
    :param order_type: Order result by ASC or DESC order.
    :type order_type: str

    """
    return web.Response(status=200)


async def teams_list(request: web.Request, search=None, limit=None, offset=None, order_type=None) -> web.Response:
    """List Teams

    Get a list of all the current user teams. You can use the query params to filter your results. On admin mode, this endpoint will return a list of all of the project&#39;s teams. [Learn more about different API modes](/docs/admin).

    :param search: Search term to filter your list results. Max length: 256 chars.
    :type search: str
    :param limit: Results limit value. By default will return maximum 25 results. Maximum of 100 results allowed per request.
    :type limit: int
    :param offset: Results offset. The default value is 0. Use this param to manage pagination.
    :type offset: int
    :param order_type: Order result by ASC or DESC order.
    :type order_type: str

    """
    return web.Response(status=200)


async def teams_update(request: web.Request, team_id, body=None) -> web.Response:
    """Update Team

    Update a team by its unique ID. Only team owners have write access for this resource.

    :param team_id: Team unique ID.
    :type team_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsUpdateRequest.from_dict(body)
    return web.Response(status=200)


async def teams_update_membership_roles(request: web.Request, team_id, membership_id, body=None) -> web.Response:
    """Update Membership Roles

    

    :param team_id: Team unique ID.
    :type team_id: str
    :param membership_id: Membership ID.
    :type membership_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsUpdateMembershipRolesRequest.from_dict(body)
    return web.Response(status=200)


async def teams_update_membership_status(request: web.Request, team_id, membership_id, body=None) -> web.Response:
    """Update Team Membership Status

    Use this endpoint to allow a user to accept an invitation to join a team after being redirected back to your app from the invitation email recieved by the user.

    :param team_id: Team unique ID.
    :type team_id: str
    :param membership_id: Membership ID.
    :type membership_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = TeamsUpdateMembershipStatusRequest.from_dict(body)
    return web.Response(status=200)
