from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_user_for_team_request import AddUserForTeamRequest
from openapi_server.models.delete_attachment200_response import DeleteAttachment200Response
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_team_membership200_response import GetTeamMembership200Response
from openapi_server.models.get_teams_for_user200_response import GetTeamsForUser200Response
from openapi_server.models.remove_user_for_team_request import RemoveUserForTeamRequest
from openapi_server.models.update_team200_response import UpdateTeam200Response
from openapi_server.models.update_team_request import UpdateTeamRequest
from openapi_server import util


async def add_user_for_team(request: web.Request, team_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Add a user to a team

    The user making this call must be a member of the team in order to add others. The user being added must exist in the same organization as the team.  Returns the complete team membership record for the newly added user.

    :param team_gid: Globally unique identifier for the team.
    :type team_gid: str
    :param body: The user to add to the team.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = AddUserForTeamRequest.from_dict(body)
    return web.Response(status=200)


async def create_team(request: web.Request, body, opt_pretty=None, opt_fields=None, limit=None, offset=None) -> web.Response:
    """Create a team

    Creates a team within the current workspace.

    :param body: The team to create.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]
    :param limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :type limit: int
    :param offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39;
    :type offset: str

    """
    body = UpdateTeamRequest.from_dict(body)
    return web.Response(status=200)


async def get_team(request: web.Request, team_gid, opt_pretty=None, opt_fields=None, limit=None, offset=None) -> web.Response:
    """Get a team

    Returns the full record for a single team.

    :param team_gid: Globally unique identifier for the team.
    :type team_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]
    :param limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :type limit: int
    :param offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39;
    :type offset: str

    """
    return web.Response(status=200)


async def get_teams_for_user(request: web.Request, user_gid, organization, opt_pretty=None, opt_fields=None, limit=None, offset=None) -> web.Response:
    """Get teams for a user

    Returns the compact records for all teams to which the given user is assigned.

    :param user_gid: A string identifying a user. This can either be the string \&quot;me\&quot;, an email, or the gid of a user.
    :type user_gid: str
    :param organization: The workspace or organization to filter teams on.
    :type organization: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]
    :param limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :type limit: int
    :param offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39;
    :type offset: str

    """
    return web.Response(status=200)


async def get_teams_for_workspace(request: web.Request, workspace_gid, opt_pretty=None, opt_fields=None, limit=None, offset=None) -> web.Response:
    """Get teams in a workspace

    Returns the compact records for all teams in the workspace visible to the authorized user.

    :param workspace_gid: Globally unique identifier for the workspace or organization.
    :type workspace_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]
    :param limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :type limit: int
    :param offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39;
    :type offset: str

    """
    return web.Response(status=200)


async def remove_user_for_team(request: web.Request, team_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Remove a user from a team

    The user making this call must be a member of the team in order to remove themselves or others.

    :param team_gid: Globally unique identifier for the team.
    :type team_gid: str
    :param body: The user to remove from the team.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = RemoveUserForTeamRequest.from_dict(body)
    return web.Response(status=200)


async def update_team(request: web.Request, body, opt_pretty=None, opt_fields=None, limit=None, offset=None) -> web.Response:
    """Update a team

    Updates a team within the current workspace.

    :param body: The team to update.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]
    :param limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :type limit: int
    :param offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39;
    :type offset: str

    """
    body = UpdateTeamRequest.from_dict(body)
    return web.Response(status=200)
