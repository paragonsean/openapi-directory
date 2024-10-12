from typing import List, Dict
from aiohttp import web

from openapi_server.models.bulk_create_team_members_request import BulkCreateTeamMembersRequest
from openapi_server.models.bulk_create_team_members_response import BulkCreateTeamMembersResponse
from openapi_server.models.bulk_update_team_members_request import BulkUpdateTeamMembersRequest
from openapi_server.models.bulk_update_team_members_response import BulkUpdateTeamMembersResponse
from openapi_server.models.create_team_member_request import CreateTeamMemberRequest
from openapi_server.models.create_team_member_response import CreateTeamMemberResponse
from openapi_server.models.retrieve_team_member_response import RetrieveTeamMemberResponse
from openapi_server.models.retrieve_wage_setting_response import RetrieveWageSettingResponse
from openapi_server.models.search_team_members_request import SearchTeamMembersRequest
from openapi_server.models.search_team_members_response import SearchTeamMembersResponse
from openapi_server.models.update_team_member_request import UpdateTeamMemberRequest
from openapi_server.models.update_team_member_response import UpdateTeamMemberResponse
from openapi_server.models.update_wage_setting_request import UpdateWageSettingRequest
from openapi_server.models.update_wage_setting_response import UpdateWageSettingResponse
from openapi_server import util


async def bulk_create_team_members(request: web.Request, body) -> web.Response:
    """BulkCreateTeamMembers

    Creates multiple &#x60;TeamMember&#x60; objects. The created &#x60;TeamMember&#x60; objects are returned on successful creates. This process is non-transactional and processes as much of the request as possible. If one of the creates in the request cannot be successfully processed, the request is not marked as failed, but the body of the response contains explicit error information for the failed create.  Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#bulk-create-team-members).

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = BulkCreateTeamMembersRequest.from_dict(body)
    return web.Response(status=200)


async def bulk_update_team_members(request: web.Request, body) -> web.Response:
    """BulkUpdateTeamMembers

    Updates multiple &#x60;TeamMember&#x60; objects. The updated &#x60;TeamMember&#x60; objects are returned on successful updates. This process is non-transactional and processes as much of the request as possible. If one of the updates in the request cannot be successfully processed, the request is not marked as failed, but the body of the response contains explicit error information for the failed update. Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#bulk-update-team-members).

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = BulkUpdateTeamMembersRequest.from_dict(body)
    return web.Response(status=200)


async def create_team_member(request: web.Request, body) -> web.Response:
    """CreateTeamMember

    Creates a single &#x60;TeamMember&#x60; object. The &#x60;TeamMember&#x60; object is returned on successful creates. You must provide the following values in your request to this endpoint: - &#x60;given_name&#x60; - &#x60;family_name&#x60;  Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#createteammember).

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateTeamMemberRequest.from_dict(body)
    return web.Response(status=200)


async def retrieve_team_member(request: web.Request, team_member_id) -> web.Response:
    """RetrieveTeamMember

    Retrieves a &#x60;TeamMember&#x60; object for the given &#x60;TeamMember.id&#x60;. Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#retrieve-a-team-member).

    :param team_member_id: The ID of the team member to retrieve.
    :type team_member_id: str

    """
    return web.Response(status=200)


async def retrieve_wage_setting(request: web.Request, team_member_id) -> web.Response:
    """RetrieveWageSetting

    Retrieves a &#x60;WageSetting&#x60; object for a team member specified by &#x60;TeamMember.id&#x60;. Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#retrievewagesetting).

    :param team_member_id: The ID of the team member for which to retrieve the wage setting.
    :type team_member_id: str

    """
    return web.Response(status=200)


async def search_team_members(request: web.Request, body) -> web.Response:
    """SearchTeamMembers

    Returns a paginated list of &#x60;TeamMember&#x60; objects for a business. The list can be filtered by the following: - location IDs - &#x60;status&#x60;

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = SearchTeamMembersRequest.from_dict(body)
    return web.Response(status=200)


async def update_team_member(request: web.Request, team_member_id, body) -> web.Response:
    """UpdateTeamMember

    Updates a single &#x60;TeamMember&#x60; object. The &#x60;TeamMember&#x60; object is returned on successful updates. Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#update-a-team-member).

    :param team_member_id: The ID of the team member to update.
    :type team_member_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = UpdateTeamMemberRequest.from_dict(body)
    return web.Response(status=200)


async def update_wage_setting(request: web.Request, team_member_id, body) -> web.Response:
    """UpdateWageSetting

    Creates or updates a &#x60;WageSetting&#x60; object. The object is created if a &#x60;WageSetting&#x60; with the specified &#x60;team_member_id&#x60; does not exist. Otherwise, it fully replaces the &#x60;WageSetting&#x60; object for the team member. The &#x60;WageSetting&#x60; is returned on a successful update. Learn about [Troubleshooting the Team API](https://developer.squareup.com/docs/team/troubleshooting#create-or-update-a-wage-setting).

    :param team_member_id: The ID of the team member for which to update the &#x60;WageSetting&#x60; object.
    :type team_member_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = UpdateWageSettingRequest.from_dict(body)
    return web.Response(status=200)
