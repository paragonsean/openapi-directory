from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_types_page import GetTypesPage
from openapi_server.models.tsi_error import TsiError
from openapi_server.models.types_batch_request import TypesBatchRequest
from openapi_server.models.types_batch_response import TypesBatchResponse
from openapi_server import util


async def time_series_types_execute_batch(request: web.Request, api_version, parameters, x_ms_client_request_id=None, x_ms_client_session_id=None) -> web.Response:
    """time_series_types_execute_batch

    Executes a batch get, create, update, delete operation on multiple time series types.

    :param api_version: Version of the API to be used with the client request. Currently supported version is \&quot;2018-11-01-preview\&quot;.
    :type api_version: str
    :param parameters: Time series types batch request body.
    :type parameters: dict | bytes
    :param x_ms_client_request_id: Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    :type x_ms_client_request_id: str
    :param x_ms_client_session_id: Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    :type x_ms_client_session_id: str

    """
    parameters = TypesBatchRequest.from_dict(parameters)
    return web.Response(status=200)


async def time_series_types_get(request: web.Request, api_version, x_ms_continuation=None, x_ms_client_request_id=None, x_ms_client_session_id=None) -> web.Response:
    """time_series_types_get

    Gets time series types in pages.

    :param api_version: Version of the API to be used with the client request. Currently supported version is \&quot;2018-11-01-preview\&quot;.
    :type api_version: str
    :param x_ms_continuation: Continuation token from previous page of results to retrieve the next page of the results in calls that support pagination. To get the first page results, specify null continuation token as parameter value. Returned continuation token is null if all results have been returned, and there is no next page of results.
    :type x_ms_continuation: str
    :param x_ms_client_request_id: Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    :type x_ms_client_request_id: str
    :param x_ms_client_session_id: Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    :type x_ms_client_session_id: str

    """
    return web.Response(status=200)
