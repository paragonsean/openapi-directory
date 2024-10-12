from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_organization_export201_response import CreateOrganizationExport201Response
from openapi_server.models.create_organization_export_request import CreateOrganizationExportRequest
from openapi_server.models.error_response import ErrorResponse
from openapi_server import util


async def create_organization_export(request: web.Request, body, opt_pretty=None, opt_fields=None, limit=None, offset=None) -> web.Response:
    """Create an organization export request

    This method creates a request to export an Organization. Asana will complete the export at some point after you create the request.

    :param body: The organization to export.
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
    body = CreateOrganizationExportRequest.from_dict(body)
    return web.Response(status=200)


async def get_organization_export(request: web.Request, organization_export_gid, opt_pretty=None, opt_fields=None) -> web.Response:
    """Get details on an org export request

    Returns details of a previously-requested Organization export.

    :param organization_export_gid: Globally unique identifier for the organization export.
    :type organization_export_gid: str
    :param opt_pretty: Provides “pretty” output. Provides the response in a “pretty” format. In the case of JSON this means doing proper line breaking and indentation to make it readable. This will take extra time and increase the response size so it is advisable only to use this during debugging.
    :type opt_pretty: bool
    :param opt_fields: Defines fields to return. Some requests return *compact* representations of objects in order to conserve resources and complete the request more efficiently. Other times requests return more information than you may need. This option allows you to list the exact set of fields that the API should be sure to return for the objects. The field names should be provided as paths, described below. The id of included objects will always be returned, regardless of the field options.
    :type opt_fields: List[str]

    """
    return web.Response(status=200)
