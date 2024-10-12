from typing import List, Dict
from aiohttp import web

from openapi_server.models.model_settings_response import ModelSettingsResponse
from openapi_server.models.tsi_error import TsiError
from openapi_server.models.update_model_settings_request import UpdateModelSettingsRequest
from openapi_server import util


async def model_settings_get(request: web.Request, api_version, x_ms_client_request_id=None, x_ms_client_session_id=None) -> web.Response:
    """model_settings_get

    Returns the model settings which includes model display name, Time Series ID properties and default type ID. Every pay-as-you-go environment has a model that is automatically created.

    :param api_version: Version of the API to be used with the client request. Currently supported version is \&quot;2018-11-01-preview\&quot;.
    :type api_version: str
    :param x_ms_client_request_id: Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    :type x_ms_client_request_id: str
    :param x_ms_client_session_id: Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    :type x_ms_client_session_id: str

    """
    return web.Response(status=200)


async def model_settings_update(request: web.Request, api_version, parameters, x_ms_client_request_id=None, x_ms_client_session_id=None) -> web.Response:
    """model_settings_update

    Updates time series model settings - either the model name or default type ID.

    :param api_version: Version of the API to be used with the client request. Currently supported version is \&quot;2018-11-01-preview\&quot;.
    :type api_version: str
    :param parameters: Model settings update request body.
    :type parameters: dict | bytes
    :param x_ms_client_request_id: Optional client request ID. Service records this value. Allows the service to trace operation across services, and allows the customer to contact support regarding a particular request.
    :type x_ms_client_request_id: str
    :param x_ms_client_session_id: Optional client session ID. Service records this value. Allows the service to trace a group of related operations across services, and allows the customer to contact support regarding a particular group of requests.
    :type x_ms_client_session_id: str

    """
    parameters = UpdateModelSettingsRequest.from_dict(parameters)
    return web.Response(status=200)
