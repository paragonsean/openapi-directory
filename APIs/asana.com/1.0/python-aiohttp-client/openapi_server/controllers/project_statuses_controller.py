from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_project_status_for_project_request import CreateProjectStatusForProjectRequest
from openapi_server.models.delete_attachment200_response import DeleteAttachment200Response
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_project_status200_response import GetProjectStatus200Response
from openapi_server.models.get_project_statuses_for_project200_response import GetProjectStatusesForProject200Response
from openapi_server import util


async def create_project_status_for_project(request: web.Request, project_gid, body, opt_pretty=None, opt_fields=None) -> web.Response:
    """Create a project status

    *Deprecated: new integrations should prefer the &#x60;/status_updates&#x60; route.*  Creates a new status update on the project.  Returns the full record of the newly created project status update.

    :param project_gid: Globally unique identifier for the project.
    :type project_gid: str
    :param body: The project status to create.
    :type body: dict | bytes
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    body = CreateProjectStatusForProjectRequest.from_dict(body)
    return web.Response(status=200)


async def delete_project_status(request: web.Request, project_status_gid, opt_pretty=None, opt_fields=None) -> web.Response:
    """Delete a project status

    *Deprecated: new integrations should prefer the &#x60;/status_updates/{status_gid}&#x60; route.*  Deletes a specific, existing project status update.  Returns an empty data record.

    :param project_status_gid: The project status update to get.
    :type project_status_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    return web.Response(status=200)


async def get_project_status(request: web.Request, project_status_gid, opt_pretty=None, opt_fields=None) -> web.Response:
    """Get a project status

    *Deprecated: new integrations should prefer the &#x60;/status_updates/{status_gid}&#x60; route.*  Returns the complete record for a single status update.

    :param project_status_gid: The project status update to get.
    :type project_status_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    return web.Response(status=200)


async def get_project_statuses_for_project(request: web.Request, project_gid, opt_pretty=None, opt_fields=None, limit=None, offset=None) -> web.Response:
    """Get statuses from a project

    *Deprecated: new integrations should prefer the &#x60;/status_updates&#x60; route.*  Returns the compact project status update records for all updates on the project.

    :param project_gid: Globally unique identifier for the project.
    :type project_gid: str
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
