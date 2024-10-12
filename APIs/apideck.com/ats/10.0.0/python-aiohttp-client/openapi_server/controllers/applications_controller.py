from typing import List, Dict
from aiohttp import web

from openapi_server.models.application import Application
from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_application_response import CreateApplicationResponse
from openapi_server.models.delete_application_response import DeleteApplicationResponse
from openapi_server.models.get_application_response import GetApplicationResponse
from openapi_server.models.get_applications_response import GetApplicationsResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_application_response import UpdateApplicationResponse
from openapi_server import util


async def applications_add(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, body, raw=None, x_apideck_service_id=None) -> web.Response:
    """Create Application

    Create Application

    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param body: 
    :type body: dict | bytes
    :param raw: Include raw response. Mostly used for debugging purposes
    :type raw: bool
    :param x_apideck_service_id: Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    :type x_apideck_service_id: str

    """
    body = Application.from_dict(body)
    return web.Response(status=200)


async def applications_all(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, raw=None, x_apideck_service_id=None, cursor=None, pass_through=None, limit=None) -> web.Response:
    """List Applications

    List Applications

    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param raw: Include raw response. Mostly used for debugging purposes
    :type raw: bool
    :param x_apideck_service_id: Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    :type x_apideck_service_id: str
    :param cursor: Cursor to start from. You can find cursors for next/previous pages in the meta.cursors property of the response.
    :type cursor: str
    :param pass_through: Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads
    :type pass_through: Dict[str, ]
    :param limit: Number of results to return. Minimum 1, Maximum 200, Default 20
    :type limit: int

    """
    return web.Response(status=200)


async def applications_delete(request: web.Request, id, x_apideck_consumer_id, x_apideck_app_id, x_apideck_service_id=None, raw=None) -> web.Response:
    """Delete Application

    Delete Application

    :param id: ID of the record you are acting upon.
    :type id: str
    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param x_apideck_service_id: Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    :type x_apideck_service_id: str
    :param raw: Include raw response. Mostly used for debugging purposes
    :type raw: bool

    """
    return web.Response(status=200)


async def applications_one(request: web.Request, id, x_apideck_consumer_id, x_apideck_app_id, x_apideck_service_id=None, raw=None) -> web.Response:
    """Get Application

    Get Application

    :param id: ID of the record you are acting upon.
    :type id: str
    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param x_apideck_service_id: Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    :type x_apideck_service_id: str
    :param raw: Include raw response. Mostly used for debugging purposes
    :type raw: bool

    """
    return web.Response(status=200)


async def applications_update(request: web.Request, id, x_apideck_consumer_id, x_apideck_app_id, body, x_apideck_service_id=None, raw=None) -> web.Response:
    """Update Application

    Update Application

    :param id: ID of the record you are acting upon.
    :type id: str
    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param body: 
    :type body: dict | bytes
    :param x_apideck_service_id: Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    :type x_apideck_service_id: str
    :param raw: Include raw response. Mostly used for debugging purposes
    :type raw: bool

    """
    body = Application.from_dict(body)
    return web.Response(status=200)
