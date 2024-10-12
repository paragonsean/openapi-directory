from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.sensitive_data import SensitiveData
from openapi_server import util


async def add_or_update_sensitive_data(request: web.Request, company_id, employee_id, body) -> web.Response:
    """Add/update sensitive data

    Sends new or updated employee sensitive data information directly to Web Pay.

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str
    :param body: Sensitive Data Model
    :type body: dict | bytes

    """
    body = SensitiveData.from_dict(body)
    return web.Response(status=200)


async def get_sensitive_data(request: web.Request, company_id, employee_id) -> web.Response:
    """Get sensitive data

    Gets employee sensitive data information directly from Web Pay.

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str

    """
    return web.Response(status=200)
