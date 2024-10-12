from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_location_response import CreateLocationResponse
from openapi_server.models.delete_location_response import DeleteLocationResponse
from openapi_server.models.get_location_response import GetLocationResponse
from openapi_server.models.get_locations_response import GetLocationsResponse
from openapi_server.models.location import Location
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_location_response import UpdateLocationResponse
from openapi_server import util


async def locations_add(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, body, raw=None, x_apideck_service_id=None) -> web.Response:
    """Create Location

    Create Location

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
    body = Location.from_dict(body)
    return web.Response(status=200)


async def locations_all(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, raw=None, x_apideck_service_id=None, cursor=None, limit=None, fields=None) -> web.Response:
    """List Locations

    List Locations

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
    :param limit: Number of results to return. Minimum 1, Maximum 200, Default 20
    :type limit: int
    :param fields: The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded.
    :type fields: str

    """
    return web.Response(status=200)


async def locations_delete(request: web.Request, id, x_apideck_consumer_id, x_apideck_app_id, x_apideck_service_id=None, raw=None) -> web.Response:
    """Delete Location

    Delete Location

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


async def locations_one(request: web.Request, id, x_apideck_consumer_id, x_apideck_app_id, x_apideck_service_id=None, raw=None, fields=None) -> web.Response:
    """Get Location

    Get Location

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
    :param fields: The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded.
    :type fields: str

    """
    return web.Response(status=200)


async def locations_update(request: web.Request, id, x_apideck_consumer_id, x_apideck_app_id, body, x_apideck_service_id=None, raw=None) -> web.Response:
    """Update Location

    Update Location

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
    body = Location.from_dict(body)
    return web.Response(status=200)
