from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_followers_request import AddFollowersRequest
from openapi_server.models.create_goal201_response import CreateGoal201Response
from openapi_server.models.create_goal_metric_request import CreateGoalMetricRequest
from openapi_server.models.create_goal_request import CreateGoalRequest
from openapi_server.models.delete_attachment200_response import DeleteAttachment200Response
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_goals200_response import GetGoals200Response
from openapi_server.models.update_goal_metric_request import UpdateGoalMetricRequest
from openapi_server import util


async def add_followers(request: web.Request, goal_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Add a collaborator to a goal

    Adds followers to a goal. Returns the goal the followers were added to. Each goal can be associated with zero or more followers in the system. Requests to add/remove followers, if successful, will return the complete updated goal record, described above.

    :param goal_gid: Globally unique identifier for the goal.
    :type goal_gid: str
    :param body: The followers to be added as collaborators
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = AddFollowersRequest.from_dict(body)
    return web.Response(status=200)


async def create_goal(request: web.Request, body, opt_pretty=None, opt_fields=None, limit=None, offset=None) -> web.Response:
    """Create a goal

    Creates a new goal in a workspace or team.  Returns the full record of the newly created goal.

    :param body: The goal to create.
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
    body = CreateGoalRequest.from_dict(body)
    return web.Response(status=200)


async def create_goal_metric(request: web.Request, goal_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Create a goal metric

    Creates and adds a goal metric to a specified goal. Note that this replaces an existing goal metric if one already exists.

    :param goal_gid: Globally unique identifier for the goal.
    :type goal_gid: str
    :param body: The goal metric to create.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = CreateGoalMetricRequest.from_dict(body)
    return web.Response(status=200)


async def delete_goal(request: web.Request, goal_gid, opt_pretty=None, opt_fields=None) -> web.Response:
    """Delete a goal

    A specific, existing goal can be deleted by making a DELETE request on the URL for that goal.  Returns an empty data record.

    :param goal_gid: Globally unique identifier for the goal.
    :type goal_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    return web.Response(status=200)


async def get_goal(request: web.Request, goal_gid, opt_pretty=None, opt_fields=None) -> web.Response:
    """Get a goal

    Returns the complete goal record for a single goal.

    :param goal_gid: Globally unique identifier for the goal.
    :type goal_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    return web.Response(status=200)


async def get_goals(request: web.Request, opt_pretty=None, opt_fields=None, limit=None, offset=None, portfolio=None, project=None, is_workspace_level=None, team=None, workspace=None, time_periods=None) -> web.Response:
    """Get goals

    Returns compact goal records.

    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]
    :param limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :type limit: int
    :param offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39;
    :type offset: str
    :param portfolio: Globally unique identifier for supporting portfolio.
    :type portfolio: str
    :param project: Globally unique identifier for supporting project.
    :type project: str
    :param is_workspace_level: Filter to goals with is_workspace_level set to query value. Must be used with the workspace parameter.
    :type is_workspace_level: bool
    :param team: Globally unique identifier for the team.
    :type team: str
    :param workspace: Globally unique identifier for the workspace.
    :type workspace: str
    :param time_periods: Globally unique identifiers for the time periods.
    :type time_periods: List[str]

    """
    return web.Response(status=200)


async def get_parent_goals_for_goal(request: web.Request, goal_gid, opt_pretty=None, opt_fields=None) -> web.Response:
    """Get parent goals from a goal

    Returns a compact representation of all of the parent goals of a goal.

    :param goal_gid: Globally unique identifier for the goal.
    :type goal_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    return web.Response(status=200)


async def remove_followers(request: web.Request, goal_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Remove a collaborator from a goal

    Removes followers from a goal. Returns the goal the followers were removed from. Each goal can be associated with zero or more followers in the system. Requests to add/remove followers, if successful, will return the complete updated goal record, described above.

    :param goal_gid: Globally unique identifier for the goal.
    :type goal_gid: str
    :param body: The followers to be removed as collaborators
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = AddFollowersRequest.from_dict(body)
    return web.Response(status=200)


async def update_goal(request: web.Request, goal_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Update a goal

    An existing goal can be updated by making a PUT request on the URL for that goal. Only the fields provided in the &#x60;data&#x60; block will be updated; any unspecified fields will remain unchanged.  Returns the complete updated goal record.

    :param goal_gid: Globally unique identifier for the goal.
    :type goal_gid: str
    :param body: The updated fields for the goal.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = CreateGoalRequest.from_dict(body)
    return web.Response(status=200)


async def update_goal_metric(request: web.Request, goal_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Update a goal metric

    Updates a goal&#39;s existing metric&#39;s &#x60;current_number_value&#x60; if one exists, otherwise responds with a 400 status code.  Returns the complete updated goal metric record.

    :param goal_gid: Globally unique identifier for the goal.
    :type goal_gid: str
    :param body: The updated fields for the goal metric.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = UpdateGoalMetricRequest.from_dict(body)
    return web.Response(status=200)
