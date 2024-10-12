from typing import List, Dict
from aiohttp import web

from openapi_server.models.application_list_result import ApplicationListResult
from openapi_server.models.application_summary import ApplicationSummary
from openapi_server.models.batch_error import BatchError
from openapi_server import util


async def application_get(request: web.Request, application_id, api_version, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """application_get

    Gets information about the specified application.

    :param application_id: The id of the application.
    :type application_id: str
    :param api_version: Client API Version.
    :type api_version: str
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)


async def application_list(request: web.Request, api_version, maxresults=None, timeout=None, client_request_id=None, return_client_request_id=None, ocp_date=None) -> web.Response:
    """application_list

    Lists all of the applications available in the specified account.

    :param api_version: Client API Version.
    :type api_version: str
    :param maxresults: Sets the maximum number of items to return in the response.
    :type maxresults: int
    :param timeout: Sets the maximum time that the server can spend processing the request, in seconds. The default is 30 seconds.
    :type timeout: int
    :param client_request_id: Caller generated request identity, in the form of a GUID with no decoration such as curly braces e.g. 9C4D50EE-2D56-4CD3-8152-34347DC9F2B0.
    :type client_request_id: str
    :param return_client_request_id: Specifies if the server should return the client-request-id identifier in the response.
    :type return_client_request_id: bool
    :param ocp_date: The time the request was issued. If not specified, this header will be automatically populated with the current system clock time.
    :type ocp_date: str

    """
    return web.Response(status=200)
