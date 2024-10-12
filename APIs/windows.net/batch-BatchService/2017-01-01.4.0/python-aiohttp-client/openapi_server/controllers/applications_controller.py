from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_list_result import ApplicationListResult
from openapi_server.models.application_summary import ApplicationSummary
from openapi_server.models.batch_error import BatchError
from openapi_server import util


async def application_get(request: web.Request, application_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Gets information about the specified application.

    

    :param application_id: The ID of the application.
    :type application_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def application_list(request: web.Request, api_version, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """Lists all of the applications available in the specified account.

    This operation returns only applications and versions that are available for use on compute nodes; that is, that can be used in an application package reference. For administrator information about applications and versions that are not yet available to compute nodes, use the Azure portal or the Azure Resource Manager API.

    :param api_version: Client API Version.
    :type api_version: str
    :param maxresults: The maximum number of items to return in the response. A maximum of 1000 applications can be returned.
    :type maxresults: int
    :param timeout: The maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: The caller-generated request identity, in the form of a GUID with no decoration such as curly braces, e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :type client_request_id: str
    :param return_client_request_id: Whether the server should return the client-request-id in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. Client libraries typically set this to the current system clock time; set it explicitly if you are calling the REST API directly.
    :type ocp_date: str

    """
    return web.Response(status=200)
