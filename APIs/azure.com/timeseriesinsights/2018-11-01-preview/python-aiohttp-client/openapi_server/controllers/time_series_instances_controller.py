from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_instances_page import GetInstancesPage
from openapi_server.models.instances_batch_request import InstancesBatchRequest
from openapi_server.models.instances_batch_response import InstancesBatchResponse
from openapi_server.models.instances_suggest_request import InstancesSuggestRequest
from openapi_server.models.instances_suggest_response import InstancesSuggestResponse
from openapi_server.models.search_instances_request import SearchInstancesRequest
from openapi_server.models.search_instances_response_page import SearchInstancesResponsePage
from openapi_server.models.tsi_error import TsiError
from openapi_server import util


async def time_series_instances_execute_batch(request: web.Request, api_version, parameters, x_ms_client_request_id=None, x_ms_client_session_id=None) -> web.Response:
    """time_series_instances_execute_batch

    Executes a batch get, create, update, delete operation on multiple time series instances.

    :param api_version: Version of the API to be used with the client request. Currently supported version is \&quot;2018-11-01-preview\&quot;.
    :type api_version: str
    :param parameters: Time series instances suggest request body.
    :type parameters: dict | bytes
    :param x_ms_client_request_id: Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    :type x_ms_client_request_id: str
    :param x_ms_client_session_id: Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    :type x_ms_client_session_id: str

    """
    parameters = InstancesBatchRequest.from_dict(parameters)
    return web.Response(status=200)


async def time_series_instances_get(request: web.Request, api_version, x_ms_continuation=None, x_ms_client_request_id=None, x_ms_client_session_id=None) -> web.Response:
    """time_series_instances_get

    Gets time series instances in pages.

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


async def time_series_instances_search(request: web.Request, api_version, parameters, x_ms_continuation=None, x_ms_client_request_id=None, x_ms_client_session_id=None) -> web.Response:
    """time_series_instances_search

    Partial list of hits on search for time series instances based on instance attributes.

    :param api_version: Version of the API to be used with the client request. Currently supported version is \&quot;2018-11-01-preview\&quot;.
    :type api_version: str
    :param parameters: Time series instances search request body.
    :type parameters: dict | bytes
    :param x_ms_continuation: Continuation token from previous page of results to retrieve the next page of the results in calls that support pagination. To get the first page results, specify null continuation token as parameter value. Returned continuation token is null if all results have been returned, and there is no next page of results.
    :type x_ms_continuation: str
    :param x_ms_client_request_id: Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    :type x_ms_client_request_id: str
    :param x_ms_client_session_id: Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    :type x_ms_client_session_id: str

    """
    parameters = SearchInstancesRequest.from_dict(parameters)
    return web.Response(status=200)


async def time_series_instances_suggest(request: web.Request, api_version, parameters, x_ms_client_request_id=None, x_ms_client_session_id=None) -> web.Response:
    """time_series_instances_suggest

    Suggests keywords based on time series instance attributes to be later used in Search Instances.

    :param api_version: Version of the API to be used with the client request. Currently supported version is \&quot;2018-11-01-preview\&quot;.
    :type api_version: str
    :param parameters: Time series instances suggest request body.
    :type parameters: dict | bytes
    :param x_ms_client_request_id: Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    :type x_ms_client_request_id: str
    :param x_ms_client_session_id: Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    :type x_ms_client_session_id: str

    """
    parameters = InstancesSuggestRequest.from_dict(parameters)
    return web.Response(status=200)
