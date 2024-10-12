from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.local_tax import LocalTax
from openapi_server import util


async def add_local_tax(request: web.Request, company_id, employee_id, body) -> web.Response:
    """Add new local tax

    Sends new employee local tax information directly to Web Pay.

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str
    :param body: LocalTax Model
    :type body: dict | bytes

    """
    body = LocalTax.from_dict(body)
    return web.Response(status=200)


async def delete_local_tax_by_tax_code(request: web.Request, company_id, employee_id, tax_code) -> web.Response:
    """Delete local tax by tax code

    Delete local tax by tax code

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str
    :param tax_code: Tax Code
    :type tax_code: str

    """
    return web.Response(status=200)


async def get_all_local_taxes(request: web.Request, company_id, employee_id) -> web.Response:
    """Get all local taxes

    Returns all local taxes for the selected employee.

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str

    """
    return web.Response(status=200)


async def get_local_tax_by_tax_code(request: web.Request, company_id, employee_id, tax_code) -> web.Response:
    """Get local taxes by tax code

    Returns all local taxes with the provided tax code for the selected employee.

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str
    :param tax_code: Tax Code
    :type tax_code: str

    """
    return web.Response(status=200)
