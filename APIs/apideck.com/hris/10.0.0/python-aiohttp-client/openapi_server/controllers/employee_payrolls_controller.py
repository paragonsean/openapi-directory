from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.get_employee_payroll_response import GetEmployeePayrollResponse
from openapi_server.models.get_employee_payrolls_response import GetEmployeePayrollsResponse
from openapi_server.models.not_found_response import NotFoundResponse
from openapi_server.models.payment_required_response import PaymentRequiredResponse
from openapi_server.models.payrolls_filter import PayrollsFilter
from openapi_server.models.unauthorized_response import UnauthorizedResponse
from openapi_server.models.unexpected_error_response import UnexpectedErrorResponse
from openapi_server.models.unprocessable_response import UnprocessableResponse
from openapi_server import util


async def employee_payrolls_all(request: web.Request, employee_id, x_apideck_consumer_id, x_apideck_app_id, raw=None, x_apideck_service_id=None, filter=None, pass_through=None, fields=None) -> web.Response:
    """List Employee Payrolls

    List payrolls for employee

    :param employee_id: ID of the employee you are acting upon.
    :type employee_id: str
    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param raw: Include raw response. Mostly used for debugging purposes
    :type raw: bool
    :param x_apideck_service_id: Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    :type x_apideck_service_id: str
    :param filter: Apply filters
    :type filter: dict | bytes
    :param pass_through: Optional unmapped key/values that will be passed through to downstream as query parameters. Ie: ?pass_through[search]&#x3D;leads becomes ?search&#x3D;leads
    :type pass_through: Dict[str, ]
    :param fields: The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded.
    :type fields: str

    """
    filter = .from_dict(filter)
    return web.Response(status=200)


async def employee_payrolls_one(request: web.Request, payroll_id, employee_id, x_apideck_consumer_id, x_apideck_app_id, raw=None, x_apideck_service_id=None, fields=None) -> web.Response:
    """Get Employee Payroll

    Get payroll for employee

    :param payroll_id: ID of the payroll you are acting upon.
    :type payroll_id: str
    :param employee_id: ID of the employee you are acting upon.
    :type employee_id: str
    :param x_apideck_consumer_id: ID of the consumer which you want to get or push data from
    :type x_apideck_consumer_id: str
    :param x_apideck_app_id: The ID of your Unify application
    :type x_apideck_app_id: str
    :param raw: Include raw response. Mostly used for debugging purposes
    :type raw: bool
    :param x_apideck_service_id: Provide the service id you want to call (e.g., pipedrive). Only needed when a consumer has activated multiple integrations for a Unified API.
    :type x_apideck_service_id: str
    :param fields: The &#39;fields&#39; parameter allows API users to specify the fields they want to include in the API response. If this parameter is not present, the API will return all available fields. If this parameter is present, only the fields specified in the comma-separated string will be included in the response. Nested properties can also be requested by using a dot notation. &lt;br /&gt;&lt;br /&gt;Example: &#x60;fields&#x3D;name,email,addresses.city&#x60;&lt;br /&gt;&lt;br /&gt;In the example above, the response will only include the fields \&quot;name\&quot;, \&quot;email\&quot; and \&quot;addresses.city\&quot;. If any other fields are available, they will be excluded.
    :type fields: str

    """
    return web.Response(status=200)
