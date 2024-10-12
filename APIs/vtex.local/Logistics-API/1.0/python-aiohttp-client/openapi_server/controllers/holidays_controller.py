from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_update_holiday_request import CreateUpdateHolidayRequest
from openapi_server import util


async def all_holidays(request: web.Request, content_type, accept) -> web.Response:
    """List all holidays

    Lists information of all holidays.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str

    """
    return web.Response(status=200)


async def create_update_holiday(request: web.Request, accept, content_type, holiday_id, body) -> web.Response:
    """Create/update holiday

    Creates or updates holidays through holiday ID.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param content_type: Type of the content being sent
    :type content_type: str
    :param holiday_id: 
    :type holiday_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateUpdateHolidayRequest.from_dict(body)
    return web.Response(status=200)


async def holiday(request: web.Request, content_type, accept, holiday_id) -> web.Response:
    """Delete holiday

    Deletes given holidays set up in your store.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param holiday_id: 
    :type holiday_id: str

    """
    return web.Response(status=200)


async def holiday_by_id(request: web.Request, content_type, accept, holiday_id) -> web.Response:
    """List holiday by ID

    Lists holiday&#39;s information by holiday ID.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param holiday_id: 
    :type holiday_id: str

    """
    return web.Response(status=200)
