from typing import List, Dict
from aiohttp import web

from openapi_server.models.v1_employee import V1Employee
from openapi_server.models.v1_employee_role import V1EmployeeRole
from openapi_server import util


async def create_employee(request: web.Request, body) -> web.Response:
    """CreateEmployee

     Use the CreateEmployee endpoint to add an employee to a Square account. Employees created with the Connect API have an initial status of &#x60;INACTIVE&#x60;. Inactive employees cannot sign in to Square Point of Sale until they are activated from the Square Dashboard. Employee status cannot be changed with the Connect API.  Employee entities cannot be deleted. To disable employee profiles, set the employee&#39;s status to &lt;code&gt;INACTIVE&lt;/code&gt;

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = V1Employee.from_dict(body)
    return web.Response(status=200)


async def create_employee_role(request: web.Request, body) -> web.Response:
    """CreateEmployeeRole

    Creates an employee role you can then assign to employees.  Square accounts can include any number of roles that can be assigned to employees. These roles define the actions and permissions granted to an employee with that role. For example, an employee with a \&quot;Shift Manager\&quot; role might be able to issue refunds in Square Point of Sale, whereas an employee with a \&quot;Clerk\&quot; role might not.  Roles are assigned with the [V1UpdateEmployee](https://developer.squareup.com/reference/square_2021-08-18/v1-employees-api/update-employee-role) endpoint. An employee can have only one role at a time.  If an employee has no role, they have none of the permissions associated with roles. All employees can accept payments with Square Point of Sale.

    :param body: An EmployeeRole object with a name and permissions, and an optional owner flag.
    :type body: dict | bytes

    """
    body = V1EmployeeRole.from_dict(body)
    return web.Response(status=200)


async def list_employee_roles(request: web.Request, order=None, limit=None, batch_token=None) -> web.Response:
    """ListEmployeeRoles

    Provides summary information for all of a business&#39;s employee roles.

    :param order: The order in which employees are listed in the response, based on their created_at field.Default value: ASC
    :type order: str
    :param limit: The maximum integer number of employee entities to return in a single response. Default 100, maximum 200.
    :type limit: int
    :param batch_token: A pagination cursor to retrieve the next set of results for your original query to the endpoint.
    :type batch_token: str

    """
    return web.Response(status=200)


async def list_employees(request: web.Request, order=None, begin_updated_at=None, end_updated_at=None, begin_created_at=None, end_created_at=None, status=None, external_id=None, limit=None, batch_token=None) -> web.Response:
    """ListEmployees

    Provides summary information for all of a business&#39;s employees.

    :param order: The order in which employees are listed in the response, based on their created_at field.      Default value: ASC
    :type order: str
    :param begin_updated_at: If filtering results by their updated_at field, the beginning of the requested reporting period, in ISO 8601 format
    :type begin_updated_at: str
    :param end_updated_at: If filtering results by there updated_at field, the end of the requested reporting period, in ISO 8601 format.
    :type end_updated_at: str
    :param begin_created_at: If filtering results by their created_at field, the beginning of the requested reporting period, in ISO 8601 format.
    :type begin_created_at: str
    :param end_created_at: If filtering results by their created_at field, the end of the requested reporting period, in ISO 8601 format.
    :type end_created_at: str
    :param status: If provided, the endpoint returns only employee entities with the specified status (ACTIVE or INACTIVE).
    :type status: str
    :param external_id: If provided, the endpoint returns only employee entities with the specified external_id.
    :type external_id: str
    :param limit: The maximum integer number of employee entities to return in a single response. Default 100, maximum 200.
    :type limit: int
    :param batch_token: A pagination cursor to retrieve the next set of results for your original query to the endpoint.
    :type batch_token: str

    """
    return web.Response(status=200)


async def retrieve_employee(request: web.Request, employee_id) -> web.Response:
    """RetrieveEmployee

    Provides the details for a single employee.

    :param employee_id: The employee&#39;s ID.
    :type employee_id: str

    """
    return web.Response(status=200)


async def retrieve_employee_role(request: web.Request, role_id) -> web.Response:
    """RetrieveEmployeeRole

    Provides the details for a single employee role.

    :param role_id: The role&#39;s ID.
    :type role_id: str

    """
    return web.Response(status=200)


async def update_employee(request: web.Request, employee_id, body) -> web.Response:
    """UpdateEmployee

    

    :param employee_id: The ID of the role to modify.
    :type employee_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = V1Employee.from_dict(body)
    return web.Response(status=200)


async def update_employee_role(request: web.Request, role_id, body) -> web.Response:
    """UpdateEmployeeRole

    Modifies the details of an employee role.

    :param role_id: The ID of the role to modify.
    :type role_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = V1EmployeeRole.from_dict(body)
    return web.Response(status=200)
