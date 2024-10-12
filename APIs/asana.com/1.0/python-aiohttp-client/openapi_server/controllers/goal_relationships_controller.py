from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_supporting_relationship_request import AddSupportingRelationshipRequest
from openapi_server.models.delete_attachment200_response import DeleteAttachment200Response
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_goal_relationship200_response import GetGoalRelationship200Response
from openapi_server.models.get_goal_relationships200_response import GetGoalRelationships200Response
from openapi_server.models.remove_supporting_relationship_request import RemoveSupportingRelationshipRequest
from openapi_server.models.update_goal_relationship_request import UpdateGoalRelationshipRequest
from openapi_server import util


async def add_supporting_relationship(request: web.Request, goal_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Add a supporting goal relationship

    Creates a goal relationship by adding a supporting resource to a given goal.  Returns the newly created goal relationship record.

    :param goal_gid: Globally unique identifier for the goal.
    :type goal_gid: str
    :param body: The supporting resource to be added to the goal
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = AddSupportingRelationshipRequest.from_dict(body)
    return web.Response(status=200)


async def get_goal_relationship(request: web.Request, goal_relationship_gid, opt_pretty=None, opt_fields=None) -> web.Response:
    """Get a goal relationship

    Returns the complete updated goal relationship record for a single goal relationship.

    :param goal_relationship_gid: Globally unique identifier for the goal relationship.
    :type goal_relationship_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    return web.Response(status=200)


async def get_goal_relationships(request: web.Request, supported_goal, opt_pretty=None, opt_fields=None, resource_subtype=None) -> web.Response:
    """Get goal relationships

    Returns compact goal relationship records.

    :param supported_goal: Globally unique identifier for the supported goal in the goal relationship.
    :type supported_goal: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]
    :param resource_subtype: If provided, filter to goal relationships with a given resource_subtype.
    :type resource_subtype: str

    """
    return web.Response(status=200)


async def remove_supporting_relationship(request: web.Request, goal_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Removes a supporting goal relationship

    Removes a goal relationship for a given parent goal.

    :param goal_gid: Globally unique identifier for the goal.
    :type goal_gid: str
    :param body: The supporting resource to be removed from the goal
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = RemoveSupportingRelationshipRequest.from_dict(body)
    return web.Response(status=200)


async def update_goal_relationship(request: web.Request, goal_relationship_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Update a goal relationship

    An existing goal relationship can be updated by making a PUT request on the URL for that goal relationship. Only the fields provided in the &#x60;data&#x60; block will be updated; any unspecified fields will remain unchanged.  Returns the complete updated goal relationship record.

    :param goal_relationship_gid: Globally unique identifier for the goal relationship.
    :type goal_relationship_gid: str
    :param body: The updated fields for the goal relationship.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = UpdateGoalRelationshipRequest.from_dict(body)
    return web.Response(status=200)
