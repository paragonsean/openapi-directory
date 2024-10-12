from typing import List, Dict
from aiohttp import web

from openapi_server.models.availability_response import AvailabilityResponse
from openapi_server.models.event_schema import EventSchema
from openapi_server.models.get_event_schema_request import GetEventSchemaRequest
from openapi_server.models.query_request import QueryRequest
from openapi_server.models.query_result_page import QueryResultPage
from openapi_server.models.tsi_error import TsiError
from openapi_server import util


async def query_execute(request: web.Request, api_version, parameters, store_type=None, x_ms_continuation=None, x_ms_client_request_id=None, x_ms_client_session_id=None) -> web.Response:
    """query_execute

    Executes Time Series Query in pages of results - Get Events, Get Series or Aggregate Series.

    :param api_version: Version of the API to be used with the client request. Currently supported version is \&quot;2018-11-01-preview\&quot;.
    :type api_version: str
    :param parameters: Time series query request body.
    :type parameters: dict | bytes
    :param store_type: For the environments with warm store enabled, the query can be executed either on the &#39;WarmStore&#39; or &#39;ColdStore&#39;. This parameter in the query defines which store the query should be executed on. If not defined, the query will be executed on the cold store.
    :type store_type: str
    :param x_ms_continuation: Continuation token from previous page of results to retrieve the next page of the results in calls that support pagination. To get the first page results, specify null continuation token as parameter value. Returned continuation token is null if all results have been returned, and there is no next page of results.
    :type x_ms_continuation: str
    :param x_ms_client_request_id: Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    :type x_ms_client_request_id: str
    :param x_ms_client_session_id: Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    :type x_ms_client_session_id: str

    """
    parameters = QueryRequest.from_dict(parameters)
    return web.Response(status=200)


async def query_get_availability(request: web.Request, api_version, store_type=None, x_ms_client_request_id=None, x_ms_client_session_id=None) -> web.Response:
    """query_get_availability

    Returns the time range and distribution of event count over the event timestamp ($ts). This API can be used to provide landing experience of navigating to the environment.

    :param api_version: Version of the API to be used with the client request. Currently supported version is \&quot;2018-11-01-preview\&quot;.
    :type api_version: str
    :param store_type: For the environments with warm store enabled, the query can be executed either on the &#39;WarmStore&#39; or &#39;ColdStore&#39;. This parameter in the query defines which store the query should be executed on. If not defined, the query will be executed on the cold store.
    :type store_type: str
    :param x_ms_client_request_id: Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    :type x_ms_client_request_id: str
    :param x_ms_client_session_id: Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    :type x_ms_client_session_id: str

    """
    return web.Response(status=200)


async def query_get_event_schema(request: web.Request, api_version, parameters, store_type=None, x_ms_client_request_id=None, x_ms_client_session_id=None) -> web.Response:
    """query_get_event_schema

    Returns environment event schema for a given search span. Event schema is a set of property definitions. Event schema may not be contain all persisted properties when there are too many properties.

    :param api_version: Version of the API to be used with the client request. Currently supported version is \&quot;2018-11-01-preview\&quot;.
    :type api_version: str
    :param parameters: Parameters to get event schema.
    :type parameters: dict | bytes
    :param store_type: For the environments with warm store enabled, the query can be executed either on the &#39;WarmStore&#39; or &#39;ColdStore&#39;. This parameter in the query defines which store the query should be executed on. If not defined, the query will be executed on the cold store.
    :type store_type: str
    :param x_ms_client_request_id: Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    :type x_ms_client_request_id: str
    :param x_ms_client_session_id: Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    :type x_ms_client_session_id: str

    """
    parameters = GetEventSchemaRequest.from_dict(parameters)
    return web.Response(status=200)
