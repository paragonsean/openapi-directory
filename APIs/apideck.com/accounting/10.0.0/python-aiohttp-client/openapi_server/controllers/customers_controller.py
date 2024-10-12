from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.create_customer_response import CreateCustomerResponse
from openapi_server.models.customer import Customer
from openapi_server.models.customers_filter import CustomersFilter
from openapi_server.models.delete_customer_response import DeleteCustomerResponse
from openapi_server.models.get_customer_response import GetCustomerResponse
from openapi_server.models.get_customers_response import GetCustomersResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server.models.update_customer_response import UpdateCustomerResponse
from openapi_server import util


async def customers_add(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, body, raw=None, x_apideck_service_id=None) -> web.Response:
    """Create Customer

    Create Customer

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
    body = Customer.from_dict(body)
    return web.Response(status=200)


async def customers_all(request: web.Request, x_apideck_consumer_id, x_apideck_app_id, raw=None, x_apideck_service_id=None, cursor=None, limit=None, filter=None, pass_through=None, fields=None) -> web.Response:
    """List Customers

    List Customers

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
    :param filter: Apply filters
    :type filter: dict | bytes
    :param pass_through: Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads
    :type pass_through: Dict[str, ]
    :param fields: The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded.
    :type fields: str

    """
    filter = .from_dict(filter)
    return web.Response(status=200)


async def customers_delete(request: web.Request, id, x_apideck_consumer_id, x_apideck_app_id, x_apideck_service_id=None, raw=None) -> web.Response:
    """Delete Customer

    Delete Customer

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


async def customers_one(request: web.Request, id, x_apideck_consumer_id, x_apideck_app_id, x_apideck_service_id=None, raw=None, fields=None) -> web.Response:
    """Get Customer

    Get Customer

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


async def customers_update(request: web.Request, id, x_apideck_consumer_id, x_apideck_app_id, body, x_apideck_service_id=None, raw=None) -> web.Response:
    """Update Customer

    Update Customer

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
    body = Customer.from_dict(body)
    return web.Response(status=200)
