from typing import List, Dict
from aiohttp import web

from openapi_server.models.delete_attachment200_response import DeleteAttachment200Response
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_project_brief200_response import GetProjectBrief200Response
from openapi_server.models.update_project_brief_request import UpdateProjectBriefRequest
from openapi_server import util


async def create_project_brief(request: web.Request, project_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Create a project brief

    Creates a new project brief.  Returns the full record of the newly created project brief.

    :param project_gid: Globally unique identifier for the project.
    :type project_gid: str
    :param body: The project brief to create.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = UpdateProjectBriefRequest.from_dict(body)
    return web.Response(status=200)


async def delete_project_brief(request: web.Request, project_brief_gid, opt_pretty=None, opt_fields=None) -> web.Response:
    """Delete a project brief

    Deletes a specific, existing project brief.  Returns an empty data record.

    :param project_brief_gid: Globally unique identifier for the project brief.
    :type project_brief_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    return web.Response(status=200)


async def get_project_brief(request: web.Request, project_brief_gid, opt_pretty=None, opt_fields=None) -> web.Response:
    """Get a project brief

    Get the full record for a project brief.

    :param project_brief_gid: Globally unique identifier for the project brief.
    :type project_brief_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    return web.Response(status=200)


async def update_project_brief(request: web.Request, project_brief_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Update a project brief

    An existing project brief can be updated by making a PUT request on the URL for that project brief. Only the fields provided in the &#x60;data&#x60; block will be updated; any unspecified fields will remain unchanged.  Returns the complete updated project brief record.

    :param project_brief_gid: Globally unique identifier for the project brief.
    :type project_brief_gid: str
    :param body: The updated fields for the project brief.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = UpdateProjectBriefRequest.from_dict(body)
    return web.Response(status=200)
