from typing import List, Dict
from aiohttp import web

from openapi_server.models.created_result import CreatedResult
from openapi_server.models.employee import Employee
from openapi_server.models.employee_cursor_results import EmployeeCursorResults
from openapi_server.models.error import Error
from openapi_server import util


async def create_employee(request: web.Request, body=None) -> web.Response:
    """Create a single Employee

    Use this endpoint to create a single Employee.

    :param body: 
    :type body: dict | bytes

    """
    body = Employee.from_dict(body)
    return web.Response(status=200)


async def delete_employee_by_id(request: web.Request, number) -> web.Response:
    """Delete single Employee

    Use this endpoint to delete a single Employee by id/number.

    :param number: 
    :type number: int

    """
    return web.Response(status=200)


async def get_all_employees(request: web.Request, cursor=None, filter=None) -> web.Response:
    """Retrieve all Employees

    Use this endpoint to retrieve all Employees in bulk.  Max number of items returned in a single call is 1000. Use the continuation cursor parameter to set the continuation cursor for retrieval of next set of data. [pagination instructions](#section/Retrieving-data/Pagination)

    :param cursor: 
    :type cursor: str
    :param filter: 
    :type filter: str

    """
    return web.Response(status=200)


async def get_employee_by_id(request: web.Request, number) -> web.Response:
    """Retrieve single Employee

    Use this endpoint to load a single Employee by id/number.

    :param number: 
    :type number: int

    """
    return web.Response(status=200)


async def get_number_of_employees(request: web.Request, filter=None) -> web.Response:
    """Retrieve the number of Employees

    Call this endpoint to get the number of Employees. You can use a filtering as well.

    :param filter: 
    :type filter: str

    """
    return web.Response(status=200)


async def get_page_of_employees(request: web.Request, filter=None, sort=None, page_size=None, skip_pages=None) -> web.Response:
    """Retrieve a page of Employees

    Use this endpoint to load a page of Employees.

    :param filter: 
    :type filter: str
    :param sort: 
    :type sort: str
    :param page_size: 
    :type page_size: int
    :param skip_pages: 
    :type skip_pages: int

    """
    return web.Response(status=200)


async def update_employee(request: web.Request, body=None) -> web.Response:
    """Update a single Employee

    Use this endpoint to update a single Employee.

    :param body: 
    :type body: dict | bytes

    """
    body = Employee.from_dict(body)
    return web.Response(status=200)
