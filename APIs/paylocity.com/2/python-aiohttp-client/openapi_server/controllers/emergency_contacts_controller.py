from typing import List, Dict
from aiohttp import web

from openapi_server.models.emergency_contact import EmergencyContact
from openapi_server.models.error import Error
from openapi_server import util


async def add_or_update_emergency_contacts(request: web.Request, company_id, employee_id, body) -> web.Response:
    """Add/update emergency contacts

    Sends new or updated employee emergency contacts directly to Web Pay.

    :param company_id: Company Id
    :type company_id: str
    :param employee_id: Employee Id
    :type employee_id: str
    :param body: Emergency Contact Model
    :type body: dict | bytes

    """
    body = EmergencyContact.from_dict(body)
    return web.Response(status=200)
