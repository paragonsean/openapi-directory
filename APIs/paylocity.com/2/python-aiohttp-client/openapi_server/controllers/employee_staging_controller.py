from typing import List, Dict
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.staged_employee import StagedEmployee
from openapi_server.models.tracking_number_response import TrackingNumberResponse
from openapi_server import util


async def add_new_employee_to_web_link(request: web.Request, company_id, body) -> web.Response:
    """Add new employee to Web Link

    Add new employee to Web Link will send partially completed or potentially erroneous new hire record to Web Link, where it can be corrected and competed by company administrator or authorized Paylocity Service Bureau employee.

    :param company_id: Company Id
    :type company_id: str
    :param body: StagedEmployee Model
    :type body: dict | bytes

    """
    body = StagedEmployee.from_dict(body)
    return web.Response(status=200)
