from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_status_for_object201_response import CreateStatusForObject201Response
from openapi_server.models.create_status_for_object_request import CreateStatusForObjectRequest
from openapi_server.models.delete_attachment200_response import DeleteAttachment200Response
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.get_statuses_for_object200_response import GetStatusesForObject200Response
from openapi_server import util


async def create_status_for_object(request: web.Request, body, opt_pretty=None, opt_fields=None, limit=None, offset=None) -> web.Response:
    """Create a status update

    Creates a new status update on an object. Returns the full record of the newly created status update.

    :param body: The status update to create.
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
    body = CreateStatusForObjectRequest.from_dict(body)
    return web.Response(status=200)


async def delete_status(request: web.Request, status_gid, opt_pretty=None, opt_fields=None) -> web.Response:
    """Delete a status update

    Deletes a specific, existing status update.  Returns an empty data record.

    :param status_gid: The status update to get.
    :type status_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    return web.Response(status=200)


async def get_status(request: web.Request, status_gid, opt_pretty=None, opt_fields=None) -> web.Response:
    """Get a status update

    Returns the complete record for a single status update.

    :param status_gid: The status update to get.
    :type status_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    return web.Response(status=200)


async def get_statuses_for_object(request: web.Request, parent, opt_pretty=None, opt_fields=None, limit=None, offset=None, created_since=None) -> web.Response:
    """Get status updates from an object

    Returns the compact status update records for all updates on the object.

    :param parent: Globally unique identifier for object to fetch statuses from. Must be a GID for a project, portfolio, or goal.
    :type parent: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]
    :param limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
    :type limit: int
    :param offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. &#39;Note: You can only pass in an offset that was returned to you via a previously paginated request.&#39;
    :type offset: str
    :param created_since: Only return statuses that have been created since the given time.
    :type created_since: str

    """
    created_since = util.deserialize_datetime(created_since)
    return web.Response(status=200)
